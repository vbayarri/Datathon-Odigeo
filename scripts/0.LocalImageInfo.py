#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import hashlib
import json
import os
import sys

import argparse_actions
import exifread
from PIL import Image

import exif_gps

# Program usage with arguments
parser = argparse.ArgumentParser(description='Obtain image information for files in image directories.')
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
			# Open image
			im=Image.open(filepath)
		
			# Open image file for reading exif info(binary mode)
			f = open(filepath, 'rb')
			exif_tags = exifread.process_file(f)
			f.close()

			# Mostrar el contenido de tags
			#for exif_tag in exif_tags:
			#	print exif_tag

			# Obtain exif information from image
			exiflocation = exif_gps.get_exif_location(exif_tags)
			exifdocname = exif_gps._get_if_exist(exif_tags, 'DocumentName')
			exifimgdesc = exif_gps._get_if_exist(exif_tags, 'ImageDescription')
			
			data[hex] = {
				'name': name,
			 	'path': filepath,
			 	'size': im.size,
			 	'EXIFF Location': exiflocation,
				'EXIFF DocumentName': exifdocname,
				'EXIFF ImageDescription': exifimgdesc
			}

			# Close image
			im.close()

		except IOError:
			data[hex] = {
				'name': name,
				'path': filepath
			}

print(json.dumps(data,indent=4, sort_keys=True).encode('utf8'))
