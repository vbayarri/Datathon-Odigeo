import codecs
import json
import sys
import os

UTF8Writer = codecs.getwriter('utf8')

with open('google.txt') as json_file:
	with open('google.csv', 'w') as csv_file:
		output = UTF8Writer(csv_file)
		data = json.load(json_file)
		for attribute, value in data.iteritems():
			hash = attribute
			path = value['path']
			pname = os.path.split(os.path.dirname(path))[1]
			name = value['name']
			vtags = value['vision_tags']
			for attribute2, value2 in vtags.iteritems():
				id = attribute2
				description = value2['description']
				score = value2['score']
				topicality = value2['topicality']

				#default_order = "'{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(hash, pname, name, id, description, score, topicality)
				#output.write(default_order)
				output.write(hash + ";")
				output.write(pname + ";")
				output.write(name + ";")
				output.write(id + ";")
				output.write(description + ";")
				output.write(str(score) + ";")
				output.write(str(topicality) + ";")
				output.write('\n')

		csv_file.close() 
