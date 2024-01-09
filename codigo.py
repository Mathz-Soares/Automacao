import pyautogui as py
import time

py.press("Win")
time.sleep(1)
py.write("Opera")
time.sleep(1)
py.press("enter")
time.sleep(3)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
py.press("enter")
time.sleep(3)
py.press("tab")
time.sleep(1)
email = "anyemail@gmail.com"
py.write(email)
time.sleep(1)
py.press("tab")
time.sleep(1)
senha = "12345"
py.write(senha)
time.sleep(2)
py.press("tab")
py.press("enter")
