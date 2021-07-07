#!/usr/bin/env python3

import argparse
import chardet
import codecs
import os

parser = argparse.ArgumentParser(description='convert encoding')
parser.add_argument('-e', '--encoding', dest='encoding', metavar=None, required=True, action='store', help='encoding')
args = parser.parse_args()

for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		if name.endswith(".cpp") or name.endswith(".h") or name.endswith(".md"):
			content = codecs.open(os.path.join(root, name), 'rb').read()
			encoding = chardet.detect(content)
			if encoding["encoding"] is None:
				continue
			if encoding["encoding"].upper() != args.encoding.upper():
				print(encoding["encoding"], "\t", os.path.join(root, name))
				content = content.decode(encoding["encoding"], 'ignore')
				codecs.open(os.path.join(root, name), 'w', encoding=args.encoding).write(content)