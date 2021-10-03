import argparse

# Parsing Keyword Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--token')
parser.add_argument('--channel')
parser.add_argument('--post_at')
args = parser.parse_args()