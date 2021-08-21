# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 01:26:17 2020

@author: adil
"""
import telebot
from telebot import types
import random
import pandas as pd
#################
#Файл с исходной перепиской


from PIL import Image
#################




##############

bot=telebot.TeleBot('1337405770:AAFkZ6K6Hec3H9gcyctet8ZifzFeUIe8ulg') #ключ бота

def menu(n):
    if n == 1 :
        itembtn1 = types.KeyboardButton('Меню')
        itembtn2 = types.KeyboardButton('Корзина')
        itembtn3 = types.KeyboardButton('Оформить заказ')
        itembtn4 = types.KeyboardButton('О нас')
        itembtn5 = types.KeyboardButton('Мои заказы')
        itembtn6 = types.KeyboardButton('Связаться с менеджером')

        # or add KeyboardButton one row at a time:
        markup = types.ReplyKeyboardMarkup()
        markup.row(itembtn1)
        markup.row(itembtn2, itembtn3)
        markup.row(itembtn4)
        markup.row(itembtn5)
        markup.row(itembtn6)
        return markup
    if n == 2 :
        itembtn1 = types.KeyboardButton('Elf Bar 800')
        itembtn2 = types.KeyboardButton('Elf Bar 1500')
        itembtn3 = types.KeyboardButton('Оформить заказ')
        itembtn4 = types.KeyboardButton('Вернуться в меню')
        itembtn5 = types.KeyboardButton('Корзина')
        # or add KeyboardButton one row at a time:
        markup = types.ReplyKeyboardMarkup()
        markup.row(itembtn1, itembtn2)
        markup.row(itembtn3)
        markup.row(itembtn4, itembtn5)
        return markup
    if n == 3 :
        itembtn1 = types.KeyboardButton('Доставка')
        itembtn2 = types.KeyboardButton('Самовывоз')
        itembtn3 = types.KeyboardButton('Отмена')
        # or add KeyboardButton one row at a time:
        markup = types.ReplyKeyboardMarkup()
        markup.row(itembtn1)
        markup.row(itembtn2)
        markup.row(itembtn3)
        return markup
    if n == 4 :
        itembtn1 = types.KeyboardButton('Отмена')
        # or add KeyboardButton one row at a time:
        markup = types.ReplyKeyboardMarkup()
        markup.row(itembtn1)
        return markup

def inltext(n):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Добавить", callback_data=n)
    keyboard.add(callback_button)
    return keyboard
def ed_inltext(n):
        keyboard = types.InlineKeyboardMarkup()
        #callback_button = types.InlineKeyboardButton(text="Добавить", callback_data=n)
        itembtn1 = types.InlineKeyboardButton(text='1', callback_data='press')
        itembtn2 = types.InlineKeyboardButton(text='2', callback_data='press')
        itembtn3 = types.InlineKeyboardButton(text='3', callback_data='press')
        itembtn4 = types.InlineKeyboardButton(text='<', callback_data='<')
        itembtn5 = types.InlineKeyboardButton(text='>', callback_data='>')
        itembtn6 = types.InlineKeyboardButton(text='Отменить позицию', callback_data='exit')
        # or add KeyboardButton one row at a tme:

        keyboard.row(itembtn1,itembtn2,itembtn3)
        keyboard.row(itembtn4,itembtn5)
        keyboard.row(itembtn6)
        return keyboard
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет ' + message.chat.first_name +'!') #reply_markup=keyboard1
    #markup = types.ReplyKeyboardMarkup(row_width=2)
    bot.send_message(message.chat.id, '1', reply_markup=menu(1))
    #bot.send_message(message.chat.id, markup)
@bot.message_handler(content_types=['text'])
def send_text(message):
    #### перессылка данных мне)
    #bot.send_message(750886541,message.chat.first_name+':   '+message.text)
    ####
    #if message.chat.id==750886541:
    #    bot.send_message(637755131,message.text )#637755131,
    #    return
#########################
# поздороваться

    if 'Меню' == message.text:
        bot.send_photo(message.chat.id,photo=open('Elf_Bar_1500.png', 'rb'))
        bot.send_message(message.chat.id, 'Elf Bar 1500:', reply_markup=inltext(1))
        bot.send_photo(message.chat.id,photo=open('Elf_Bar_800.png', 'rb'))
        bot.send_message(message.chat.id, 'Elf Bar 1500:', reply_markup=inltext(2))

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='menu')
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, 'Для того, чтобы вернуться в меню и продолжить заказ нажмите на кнопку ', reply_markup=keyboard)
    #if 'Elf Bar 800'== message.text:


    #if 'Elf Bar 1500'== message.text:
    #    bot.send_photo(message.chat.id,photo=open('Elf_Bar_1500.png', 'rb'))

    if 'Вернуться в меню'== message.text:
        bot.send_message(message.chat.id, '1', reply_markup=menu(1))

    if 'Оформить заказ'== message.text:
        bot.send_message(message.chat.id, '1', reply_markup=menu(3))
    if 'Отмена'== message.text:
        bot.send_message(message.chat.id, '1', reply_markup=menu(1))
    if 'Самовывоз'== message.text:
        bot.send_message(message.chat.id, 'Заберите товар по адрессу ...', reply_markup=menu(1))
    if 'Доставка'== message.text:
        bot.send_message(message.chat.id, 'Ввеите ваш адресс:', reply_markup=menu(4))
    if 'Корзина'== message.text:
        bot.send_message(message.chat.id, 'На данный момент корзина пуста', reply_markup=menu(1))
    if 'О нас'== message.text:
        bot.send_message(message.chat.id, 'Официальный ретейлер пш пш',reply_markup=menu(1))
    if 'Мои заказы'== message.text:
        bot.send_message(message.chat.id, 'У вас еще нет заказов',reply_markup=menu(1))
    if 'Связаться с менеджером'== message.text:
        bot.send_message(message.chat.id, 'Номер: +77080070007',reply_markup=menu(1))
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="elf_1500  общая цена 1500")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,  reply_markup=ed_inltext(1))
            #bot.send_message(call.message.chat.id,"elf_1500")
        elif call.data == '2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="elf_800  общая цена 500")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,  reply_markup=ed_inltext(2))
            #bot.send_message(call.message.chat.id,"elf_800")
        elif call.data=='press' :
            keyboard = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="Добавлено", callback_data='test')
            callback_button2 = types.InlineKeyboardButton(text="Оформить заказ", callback_data="test")
            keyboard.row(callback_button1,callback_button2)

            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,  reply_markup=keyboard)
        else:
            bot.send_message(call.message.chat.id, call.data)


bot.polling() # как в ткинтере чтоб бот не выключался

