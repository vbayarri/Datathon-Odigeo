import io, os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# filepath = The filepath of the image file to annotate
def get_vision_labels(filepath):

	# Instantiates a client
	client = vision.ImageAnnotatorClient()
		
	# Loads the image into memory
	with io.open(filepath, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	return labels

def get_vision_text(filepath):

	# Instantiates a client
    client = vision.ImageAnnotatorClient()
		
	# Loads the image into memory
    with io.open(filepath, 'rb') as image_file:
		content = image_file.read()

    image = types.Image(content=content)

	# Performs text detection on the image file
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
	
    # Return detected text
    return document
	