""" Analyze a frequency and provide information about its pitch, octave,
intonation, and perceptibility. """

from argparse import ArgumentParser
from math import log2
import sys


# Replace this comment with your implementation of the following functions:
#   get_pitch()
#   get_octave()
#   check_intonation()
#   who_can_hear()
#   main()


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a frequency) and one optional argument,
    preceded by "-a4" (the value to use as the frequency of A4).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("freq", type=float, help="a frequency in Hz")
    parser.add_argument("-a4", type=float, default=440.0,
                        help="frequency to use for A4")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.freq, a4=args.a4)
