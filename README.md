# spython
codigos utiles de python
~~~python
import os

directorios =os.getcwd().split("\\")
directorio = directorios[len(directorios)-1]
a=os.listdir(".")	
for x in os.listdir("."): os.rename(x, x.replace("Screenshot_", directorio + " "))
~~~
# crear archivos para wordpress
~~~python
lista = ["header.php","footer.php","sidebar.php","front-page.php","home.php","single.php","page.php","category.php","comments.php","search.php","404.php","functions.php"]

for x in lista:
	file = open(x, "w")
	file.close()
~~~
# quitar un .mp4 extra 
~~~python
import os
a=os.listdir(".")


for x in range(len(a)) : a[x]=a[x].replace(".mp4", "")

for x in a : os.mkdir(x)
~~~
# no se que hace
~~~python
import os
directorios = os.listdir()
lista =["1.	Manual del tema","2.	Quien deberia leer este manual","3.	Qué es un tema","4.	Licencias de WordPress y la GPL","5.	Configuración de un entorno de desarrollo","6.	Ejemplos de desarrollo de temas","7.	Archivos de plantilla","8.	Hoja de estilos principal (style.css)","9.	Tipos de publicaciones","10.	Organizar archivos de tema","11.	Jerarquía de plantilla","12.	Etiquetas de plantilla","13.	El lazo","14.	Funciones temáticas","15.	Vinculación de archivos de tema y directorios","16.	Incluyendo CSS y JavaScript","17.	Etiquetas condicionales","18.	Categorías, etiquetas y taxonomías personalizadas","19.	Publicar archivos de plantilla","20.	Plantillas de página","21.	Archivos de plantilla de archivos adjuntos","22.	Archivos de plantilla de tipo de publicación personalizada","23.	Archivos de plantilla parciales y varios","24.	Plantilla de comentarios","25.	Plantillas de taxonomía","26.	404 páginas","27.	Menús de administración","28.	Encabezados personalizados","29.	Logotipo personalizado","30.	Formatos de publicaciones","31.	Puestos pegajosos","32.	la página de ","33.	Widgets","34.	Menús de navegación","35.	Paginación","36.	Medios de comunicación","37.	Audio","38.	Imágenes","39.	Galerías","40.	Seguridad del tema","41.	Vulnerabilidades Comunes","42.	Privacidad del tema","43.	Temas infantiles","44.	Mejores prácticas de IU","45.	Mejores prácticas de JavaScript","46.	ganchos. Lanzando su tema","47.	Pruebas","48.	Enviar su tema a WordPress.org","49.	Lista de etiquetas de plantilla","50.	Lista de etiquetas condicionales"]
for x in range(50): os.rename(directorios[x], lista[x]+".ogg")

# otro
import os

directorios =os.getcwd().split("\\")
directorio = directorios[len(directorios)-1]
a=os.listdir(".")	
for x in os.listdir("."): os.rename(x, x.replace("Screenshot_", directorio + " "))

~~~
