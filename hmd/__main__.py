#!/usr/bin/env python

import errno
import os
import sys

from __init__ import *
try:
    from src.abstract.automata.automata import AbstractAutomata
    from src.abstract.automata.automata import AbstractAutomataMachine
    from src.abstract.generator.generator import AbstractGenerator
    from src.abstract.lexer.lexer import AbstractLexer
    from src.abstract.lexer.token import AbstractToken
    from src.abstract.matcher.bsearch import bSearchMatcher
    from src.abstract.matcher.bsearch import bSearchPreprocessor
    from src.abstract.parser.parser import AbstractParser
    from src.debug import *
    from src.mindslab.generator import HMDGenerator
    from src.mindslab.generator import HMDStruct
    from src.mindslab.grammar import HMDGrammar
    from src.mindslab.syntax import *
    from tests.test_automata import TestAutomata
    from tests.test_bsearch import TestbSearch
    from tests.test_lexer import TestLexer
    from tests.test_parser import TestParser
    import argparse
    import unittest
except ImportError as message:
    raise ImportError(message)


if __name__ == '__main__':

    # print logo if no flag
    if not len(sys.argv) - 1:
        sys.stdout.write(__logo__)
        sys.exit()

    # adjust path if `this` is packed executable.
    if __package__ is None and not hasattr(sys, 'frozen'):
        path = os.path.realpath(os.path.abspath(__file__))
        sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

    # arguments
    aparser = argparse.ArgumentParser(prog=__program__)
    n_data = aparser.add_argument_group('data arguments')
    n_build = aparser.add_argument_group('build arguments')
    n_optim = aparser.add_argument_group('optimization arguments')
    n_test = aparser.add_argument_group('testing arguments')

    # -v, --version: show program's version number and exit.
    aparser.add_argument('-v', '--version',
                         action='version',
                         version=__version__)

    # -c <str>: compile single inline (hmd) definition.
    n_data.add_argument('-c',
                        type=str,
                        nargs='?',
                        metavar='str',
                        help='compile string (default: output to STDOUT)')

    # -f <file>: compile file hmd definition.
    n_data.add_argument('-f',
                        type=str,
                        nargs='?',
                        metavar='file',
                        help='compile file (default: output to STDOUT)')

    # -o <file>: output matrix into file.
    n_data.add_argument('-o',
                        type=str,
                        nargs='?',
                        metavar='file',
                        help="save output to file")

    # -l <int>: limit total categories count. Any defincies or extraneous
    #           categories will automatically repair itself.
    n_build.add_argument('-l',
                         type=int,
                         nargs='?',
                         metavar='int',
                         default=10,
                         help='set limit to category count (default: 10)')

    # -s: optimize ouptut matrix definitions by sorting lines and groupings.
    n_optim.add_argument('-s',
                         action='store_true',
                         default=False,
                         help='sort inline definition groups (default: off)')

    # -u: remove repeated lines (unique matrix results only).
    n_optim.add_argument('-u',
                         action='store_true',
                         default=False,
                         help='remove repeated lines (default: off)')

    # -x: convert inline terms into lemmas.
    n_optim.add_argument('-x',
                         action='store_true',
                         default=False,
                         help=' convert inline terms into lemmas (default: off)')

    # -t: run test suite and exit.
    n_test.add_argument('-t', '--test',
                        action='store_true',
                        default=False,
                        help="run tests (default: off)")

    args = aparser.parse_args()
    generator = HMDGenerator(
        max_categories=(args.l or 10),
        hmd_sorted=(args.s or False),
        hmd_unique=(args.u or False))

    try:

        # self-test
        if args.test:
            test_suites, test_cases = [], (
                TestAutomata,
                TestLexer,
                TestParser,
                TestbSearch
            )
            for test_case in test_cases:
                test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
                test_suites.append(test_suite)
            # sys.stdout = sys.stderr = open(os.devnull, 'wb') # /dev/null
            result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(test_suites))
            sys.exit(not result.wasSuccessful())

        # compile string
        if args.c:
            result = generator.generate([args.c])

        # compile file
        elif args.f:
            if not os.path.isfile(args.f):
                debug('w', "file '%s' does not exist.\n" % args.f)
                sys.exit(errno.ENOENT)
            with open(args.f) as f:
                c = f.read().split('\n')
                result = generator.generate(c)

        # output to file
        if args.o:
            with open(args.o, 'w') as f:
                f.write(result)

        # output to STDOUT
        else:
            try: sys.stdout.write(result)
            except: pass

    except KeyboardInterrupt: pass
    finally:
        del generator
        sys.exit()
