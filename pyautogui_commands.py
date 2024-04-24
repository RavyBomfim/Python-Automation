import pyautogui

# pyautogui - main commands (principais comandos)

# click (clicar) -> pyautogui.click
# write (escrever) -> pyautogui.write
# press a key (pressionar uma tecla) -> pyautogui.press
# hotkeys (teclas de atalho) -> pyautogui.hotkey
# scroll (rola a página) -> pyautogui.scroll
''' The scroll with a positive number will scroll the page up and with a negative number will scroll the page down. (O scroll com número positivo vai rolar a página para cima e com número negativo vai rolar a página para baixo.)'''

# Exs:
pyautogui.click()
pyautogui.write('Hello, world!')
pyautogui.press('capslock')
pyautogui.press('g')
pyautogui.press('win')
pyautogui.hotkey('ctrl', 'c')
pyautogui.scroll(1000) # Scroll the page up (Rola a página para cima)
pyautogui.scroll(-1000) # Scroll the page down (Rola a página para baixo)