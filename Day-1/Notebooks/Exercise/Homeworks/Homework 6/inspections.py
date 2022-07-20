"""A tool to review heath inspections in the food service industry."""

from argparse import ArgumentParser
import pandas as pd
import sys


# Replace this comment with your implementation of the Inspections class.


def main(businessfile, inspectionfile, lat1, lon1, lat2, lon2):
    """Load business data and count critical violations for select businesses.
    
    The user will supply coordinates for a bounding box. Results will be limited
    to businesses within this box.
    
    Args:
        businessfile (str): path to CSV file containing data about
            businesses that serve food.
        inspectionfile (str): path to CSV file containing health inspection
            data.
            lat1 (float): one latitude value to use as a side of the
                bounding box.
            lon1 (float): one longitude value to use as a side of the
                bounding box.
            lat2 (float): another latitude value to use as a side of the
                bounding box.
            lon2 (float): another longitude value to use as a side of the
                bounding box.
    
    Side effects:
        Writes to stdout.
    """
    insp = Inspections(businessfile, inspectionfile)
    df = (insp.find_violations(lat1, lon1, lat2, lon2)
          .astype({"Inspection_results": "int32"}))
    print(df.shape)
    df_by_values = df.groupby("Inspection_results")
    for group in sorted(df_by_values.groups, reverse=True):
        header = f"{group} violations"
        print(header)
        print("-"*len(header))
        names = df_by_values.get_group(group)["Name"].to_list()
        print("\n".join(n for n in sorted(names)))
        print()


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect six mandatory arguments:
        - path to a CSV file containing information about businesses, including
          at least the following columns: "Establishment_id", "Name",
          "Latitude", "Longitude".
        - path to a CSV file containing information about health inspections,
          including at least the following columns: "Establishment_id",
          "Inspection_results". "Inspection_results" should contain the string
          "Critical Violations observed" if critical violations were observed.
        - a latitude value to use as an edge of a bounding box
        - a longitude value to use as an edge of the bounding box
        - another latitude value to use as an edge of the bounding box
        - another longitude value to use as an edge of the bounding box
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("businessfile", help="CSV file with information about"
                        " businesses that serve food")
    parser.add_argument("inspectionfile", help="CSV file with information about"
                        " health inspections")
    parser.add_argument("lat1", type=float,
                        help="First latitude value to use for bounding box")
    parser.add_argument("lon1", type=float,
                        help="First longitude to use for bounding box")
    parser.add_argument("lat2", type=float,
                        help="Second latitude value to use for bounding box")
    parser.add_argument("lon2", type=float,
                        help="Second longitude to use for bounding box")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.businessfile, args.inspectionfile, args.lat1, args.lon1,
         args.lat2, args.lon2)
