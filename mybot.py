import telebot
import mysql.connector

import tokenbot

from datetime import datetime
TOKEN=tokenbot.TOKEN
Bot = telebot.TeleBot(TOKEN)
database=mysql.connector.connect(host='localhost',user='root',password='',database='apotik')
sql=database.cursor()
from telebot import apihelper
today=datetime.now()

class mybot:
    def __init__(self):
        self.message

    @Bot.message_handler(commands=['start'])
    def start(message):
        replyStart = tokenbot.HELLO + "\n Yang Membuat Masih belajar :)" +"\n @Akmalsukma"+"\n" \
                        "hari ini tanggal "+str(today)
        Bot.reply_to(message, replyStart)


    @Bot.message_handler(commands=['dataobat'])
    def data_obat(message):
        query="SELECT kode_obat,nama_obat,kegunaan_obat FROM obat"
        sql.execute(query)
        selectdata=sql.fetchall()
        rowdata=sql.rowcount
        data=''
        if(rowdata>0):
            # print(selectdata[0])
            no=0
            for x in selectdata:
                no+=1
                data=data+ str(x)
                data=data.replace('(','')
                data = data.replace("'", "")
                data = data.replace(',', '')
                data = data.replace(')', '\n')
                #print(data)
        else:
            print('Data Obat Kosong')

        Bot.reply_to(message,str(data))

print("Bot working")
Bot.polling(none_stop=True)