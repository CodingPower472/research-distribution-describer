
import csv
import argparse

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The file you\'d like to perform statistical analysis on')
    return parser.parse_args()

args = parse_args()
print('File: %s' % args.file)
