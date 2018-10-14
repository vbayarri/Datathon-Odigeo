# Datathon-Odigeo

Code Used on Odigeo Datathon

# Información sobre los directorios

- data_sample: paquete inicial de imágenes y fichero con información de clasificación.
- scripts: utilidades de tratamiento de informacion. Requiere variable de entorno: GOOGLE_APPLICATION_CREDENTIALS
	- LocalImageInfo: retorna el tamaño de la imagen y sus datos EXIFF
	- GoogleImageInfo: retorna las labels de la imagen así como lo textos detectados
- data_sample_analysis:contiene los resultados de la ejecución de los scripts sobre el juego de datos data_sample.
	- google.json: información retornada por Google sobre los juegos de datos (gooble vision api + OCR)
	- local.json: información obtenida de las imágenes.
	- también contiene un script para pasar los resultados de formato json a csv.
- env: debe incluirse un json con las credenciales para llamar a Google. Ver https://cloud.google.com/vision/docs/libraries#client-libraries-install-python

# Información relevante:

	- Tamaño de las imágenes: 
		- No todas las imágenes están con las mismas dimensiones.
		- La mayoría son 1024x768, aunque también se encuentran fotos en 750x563, 533x400 y 768x576.
		- EXIF: 
			- Las imágenes contienen información de la ubicación de la toma en GPS en algunas fotografías.
	- Categoria de los hoteles:
		- GuestHouse se puede considerar Hostal o Bed&Breakfast
	- Google proporciona labels sobre las imágenes y el reconocimento de OCR está identificando textos de la fachada de los edificios (Hotel por ejemplo)

# Información del data sample.
- Todos los hoteles se han podido identificar en Google en diversos proveedores con el buscador de imágenes.

	ID,TYPE,Nombre
	--------------
	2447106,Hotel,Temple Bar Inn Dublin,
	2447109,Guesthouse,Adonis Paris Sud,Bed&Breakfast
	2450213,Hotel,Luxelthe,
	2450215,Hotel,Marquis Urban,
	2450217,Guesthouse,Hostal La Casa de Enfrente ,Hostal
	2450220,Guesthouse,Hostal San Vicente II,Hostal
