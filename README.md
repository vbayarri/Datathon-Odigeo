# Datathon-Odigeo
Code Used on Odigeo Datathon

# Información sobre los directorios
- data-sample: paquete inicial de imágenes y fichero con información de clasificación.
- scripts: utilidades de tratamiento de informacion. Requiere variable de entorno: GOOGLE_APPLICATION_CREDENTIALS
	- LocalImageInfo: retorna el tamaño de la imagen y sus datos EXIFF
	- GoogleImageInfo: retorna las labels de la imagen así como lo textos detectados
- env: debe incluirse un json con las credenciales para llamar a Google. Ver https://cloud.google.com/vision/docs/libraries#client-libraries-install-python

# Información relevante:
	- Tamaño de las imágenes: 
		- No todas las imágenes están con las mismas dimensiones.
		- La mayoría son 1024x768, aunque también se encuentran fotos en 750x563, 533x400 y 768x576.
	- EXIF: 
		- Las imágenes contienen información de la ubicación de la toma en GPS en algunas fotografías.
	