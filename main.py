import telebot
#from fpdf import FPDF
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
import requests
from io import BytesIO
import os 
import ftplib
bot = telebot.TeleBot('6850631961:AAGJIMlS4byGQTgePdRmXgJ6HvUdvcTru9A')
#from googleapiclient.discovery import build
#from google.oauth2 import service_account

#tic user name :
tic_user_name='@tic_svu_bot'
#tiba user name :
tiba_user_name='@tiba_svu_bot'
#ite user name :
ite_user_name='@ITE_SVU_bot'
#bact user name:
bact_user_name='@bactt_svu_bot'
#bait user name:
bait_user_name='@baitt_svu_bot'
#bl user name:
bl_user_name='@bll_svu_bot'
#bscn user name:
bscm_user_name='@bscmm_svu_bot'
#bmc user name:
bmc_user_name='@bmc_svu_bot'
#tith user name:
tith_user_name='@tith_svu_bot'
#bthm user name:
bthm_user_name='@bthm_svu_bot'

@bot.message_handler(commands=['start','START','HELP','help','ابدا','ابدأ'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itema = telebot.types.KeyboardButton('المعهد')
    itemb = telebot.types.KeyboardButton('الاجازة')
    itemc = telebot.types.KeyboardButton('الماجستير')
    itemd = telebot.types.KeyboardButton('الخدمات')
    
   
    
    markup.row(itema, itemb)
    markup.row(itemc, itemd)
    
    
    
    
    
    bot.send_message(message.chat.id, "Please choose your section:", reply_markup=markup)
    
    
#معاهد    
@bot.message_handler(func=lambda message: message.text == 'المعهد')
def handle_institute(message): 
    markup = telebot.types.InlineKeyboardMarkup()   
    item1 = telebot.types.InlineKeyboardButton('المعهد التقني للحاسوب (TIC)', url='https://t.me/tic_svu_bot')
    item2 = telebot.types.InlineKeyboardButton('المعهد التقاني لادارة الاعمال(TIBA)', url='https://t.me/tiba1_svu_bot')
    item10= telebot.types.InlineKeyboardButton('المعهد التقاني للعلوم السياحية والفندقية(TITH)',url='https://t.me/tith_svu_bot')
    
    markup.row(item1)
    markup.row(item2)
    markup.row(item10)
    
    
    bot.send_message(message.chat.id, "Please choose your specialization:", reply_markup=markup)
    
    
    
#اجازات
@bot.message_handler(func=lambda message: message.text == 'الاجازة')
def handle_university_degree(message): 
    markup = telebot.types.InlineKeyboardMarkup()  
    item3 = InlineKeyboardButton('الهندسة المعلوماتية(ITE)',url='https://t.me/ITE_SVU_bot')
    item4 = InlineKeyboardButton('تقانة الاتصالات (BACT)',url='https://t.me/bactt_svu_bot')
    item10 = InlineKeyboardButton('المعهد التقاني للعلوم السياحية والفندقية(TITH)',url='https://t.me/tith_svu_bot')
    item5 = InlineKeyboardButton('تقانة المعلومات (BAIT)',url='https://t.me/baitt_svu_bot')
    item6 = InlineKeyboardButton('الحقوق (BL)',url='https://t.me/bll_svu_bot')
    item7 = InlineKeyboardButton('علوم الادارة(الاقتصاد)(BSCM)',url='https://t.me/bscmm_svu_bot')
    item8 = InlineKeyboardButton('الاعلام والاتصال(BMC)',url='https://t.me/bmc_svu_bot')
    item9 = InlineKeyboardButton('الادارة السياحية والفندقية(BTHM)',url='https://t.me/bthm_svu_bot')
    
    
    markup.row(item3, item4)
    markup.row(item5, item6)
    markup.row(item7, item8)
    markup.row(item9, item10)
    
    
    bot.send_message(message.chat.id, "Please choose your specialization:", reply_markup=markup)    
    
    
#ماجستير    
@bot.message_handler(func=lambda message: message.text == 'الماجستير')
def handle_master(message): 
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)    
    item1 = telebot.types.KeyboardButton('ماجستير علوم الويب') 
    item2 = telebot.types.KeyboardButton('ماجستير الشبكات') 
    
    
    
    markup.row(item1,item2)
    
    bot.send_message(message.chat.id, "Please choose your master:", reply_markup=markup)    
    
    

#الخدمات
@bot.message_handler(func=lambda message: message.text == 'الخدمات')
def handle_institute(message):  
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='الاشتراك الذهبي', callback_data='gold'))
    markup.add(InlineKeyboardButton(text='الاشتراك الفضي', callback_data='silver'))
    
    
    bot.send_message(message.chat.id, 'Click the button to download a file :', reply_markup=markup) 
    
    
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'gold':
        
       photo_url = f'https://svu1.org/telegr_bot/photos/%D8%A7%D9%84%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83%20%D8%A7%D9%84%D8%B0%D9%87%D8%A8%D9%8A.jpg'  # Replace with the actual path of the JPG photo
       response = requests.get(photo_url, stream=True)
    
       # Save the file locally
       with open('الاشتراك الذهبي.jpg', 'wb') as f:
        
            f.write(response.content)

          # Send the file to the user
            bot.send_chat_action(call.message.chat.id, 'upload_document')
            with open('الاشتراك الذهبي.jpg', 'rb') as f:
                
               bot.send_document(call.message.chat.id, f,timeout=300) 
            
            
    if call.data == 'silver':
        
       photo_url = f'https://svu1.org/telegr_bot/photos/%D8%A7%D9%84%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83%20%D8%A7%D9%84%D9%81%D8%B6%D9%8A.jpg'  # Replace with the actual path of the JPG photo
       response = requests.get(photo_url, stream=True)
       # Save the file locally
       with open('الاشتراك الفضي.jpg', 'wb') as f:
        
            f.write(response.content)

          # Send the file to the user
            bot.send_chat_action(call.message.chat.id, 'upload_document')
            with open('الاشتراك الفضي.jpg', 'rb') as f:
                
               bot.send_document(call.message.chat.id, f,timeout=300)   


bot.polling()