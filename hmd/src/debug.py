#!/usr/bin/env python

import sys
import time

def debug(category='', message=''):
    ''' custom debugging function.
    params:
      + category {str} -- INFO, DEBUG, WARN
      + message {str} -- a message to print
    '''

    # colors
    rst = '\033[39m' # reset
    c_w = '\033[97m' # white
    c_p = '\033[95m' # purple
    c_g = '\033[92m' # green
    c_r = '\033[91m' # red
    c_b = '\033[96m' # blue

    # create template
    timestamp = '%s[%s]%s' % (c_w, time.asctime(), rst)
    template = ' '.join([timestamp, '%s[%s%s%s] %s%s', rst])
    category = category.lower().strip()

    # INFO
    if category in ['i', 'info']:
        log = template % (c_w, c_g, 'info', c_w, c_g, message)
        sys.stdout.write(log)

    # DEBUG
    elif category in ['d', 'debug']:
        log = template % (c_w, c_p, 'debug', c_w, c_p, message)
        sys.stdout.write(log)

    # WARN
    elif category in ['w', 'warn']:
        log = template % (c_w, c_r, 'warn', c_w, c_r, message)
        sys.stderr.write(log)

    # BUG
    elif category in ['b', 'bug']:
        log = template % (c_w, c_b, 'bug', c_w, c_b, message)
        sys.stderr.write(log)

    # default
    else:
        log = template % (c_w, c_w, 'log', c_w, c_w, message)
        sys.stdout.write(log)
