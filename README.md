# IAC Selenium Automation Test

Este repositorio documenta e implementa diversas estrategias de automatización de pruebas de interfaz de usuario usando **Selenium** y **Python** sobre la web del [Instituto de Astrofísica de Canarias](https://www.iac.es/).

## 📋 Requisitos Previos

- **Python 3.x** instalado.
- Navegadores preinstalados: Google Chrome, Microsoft Edge y Mozilla Firefox.
- Instalar las dependencias de este entorno ubicadas en `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

## 🏗️ Arquitectura Profesional (Pytest + POM)

Para escalar la automatización a niveles de entorno empresarial, se ha dividido y estructurado el código usando el patrón **Page Object Model (POM)** con el ejecutor automático **Pytest**:

- **`pages/`**: Contiene la lógica visual de las páginas de la web. Separando de este modo los selectores "Locators" (XPath y CSS) del test en sí.
  - `base_page.py`: Acciones universales como esperas dinámicas, clics y teclado.
  - `home_page.py`: Interacciones específicas (lupa, cookies, input de la home de la web del IAC).
- **`tests/`**: Dónde viven nuestros verdaderos reportes de calidad.
  - `conftest.py`: El cerebro oculto. Dispone de un _fixture_ mágico para abrir automáticamente y de fondo Chrome, Edge y Firefox, y limpiarlos al acabar sin tocar el test.
  - `test_busqueda.py`: Un bloque de código ultra-simple y en lenguaje casi natural que consume las directrices de la carpeta _pages_.

### 🚀 ¿Cómo lanzar los Tests Pro?

Al utilizar `pytest`, el sistema recogerá todos los tests independientemente y nos montará una infraestructura de reporting automático.
Para probarlo y ver cómo la búsqueda se repite transparentemente en los tres navegadores:

```bash
pytest --html=reporte.html
```
*Al terminar, busca e inspecciona el archivo `reporte.html` para ver un resumen formal de las pasadas del test.*

---

## 📙 Script Original y Básico (Versión de Introducción)

Si prefieres la forma lineal interactiva y aprender paso por paso, en el directorio raíz se encuentra `0-test-welcome-iac.py`.

###  ¿Qué hace el script simple?
1. Abre de forma consecutiva (y no las cierra) tres ventanas: Chrome, Edge y Firefox buscando la URL `https://www.iac.es/`.
2. Intercepta el diálogo de `Cookiebot` usando una espera dinámica (WebDriverWait) para denegarlo.
3. Simula la pulsación del buscador y expide la frase `ofertas de trabajo` presionando Enter automáticamente.

### ¿Cómo ejecutar el modo básico?
```bash
python 0-test-welcome-iac.py
```
