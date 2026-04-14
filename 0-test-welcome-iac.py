from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def rechazar_cookies(driver, navegador):
    try:
        print(f"[{navegador}] Esperando banner de cookies...")
        wait = WebDriverWait(driver, 10)
        # La web del IAC usa Cookiebot. El botón para denegar habitualmente tiene el ID CybotCookiebotDialogBodyButtonDecline
        # También añadimos un selector flexible por si acaso.
        boton_rechazar = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='CybotCookiebotDialogBodyButtonDecline' or translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='denegar' or translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='rechazar']")
        ))
        boton_rechazar.click()
        print(f"[{navegador}] Cookies rechazadas con éxito.")
        time.sleep(1) # Pequeña pausa para asegurar que el banner desaparece
    except Exception as e:
        print(f"[{navegador}] No se encontraron o no se pudieron rechazar las cookies.")

def buscar_ofertas(driver, navegador):
    try:
        print(f"[{navegador}] Buscando icono de la lupa...")
        wait = WebDriverWait(driver, 10)
        
        # Buscar el icono de la lupa
        lupa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-icon, #block-searchicon")))
        lupa.click()
        
        print(f"[{navegador}] Escribiendo 'ofertas de trabajo' en el buscador...")
        input_buscar = wait.until(EC.element_to_be_clickable((By.ID, "edit-search")))
        input_buscar.send_keys("ofertas de trabajo")
        input_buscar.send_keys(Keys.RETURN)
        print(f"[{navegador}] Búsqueda de ofertas enviada con éxito.")
    except Exception as e:
        print(f"[{navegador}] Error durante la búsqueda: {e}")

def main():
    url = "https://www.iac.es/"

    print("Abriendo Google Chrome...")
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver_chrome = webdriver.Chrome(options=chrome_options)
    driver_chrome.get(url)
    rechazar_cookies(driver_chrome, "Chrome")
    buscar_ofertas(driver_chrome, "Chrome")

    print("\nAbriendo Microsoft Edge...")
    edge_options = EdgeOptions()
    edge_options.add_experimental_option("detach", True)
    driver_edge = webdriver.Edge(options=edge_options)
    driver_edge.get(url)
    rechazar_cookies(driver_edge, "Edge")
    buscar_ofertas(driver_edge, "Edge")

    print("\nAbriendo Mozilla Firefox...")
    # Firefox no tiene la opción 'detach' nativa como Chromium, 
    # por lo que evitamos que se cierre manteniendo el script de Python en ejecución.
    driver_firefox = webdriver.Firefox()
    driver_firefox.get(url)
    rechazar_cookies(driver_firefox, "Firefox")
    buscar_ofertas(driver_firefox, "Firefox")
    
    print("\n¡Los tres navegadores han sido configurados y han realizado la búsqueda!")
    print("Presiona la tecla Enter en esta consola para finalizar el script y cerrar Firefox.")
    input()

if __name__ == "__main__":
    main()
