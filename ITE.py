import telebot
#from fpdf import FPDF
import requests
from io import BytesIO
import os 
bot = telebot.TeleBot('6468165247:AAE39qKs8XZRvQwH6K3jfUrGr-LxghIoUD0')
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
#from googleapiclient.discovery import build
#from google.oauth2 import service_account
import threading


class User:
    def __init__(self):
        self.navigation_stack = []

users = {}
#الهندسة المعلوماتية


lock = threading.Lock()
def go_back(chat_id):
    user = users.get(chat_id)
    if user is None:
        return

    if len(user.navigation_stack) > 1:
        user.navigation_stack.pop()
        previous_message = user.navigation_stack[-1]
        bot.send_message(previous_message[0], previous_message[1], reply_markup=previous_message[2])
    else:
        bot.send_message(chat_id, "GO TO /start PLEASE")
        
 #Back button handler
@bot.message_handler(func=lambda message: message.text == 'Back')
def handle_back(message):
    chat_id = message.chat.id
    go_back(chat_id)   
    
@bot.message_handler(commands=['start','START','HELP','help','ابدا','ابدأ'])
def start(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('الهندسة المعلوماتية(ITE)')

    markup.row(item1)


    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id, "انقر على الزر:", markup))
    bot.send_message(chat_id, "انقر على الزر:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'الهندسة المعلوماتية(ITE)')
def handle_tic_subject(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item15 = telebot.types.KeyboardButton('(ITE)السنة الاولى')
    item16 = telebot.types.KeyboardButton('(ITE)السنة الثانية')
    item17 = telebot.types.KeyboardButton('(ITE)السنة الثالثة')
    item18 = telebot.types.KeyboardButton('مقررات اختصاص هندسة البرمجيات (SE)')
    item19 = telebot.types.KeyboardButton('مقررات اختصاص الذكاء الصنعي (AI)')   
    item10000001 = telebot.types.KeyboardButton('مقررات اختصاص النظم والشبكات الحاسوبية (SCN)')
    item2=telebot.types.KeyboardButton('مقررات اختصاص الأمن السيبراني (CS)')
    back_button = telebot.types.KeyboardButton('Back')  

    markup.row(item15,item16)
    markup.row(item17,item18)
    markup.row(item19,item10000001)
    markup.row(item2)
    markup.row(back_button)
    
    
    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  "اختر سنة دراسية أو أرسل رمز المادة", markup))
    bot.send_message(chat_id, "اختر سنة دراسية أو أرسل رمز المادة", reply_markup=markup)

#-----------------------------------------السنة الاولى---------------------------------
@bot.message_handler(func=lambda message: message.text == '(ITE)السنة الاولى')
def handle_first_year(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item44 = telebot.types.KeyboardButton('البرمجة 1 (BPG401)')
    item45 = telebot.types.KeyboardButton('1 التحليل الرياضي (BMA401)')
    item46 = telebot.types.KeyboardButton('انجليزي 1 (L1)')
    item47 = telebot.types.KeyboardButton('الفيزياء (BPH401)')
    item48 = telebot.types.KeyboardButton('الهيكلة الجبرية (BAS401)')
    item49 = telebot.types.KeyboardButton('مهارات الحاسوب (GCS301)')
    item50 = telebot.types.KeyboardButton('التعليم الالكتروني (GOE301)')
    item51 = telebot.types.KeyboardButton('مهارات التواصل (GWT301)')
    item52 = telebot.types.KeyboardButton('الجبر الخطي (BLA401)')
    item53 = telebot.types.KeyboardButton('التحليل الرياضي 2 (BMA402)')
    item54 = telebot.types.KeyboardButton('انجليزي 2 (L2)')
    item55 = telebot.types.KeyboardButton('الدارات الالكترونية (BEC401)')
    item56 = telebot.types.KeyboardButton('الدارات المنطقية (BLC401)')
    item57 = telebot.types.KeyboardButton('البرمجة 2 (BPG402)')
    back_button = telebot.types.KeyboardButton('Back')



    markup.row(item44,item45)
    markup.row(item46,item47)
    markup.row(item48,item49)
    markup.row(item50,item51)
    markup.row(item52,item53)
    markup.row(item54,item55)
    markup.row(item56,item57)
    markup.row(back_button)
    
    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)



#'البرمجة 1
@bot.message_handler(func=lambda message: message.text == 'البرمجة 1 (BPG401)')
def handle_BPGI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BPG401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BPG401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BPG401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   




#'1 التحليل الرياضي
@bot.message_handler(func=lambda message: message.text == '1 التحليل الرياضي (BMA401)')
def handle_BMAI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BMA401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BMA401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BMA401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    



