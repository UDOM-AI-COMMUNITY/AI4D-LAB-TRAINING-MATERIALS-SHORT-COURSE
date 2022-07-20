""" Calculate the cost of electricity using a three-tiered pricing system. """


from argparse import ArgumentParser
import sys


# Replace this comment with your implementation of the following functions:
#   energy_tier()
#   energy_cost()
#   main()


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument (a file containing electricity usage data).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("usage_file", help="file containing hourly electricty"
                        " usage")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print(f"Based on the usage in {args.usage_file},"
          f" the total bill is ${main(args.usage_file):.02f}.")
