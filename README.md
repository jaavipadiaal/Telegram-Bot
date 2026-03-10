# Telegram Bot con Docker

Este es un bot de Telegram programado en Python que utiliza la librería `pyTelegramBotAPI`. El bot está diseñado para ser ejecutado dentro de un contenedor Docker para facilitar su despliegue y gestión.

## Funcionalidades
* Responde a los comandos `/start` y `/hola`.
* Implementa un efecto "eco": repite cualquier otro mensaje que reciba.

## Requisitos previos
* [Docker](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.
* Un token de bot obtenido a través de [@BotFather](https://t.me/botfather) en Telegram.

## Configuración
1. Clona este repositorio.
2. Crea un archivo llamado `token.txt` en la raíz del proyecto.
3. Añade tu token en el archivo con el siguiente formato:
   
   ```text
   
     BOT_TOKEN=tu-token-aqui
   
   ```

## Como ejecutar el bot
1. Construir la imagen de docker
   
      ```text
      
      docker build -t telegram-bot-app .
      
      ```
2. Ejecutar el contenedor
      ```text
      
      docker run -dti --env-file token.txt --name javierpg-bot telegram-bot-app
          
      ```

## Gestion del contenedor
1. Ver estado
   
      ```text
      
      docker ps
      
      ```
2. Detener el bot
      ```text
      
      docker stop javierpg-bot
         
      ```
3. Eliminar el bot
      ```text
      
      docker rm javierpg-bot
               
      ```

---

## Autor
Proyecto desarrollado Bot Telegram del [IES Zaidín Vergeles](https://www.ieszaidinvergeles.org/).

* **Desarrollador:** Javier Padial González
* **Tecnologías utilizadas:** Python, Docker, Telegram Bot API.
* **Año:** 2026
