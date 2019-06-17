import yaml
import json
import argparse


def y2j(filename):
    yconf = 'conf/{}.yml'.format(filename)
    jconf = 'conf/{}.json'.format(filename)

    with open(yconf,'r') as yf:
        yfile = yaml.safe_load(yf)

    print(yfile)

    with open(jconf, 'w') as jf:
        json.dump(yfile,jf)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--conf', default='test',help='file to covert')
    args = parser.parse_args()
    y2j(args.conf)