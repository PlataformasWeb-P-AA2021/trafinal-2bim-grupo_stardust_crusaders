# Guìa instalacion Nginx -x Ubuntu
1. Instalar la libreria gunicorn (get apt install gunicorn)
2. Agregar la variable **ALLOWED_HOSTS** en el archivo **settings.py** para permitir el acceso a gunicorn desde el servidor web 
**ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]**
3. Agregar en el archivo **urls.py** lo siguiente(archivos para manejo de static)
4. Recopilar el contenido de la carpeta mediante la linea **python manage.py collectstatic**
5. Levantar el proyecto en gunicorn.
6. Terminar la ejecucion del servicio a traves de Ctrl+c
7. En el directorio /etc/systemd/system/ agregar un archivo con la siguiente extension. (usar sudo para crearlo y editarlo)
   El nombre del archivo serà proyecto01
8. Iniciar y habilitar el proceso mediante los siguientes comandos
9. Verificar que todo este correcto
10. Verificar 

