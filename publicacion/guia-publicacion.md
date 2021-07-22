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

   El nombre del archivo serà **proyecto01.service**

   ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso7.jpeg)

8. Iniciar y habilitar el proceso mediante los siguientes comandos

   - **sudo systemctl start proyecto01**
   
   - **sudo systemctl enable proyecto01**

9. Verificar que todo este correcto mediante el comando: **sudo systemctl status proyecto01**

   ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso9.jpeg)

10. Verificar que el archivo **aplication.sock** esté creado en el directorio del proyecto. 

      ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso10.jpeg)
 
11. Se asume que se encuentra instalado nginx, sino utilizamos el comando: **pip install nginx**

   - Los comandos para iniciar, reiniciar, parar y verificar el servicio son:

      - sudo service nginx start
      - sudo service nginx stop
      - sudo service nginx restart
      - sudo service nginx status

12. Crear el archivo **sites-available** de nginx.

    - La ruta de acceso es: **/etc/nginx/sites-available/**. Se debe ingresar con permisos de administrador (sudo).
    
     - Para crear el archivo usamos el comando: **sudo touch /etc/nginx/sites-available/proyecto01**
     
     - La estrucura del archivo es la siguente:
     
     ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso12.jpeg)
     
13. Iniciar un enlace simbólico del archivo creado en el directorio sites-available. 

      - **sudo ln -s /etc/nginx/sites-available/proyecto01 /etc/nginx/sites-enabled**

14. Iniciar o reiniciar el servicio de nginx a traves de los comandos especificados en el paso 11


      ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso14.jpeg)
      
15. Si todo marcha bien, en un navegador se debe deplegarara el proyecto a través de nginx: **http://0.0.0.0:81**


      ![foo](https://github.com/PlataformasWeb-P-AA2021/trafinal-2bim-grupo_stardust_crusaders/blob/main/img/paso15.jpeg)
     



 
