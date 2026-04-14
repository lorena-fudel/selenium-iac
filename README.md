# IAC Selenium Automation Test

Este proyecto contiene un script automatizado usando Selenium (`0-test-welcome-iac.py`) diseñado para demostrar la automatización de pruebas multi-navegador sobre la web del **Instituto de Astrofísica de Canarias** (https://www.iac.es/).

## 📋 Requisitos Previos

- **Python 3.x**
- La librería de Selenium (se instala ejecutando `pip install selenium` en tu terminal).
- Navegadores soportados instalados: **Google Chrome**, **Microsoft Edge** y **Mozilla Firefox**.

## 🚀 ¿Qué hace el script?

Cuando se ejecuta, de forma secuencial por cada navegador, realiza el siguiente flujo:
1. Abre el navegador (Chrome, Edge y finalmente Firefox).
2. Navega a la web principal `https://www.iac.es/`.
3. Intercepta el banner de cookies (Cookiebot) que oscurece la pantalla, **esperando** a que cargue y pulsando automáticamente el botón de **rechazar cookies**.
4. Realiza una pequeña pausa consciente para que el banner desaparezca para siempre.
5. Busca el icono de herramientas del buscador en la esquina superior (la típica lupa) y le hace clic.
6. Localiza el campo de texto de la búsqueda, introduce las palabras `ofertas de trabajo`.
7. Envía un pulso de tecla `ENTER` para enviar la petición a la web y recargar la página.
8. Una vez terminados los tres navegadores, retiene las ventanas abiertas permanentemente para que puedas consultar cómo ha quedado el resultado de la búsqueda en cada pantalla por separado.

## 💻 ¿Cómo ejecutarlo?

Simplemente abre una terminal (o línea de comandos) en este mismo directorio y escribe:
```bash
python 0-test-welcome-iac.py
```
