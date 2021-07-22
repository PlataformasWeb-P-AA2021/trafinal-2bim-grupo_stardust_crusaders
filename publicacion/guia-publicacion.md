# Guìa instalacion Nginx -x Ubuntu
1. Instalar la libreria gunicorn (get apt install gunicorn)
2. Agregar la variable **ALLOWED_HOSTS** en el archivo **settings.py** para permitir el acceso a gunicorn desde el servidor web 
**ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]**

   ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso2.jpeg)

3. Agregar en el archivo **urls.py** lo siguiente

   - importar
   
      **from django.contrib.staticfiles.urls import staticfiles_urlpatterns**

   - agregar el siguiente valor a la variable urlpatterns
   
      **urlpatterns += staticfiles_urlpatterns()**


   ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso3.jpeg)

4. Recopilar el contenido de la carpeta mediante la linea: **python manage.py collectstatic**

5. Levantar el proyecto en gunicorn a traves de: **gunicorn --bind 0.0.0.0:8000 trabajoFinal.wsgi**

   ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso5.jpeg)

6. Terminar la ejecucion del servicio a traves de Ctrl+c
7. En el directorio /etc/systemd/system/ agregar un archivo con la siguiente extension. (usar sudo para crearlo y editarlo)
   El nombre del archivo serà proyecto01
8. Iniciar y habilitar el proceso mediante los siguientes comandos
9. Verificar que todo este correcto
10. Verificar 

