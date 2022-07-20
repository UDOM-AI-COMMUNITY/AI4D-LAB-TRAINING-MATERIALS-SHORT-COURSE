""" Simulate a battle between two Battle Aardvarks. """


from argparse import ArgumentParser
from random import randint
import sys
from time import sleep


# Replace this comment with your implementations of the Aardvark and Catalog
# classes and the battle() function.


def main(filename, a1_name, a2_name, pause=2.0):
    """ Create two aardvarks from the aardvark catalog and stage a battle.
    
    Args:
        filename (str): A file with other data.
        a1_name (str): The name of the first aardvark, taken from the file.
        a2_name (str): The name of the second aardvark, taken from the file.
        pause (float): an amount of time in seconds to pause between attacks in
            a battle. Allows the user time to read the outcome of each attack.
            Default: 2.0.
        
    Side effects:
        See battle().
    """
    catalog = Catalog(filename)
    a1 = catalog.get_aardvark(a1_name)
    a2 = catalog.get_aardvark(a2_name)
    if a1_name == a2_name:
        a1.name += " 1"
        a2.name += " 2"
    battle(a1, a2, pause)

      
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect three mandatory arguments:
        - filename: a path to a CSV file containing aardvark stats
        - aardvark_1: the name of the first aardvark in the battle
        - aardvark_2: the name of the second aardvark in the battle

    Also allow one optional argument, which should be preceded by -p or --pause:
        - pause: the number of seconds to pause after each attack in the battle
          (defaults to 2.0)
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filename",
                        help="path to CSV file containing aardvark stats")
    parser.add_argument("aardvark_1", help="name of first aardvark")
    parser.add_argument("aardvark_2", help="name of second aardvark")
    parser.add_argument("-p", "--pause", type=float, default=2.0,
                        help="pause in seconds between attacks in the battle")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.aardvark_1, args.aardvark_2, pause=args.pause)
