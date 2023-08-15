import telebot
from bs4 import BeautifulSoup
import requests
from PIL import Image
import time

#токен бота
token = ""
#ссылка на тг канал(@ссылка)
channel_id = "@"
bot = telebot.TeleBot(token)

#ссылка на сайт
URL = ""
#загрузка главной страницы
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#выбор div с содержанием
post = soup.find("div", class_="card")
#получение названия поста
title1 = soup.find("h2",class_="h5 mb-025 mt-0").find('a').getText()

#загрузка 2 страницы
URL2 = soup.find("h2",class_="h5 mb-025 mt-0").find('a').get("href")
page2 = requests.get(URL2)
soup2 = BeautifulSoup(page2.content, "html.parser")
#получение версий
version_1 = soup2.findAll('a' ,class_="green")

#получение ссылки на фото
img = soup2.find("div", class_="max-w-750 mr-center text-center").find("img").get("data-lazy-src")
print(img)

#заргузка 3 страницы с файлам
URL3 = soup2.find("div",class_="row gap-1 align-items-center mt-125").find('span').get("data-link")
page3 = requests.get(URL3)
soup3 = BeautifulSoup(page3.content, "html.parser")

#ожидание 6 секунд и получение ссылки на файл
time.sleep(6)
file1 = soup3.find("a", class_="btn btn--green btn--green--big btn--icon-normal btn--extra-green").get("href")
print (file1)

version_join = []
version_out = []
l = 0
j= len(version_1)
version_join = []
version_out_2=[]

#проверка и добавление версии
while l < j:
    version_out_2 =  version_1[l].getText() 
    version_join.append(version_out_2)
    if version_join[l] == '1.15':
        version_out.append("1.15")
    if version_join[l] == '1.16':
        version_out.append("1.16")    
    if version_join[l] == '1.17':
        version_out.append("1.17")    
    if version_join[l] == '1.18':
        version_out.append("1.18")  
    if version_join[l] == '1.19':
        version_out.append("1.19")  
    if version_join[l] == '1.20':
        version_out.append("1.20") 
    l = l+1   

info = title1
teg_version = []
i = 0
ii = len(version_out)

#добавление тега по версии
while i < ii:
    if version_out[i] == '1.20':
        teg_version.append("#м120")
    if version_out[i] == '1.19':
        teg_version.append("#м119")
    if version_out[i] == '1.18':
        teg_version.append("#м118")
    if version_out[i] == '1.17':
        teg_version.append("#м117") 
    if version_out[i] == '1.16':
        teg_version.append("#м116")  
    if version_out[i] == '1.15':
        teg_version.append("#м115")                                                              
    i = i+1

n0 = " "
n1 = "▻мод майнкрафт пе."
n2 = "▻версия:" 
n3 = "▻" + info
n4 = " , #пе " ", #мод"
n5 = "▻Канал по модам: https://t.me/minemob1"
n6 =  ((' , '.join(teg_version)))
n7 =  ((' , '.join(version_out)))    

#загрузка файла
def download_file(url=''):
    try:
        response = requests.get(url=url)
        with open(info + '.zip', 'wb') as file:
            file.write(response.content)
        return '+' 

    except Exception as _ex:
        return '-'
def main():
    print(download_file(url=file1))    

if __name__ == '__main__':
    main()    

#проверочный текст поста
print ( n1,n2 + n7,n3,n0,n6 + n4, n5 ,sep="\n" )

#публикация фото + текст и отдельным сообщением файла
@bot.message_handler(content_types=['text'])
def commands(message):
    text =f'▻мод майнкрафт пе.\n▻версия: {n7}\n▻ {info} \n {n0} \n{n6} , #пе , #мод\n ▻Канал по модам: https://t.me/minemob1'
    bot.send_photo(channel_id, (img) , (text))
    bot.send_document(channel_id, open(info + '.zip', 'rb'))
    
bot.polling()
