# Uso de Selenium en el Desarrollo de Software

La automatización que hemos construido con Selenium es la base de lo que en la industria se conoce como **Automatización de Pruebas de Interfaz de Usuario (UI)** o **Pruebas End-to-End (E2E)**.

Dentro del desarrollo de software profesional, Selenium cumple ciertos propósitos clave:

### 1. Pruebas End-to-End (Simular al usuario real)
En desarrollo, no basta con probar bloques aislados de código en back-end (pruebas unitarias). Selenium permite controlar visualmente la pantalla como lo haría una persona humana: localiza botones, abre menús, teclea contraseñas y hace clics. Su objetivo es confirmar que "el viaje completo" funciona tal y como lo experimentaría el usuario final.

### 2. Pruebas de Regresión (Impedir que se rompa el pasado)
Al desarrollar una funcionalidad nueva o arreglar un bug, es fácil romper en el proceso algo que ya funcionaba. Antes de mandar los cambios a producción, los equipos corren automáticamente baterías de tests en Selenium (similares al creado aquí) para asegurarse de que una nueva actualización en el buscador, por ejemplo, no haya estropeado el menú principal que funcionaba perfectamente.

### 3. Pruebas Multi-Navegador (Cross-Browser Testing)
Asegura que tu desarrollo se comporta correctamente sea cual sea el visor que utiliza el cliente. Si un script en JavaScript de tu nueva página despliega un menú en Edge pero falla en Firefox, correr estos tests te permitirá ver el fallo en seguida sin requerir probar navegador por navegador a mano.

### 4. Automatización de Tareas (Botting) y "Web Scraping"
Pese a que nació para testing, muchos programadores usan toda esta estructura para automatizar flujos repetitivos y burocráticos (ej. bajar un reporte a fin de mes de un portal corporativo interno) o para extraer inteligentemente (Web Scraping) millones de registros de pantallas dinámicas donde librerías simples de backend no sirven.

---

**Resumen general del flujo:** En un entorno laboral, este simple script se subiría a la nube o a unos entornos llamados de integración continua. Cada vez que el equipo guarde nuevo código de la web del IAC, estos "robots" probarían independientemente los clics y campos, garantizando un sello de calidad mínimo antes del despliegue en un servidor público.
