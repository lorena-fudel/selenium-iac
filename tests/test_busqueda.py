from pages.home_page import HomePage
import time

def test_buscar_ofertas_trabajo(driver):
    """
    Este es el test. Como puedes ver, no hay código complejo de Selenium aquí (ni import By, ni XPATH).
    Su escritura es casi lenguaje humano.
    """
    # 1. Instanciamos la página que creamos en POM
    home = HomePage(driver)
    
    # 2. Instrucciones que haríamos como usuario
    home.cargar()
    home.rechazar_cookies()
    home.buscar_texto("ofertas de trabajo")
    
    # Pausa solo para que te dé tiempo de contemplar el resultado 
    # (en entornos reales que corren fantasma, se quita la pausa)
    time.sleep(2)
    
    # 3. Y aquí meteríamos la Aserción (comprobación de calidad real):
    # Por ejemplo, comprobamos que en la URL resultante pone "search" o en el body
    assert "ofertas de trabajo" in driver.page_source.lower() or "search" in driver.current_url.lower()
