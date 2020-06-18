#!/usr/bin/env python3
'''
Created on 22 Dec 2019

@author: Nathan

Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
'''

import sys
from urllib.request import  urlopen


def fetch_words(url):
    """Fetch a list of words froma URL.
    
    Args:
        URL: The URL of a UTF-8 text document.
        
    Returns:
        a list of strings containing the words from the the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.
    
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)
        
        
def main(url):
    """Print each word from a text document from a URL.
    
    Args:
        URL: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)
    
    
if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename