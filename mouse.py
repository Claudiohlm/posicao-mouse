import pyautogui
import time

print("Mova o mouse. Pressione CTRL+C para parar.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}  Y: {y}", end="\r")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nEncerrado.")