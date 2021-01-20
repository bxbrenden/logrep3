#!/usr/bin/env python3

# This is a Python 3 adaptation of a script originally written by Hans-Georg Eßer for Linux Pro Magazine's 2020
#     special edition "LibreOffice". Hans's GitHub page is: https://github.com/hgesser

from re import search, split
import sys
import xml.dom.minidom
from zipfile import ZipFile


def usage():
    print('USAGE: ./logrep3.py <PATTERN> <FILE_1> [<FILE_2>... <FILE_N>]')
    sys.exit(1)


def highlight(line, pattern):
    normal = '\033[0m'
    high = '\033[31m'  # 31 is red
    parts = split(pattern, line)

    return (high + pattern + normal).join(parts)


def apply_highlights(pattern, doclist):
    '''Given a line from an XML file and a search pattern, print the file name
       and the line that matches `pattern` with the match highlighted in red'''

    for doc in doclist:
        zipf = ZipFile(doc, 'r')

        with zipf.open('content.xml', 'r') as cf:
            content = cf.read()

        # Convert the one-line XML string into line-delimited XML
        dom = xml.dom.minidom.parseString(content)
        pretty_xml = dom.toprettyxml()

        for line_num, line in enumerate(pretty_xml.split('\n')):
            if search('</?text:(p|span)>', line):
                if pattern in line:
                    line = highlight(line, pattern)
                    print(f'{doc}, {line.strip()}')


def main():
    try:
        pattern = sys.argv[1]
    except IndexError:
        print('Failed to get search pattern from args.')
        usage()
    try:
        doclist = sys.argv[2:]
        # print(f'The doclist is set to {doclist}')
    except IndexError:
        print('Failed to get any document file names from args')
        usage()

    apply_highlights(pattern, doclist)


if __name__ == '__main__':
    main()
