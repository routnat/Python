'''
Created on 27 Dec 2019

@author: Nathan
'''

import sys
from math import log

def convert(s):
    '''convert to an integer.'''
    try:
        return int(s)
        #print("conversion succeeded! x =", x)
    except (ValueError, TypeError) as e:
        #print("Conversion failed!")
        print ("conversion error: {}"\
               .format(str(e)),
               file=sys.stderr)
        raise
    


def string_log(s):
    v = convert(s)
    return log(v)