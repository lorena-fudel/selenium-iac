from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Clase base que contiene funciones genéricas de Selenium que heredarán todas las páginas."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to(self, url):
        self.driver.get(url)

    def click(self, locator):
        """Espera a que un elemento sea clicable y le hace clic."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Espera a que un campo de texto esté disponible y escribe en él."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(text)
