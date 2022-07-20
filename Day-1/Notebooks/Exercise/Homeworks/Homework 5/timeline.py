"""Create a timeline from data in a file.

Read events, sort them chronologically, optionally filter by date range, and
display the events.
"""


from argparse import ArgumentParser
import functools
import re
import sys


MONTHS = {
    1 : "Jan",
    2 : "Feb",
    3 : "Mar",
    4 : "Apr",
    5 : "May",
    6 : "Jun",
    7 : "Jul",
    8 : "Aug",
    9 : "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

MONTHS_INVERSE = {abbr: num for num, abbr in MONTHS.items()}


# Replace this comment with your implementations of the Event and Timeline
# classes and the parse_date() function.


def main(event_file, start_date=None, end_date=None):
    """Read events from a file and print out a timeline of events from
    start_date to end_date.
    
    Args:
        event_file (str): path to a tab-delimited file where each line consists
            of a date, a tab, and a description of an event.
        start_date (Event, str, tuple, or None): the earliest date of interest
            (if None, include dates as far back as possible).
        end_date (Event, str, tuple, or None): the latest date of interest (if
            None, include dates as far forward as possible).
    
    Side effects:
        Writes to stdout.
    """
    tl = Timeline(event_file)
    tl.print_events(start_date=start_date, end_date=end_date)


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect one mandatory argument, a path to a tab-delimited file containing
    dates and event descriptions. 
    
    Also allow two optional arguments:
        - startdate: the earliest date to include in the timeline; should be
          preceded by -s or --startdate. If omitted, dates will extend back
          as far as possible.
        - enddate: the latest date to include in the timeline; should be
          preceded by -e or --enddate. If omitted, dates will extend forward
          as far as possible.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("event_file", help="tab-delimited file containing"
                        " dates and descriptions of events")
    parser.add_argument("-s", "--startdate", help="if specified, only show"
                        " events that occur on or after this date")
    parser.add_argument("-e", "--enddate", help="if specified, only show events"
                        " that occur on or before this date")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.event_file, start_date=args.startdate, end_date=args.enddate)
