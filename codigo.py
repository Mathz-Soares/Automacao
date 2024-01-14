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
py.click(x=694, y=557)
time.sleep(3)

import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    py.click(x=556, y=282)
    py.write(tabela.loc[linha, "codigo"])
    py.press("tab")
    py.write(tabela.loc[linha, "marca"])
    py.press("tab")
    py.write(tabela.loc[linha, "tipo"])
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        py.write(obs)
    py.press("tab")
    py.press("enter")
    py.scroll(1000)

