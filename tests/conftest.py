import pytest
from selenium import webdriver

# Esta etiqueta @pytest.fixture hace que esta función sirva como una configuración mágica.
# Al pasar el array params=["chrome", "edge", "firefox"], Pytest ejecutará el MISMO tester 3 veces, 
# una vez en cada navegador de forma automática.
@pytest.fixture(params=["chrome", "edge", "firefox"], scope="function")
def driver(request):
    navegador = request.param
    
    # -------- SETUP (Preparación antes del test) --------
    if navegador == "chrome":
        driver_instance = webdriver.Chrome()
    elif navegador == "edge":
        driver_instance = webdriver.Edge()
    elif navegador == "firefox":
        driver_instance = webdriver.Firefox()

    driver_instance.maximize_window()
    
    # Entrega el control del navegador abierto al test
    yield driver_instance
    
    # -------- TEARDOWN (Limpieza después del test) --------
    # Cuando el test acaba, cierra la ventana pase lo que pase, para evitar fuga de memoria
    driver_instance.quit()
