#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
import argparse
import codecs
import hashlib
import json
import os
import sys

import argparse_actions

import vision

# Program usage with arguments
parser = argparse.ArgumentParser(description='Obtain google image information for files in image directories.')
parser.add_argument('source', action=argparse_actions.FolderExistsAction, help= 'input directory image path')
args = parser.parse_args()

# Permitir el output de UTF8
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

# Recorrido transversal por los directorios
data =  {}
for root, dirs, files in os.walk(args.source, topdown=True):
    for name in files:
		filepath = os.path.join(root, name)
		hex = hashlib.sha224(filepath).hexdigest()

		try:
			# Use Google Cloud to annotate images
			vision_labels = vision.get_vision_labels(filepath)
			vision_text = vision.get_vision_text(filepath)
			# More info on https://cloud.google.com/vision/docs/ocr

			vision_tags = {}
			for label in vision_labels:
				vision_tags[label.mid] = {
					'description': label.description,
					'score': label.score,
					'topicality': label.topicality
				}

			data[hex] = {
				'name': name,
				'path': filepath,
				'vision_tags': vision_tags,
				'vision_text': vision_text.text
			}

		except IOError:
			data[hex] = {
				'name': name,
				'path': filepath
			}

print(json.dumps(data,indent=4, sort_keys=True).encode('utf8'))