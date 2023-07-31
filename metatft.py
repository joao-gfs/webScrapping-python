from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

lista_comps = []

driver = webdriver.Firefox()

driver.get('https://www.metatft.com/')

sleep(3)

site = BeautifulSoup(driver.page_source, 'html.parser')

patch = site.find('h3', attrs={'class': 'HomePageBannerSubTitle'}).text
patch = patch.replace('Up to date for Patch ', '')

buttonComp = driver.find_element(By.LINK_TEXT, 'View Comps')

buttonComp.click()

sleep(3)

site = BeautifulSoup(driver.page_source, 'html.parser')

comps = site.findAll('div', attrs={'class': 'row_content'})

i = 0
for comp in comps:

    nome = comp.find('div', attrs={'class': 'Comp_Title'}).text

    posicao = comp.find('div', attrs={'class': 'Stat_Number'}).text
    posicao = float(posicao)

    pickRate = comp.find('div', attrs={'class': 'Stat_Number Stat_Number_Pick'}).text
    pickRate = float(pickRate)

    winRate = comp.find('div', attrs={'class': 'Stat_Number Stat_Number_Percent'}).text
    winRate = float(winRate.replace('%', ''))

    lista_comps.append([nome, posicao, pickRate, winRate])

    i+=1

print(f'{i} comps encontrada(s)')

planilha = pd.DataFrame(lista_comps, columns=['Nome', 'Posição Média', 'Pick Rate', 'Win Rate'])

planilha.to_excel(f'comps_{patch}.xlsx', index=False)

print(f'Planilha de comps para o patch {patch} gerada com sucesso!')