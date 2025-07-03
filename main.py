from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# ===================== CONFIGURACIÓN =====================
load_dotenv()
usuario = os.environ.get('USUARIO_FGA')
contrasena = os.environ.get("CONTRASENA_FGA")
url = 'https://gestion.fga.com.co/login'  
carpeta_cargues = r"C:\Users\57318\Cargues"

# ===================== CONFIGURAR CHROME =====================
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

# ===================== INICIAR SESIÓN =====================
driver.get(url)
driver.maximize_window()

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys(usuario)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(contrasena)
driver.find_element(By.XPATH, '//*[@id="frmIniciarSesion form-login"]/div[3]/div[2]/button').click()

# Navegar a sección de carga
sidebar_admin = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/li/div[1]/a')
))
sidebar_admin.click()

carga_gestion = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/li/div[1]/ul/li/div/a')
))
carga_gestion.click()

# ===================== PROCESO DE CARGA DE ARCHIVOS =====================

input_file = wait.until(EC.presence_of_element_located((By.ID, "archivo")))

# Listar archivos CSV en carpeta cargues
archivos_cargues = [f for f in os.listdir(carpeta_cargues) if f.endswith('.csv')]

for archivo in archivos_cargues:
    ruta_archivo = os.path.abspath(os.path.join(carpeta_cargues, archivo))
    
    # Subir archivo al input invisible
    input_file.send_keys(ruta_archivo)
    print(f"Cargando archivo: {archivo}")
    
    # Esperar proceso de carga + descarga del log (manual)
    time.sleep(30)  # Tiempo aproximado para que la página procese y descargue el log

    print("Esperando manualmente la descarga del log...")

print("Todos los cargues han sido procesados.")
driver.quit()

# ===================== CIERRE DEL NAVEGADOR =====================
