import pyautogui
import time

while True:
    # Obtiene las coordenadas del mouse actual
    x, y = pyautogui.position()

    # Haz clic en la posición actual del mouse
    pyautogui.click(x, y)

    # Espera 30 segundos antes de hacer clic nuevamente
    time.sleep(30)
