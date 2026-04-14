# Uso de Selenium y Pytest en el Desarrollo de Software

La automatización construida con herramientas como Selenium es la base de lo que en el ecosistema de calidad de software se conoce como **Automatización de Pruebas de Interfaz de Usuario (UI)** o **Pruebas End-to-End (E2E)**.

Se diferencian de las pruebas unitarias en que no prueban una función matemática en el *back-end*, sino el sistema vivo real desde los zapatos de un usuario final humano.

### Las 3 Capas de la Automatización UI en la Industria:

#### 1. Casos de Uso Diarios (El "Por qué" lo usamos)
* **Pruebas E2E**: Localizar elementos visuales, abrir menús interactivos, teclear o emular flujos completos como iniciar sesión en un portal.
* **Pruebas de Regresión**: Blindajes del código. Evita que un nuevo cambio en el HTML o en el API rompa funcionalidad fundamental del pasado.
* **Cross-Browser Testing**: Escalar un test en los diferentes ecosistemas del cliente (Chrome en Windows, Safari en MacOS).

#### 2. Frameworks de Prueba (Ej: `pytest`)
Nadie aúna "tests" bajo scripts independientes. El nivel profesional requiere herramientas automatizadas para la recogida de métricas:
* **Ejecución Centralizada:** Capacidad para poner a buscar 10 o 500 pruebas funcionales de una tacada mediante un único comando en terminal (`pytest`).
* **Reporting:** Generación automática de reportes XML/HTML (`pytest-html`) sobre lo que ha pasado, sin tener que analizar visualmente la consola.
* **Setups & Teardowns (Fixtures):** Pytest delega la carga inicial y el cerrado/limpiado del navegador (ej: el borrado de las cookies residuales) a los ficheros como `conftest.py`, dejando el foco íntegramente al Test.

#### 3. Page Object Model (El patrón rey: POM)
Es el patrón de arquitectura más estandarizado a nivel mundial para escribir rutinas de Selenium:
* Promueve un mantenimiento inteligente e inquebrantable de los scripts.
* Separa la **Capa Estructural** (los Locators CSS, XPath...) en "Páginas", fuera del espacio interactivo.
* Separa la **Capa Lógica** (el código `test`) de manera que las comprobaciones de QA tengan forma del lenguaje humano (*ej: cargar(), buscar("botón")*). ¡Si cambia una imagen en el Front-End, no tocas nunca el test en sí mismo, sencillamente ajustas la variable del elemento en la página (POM)!

---

**Resumen general del flujo:** En un entorno laboral, toda esta arquitectura orientada a objetos usando POM y Pytest viviría dentro del repositorio troncal. En el momento en que un programador haga `git push` a "producción", un sistema automático bajará todo tu código, preparará los *Fixtures* e internamente validará mediante comprobaciones (Asserts) que tu Test de búsqueda haya dado luz verde.
