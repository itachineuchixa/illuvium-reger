# -*- coding: utf-8 -*-

import requests
from random import choice, randint
import time


#input mails and proxy
print(""" 
╔══╗╔╗─╔╗─╔╦╗╔╗─╔╗╔══╗╔╦╗╔═╦═╗
╚║║╝║║─║║─║║║║╚╦╝║╚║║╝║║║║║║║║
╔║║╗║╚╗║╚╗║║║╚╗║╔╝╔║║╗║║║║║║║║
╚══╝╚═╝╚═╝╚═╝─╚═╝─╚══╝╚═╝╚╩═╩╝""")
inputmail = input("Перетяните файл с  почтами:")
proxyuse = input("Использовать фри прокси? y/n: ")
with open(inputmail, 'r', encoding="UTF-8") as file:
    mails = [row.strip() for row in file]
mail=[]
for x in mails:
        mail.append(x.split(";")[0])
def take_random_proxy():
        with open('freeproxy.txt', 'r') as file:
                proxies = [row.strip() for row in file]


        return choice(proxies)
#main function
def mainth(mail):
        headers = {'accept':'*/*', 'accept-language':'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,cy;q=0.6', 'cache-control':'no-cache', 'pragma':'no-cache', 'sec-ch-ua':'\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Microsoft Edge\";v=\"100\"', 'sec-ch-ua-mobile':'?0', 'sec-ch-ua-platform':'\"Windows\"', 'sec-fetch-dest':'script', 'sec-fetch-mode':'no-cors', 'sec-fetch-site':'cross-site'}
        if proxyuse == 'y' or proxyuse == 'Y':

                proxi = str(take_random_proxy())
                proxy_type = proxi.split('"host": "')[1].split('"')[0]
                proxy_port = proxi.split('"port": ')[1].split(',')[0]
                proxies = {'http': f'http://{proxy_type}:{proxy_port}'}
                req = requests.get(f"https://illuvium.us1.list-manage.com/subscribe/post-json?u=fb9311e6ac7efeb35ab7fd1f0&id=653b53d09f&EMAIL={mail}&c=__jp0", headers=headers, proxies=proxies)
        else:

                req = requests.get(f"https://illuvium.us1.list-manage.com/subscribe/post-json?u=fb9311e6ac7efeb35ab7fd1f0&id=653b53d09f&EMAIL={mail}&c=__jp0", headers=headers)
        if req.text == '__jp0({"result":"success","msg":"Thank you for subscribing!"})':
                print(f"Почта {mail} успешно зарегистрирована!")
        time.sleep(3)
        if req.text != '__jp0({"result":"success","msg":"Thank you for subscribing!"})':
                print("Произошла ошибка!")
                time.sleep(15)


if __name__ == '__main__':
        for i in range(len(mail)):
                mainth(mail[i])