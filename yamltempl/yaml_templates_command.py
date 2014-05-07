#! /usr/bin/env python

import argparse
import sys
from yamltempl import yamlutils, vtl


def main():
    parser = argparse.ArgumentParser(
        description="Merge yaml data into a Velocity Template Language template")
    parser.add_argument('yamlfile',
                        metavar='filename.yaml',
                        type=argparse.FileType('r'),
                        help='the yaml file containing the data')
    parser.add_argument('-t', '--template',
                        metavar='file',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='the template file. If omitted, the template '
                             'is read from standard input')
    parser.add_argument('-o', '--output',
                        metavar='file',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='the output file, where the result should be '
                             'written. Standard output is used if omitted')
    args = parser.parse_args()
    yamldata = yamlutils.ordered_load(args.yamlfile)
    args.yamlfile.close()
    templ = args.template.read().decode('utf8')
    args.template.close()
    result = vtl.merge(yamldata, templ)
    args.output.write(result.encode('utf8'))
    args.output.close()


if __name__ == '__main__':
    main()
