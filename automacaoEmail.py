import pyautogui
import time
pyautogui.PAUSE = 1.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://outlook.live.com/mail/0/"
pyautogui.write(link) 
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=169, y=268)
pyautogui.write("seu email aqui") 
pyautogui.click(x=581, y=463)
pyautogui.write("Teste envio email") 
pyautogui.click(x=623, y=526)
pyautogui.write("Oi, estou funcionando!") 
pyautogui.click(x=595, y=330)