#'انجليزي 1 
@bot.message_handler(func=lambda message: message.text == 'انجليزي 1 (L1)')
def handle_L1I(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of L1'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of L1'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of L1'))

    bot.send_message(message.chat.id, 'انقر الزر لتحميل الملف:', reply_markup=markup)  
    


#'الفيزياء
@bot.message_handler(func=lambda message: message.text == 'الفيزياء (BPH401)')
def handle_BPHI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BPH401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BPH401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BPH401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   




#'الهيكلة الجبرية
@bot.message_handler(func=lambda message: message.text == 'الهيكلة الجبرية (BAS401)')
def handle_BASI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BAS401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BAS401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BAS401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   



#'مهارات الحاسوب
@bot.message_handler(func=lambda message: message.text == 'مهارات الحاسوب (GCS301)')
def handle_GCSI301(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of GCS301'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of GCS301'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of GCS301'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  




#'التعليم الالكتروني
@bot.message_handler(func=lambda message: message.text == 'التعليم الالكتروني (GOE301)')
def handle_GOEI301(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of GOE301'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of GOE301'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of GOE301'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   




#'مهارات التواصل 
@bot.message_handler(func=lambda message: message.text == 'مهارات التواصل (GWT301)')
def handle_GWTI301(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of GWT301'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of GWT301'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of GWT301'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   




#'الجبر الخطي
@bot.message_handler(func=lambda message: message.text == 'الجبر الخطي (BLA401)')
def handle_BLAI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BLA401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BLA401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BLA401'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
  






#'التحليل الرياضي 2
@bot.message_handler(func=lambda message: message.text == 'التحليل الرياضي 2 (BMA402)')
def handle_BMAI402(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BMA402'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BMA402'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BMA402'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    



#'انجليزي 2
@bot.message_handler(func=lambda message: message.text == 'انجليزي 2 (L2)')
def handle_E2I(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of L2'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of L2'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of L2'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
 


#'الدارات الالكترونية
@bot.message_handler(func=lambda message: message.text == 'الدارات الالكترونية (BEC401)')
def handle_BECI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BEC401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BEC401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BEC401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    




#'الدارات المنطقية
@bot.message_handler(func=lambda message: message.text == 'الدارات المنطقية (BLC401)')
def handle_BLCI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BLC401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BLC401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BLC401'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
    










#'البرمجة 2   
@bot.message_handler(func=lambda message: message.text == 'البرمجة 2 (BPG402)')
def handle_BPGI402(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BPG402'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BPG402'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BPG402'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   






#----------------------------------------السنة الثانية-------------------------------------------- 
@bot.message_handler(func=lambda message: message.text == '(ITE)السنة الثانية')
def handle_second_year(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item58 = telebot.types.KeyboardButton('بنى المعطيات والخوارزميات (BDA501)')
    item59 = telebot.types.KeyboardButton('انجليزي 3 (L3)')
    item60 = telebot.types.KeyboardButton('تحليل عددي (BNA401)')
    item61 = telebot.types.KeyboardButton('برمجة الويب  1 (BWP401)')
    item62 = telebot.types.KeyboardButton('بنيان الحاسوب  1 (BCA501)')
    item63 = telebot.types.KeyboardButton('معالجة الاشارة (BSP501)')
    item64 = telebot.types.KeyboardButton('أساليب الادارة (GMN401)')
    item65 = telebot.types.KeyboardButton('نظم الاتصالات (BTS501)')
    item66 = telebot.types.KeyboardButton('رياضيات متقطعة (BDM501)')
    item67 = telebot.types.KeyboardButton('نظم قواعد البيانات 1 (BDB501)')
    item68 = telebot.types.KeyboardButton('برمجة الويب  2 (BWP501)')
    item69 = telebot.types.KeyboardButton('انجليزي 4 (L4)')
    item70 = telebot.types.KeyboardButton('مخبر نظم قواعد البيانات (BDBL501)')
    back_button = telebot.types.KeyboardButton('Back')

    markup.row(item58,item59)
    markup.row(item60,item61)
    markup.row(item62,item63)
    markup.row(item64,item65)
    markup.row(item66,item67)
    markup.row(item68,item69)
    markup.row(item70)
    markup.row(back_button)

    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)


#'بنى المعطيات والخوارزميات 
@bot.message_handler(func=lambda message: message.text == 'بنى المعطيات والخوارزميات (BDA501)')
def handle_BDAI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BDA501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BDA501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BDA501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    


#'انجليزي 3
@bot.message_handler(func=lambda message: message.text == 'انجليزي 3 (L3)')
def handle_L3I(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of L3'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of L3'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of L3'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  



#'تحليل عددي 
@bot.message_handler(func=lambda message: message.text == 'تحليل عددي (BNA401)')
def handle_BNAI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BNA401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BNA401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BNA401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    

#'برمجة الويب  1
@bot.message_handler(func=lambda message: message.text == 'برمجة الويب  1 (BWP401)')
def handle_BWPI401(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BWP401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BWP401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BWP401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'بنيان الحاسوب  1
@bot.message_handler(func=lambda message: message.text == 'بنيان الحاسوب  1 (BCA501)')
def handle_BCAI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BCA501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BCA501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BCA501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'معالجة الاشارة
@bot.message_handler(func=lambda message: message.text == 'معالجة الاشارة (BSP501)')
def handle_BSPI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BSP501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BSP501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BSP501'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  


#'أساليب الادارة

@bot.message_handler(func=lambda message: message.text == 'أساليب الادارة (GMN401)')
def handle_GMNI401(message):  
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of GMN401'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of GMN401'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of GMN401'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    


#'نظم الاتصالات 
@bot.message_handler(func=lambda message: message.text == 'نظم الاتصالات (BTS501)')
def handle_BTSI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BTS501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BTS501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BTS501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'رياضيات متقطعة
@bot.message_handler(func=lambda message: message.text == 'رياضيات متقطعة (BDM501)')
def handle_BDMI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BDM501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BDM501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BDM501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    


#'نظم قواعد البيانات 1
@bot.message_handler(func=lambda message: message.text == 'نظم قواعد البيانات 1 (BDB501)')
def handle_BDBI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BDB501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BDB501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BDB501'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'برمجة الويب  2 
@bot.message_handler(func=lambda message: message.text == 'برمجة الويب  2 (BWP501)')
def handle_BWPI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BWP501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BWP501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BWP501'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   

#'انجليزي 4
@bot.message_handler(func=lambda message: message.text == 'انجليزي 4 (L4)')
def handle_L4I(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of L4'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of L4'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of L4'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  


#'مخبر نظم قواعد البيانات     
@bot.message_handler(func=lambda message: message.text == 'مخبر نظم قواعد البيانات (BDBL501)')
def handle_BDBLI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BDBL501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BDBL501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BDBL501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  





#--------------------------------------السنة الثالثة---------------------------------------  
@bot.message_handler(func=lambda message: message.text == '(ITE)السنة الثالثة')
def handle_third_year(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item71 = telebot.types.KeyboardButton('الأوتومات واللغات الصورية (BAU501)')
    item72 = telebot.types.KeyboardButton('انجليزي 5 (L5)')
    item73 = telebot.types.KeyboardButton('نظم التشغيل (BOS501)')
    item74 = telebot.types.KeyboardButton('مخبر نظم التشغيل (BOSL501)')
    item75 = telebot.types.KeyboardButton('الاحتمالات والإحصاء (BPS601)')
    item76 = telebot.types.KeyboardButton('المحاسبة (GAC501)')
    item77 = telebot.types.KeyboardButton('البرمجة 3 (BPG601)')
    item78 = telebot.types.KeyboardButton('الشبكات الحاسوبية (BNT501)')
    item79 = telebot.types.KeyboardButton('الذكاء الصنعي (BAI501)')
    item80 = telebot.types.KeyboardButton('هندسة البرمجيات 1 (BSE601)')
    item81 = telebot.types.KeyboardButton('المترجمات (BCM601)')
    item82 = telebot.types.KeyboardButton('البيانيات (BCG601)')
    back_button = telebot.types.KeyboardButton('Back')


    markup.row(item71,item72)
    markup.row(item73,item74)
    markup.row(item75,item76)
    markup.row(item77,item78)
    markup.row(item79,item80)
    markup.row(item81,item82)
    markup.row(back_button)


    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)


#'الأوتومات واللغات الصورية 
@bot.message_handler(func=lambda message: message.text == 'الأوتومات واللغات الصورية (BAU501)')
def handle_BAUI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BAU501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BAU501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BAU501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  



#'انجليزي 5 
@bot.message_handler(func=lambda message: message.text == 'انجليزي 5 (L5)')
def handle_L5I(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of L5'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of L5'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of L5'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
  



#'نظم التشغيل 
@bot.message_handler(func=lambda message: message.text == 'نظم التشغيل (BOS501)')
def handle_BOSI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BOS501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BOS501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BOS501'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'مخبر نظم التشغيل 
@bot.message_handler(func=lambda message: message.text == 'مخبر نظم التشغيل (BOSL501)')
def handle_BOSLI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BOSL501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BOSL501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BOSL501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  




#'الاحتمالات والإحصاء 
@bot.message_handler(func=lambda message: message.text == 'الاحتمالات والإحصاء (BPS601)')
def handle_BPSI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BPS601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BPS601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BPS601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  




#'المحاسبة 
@bot.message_handler(func=lambda message: message.text == 'المحاسبة (GAC501)')
def handle_GACI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of GAC501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of GAC501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of GAC501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  

#'البرمجة 3
@bot.message_handler(func=lambda message: message.text == 'البرمجة 3 (BPG601)')
def handle_BPGI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BPG601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BPG601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BPG601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  



#'الشبكات الحاسوبية 
@bot.message_handler(func=lambda message: message.text == 'الشبكات الحاسوبية (BNT501)')
def handle_BNTI501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BNT501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BNT501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BNT501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
 



#'الذكاء الصنعي 
@bot.message_handler(func=lambda message: message.text == 'الذكاء الصنعي (BAI501)')
def handle_BAII501(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BAI501'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BAI501'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BAI501'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   



#'هندسة البرمجيات 1
@bot.message_handler(func=lambda message: message.text == 'هندسة البرمجيات 1 (BSE601)')
def handle_BSEI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BSE601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BSE601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BSE601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
  



#'المترجمات
@bot.message_handler(func=lambda message: message.text == 'المترجمات (BCM601)')
def handle_BCMI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BCM601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BCM601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BCM601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   



#'البيانيات 
@bot.message_handler(func=lambda message: message.text == 'البيانيات (BCG601)')
def handle_BCGI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of BCG601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of BCG601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of BCG601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
 








#----------------------------------------هندسة برمجيات-------------------------------------------    
@bot.message_handler(func=lambda message: message.text == 'مقررات اختصاص هندسة البرمجيات (SE)')
def handle_SE(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item84 = telebot.types.KeyboardButton('هندسة البرمجيات 2 (SSE602)')
    item85 = telebot.types.KeyboardButton('بنى المعطيات والخوارزميات 2 (SDA601)')
    item86 = telebot.types.KeyboardButton('تحليل وتصميم الخوارزميات (SAD601)')
    item87 = telebot.types.KeyboardButton('نظم قواعد البيانات 2 (SDB601)')
    item88 = telebot.types.KeyboardButton('مخبر نظم قواعد البيانات 2 (SDBL601)')
    item89 = telebot.types.KeyboardButton('تنقيب البيانات (SDE601)')
    item90 = telebot.types.KeyboardButton('استرجاع المعلومات (SIR601)')
    item91 = telebot.types.KeyboardButton('الويب الدلالي (SSW601)')
    item92 = telebot.types.KeyboardButton('جودة البرمجيات (SSQ601)')
    back_button = telebot.types.KeyboardButton('Back')

    markup.row(item84,item85)
    markup.row(item86,item87)
    markup.row(item88,item89)
    markup.row(item90,item91)
    markup.row(item92)
    markup.row(back_button)

    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)


#'هندسة البرمجيات 2 
@bot.message_handler(func=lambda message: message.text == 'هندسة البرمجيات 2 (SSE602)')
def handle_SSEI602(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SSE602'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SSE602'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SSE602'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
 

#'بنى المعطيات والخوارزميات 2 
@bot.message_handler(func=lambda message: message.text == 'بنى المعطيات والخوارزميات 2 (SDA601)')
def handle_SDAI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SDA601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SDA601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SDA601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  


#'تحليل وتصميم الخوارزميات 
@bot.message_handler(func=lambda message: message.text == 'تحليل وتصميم الخوارزميات (SAD601)')
def handle_SADI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SAD601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SAD601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SAD601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   




#'نظم قواعد البيانات 2
@bot.message_handler(func=lambda message: message.text == 'نظم قواعد البيانات 2 (SDB601)')
def handle_SDBI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SDB601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SDB601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SDB601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
 





#'مخبر نظم قواعد البيانات 2 
@bot.message_handler(func=lambda message: message.text == 'مخبر نظم قواعد البيانات 2 (SDBL601)')
def handle_SDBLI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SDBL601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SDBL601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SDBL601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   




#'تنقيب البيانات 
@bot.message_handler(func=lambda message: message.text == 'تنقيب البيانات (SDE601)')
def handle_SDEI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SDE601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SDE601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SDE601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  





#'استرجاع المعلومات
@bot.message_handler(func=lambda message: message.text == 'استرجاع المعلومات (SIR601)')
def handle_SIRI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SIR601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SIR601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SIR601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  







#'الويب الدلالي
@bot.message_handler(func=lambda message: message.text == 'الويب الدلالي (SSW601)')
def handle_SWWI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SSW601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SSW601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SSW601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   





#'جودة البرمجيات (SSQ601)'
@bot.message_handler(func=lambda message: message.text == 'جودة البرمجيات (SSQ601)')
def handle_SSQI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SSQ601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SSQ601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SSQ601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  




#---------------------------------------الذكاء الاصطناعي------------------------------------------------    
@bot.message_handler(func=lambda message: message.text == 'مقررات اختصاص الذكاء الصنعي (AI)')
def handle_AI(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item93 = telebot.types.KeyboardButton('الشبكات العصبونية والمنطق العائم (ANN601)')
    item94 = telebot.types.KeyboardButton('الواقع الافتراضي (AVR601)')
    item95 = telebot.types.KeyboardButton('تعلم الآلة (AML601)')
    item96 = telebot.types.KeyboardButton('معالجة اللغات الطبيعية (ANL601)')
    item97 = telebot.types.KeyboardButton('النظم الخبيرة (AES601)')
    item98 = telebot.types.KeyboardButton('معالجة الصورة الرقمية (AIP601)')
    item99 = telebot.types.KeyboardButton('الرؤية الحاسوبية(ACV601)')
    item100 = telebot.types.KeyboardButton('استرجاع المعلومات (SIR601)')
    item101 = telebot.types.KeyboardButton('الويب الدلالي (SSW601)')
    back_button = telebot.types.KeyboardButton('Back')

    markup.row(item93,item94)
    markup.row(item95,item96)
    markup.row(item97,item98)
    markup.row(item99,item100)
    markup.row(item101)
    markup.row(back_button)

    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)


#'الشبكات العصبونية والمنطق العائم 
@bot.message_handler(func=lambda message: message.text == 'الشبكات العصبونية والمنطق العائم (ANN601)')
def handle_ANNI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of ANN601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of ANN601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of ANN601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
 



#'الواقع الافتراضي 
@bot.message_handler(func=lambda message: message.text == 'الواقع الافتراضي (AVR601)')
def handle_AVRI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of AVR601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of AVR601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of AVR601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'تعلم الآلة 
@bot.message_handler(func=lambda message: message.text == 'تعلم الآلة (AML601)')
def handle_AMLI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of AML601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of AML601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of AML601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'معالجة اللغات الطبيعية 
@bot.message_handler(func=lambda message: message.text == 'معالجة اللغات الطبيعية (ANL601)')
def handle_ANLI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of ANL601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of ANL601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of ANL601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    

#'النظم الخبيرة 
@bot.message_handler(func=lambda message: message.text == 'النظم الخبيرة (AES601)')
def handle_AESI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of AES601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of AES601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of AES601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   


#'معالجة الصورة الرقمية 
@bot.message_handler(func=lambda message: message.text == 'معالجة الصورة الرقمية (AIP601)')
def handle_AIPI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of AIP601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of AIP601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of AIP601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
  



#'الرؤية الحاسوبية
@bot.message_handler(func=lambda message: message.text == 'الرؤية الحاسوبية(ACV601)')
def handle_ACVI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of ACV601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of ACV601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of ACV601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  




#'استرجاع المعلومات 
@bot.message_handler(func=lambda message: message.text == 'استرجاع المعلومات (SIR601)')
def handle_SIRI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SIR601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SIR601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SIR601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   

#'الويب الدلالي (SSW601)' 
@bot.message_handler(func=lambda message: message.text == 'الويب الدلالي (SSW601)')
def handle_SSWI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of SSW601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of SSW601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of SSW601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  







#----------------------------------------شبكات---------------------------------------------    
@bot.message_handler(func=lambda message: message.text == 'مقررات اختصاص النظم والشبكات الحاسوبية (SCN)')
def handle_SCN(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item102 = telebot.types.KeyboardButton('بنيان الحاسوب 2 (NCA601)')
    item103 = telebot.types.KeyboardButton('برمجة التطبيقات الشبكية (NNP601)')
    item104 = telebot.types.KeyboardButton('خدمات شبكية (NNS601)')
    item105 = telebot.types.KeyboardButton('شبكات 2 (NNT601)')
    item106 = telebot.types.KeyboardButton('نظم التشغيل 2 (NOS601)')
    item107 = telebot.types.KeyboardButton('مخبر نظم التشغيل 2 (NOSL601)')
    item108 = telebot.types.KeyboardButton('ادارة الشبكات (NNM601)')
    item109 = telebot.types.KeyboardButton('أمن الشبكات الحاسوبية (NSS601)')
    item110 = telebot.types.KeyboardButton('النظم الموزعة والسحابية (NDS601)')
    item111 = telebot.types.KeyboardButton('نظم الزمن الحقيقي (NRT601)')
    back_button = telebot.types.KeyboardButton('Back')


    markup.row(item102,item103)
    markup.row(item104,item105)
    markup.row(item106,item107)
    markup.row(item108,item109)
    markup.row(item110,item111)
    markup.row(back_button)

    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)

# 'بنيان الحاسوب 2 
@bot.message_handler(func=lambda message: message.text == 'بنيان الحاسوب 2 (NCA601)')
def handle_NCAI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NCA601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NCA601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NCA601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
 




#  'برمجة التطبيقات الشبكية 
@bot.message_handler(func=lambda message: message.text == 'برمجة التطبيقات الشبكية (NNP601)')
def handle_NNPI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NNP601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NNP601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NNP601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
 



#   'خدمات شبكية (NNS601)' 
@bot.message_handler(func=lambda message: message.text == 'خدمات شبكية (NNS601)')
def handle_NNSI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NNS601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NNS601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NNS601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    


#   'شبكات 2 
@bot.message_handler(func=lambda message: message.text == 'شبكات 2 (NNT601)')
def handle_NNTI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NNT601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NNT601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NNT601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    




#  'نظم التشغيل 2 
@bot.message_handler(func=lambda message: message.text == 'نظم التشغيل 2 (NOS601)')
def handle_NOSI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NOS601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NOS601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NOS601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  



#'مخبر نظم التشغيل 2 
@bot.message_handler(func=lambda message: message.text == 'مخبر نظم التشغيل 2 (NOSL601)')
def handle_NOSLI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NOSL601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NOSL601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NOSL601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
 




#  'ادارة الشبكات 
@bot.message_handler(func=lambda message: message.text == 'ادارة الشبكات (NNM601)')
def handle_NNMI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NNM601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NNM601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NNM601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  





#  'أمن الشبكات الحاسوبية
@bot.message_handler(func=lambda message: message.text == 'أمن الشبكات الحاسوبية (NSS601)')
def handle_NSSI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NSS601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NSS601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NSS601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
    



# 'النظم الموزعة والسحابية 
@bot.message_handler(func=lambda message: message.text == 'النظم الموزعة والسحابية (NDS601)')
def handle_NDSI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NDS601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NDS601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NDS601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
  





#'نظم الزمن الحقيقي 
@bot.message_handler(func=lambda message: message.text == 'نظم الزمن الحقيقي (NRT601)')
def handle_NRTI601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of NRT601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of NRT601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of NRT601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
  

#---------------------------------الامن السيبراني----------------------------------

@bot.message_handler(func=lambda message: message.text == 'مقررات اختصاص الأمن السيبراني (CS)')
def handle_CS(message):
    chat_id = message.chat.id
    
    user = users.get(chat_id)
    if user is None:
        user = User()
        users[chat_id] = user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item102 = telebot.types.KeyboardButton('النظم التعمية(CCR601)')
    item103 = telebot.types.KeyboardButton('الاختراق الأخلاقي(CEH601)')
    item104 = telebot.types.KeyboardButton('الاستجابة للأحداث الأمنية(CIR601)')
    item105 = telebot.types.KeyboardButton('الأمن في النظم الحديثة(CMS601)')
    item106 = telebot.types.KeyboardButton('ادارة الأمن(CSM601)')
    item107 = telebot.types.KeyboardButton('أمن نظم التشغيل(CSO601)')
    back_button = telebot.types.KeyboardButton('Back')

    markup.row(item102,item103)
    markup.row(item104,item105)
    markup.row(item106,item107)
    markup.row(back_button) 

    user_navigation_stack = user.navigation_stack
    user_navigation_stack.append((chat_id,  " اختر مادة : ", markup))
    bot.send_message(chat_id,  " اختر مادة : ", reply_markup=markup)


#'النظم التعمية(CCR601)'
@bot.message_handler(func=lambda message: message.text == 'النظم التعمية(CCR601)')
def handle_CCR601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of CCR601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of CCR601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of CCR601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    

#'الاختراق الأخلاقي(CEH601)'
@bot.message_handler(func=lambda message: message.text == 'الاختراق الأخلاقي(CEH601)')
def handle_CEH601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of CEH601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of CEH601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of CEH601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
           

#'الاستجابة للأحداث الأمنية(CIR601)'
@bot.message_handler(func=lambda message: message.text == 'الاستجابة للأحداث الأمنية(CIR601)')
def handle_CIR601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of CIR601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of CIR601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of CIR601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  


#'الأمن في النظم الحديثة(CMS601)'
@bot.message_handler(func=lambda message: message.text == 'الأمن في النظم الحديثة(CMS601)')
def handle_CMS601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of CMS601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of CMS601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of CMS601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
    

#'ادارة الأمن(CSM601)'
@bot.message_handler(func=lambda message: message.text == 'ادارة الأمن(CSM601)')
def handle_CSM601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of CSM601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of CSM601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of CSM601'))

    bot.send_message(message.chat.id,' انقر الزر لتحميل الملف :', reply_markup=markup)  
   

#'أمن نظم التشغيل(CSO601)'
@bot.message_handler(func=lambda message: message.text == 'أمن نظم التشغيل(CSO601)')
def handle_CSO601(message):  

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='المحتوى العلمي', callback_data='books of CSO601'))
    #markup.add(InlineKeyboardButton(text='المحاضرات', callback_data='lectures of CSO601'))
    markup.add(InlineKeyboardButton(text='الملخصات', callback_data='summaries of CSO601'))

    bot.send_message(message.chat.id, ' انقر الزر لتحميل الملف :', reply_markup=markup)  
   

  
#--------------------------------------ادخال رمز المادة--------------------------------------------------------

@bot.message_handler(func=lambda message: True)
def handle_subject_symbols(message):
    # Get the symbols entered by the user
    symbols = message.text

    # Process the symbols and generate a response
    response = process_symbols(symbols,message)

    # Send the response back to the user
    bot.send_message(message.chat.id, response)

def process_symbols(symbols,message):

    #سنة اولى
    if symbols == 'BPG401' or symbols == 'bpg401' :
        return handle_BPGI401(message)
    elif symbols == 'BMA401' or symbols == 'bma401':
        return handle_BMAI401(message)
    elif symbols == 'L1' or symbols == 'l1':
        return handle_L1I(message)
    elif symbols == 'BPH401' or symbols == 'bph401':
        return handle_BPHI401(message)
    elif symbols == 'BAS401' or symbols == 'bas401':
        return handle_BASI401(message)
    elif symbols == 'GCS301' or symbols == 'gcs301':
        return handle_GCSI301(message)
    elif symbols == 'GOE301' or symbols == 'goe301' :
        return handle_GOEI301(message)
    elif symbols == 'GWT301' or symbols == 'gwt301':
        return handle_GWTI301(message)
    elif symbols == 'BLA401' or symbols == 'bla401':
        return handle_BLAI401(message)
    elif symbols == 'BMA402' or symbols == 'bma402':
        return handle_BMAI402(message)
    elif symbols == 'L2'or symbols == 'l2':
        return handle_E2I(message)
    elif symbols == 'BEC401'or symbols == 'bec401':
        return handle_BECI401(message)
    elif symbols == 'BLC401' or symbols == 'blc401':
        return handle_BLCI401(message)
    elif symbols == 'BPG402' or symbols == 'bpg402':
        return handle_BPGI402(message)
    #سنة ثانية
    elif symbols == 'BDA501' or symbols == 'bda501':
        return handle_BDAI501(message)
    elif symbols == 'L3' or symbols == 'l3':
        return handle_L3I(message)
    elif symbols == 'BNA401' or symbols == 'bna401':
        return handle_BNAI401(message)
    elif symbols == 'BWP401' or symbols == 'bwp401':
        return handle_BWPI401(message)
    elif symbols == 'BCA501' or symbols == 'bcau501':
        return handle_BCAI501(message)
    elif symbols == 'BSP501' or symbols == 'bsp501':
        return handle_BSPI501(message)
    elif symbols == 'GMN401' or symbols == 'gmn401':
        return handle_GMNI401(message)
    elif symbols == 'BTS501' or symbols == 'bts501':
        return handle_BTSI501(message)
    elif symbols == 'BDM501' or symbols == 'bdm501':
        return handle_BDMI501(message)
    elif symbols == 'BDB501' or symbols == 'bdb501':
        return handle_BDBI501(message)
    elif symbols == 'BWP501' or symbols == 'bwp501':
        return handle_BWPI501(message)
    elif symbols == 'L4' or symbols == 'l4':
        return handle_L4I(message)
    elif symbols == 'BDBL501' or symbols == 'bdbl501':
        return handle_BDBLI501(message)
    #سنة ثالثة
    elif symbols == 'BAU501' or symbols == 'bau501':
        return handle_BAUI501(message)
    elif symbols == 'L5' or symbols == 'l5':
        return handle_L5I(message)
    elif symbols == 'BOS501' or symbols == 'bos501':
        return handle_BOSI501(message)
    elif symbols == 'BOSL501' or symbols == 'bosl501':
        return handle_BOSLI501(message)
    elif symbols == 'BPS601' or symbols == 'bps601':
        return handle_BPSI601(message)
    elif symbols == 'GAC501' or symbols == 'gac501':
        return handle_GACI501(message)
    elif symbols == 'BPG601' or symbols == 'bpg601':
        return handle_BPGI601(message)
    elif symbols == 'BNT501' or symbols == 'bnt501':
        return handle_BNTI501(message)
    elif symbols == 'BAI501' or symbols == 'bai501':
        return handle_BAII501(message)
    elif symbols == 'BSE601' or symbols == 'bse601':
        return handle_BDBI501(message)
    elif symbols == 'BCM601' or symbols == 'bcm601':
        return handle_BCMI601(message)
    elif symbols == 'BCG601' or symbols == 'bcg601':
        return handle_BCGI601(message)
    #هندسة برمجيات
    elif symbols == 'SSE602' or symbols == 'sse602':
        return handle_SSEI602(message)
    elif symbols == 'SDA601' or symbols == 'sda601':
        return handle_SDAI601(message)
    elif symbols == 'SAD601' or symbols == 'sad601':
        return handle_SADI601(message)
    elif symbols == 'SDB601' or symbols == 'sdb601':
        return handle_SDBI601(message)
    elif symbols == 'SDBL601' or symbols == 'sdbl601':
        return handle_BCAI501(message)
    elif symbols == 'SDE601' or symbols == 'sde601':
        return handle_SDEI601(message)
    elif symbols == 'SIR601' or symbols == 'sir601':
        return handle_SIRI601(message)
    elif symbols == 'SSW601' or symbols == 'ssw601':
        return handle_SSWI601(message)
    elif symbols == 'SSQ601' or symbols == 'ssq601':
        return handle_SSQI601(message)
    #الذكاء الاصطناعي
    elif symbols == 'ANN601' or symbols == 'ann601':
        return handle_ANNI601(message)
    elif symbols == 'AVR601' or symbols == 'avr601':
        return handle_AVRI601(message)
    elif symbols == 'AML601' or symbols == 'aml601':
        return handle_AMLI601(message)
    elif symbols == 'ANL601' or symbols == 'anl601':
        return handle_ANLI601(message)
    elif symbols == 'AES601' or symbols == 'aes601':
        return handle_AESI601(message)
    elif symbols == 'AIP601' or symbols == 'aip601':
        return handle_AIPI601(message)
    elif symbols == 'ACV601' or symbols == 'acv601':
        return handle_ACVI601(message)
    elif symbols == 'SIR601' or symbols == 'sir601':
        return handle_SIRI601(message)
    elif symbols == 'SSW601' or symbols == 'ssw601':
        return handle_SSWI601(message)
    #الشبكات
    elif symbols == 'NCA601' or symbols == 'nca601':
        return handle_NCAI601(message)
    elif symbols == 'NNP601' or symbols == 'nnp601':
        return handle_NNPI601(message)
    elif symbols == 'NNS601' or symbols == 'nns601':
        return handle_NNSI601(message)
    elif symbols == 'NNT601' or symbols == 'nnt601':
        return handle_NNTI601(message)
    elif symbols == 'NOS601' or symbols == 'nos601':
        return handle_NOSI601(message)
    elif symbols == 'NOSL601' or symbols == 'nosl601':
        return handle_NOSLI601(message)
    elif symbols == 'NNM601' or symbols == 'nnm601':
        return handle_NNMI601(message)
    elif symbols == 'NSS601' or symbols == 'nsss601':
        return handle_NSSI601(message)
    elif symbols == 'NDS601' or symbols == 'nds601':
        return handle_NDSI601(message)
    elif symbols == 'NRT601' or symbols == 'nrt601':
        return handle_NRTI601(message)

    #امن سيبراني
    elif symbols == 'CCR601' or symbols == 'ccr601':
        return handle_CCR601(message)
    elif symbols == 'CEH601' or symbols == 'ceh601':
        return handle_CEH601(message)
    elif symbols == 'CIR601' or symbols == 'cir601':
        return handle_CIR601(message)
    elif symbols == 'CMS601' or symbols == 'cms601':
        return handle_CMS601(message)
    elif symbols == 'CSM601' or symbols == 'csm601':
        return handle_CSM601(message)
    elif symbols == 'CSO601' or symbols == 'cso601':
        return handle_CSO601(message)


    else:
        return "Invalid symbol."   


   #-----------------------تحميل المحاضرات ------------------------------

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
  with lock:
#سنة اولى
 #BPG401
  #المحتوى العلمي 
    if call.data == 'books of BPG401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BPG401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('البرمجة 1 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('البرمجة 1 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BPG401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 


    elif call.data== 'Back':
      go_back(call.message.chat.id)
    
#BMA401
  #المحتوى العلمي 
    elif call.data == 'books of BMA401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BMA401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('1 التحليل الرياضي .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('1 التحليل الرياضي .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BMA401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 


#ENG1
  #المحتوى العلمي 
    elif call.data == 'books of L1':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 

   #الملخصات
    elif call.data == 'summaries of L1':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 


#BPH401
  #المحتوى العلمي 
    elif call.data == 'books of BPH401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BPH401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الفيزياء .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الفيزياء .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BPH401':
      bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 


       #BAS401
  #المحتوى العلمي 
    elif call.data == 'books of BAS401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BAS401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الهيكلة الجبرية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الهيكلة الجبرية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BAS401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 


#GCS301
  #المحتوى العلمي 
    elif call.data == 'books of GCS301':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/GCS301/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('مهارات الحاسوب .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('مهارات الحاسوب .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of GCS301':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 




#GOE301
  #المحتوى العلمي 
    elif call.data == 'books of GOE301':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/GOE301/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('التعليم الالكتروني .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('التعليم الالكتروني .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of GOE301':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 



#GWT301
  #المحتوى العلمي 
    elif call.data == 'books of GWT301':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/GTW301/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('مهارات التواصل .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('مهارات التواصل .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of GWT301':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 



#BLA401
  #المحتوى العلمي 
    elif call.data == 'books of BLA401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BLA401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الجبر الخطي .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الجبر الخطي .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BLA401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  



#BMA402
  #المحتوى العلمي 
    elif call.data == 'books of BMA402':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BMA402/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('التحليل الرياضي 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('التحليل الرياضي 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BMA402':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 



#L2
  #المحتوى العلمي 
    elif call.data == 'books of L2':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 

   #الملخصات
    elif call.data == 'summaries of L2':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 




#BEC401
  #المحتوى العلمي 
    elif call.data == 'books of BEC401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BEC401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الدارات الالكترونية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الدارات الالكترونية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BEC401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 



#BLC401
  #المحتوى العلمي 
    elif call.data == 'books of BLC401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BLC401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الدارات المنطقية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الدارات المنطقية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BLC401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 



#BPG402
  #المحتوى العلمي 
    elif call.data == 'books of BPG402':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BPG402%20----------/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/BPG402.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('برمجة 2.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('برمجة 2.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)

   #الملخصات
    elif call.data == 'summaries of BPG402':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 



#السنة الثانية

#BDA501
  #المحتوى العلمي 
    elif call.data == 'books of BDA501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BDA501%20--------/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/BDA501/BDA501.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('بنى المعطيات.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('بنى المعطيات.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
        
   #الملخصات
    elif call.data == 'summaries of BDA501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      


#L3
  #المحتوى العلمي 
    elif call.data == 'books of L3':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       
   #الملخصات
    elif call.data == 'summaries of L3':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
     


#BNA401
  #المحتوى العلمي 
    elif call.data == 'books of BNA401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BNA401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('تحليل عددي .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('تحليل عددي .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BNA401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      


#BWP401
  #المحتوى العلمي 
    elif call.data == 'books of BWP401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BWP401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('برمجة الويب  1 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('برمجة الويب  1 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of BWP401':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
     


#BCA501
  #المحتوى العلمي 
    elif call.data == 'books of BCA501':

        file_url = f'https://svu1.org/telegr_bot/ITE/BCA501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('بنيان الحاسوب  1 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('بنيان الحاسوب  1 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of BCA501':
      bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       


#BSP501
  #المحتوى العلمي 
    elif call.data == 'books of BSP501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BSP501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('معالجة الاشارة .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('معالجة الاشارة .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of BSP501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    


#GMN401
  #المحتوى العلمي 
    elif call.data == 'books of GMN401':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/GMN401/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/Fundamentals%20of%20Management%20-%20Dr%20Iyad%20Zoukar.pdf'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('أساليب الادارة .pdf', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('أساليب الادارة .pdf', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of GMN401':
      bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      


#BTS501
  #المحتوى العلمي 
    elif call.data == 'books of BTS501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BTS501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('نظم الاتصالات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('نظم الاتصالات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BTS501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      


#BDM501
  #المحتوى العلمي 
    elif call.data == 'books of BDM501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BDM501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('رياضيات متقطعة .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('رياضيات متقطعة .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of BDM501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    

#BDB501
  #المحتوى العلمي 
    elif call.data == 'books of BDB501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BDB501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('نظم قواعد البيانات 1 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('نظم قواعد البيانات 1 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BDB501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
   

#BWP501
  #المحتوى العلمي 
    elif call.data == 'books of BWP501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BWP501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('برمجة الويب  2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('برمجة الويب  2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BWP501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
     


#L4
  #المحتوى العلمي 
    elif call.data == 'books of L4':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
    
   #الملخصات
    elif call.data == 'summaries of L4':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    

#BDBL501
  #المحتوى العلمي 
    elif call.data == 'books of BDBL501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BDBL501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('مخبر نظم قواعد البيانات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('مخبر نظم قواعد البيانات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of BDBL501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      


#السنة التالتة
#الأوتومات واللغات الصورية (BAU501)

 #المحتوى العلمي 
    elif call.data == 'books of BAU501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BAU501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%AA%D9%81%D8%A7%D8%B9%D9%84%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الأوتومات واللغات الصورية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الأوتومات واللغات الصورية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BAU501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       

#انجليزي 5 (L5)

 #المحتوى العلمي 
    elif call.data == 'books of L5':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    
   #الملخصات
    elif call.data == 'summaries of L5':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    

#مخبر نظم التشغيل (BOSL501)

 #المحتوى العلمي 
    elif call.data == 'books of BOSL501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BOSL501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('مخبر نظم التشغيل .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('مخبر نظم التشغيل .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BOSL501':
      bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    

# نظم التشغيل (BOS501)
#المحتوى العلمي 
    elif call.data == 'books of BOS501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BOS501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('نظم التشغيل .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('نظم التشغيل .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of BOS501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

       # الاحتمالات والإحصاء (BPS601)
#المحتوى العلمي 
    elif call.data == 'books of BPS601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BPS601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الاحتمالات والإحصاء .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الاحتمالات والإحصاء .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BPS601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
  

  # المحاسبة (GAC501)
#المحتوى العلمي 
    elif call.data == 'books of GAC501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/GAC501%20-----/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('المحاسبة .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('المحاسبة .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
        
   #الملخصات
    elif call.data == 'summaries of GAC501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
           

         # البرمجة 3 (BPG601)
#المحتوى العلمي 
    elif call.data == 'books of BPG601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BPG601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' البرمجة 3  .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' البرمجة 3  .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of BPG601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

      # الشبكات الحاسوبية (BNT501)
#المحتوى العلمي 
    elif call.data == 'books of BNT501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BNT501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الشبكات الحاسوبية.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الشبكات الحاسوبية.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of BNT501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       


      # الذكاء الصنعي (BAI501)
#المحتوى العلمي 
    elif call.data == 'books of BAI501':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BAI501/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الذكاء الصنعي .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الذكاء الصنعي .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of BAI501':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
   


      # هندسة البرمجيات 1 (BSE601)
#المحتوى العلمي 
    elif call.data == 'books of BSE601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BSE601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' هندسة البرمجيات 1 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' هندسة البرمجيات 1 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of BSE601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      

    #المترجمات (BCM601)
#المحتوى العلمي 
    elif call.data == 'books of BCM601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BCM601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' المترجمات.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' المترجمات.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of BCM601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       

         # البيانيات (BCG601)
#المحتوى العلمي 
    elif call.data == 'books of BCG601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/BCG601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' البيانيات.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' البيانيات.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of BCG601':
      bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

#هندسة برمجيات
        #هندسة البرمجيات 2 (SSE602)
#المحتوى العلمي 
    elif call.data == 'books of SSE602':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/SSE602/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' هندسة البرمجيات 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' هندسة البرمجيات 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of SSE602':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
          


        # بنى المعطيات والخوارزميات 2 (SDA601)
#المحتوى العلمي 
    elif call.data == 'books of SDA601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/SDA601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' بنى المعطيات والخوارزميات 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' بنى المعطيات والخوارزميات 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of SDA601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
     

        #نظم قواعد البيانات 2 (SDB601)
#المحتوى العلمي 
    elif call.data == 'books of SDB601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/SDB602/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDFs-20240220.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' نظم قواعد البيانات 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' نظم قواعد البيانات 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
#الملخصات
    elif call.data == 'summaries of SDB601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       
       #تحليل وتصميم الخوارزميات (SAD601)
#المحتوى العلمي 
    elif call.data == 'books of SAD601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/SAD601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' تحليل وتصميم الخوارزميات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' تحليل وتصميم الخوارزميات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of SAD601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

 #مخبر نظم قواعد البيانات 2 (SDBL601)
#المحتوى العلمي 
    elif call.data == 'books of SDBL601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/SDBL601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' مخبر نظم قواعد البيانات 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' مخبر نظم قواعد البيانات 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of SDBL601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

 #تنقيب البيانات (SDE601)
#المحتوى العلمي 
    elif call.data == 'books of SDE601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/SDE601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('تنقيب البيانات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('تنقيب البيانات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of SDE601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
    

        #استرجاع المعلومات (SIR601)
#المحتوى العلمي 
    elif call.data == 'books of SIR601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/SIR601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('استرجاع المعلومات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('استرجاع المعلومات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of SIR601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       
        #الويب الدلالي (SSW601)
#المحتوى العلمي 
    elif call.data == 'books of SSW601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/SSW601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الويب الدلالي .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الويب الدلالي .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of SSW601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

       #جودة البرمجيات (SSQ601)
#المحتوى العلمي 
    elif call.data == 'books of SSQ601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/SSQ601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('جودة البرمجيات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('جودة البرمجيات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of SSQ601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      
#الذكاء الاصطناعي-

    #الشبكات العصبونية والمنطق العائم (ANN601)
#المحتوى العلمي 
    elif call.data == 'books of ANN601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/ANN601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الشبكات العصبونية.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الشبكات العصبونية.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of ANN601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
     

    #الواقع الافتراضي (AVR601)
#المحتوى العلمي 
    elif call.data == 'books of AVR601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/AVR601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الواقع الافتراضي.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الواقع الافتراضي.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of AVR601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       

    #تعلم الآلة (AML601)
#المحتوى العلمي 
    elif call.data == 'books of AML601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/AML601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('تعلم الآلة .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('تعلم الآلة .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
        
   #الملخصات
    elif call.data == 'summaries of AML601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
          

    #معالجة اللغات الطبيعية (ANL601)
#المحتوى العلمي 
    elif call.data == 'books of ANL601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/ANL601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('معالجة اللغات الطبيعية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('معالجة اللغات الطبيعية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of ANL601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
           

    #النظم الخبيرة (AES601)
#المحتوى العلمي 
    elif call.data == 'books of AES601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/AES601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('النظم الخبيرة .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('النظم الخبيرة .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of AES601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
     

    #معالجة الصورة الرقمية (AIP601)
#المحتوى العلمي 
    elif call.data == 'books of AIP601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/AIP601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('معالجة الصورة الرقمية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('معالجة الصورة الرقمية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of AIP601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      
       
    #الرؤية الحاسوبية(ACV601)
#المحتوى العلمي 
    elif call.data == 'books of ACV601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/ACV601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الرؤية الحاسوبية.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الرؤية الحاسوبية.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of ACV601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
   

           #استرجاع المعلومات (SIR601)
#المحتوى العلمي 
    elif call.data == 'books of SIR601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/SIR601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('استرجاع المعلومات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('استرجاع المعلومات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of SIR601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

           #الويب الدلالي (SSW601)
#المحتوى العلمي 
    elif call.data == 'books of SSW601':

        file_url = f'https://svu1.org/telegr_bot/ITE/SSW601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الويب الدلالي .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الويب الدلالي .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of SSW601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
       

#شبكات


#بنيان الحاسوب 2 (NCA601)
#المحتوى العلمي 
    elif call.data == 'books of NCA601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NCA601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('بنيان الحاسوب 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('بنيان الحاسوب 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of NCA601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       

#برمجة التطبيقات الشبكية (NNP601)
#المحتوى العلمي 
    elif call.data == 'books of NNP601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NNP601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('برمجة التطبيقات.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('برمجة التطبيقات.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of NNP601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      

#خدمات شبكية (NNS601)
#المحتوى العلمي 
    elif call.data == 'books of NNS601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NNS601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('خدمات شبكية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('خدمات شبكية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of NNS601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      
#شبكات 2 (NNT601)
#المحتوى العلمي 
    elif call.data == 'books of NNT601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NNT601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('شبكات 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('شبكات 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of NNT601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
             

#نظم التشغيل 2 (NOS601)
#المحتوى العلمي 
    elif call.data == 'books of NOS601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NOS601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('نظم التشغيل 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('نظم التشغيل 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of NOS601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
             


#مخبر نظم التشغيل 2 (NOSL601)
#المحتوى العلمي 
    elif call.data == 'books of NOSL601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NOSL601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' مخبر نظم التشغيل 2 .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' مخبر نظم التشغيل 2 .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
         
   #الملخصات
    elif call.data == 'summaries of NOSL601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      

       #ادارة الشبكات (NNM601)
#المحتوى العلمي 
    elif call.data == 'books of NNM601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NNM601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open(' ادارة الشبكات .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open(' ادارة الشبكات .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of NNM601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

       #أمن الشبكات الحاسوبية (NSS601)
#المحتوى العلمي 
    elif call.data == 'books of NSS601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NNS601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('أمن الشبكات الحاسوبية .zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('أمن الشبكات الحاسوبية .zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of NSS601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
         

    #النظم الموزعة والسحابية (NDS601)
#المحتوى العلمي 
    elif call.data == 'books of NDS601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/NDS601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('لنظم الموزعة.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('لنظم الموزعة.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of NDS601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
                  
   #نظم الزمن الحقيقي (NRT601)========
#المحتوى العلمي 
    elif call.data == 'books of NRT601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      

   #الملخصات
    elif call.data == 'summaries of NRT601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      

#امن سيبراني
#النظم التعمية(CCR601)
#المحتوى العلمي 
    elif call.data == 'books of CCR601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/CCR601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('النظم التعمية.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('النظم التعمية.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
          
   #الملخصات
    elif call.data == 'summaries of CCR601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
      

#الاختراق الأخلاقي(CEH601)
#المحتوى العلمي 
    elif call.data == 'books of CEH601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/CEH601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الاختراق الأخلاقي.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الاختراق الأخلاقي.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of CEH601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
      

#الاستجابة للأحداث الأمنية(CIR601)
#المحتوى العلمي 
    elif call.data == 'books of CIR601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/CIR601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الاستجابة للأحداث الأمنية.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الاستجابة للأحداث الأمنية.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of CIR601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
       


#الأمن في النظم الحديثة(CMS601)
#المحتوى العلمي 
    elif call.data == 'books of CMS601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/CMS601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('الأمن في النظم الحديثة.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('الأمن في النظم الحديثة.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of CMS601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً')  
       
#ادارة الأمن(CSM601)
#المحتوى العلمي 
    elif call.data == 'books of CSM601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/CSM601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('ادارة الأمن.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('ادارة الأمن.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
            
   #الملخصات
    elif call.data == 'summaries of CSM601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
        


#أمن نظم التشغيل(CSO601)
#المحتوى العلمي 
    elif call.data == 'books of CSO601':
        # Download the file from Google Drive

        file_url = f'https://svu1.org/telegr_bot/ITE/%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA/CSO601/%D8%A7%D9%84%D9%85%D8%AD%D8%AA%D9%88%D9%89%20%D8%A7%D9%84%D8%B9%D9%84%D9%85%D9%8A/PDF/PDF.zip'
        response = requests.get(file_url, stream=True)

        # Save the file locally
        with open('أمن نظم التشغيل.zip', 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        with open('أمن نظم التشغيل.zip', 'rb') as f:
            bot.send_document(call.message.chat.id, f,timeout=300)
           
   #الملخصات
    elif call.data == 'summaries of CSO601':
       bot.send_message(call.message.chat.id, text='سيتوفر المحتوى قريباً') 
     

bot.polling()