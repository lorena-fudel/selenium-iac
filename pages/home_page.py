from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HomePage(BasePage):
    """Representa la página principal de la web del IAC."""
    
    # ---------------- LÓGICA POM: LOCATORS ----------------
    # Definimos como variables "dónde" están las cosas.
    # Si mañana cambian el diseño de la web, SOLO modificaremos estas 3 líneas.
    BOTON_RECHAZAR_COOKIES = (By.XPATH, "//*[@id='CybotCookiebotDialogBodyButtonDecline' or translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='denegar']")
    LUPA_BUSCADOR = (By.CSS_SELECTOR, ".search-icon, #block-searchicon")
    INPUT_BUSQUEDA = (By.ID, "edit-search")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.iac.es/"

    def cargar(self):
        """Abre la URL inicial."""
        self.go_to(self.url)

    def rechazar_cookies(self):
        """Lógica de negocio para rechazar cookies."""
        try:
            self.click(self.BOTON_RECHAZAR_COOKIES)
            time.sleep(1) # pausa visual
        except:
            print("El banner no ha aparecido o ya fue rechazado.")

    def buscar_texto(self, texto):
        """Lógica de negocio: Pulsa la lupa e introduce un texto."""
        self.click(self.LUPA_BUSCADOR)
        self.send_keys(self.INPUT_BUSQUEDA, texto)
        self.send_keys(self.INPUT_BUSQUEDA, Keys.RETURN)
