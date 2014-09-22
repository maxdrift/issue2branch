#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import getopt
import re

HELP_TEXT = '''issue2branch - Riccardo Massari\n
usage: issue2branch.py [options] <issue title #issuenumber>
available options are:
-h, --help\tShow this help
-p, --prefix\tSpecify a prefix string (default: gh)'''

DEFAULT_PREFIX = 'gh'

def dashify(issue, prefix):
    try:
        iname, inumber = issue.rsplit('#', 1)
    except ValueError:
        print "Invalid input format\n"
        print HELP_TEXT
        sys.exit(2)
    inumber_val = int(inumber.strip())
    dashed_iname = re.sub('[^0-9a-zA-Z_]+', '-', iname.strip()).lower().strip('-')
    return '%s-%d-%s' % (prefix, inumber_val, dashed_iname)

def main(argv):
    prefix = DEFAULT_PREFIX
    if len(argv) == 0:
        print HELP_TEXT
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv, 'hp:', ['help', 'prefix='])
    except getopt.GetoptError:
        print HELP_TEXT
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print HELP_TEXT
            sys.exit()
        elif opt in ('-p', '--prefix'):
            prefix = arg
    return dashify(' '.join(args), prefix=prefix)

if __name__ == '__main__':
    print main(sys.argv[1:])
