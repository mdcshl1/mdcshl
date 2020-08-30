from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import *
from telegram import *
import requests
import json
import random
from datetime import datetime
from flask import Flask, request
#from waitress import serve

app = Flask(__name__)
URL="https://mdchsl.herokuapp.com/"

channel_id ="@MedicoHero"
channel_id2="-1001412600360"
TOKEN="1310013681:AAH3GedNySqa1aQZvCz2EVC8XQW_BWGkh4U"
updater = Updater("1310013681:AAH3GedNySqa1aQZvCz2EVC8XQW_BWGkh4U", use_context=True)
ss = Bot(TOKEN)

#چک vip
def user_vaz(user_id):
    if(user_id not in vaz):return ""
    return vaz[user_id]


#ezafe kardane bank test
#viruvig1=[["صورت سوال",["گزينه 1","گزينه 2","گزينه 3","گزينه 4"],"2"],["soal2",["1","2","3","4"],1],["soal3",["1","2","3","4"],3],["soal4",["1","2","3","4"],0]]
#def viruvig(update, context):
    #chat_id = update.message.from_user["id"]
   # global nomtest
  #  nomtest[chat_id] = 0
 #   listest[chat_id] = viruvig1
#    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=listest[chat_id][nomtest[chat_id]][2],type="quiz", reply_markup = InlineKeyboardMarkup(shishe))
###
#def quiz (update, context):
#    global vaz
#    chat_id = update.message.from_user["id"]
#    file = open("vip.txt", "r")
#    codes = json.loads(file.read())
##    file.close()
#    users = list (codes.values())
#    if (chat_id in users):
        #اگر ويپ بود چيکار کنه
#    else:
#        update.message.reply_text("شما اجازه دسترسي به اين بخش را نداريد! \n براي دسترسي بايد اکانت خودتون رو به VIP تغيير بدين \n يا کد کاربري خودتون رو وارد کنيد")
#        vaz[chat_id]s="check"


#def vipcheck(update, context):
#    global vaz
#    chat_id = update.message.from_user["id"]

#    file = open("vip.txt","r")   
#    codes = json.loads(file.read())

#    file.close()
#    if (update.message.text in codes) and (codes[update.message.text]==0):
#        codes[update.message.text] = chat_id
#        file = open("vip.txt","w")
#        file.write(json.dumps(codes))
#        file.close()
#        update.message.reply_text("ثبت نام با موفقيت انجام شد!")
#        welcome(update,context)
#    elif(update.message in codes)and(codes[update.message.text]==chat_id):
#        update.message.reply_text("gabla vip shodi!")
#    else:
 #       update.message.reply_text("کد وارد شده صحيح نمي باشد! \n براي پيگيري از ادمين اقدام کنيد")
#    vaz[chat_id]=""



#براي شرط vip  هر تابع کافيه دستور زير رو بذاري

#کوييز




keyboardend=[[InlineKeyboardButton("🔚پایان آزمون",callback_data="endv")]]


def quizing (update,context): 
    update.message.reply_text("براي ساخت آزمون جديد بايد آزمون قبلي رو تموم بکنيد!", reply_markup = InlineKeyboardMarkup(keyboardend))
        

#کنترل دکمه هاي شيشه اي
def glassing(update, context):
    chat_id = update.callback_query.from_user["id"]
    update.callback_query.answer()
    global nomtest,tedadquiz
    data = update.callback_query.data
    if data == 'baz':
        welcome(update.callback_query,context)

    if data == 'next':
        if (chat_id in nomtest):
            nomtest[chat_id] = nomtest[chat_id] + 1
            if (nomtest[chat_id])<len(listest[chat_id]):
                update.callback_query.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=listest[chat_id][nomtest[chat_id]][2],type="quiz", reply_markup = InlineKeyboardMarkup(shishe))
            else:
                update.callback_query.message.reply_text("پايان"),pgtwo(update.callback_query,context)
        else:
             update.callback_query.message.reply_text("مدت زيادي از شروع کوئيز گذشته از اول مبحث خودتون رو انتخاب کنيد"),pgtwo(update.callback_query,context)
            
    
    if data == 'why':
        update.callback_query.message.reply_text('فقط کافيه سوال رو تو مديکوگروپ ارسال کني تا ادمين ها برات تحليلش کنن \n لینک گروه؛👇🏻👇🏻👇🏻👇🏻👇🏻 \n \n https://t.me/joinchat/RG0k4hhp-6BYfI-Q9HFdqA', reply_markup = InlineKeyboardMarkup(shishe))

    if data == 'backket':
        refrens(update.callback_query, context)

    if data == 'bkl':
        teaching(update.callback_query, context)
        
    if data == 'janquira':
        update.callback_query.message.reply_text("لينک دانلود:\n[http://46.4.162.94:8080/2136987454196924/Junqueira's_Basic_Histology%2014th%20Edition%202016.pdf] \n \n کتاب بافت شناسی جان کوئیرا 2016 \n ویرایش چهاردهم  \n\n\n\n\n مدیکوبات \n @MedicoHeroBot")

    if data == 'end':
        quizender(update.callback_query, context)

    if data == 'endv':
        vaz[chat_id]=""
        tedadquiz[chat_id] = ""
        esmquiz[chat_id]=""
        users_quiz[chat_id]=""
        pgtwo(update.callback_query, context)

    if data == 'nontime':
        quiztype[chat_id]=0
        update.callback_query.message.edit_text("کدوم درس؟", reply_markup = InlineKeyboardMarkup(esmq))

    if data == 'timedar':
        quiztype[chat_id]=45
        update.callback_query.message.edit_text("کدوم درس؟", reply_markup = InlineKeyboardMarkup(esmq))
        
        
    if data == '10':
        update.callback_query.answer(text="برگشت")
        tedadquiz[chat_id] = 10
        update.callback_query.message.edit_text("نوع آزمون را انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(noeq))

    if data == '25':
        tedadquiz[chat_id] = 25
        update.callback_query.message.edit_text("نوع آزمون را انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(noeq))

    if data == '20':
        tedadquiz[chat_id] = 20
        update.callback_query.message.edit_text("نوع آزمون را انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(noeq))

    if data == '30':
        tedadquiz[chat_id] = 30
        update.callback_query.message.edit_text("نوع آزمون را انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(noeq))

    if data == '40':
        tedadquiz[chat_id] = 40
        update.callback_query.message.edit_text("نوع آزمون را انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(noeq))

    if data == '50':
        tedadquiz[chat_id] = 50
        update.callback_query.message.edit_text("نوع آزمون را انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(noeq))

    if data == 'bazq':
        update.callback_query.message.edit_text("کدوم درس؟", reply_markup = InlineKeyboardMarkup(esmq))

    if data == 'bazt':
        vaz[chat_id] = ''
        quiztype[chat_id]=''
        tedadquiz[chat_id] = ''
        pgtwo(update.callback_query, context)

    if data == 'headvaneckq':
        update.callback_query.message.edit_text("مبحث مورد نظر خودتون رو انتخاب کنيد!📗" , reply_markup = InlineKeyboardMarkup(headvaneckq))

    if data == 'heart':
        update.callback_query.message.edit_text("مبحث مورد نظر خودتون رو انتخاب کنيد!📗" , reply_markup = InlineKeyboardMarkup(heartq))

    if data == 'bio2q':
        update.callback_query.message.edit_text("مبحث مورد نظر خودتون رو انتخاب کنيد!📗" , reply_markup = InlineKeyboardMarkup(biotwoq))

    if data == 'bio1q':
        update.callback_query.message.edit_text("مبحث مورد نظر خودتون رو انتخاب کنيد!📗" , reply_markup = InlineKeyboardMarkup(bioyekq))

    if data == 'boneheadqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("bonehead.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            boneheadsquiz[chat_id] = qs
            esmquiz[chat_id]= boneheadsquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''

    if data == 'heartfizioqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("bloodfizio.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            heartfiziosquiz[chat_id] = qs
            esmquiz[chat_id]= heartfiziosquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''


    if data == 'hearthistoqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("hearthisto.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            hearthistosquiz[chat_id] = qs
            esmquiz[chat_id]= hearthistosquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''



    if data == 'heartanaqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("heartana.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            heartanasquiz[chat_id] = qs
            esmquiz[chat_id]= heartanasquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''



    if data == 'gliqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("glicoliz.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            gliquiz[chat_id] = qs
            esmquiz[chat_id]= gliquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''
             
    if data == 'carbqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("carbohydrat.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            carbsquiz[chat_id] = qs
            esmquiz[chat_id]= carbsquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''


    if data == 'kereqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("kerebs.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            kerequiz[chat_id] = qs
            esmquiz[chat_id]= kerequiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''


    if data == 'muscleheadqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("musclehead.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            muscleheadquiz[chat_id] = qs
            esmquiz[chat_id]= muscleheadquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''

    if data == 'muscleneckqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("muscleneck.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            muscleneckquiz[chat_id] = qs
            esmquiz[chat_id]= muscleneckquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''

    

    if data == 'virusq':
        update.callback_query.message.edit_text("مبحث مورد نظر خودتون رو انتخاب کنيد!📗" , reply_markup = InlineKeyboardMarkup(virusq))

    if data == 'parvoqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("parvo.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            parvoquiz[chat_id] = qs
            esmquiz[chat_id]= parvoquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''


    if data == 'adenoqq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            test = open("adenov.txt", encoding="UTF-8")
            qs = json.loads(test.read())
            adenoquiz[chat_id] = qs
            esmquiz[chat_id]= adenoquiz[chat_id]
            if ((tedadquiz[chat_id])<=len(esmquiz[chat_id])):
                quizi(update.callback_query, context)
            
            else:
                 update.callback_query.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), pgtwo(update.callback_query,context)
                 vaz[chat_id] = ""
        else:
            update.callback_query.message.reply_text("زمان  کوئيز قبلي به اتمام رسيده \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update.callback_query,context)
            quiztype[chat_id] = ''


             
##بخش آموزش
    if data == 'hipf':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,3)

        
    if data == 'hips':
        testha = [["1- از بین عناصر زیر، کدامیک از هردو سوراخ سیاتیک بزرگ و کوچک می‌گذرد؟",["شریان پودندال تحتانی","شریان گلوتئال تحتانی","عصب سیاتیک","عصب جلدی رانی خلفی"],"0"],["2- بترتیب ASIS و PSIS محل اتصال کدامیک از عناصر زیر است؟",["سارتوریوس - لیگامنت ساکروتوبروز","رکتوس فموریس - گراسیلیس","سارتوریوس - گراسیلیس","رکتوس فموریس - لیگامنت ساکروتوبروز"],"0"],["3- به بخش ایلیوم استخوان لگن تمام عضلات زیر اتصال دارند بجز:",["گلوتئال فوقانی","گراسیلیس","لاتیسموس دورسی","رکتوس فموریس"],"1"],["4- ایلیاک توبروزیتی محل اتصال کدامیک از عناصر زیر می باشد؟",["لیگامنت ساکروتوبروز","لیگامنت ساکرو اسپاینوس","لیگامنت ساکروایلیاک","عضله ژملوس فوقانی"],"2"],["5- تمام عضلات زیر به تروکانتر بزرگ فمور اتصال دارند، بجز:",["گلوتوس مینیموس","گلوتوس مدیوس","گلوتوس ماگزیموس","پریفورمیس"],"2"],["6- تمام عناصر زیر در نمای خلفی بدن مشاهده می‌شوند، بجز:",["تروکانتر بزرگ","تروکانتر کوچک","اینترتروکانتریک کرست","اینترتروکانتریک لاین"],"3"]]

        for i in range(len(testha)):
            update.callback_query.message.reply_poll(question=testha[i][0],options=testha[i][1],correct_option_id=int(testha[i][2]),type="quiz")
        update.callback_query.message.reply_text("حالا که تست ها رو زدين و تموم شد، تحليل تست ها رو بخونيد تا کامل کامل مسلط بشين! \n 👇🏻👇🏻👇🏻👇🏻",reply_markup=InlineKeyboardMarkup(learnk))

    if data == 'hipt':
        update.callback_query.message.reply_text("⚜️سوال ۰۱⚜️\n ⬅️نکات مهم و پرتکرار: \n این نکته خیلی مهم رو یادتون باشه که🌱🌱شریان int.pudendal از هردو سوراخ عبور میکنه🌱🌱\n \n⚜️سوال ۰۲⚜️\n⬅️نکات مهم و پر تکرار:\n🔸 به ASIS سارتوریوس، به ant.inf.iliac spin ، رکتوس فموریس و به PSIS، لیگامنت ساکروتوبروز وصل می‌شه!\n\n⚜️سوال ۰۳⚜️\n⬅️نکات مهم و پرتکرار:\n🔸 اگر فیلم رو خوب دیده باشین سوال آسونیه فقط گزینه ۳ رو دقت کنید که؛\n✅به ایلیاک کرست، لاتیسموس دورسی میچسبه!\n\n⚜️سوال ۰۴⚜️\n⬅️نکات مهم و پرتکرار؛\n🔸ایلیاک توبروزیته کجا بود؟!🤔\nآفرین! زیر صفحه auricular ایلیوم.\nاین صفحه محل مفصل شدن ساکروم با ایلیوم هست پس باید یه لیگامانی وصل بشه که این دوتا رو محکم بهم بچسبونه!\nپس میشه؛ sacroilliac ligament!\n\n⚜️سوال ۰۵⚜️\n⬅️نکات مهم و پرتکرار:n🔸 اینم تست خیلی جالبیه که خوبه حفظش باشین!\nاینسرشن گلوتوس‌های مدیوس و مینیموس تروکانتر بزرگ \nو اینسرشن ماگزیموس روی تنه فموره🙃!\n\n⚜️سوال ۰۶⚜️\n⬅️نکات مهم و پرتکرار:\n🔸 😁لذت آناتومی😅!")

    if data == 'heartf':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,2)

        
    if data == 'hearts':
        testha = [["1",["1","2","3","4"],"0"],["1",["1","2","3","4"],"2"],["1",["1","2","3","4"],"3"],["1",["1","2","3","4"],"2"],["1",["1","2","3","4"],"2"]]
        for i in range(len(testha)):
            update.callback_query.message.reply_poll(question=testha[i][0],options=testha[i][1],correct_option_id=int(testha[i][2]),type="quiz")

    if data == 'heartt':
        update.callback_query.message.reply_text("متن تحليل"),update.callback_query.message.reply_text("حالا با اطمینان میتونی بگی که مبحث رو یاد گرفتی پس باخیال راحت برو سراغ بقیه چیزها! \n راستی از مرور مطالب غافل نشین که تو این مسیر پرفراز و نشیب خیلی ضروریه!")

##librery
    if data == 'anagry':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,8)

    if data == 'atlasgry':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,9)

    if data == 'snellana':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,10)

    if data == 'neterana':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,11)

    if data == 'imenabbas':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,12)
        
    if data == 'longman':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,13)

    if data == 'janinneter':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,14)

    if data == 'leninjer':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,15)

    if data == 'harper':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,16)

    if data == 'devline':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,17)

    if data == 'guyton':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,18)

    if data == 'bernva':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,19)

    if data == 'junqu':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,20)

    if data == 'neterbaft':
        Bot(TOKEN).forwardMessage(chat_id,channel_id2,21)
##
    if data == 'nextq':
        if (chat_id in tedadquiz) and (chat_id in quiztype):
            n=tedadquiz[chat_id]
            shomare[chat_id] = shomare[chat_id] + 1
            if (shomare[chat_id]< n ):
                global quiz_ids
                dpoll=update.callback_query.message.reply_poll(question=(qids[chat_id])[shomare[chat_id]][0],options=(qids[chat_id])[shomare[chat_id]][1],correct_option_id=(qids[chat_id])[shomare[chat_id]][2],type="quiz",open_period = quiztype[chat_id],is_anonymous=False, reply_markup = InlineKeyboardMarkup(shisheq))
                quiz_ids[dpoll.poll.id]=esmquiz[chat_id].index(qids[chat_id][shomare[chat_id]])

            
            else:
                update.callback_query.message.reply_text("آزمون به پایان رسید! \n\n برای تصحیح کوئیز روی دکمه زیر کلیک کنید! \n\n\n 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻🎯",reply_markup=dk) 
        else:
            update.callback_query.message.reply_text("فرصت پاسخ گويي به اتمام رسيد لطفا از اول شروع کيد"), pgtwo(update.callback_query, context)
            

    if data == 'nextql':
        if admin[1] == "open":
            n=tedadquiz[chat_id]
            shomare[chat_id] = shomare[chat_id] + 1
            if (shomare[chat_id]< n ):
                dpoll=update.callback_query.message.reply_poll(question=(qids[chat_id])[shomare[chat_id]][0],options=(qids[chat_id])[shomare[chat_id]][1],correct_option_id=(qids[chat_id])[shomare[chat_id]][2],type="quiz",open_period = 45,is_anonymous=False, reply_markup = InlineKeyboardMarkup(shisheql))
                quiz_ids[dpoll.poll.id]=esmquiz[chat_id].index(qids[chat_id][shomare[chat_id]])

            
            else:
                update.callback_query.message.reply_text("آزمون به پایان رسید! \n\n برای تصحیح کوئیز روی دکمه زیر کلیک کنید! \n\n\n 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻🎯",reply_markup=dk) 

        if admin[1] == "close":
                update.callback_query.message.reply_text("زمان ليگ تموم شده پس کجا بودي تا الان!"),welcome(update.callback_query, context)




    if data == 'startlig':
        if admin[1] == "open":
            if (chat_id not in yekbar):
                global liging
                liging[chat_id]="l"
                tedadquiz[chat_id] = 45
                test = open("lig.txt", encoding="UTF-8")
                qs = json.loads(test.read())
                lig[chat_id] = qs
                esmquiz[chat_id]= lig[chat_id]
                ligi(update.callback_query, context)

            else:

                update.callback_query.message.edit_text("فقط يکبار اجازه شرکت در ليگ را داريد!🎈 \n تا ليگ بعدي منتظر باشین "),welcome(update.callback_query,context)
        if admin[1] == "close":
            update.callback_query.message.reply_text("يادت نرفته که ليگ هامون پنج شنبه ها برگذار میشن👀! \n زیاد عجله نکن و فعلا از بقیه امکانات بات استفاده کن!"),welcome(update.callback_query,context)



    if data == 'amar':
        if admin[1] == "open":
            afrad = list(rotbelig.values())
            decind = sorted(afrad,key= lambda k:k[1],reverse = True)
            s = ""
            n=0
            for x in decind:
                n = n+1
                tartibi =str(n)+". "+ x[0]+"  =  "+str(x[1])+"\n"
                s = s+ tartibi
            
            update.callback_query.message.edit_text("آمار کوييز ها تا اين لحظه: \n"+ s , reply_markup = InlineKeyboardMarkup(retrys))
        if admin[1] == "close":
            update.callback_query.message.reply_text("يادت نرفته که ليگ هامون پنج شنبه ها برگذار میشن👀! \n زیاد عجله نکن و فعلا از بقیه امکانات بات استفاده کن!"),welcome(update,context)


    if data == 'retri':
            update.callback_query.message.edit_text("به لیگ این هفته مدیکو خوش اومدی! \n طبق روال همیشه یه توضیح کوچیک بدم؛ \nموضوع کوییز: \n تعداد سوالات🧩: 45تا \n مهلت شرکت⏳: تا پایان ساعت 24 امشب \n\n  📊توضیح: بعد از شرکت از دکمه آمار می‌تونید رتبه خودتون رو ببینید! \n *برای بعضی کوئیزها هم جایزه توپ داریم که توی کانال به اطلاعتون می‌رسونیم!🙃😉 \n موفق باشی🌷" ,reply_markup = InlineKeyboardMarkup(ligkey))

retrys = [[InlineKeyboardButton("بازگشت",callback_data = 'retri')]]

quiztype = {}

heartq = [[InlineKeyboardButton("آناتومی قلب", callback_data = 'heartanaqq'),InlineKeyboardButton("بافت شناسی قلب", callback_data = 'hearthistoqq')],
               [InlineKeyboardButton("فیزیولوژی قلب", callback_data = 'heartfizioqq'),InlineKeyboardButton("فیزیولوژی گردش خون", callback_data = 'bloodfizioqq')],[InlineKeyboardButton("بازگشت", callback_data = 'bazq')]]
    
biotwoq = [[InlineKeyboardButton("گلیکولیز", callback_data = "gliqq"),InlineKeyboardButton("چرخه کربس", callback_data = 'kereqq')],[InlineKeyboardButton("بازگشت", callback_data = 'bazq')]]        

#bioyekq = [[InlineKeyboardButton("کربوهیدرات", callback_data = "carbqq"),InlineKeyboardButton("چرخه کربس", callback_data = 'kereqq')],[InlineKeyboardButton("بازگشت", callback_data = 'bazq')]]        
bioyekq = [[InlineKeyboardButton("کربوهیدرات", callback_data = "carbqq")],[InlineKeyboardButton("بازگشت", callback_data = 'bazq')]]        


headvaneckq = [[InlineKeyboardButton("استخوان هاي سروگردن", callback_data = 'boneheadqq'),InlineKeyboardButton("عضلات گردن", callback_data = 'muscleneckqq')],
               [InlineKeyboardButton("عضلات صورت", callback_data = 'muscleheadqq')],[InlineKeyboardButton("بازگشت", callback_data = 'bazq')]]
virusq = [[InlineKeyboardButton("آدنوويروس", callback_data = "adenoqq"),InlineKeyboardButton("پاروويروس", callback_data = 'parvoqq')],[InlineKeyboardButton("بازگشت", callback_data = 'bazq')]]        

#
def checkozv(user_id):
    resp=requests.get("https://api.telegram.org/bot"+TOKEN+"/getChatMember?chat_id="+channel_id+"&user_id="+str(user_id)).json()
    if (resp["ok"]==True and resp["result"]["status"]in ["member","creator","administrator"]):return True
    print(resp["ok"],resp["result"]["status"])
    return False 

def reaction(update,context):
    if(checkozv(update.message.from_user["id"])):
        if(user_vaz(update.message.from_user["id"])==""):
            if(update.message.text in diction):
                diction[update.message.text](update,context)
            else:
                update.message.reply_text("با عرض پوزش، دستور مورد نظر يافت نشد!\n لطفا از دستورات زير استفاده کنيد يا در صورت بروز مشکل با ادمين از بخش ارتباط با ما درتماس باشيد🤖" ), welcome(update,context)
        else:
            vaz_dict[vaz[update.message.from_user["id"]]](update,context)
    else:
        update.message.reply_text("براي استفاده از امکانات ربات اول عضوکانال زير بشو و بعد دستور /start رو دوباره اجرا کن  \n 👇🏻👇🏻👇🏻👇🏻👇🏻")
        update.message.reply_text("[🧑🏻‍⚕️👨🏼‍⚕️MedicoHero🦸🏻‍♂️🦸🏻](https://t.me/MedicoHero)",parse_mode="Markdown")


#

def welcome(bot, context):
    keyboard = [['تست هاي علوم پايه⛑'],['فیلم و نکات آموزشی🎓','📚کتابخونه 📚'],['لیگ هفتگی 🎰'],['مديکوکانال','مديکوسايت','مديکوگروپ'],['ارتباط با ما📞'],['ارتقاء به  VIP🎖']]
    bot.message.reply_text(('سلام {} عزيز؛ \n'.format(bot.message.from_user.first_name))+'به مديکو بات خوش آمديد! ☺️☺️\n چطور میتونم کمکت کنم؟! \n\n *اگر میخوای تس بزنی یا کوئیز آنلاین بدی از بخش تست های علوم پایه⛑ اقدام کن! \n\n *اگر بدنبال جزوه و رفرنسی برو توی کتابخونه📚\n \n *یا اگه دنبال آموزش ها و جمع بندی هامون اومدی از فیلم ها و نکات آموزشی🎓 میتونی پیداشون کنی \n\n در ادامه راه های ارتباطی با ما رو میتونی ببینی و همچنین\n \n لیگ هفتگی مون رو میتونی طبق اطلاعیه کانال شرکت کنی \n با آرزوی موفقیت🌺 ️',reply_markup = ReplyKeyboardMarkup(keyboard , resize_keyboard = True, one_time_keyboard = True ))

#  
bazgashtbemnue =[
            [InlineKeyboardButton("بازگشت به منو 🔙",callback_data='baz')]]

bazgashtbemnue1 =[[InlineKeyboardButton("👨‍💻ادمین",url = 'https://t.me/medicoadmin')],
            [InlineKeyboardButton("بازگشت به منو 🔙",callback_data='baz')]]
                  

shishe=[[InlineKeyboardButton("چرا؟🧐",callback_data = 'why'),           InlineKeyboardButton("بعدي", callback_data = 'next')]]

#

def ertebat(update, context):
    update.message.reply_text("با کليد روي لينک زير ميتونيد با ادمين مديکو در تماس باشيد!📞 \n منتظرشنيدن نظرات قشنگ شما هستيم. \n 👨‍💻@Medicoadmin", reply_markup = InlineKeyboardMarkup(bazgashtbemnue1))

def site(update, context):
    update.message.reply_text("براي وارد شدن به سايت مديکو ميتونيد از لينک هاي زير اقدام کنيد🩺: \n صفحه اصلي سايت💻: https://medicohero.com/ \n ورود به دوره ها📑: https://medicohero.com/course/ \n دسترسي به پروفايل کاربري👤: https://medicohero.com/my-account/", reply_markup = InlineKeyboardMarkup(bazgashtbemnue))


def chanel(update, context):
    update.message.reply_text("لينک ورود به کانال مديکو هيرو🌪: \n https://t.me/joinchat/AAAAAFhk3oo2EU0_92rLtg", reply_markup = InlineKeyboardMarkup(bazgashtbemnue))

def ertegha(update, context):
    update.message.reply_text("اصلا اکانت VIP چی هست؟! \n حتما براتون پیش اومده که وقتی داشتین گشت و گذار می‌کردین توی بات با پیام (شما اجازه دسترسی به این بخش رو ندارید) روبرو شدین😳! \n خلاصه بگم که اگر اکانتتون رو VIP کنید اول از همه به ما کمک کردین تا خودمون رو توسعه بدیم!(😁) \n علاوه بر اون: \n *دسترسی به یکسری از مطالب آموزشی خاص رو پیدا می‌کنید. \n *بخش کوئیز براتون باز می‌شه که میتونید باهاش کوئیز بدین و کارنامه بگیرین \n و کلی چیز دیگه که بتدریج قراره اضافه بشه ! \n\n برای ارتقا چیکار کنم؟! \n کافیه یک پیام به آیدی زیر بدی و درخواست ارتقا بدی!(به همین سادگی) \n و تازه یه تخفیف عالییی ♨️♨️ براتون درنظر گرفتیم!🥳🥳  \n برای درخواست ارتقا و کسب اطلاعات بیشتر: \n                                  با ادمین درارتباط باشین🙃", reply_markup = InlineKeyboardMarkup(bazgashtbemnue1))
    
def group(update, context):
    update.message.reply_text("براي وارد شدن به گروه رفع اشکال از لينک زير اقدام کنيد😋: \n 🎯سوالايي که بلد نيستين رو بفرستين تا ادمين ها جواب بدن و تحليل شون کنن\n👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻  \n https://t.me/joinchat/RG0k4hhp-6BYfI-Q9HFdqA", reply_markup = InlineKeyboardMarkup(bazgashtbemnue))
#
def pgtwo(update, context):
    keyboard2 = [['کوییز(+کارنامه)','تست های مبحثی'],['آزمون هاي قطبي'],['بازگشت']]
    update.message.reply_text(' دوست داري تست ها رو چجوري برات بيارم؟! \n تست ها رو تک تک برات بيارم \n يا کوييز بدي و کارنامه بگيري؟!',reply_markup = ReplyKeyboardMarkup(keyboard2 , resize_keyboard = True , one_time_keyboard = True ))

def pgthree(update, contex):
#    keyboard3 = [['بلوک قلب❤️'],['ویروس شناسی🦠'],['آناتومی سروگردن💀','آناتومی اندام فوقانی💪🏻'],['بیوشیمی2 🧪','🧪بیوشیمی1 '],['🔙']]
     keyboard3 = [['بلوک قلب❤️'],['ویروس شناسی🦠'],['آناتومی سروگردن💀','coming soon...'],['بیوشیمی2 🧪','🧪بیوشیمی1 '],['🔙']]
     update.message.reply_text("درس مورد نظر خودتون رو انتخاب کنید!  \n اگر درس مورد نظرتون داخل لیست نیست میتونید به ادمین اطلاع بدین تا خیلی زود تست هاش اضافه بشن !\n مرسی که دنبالمون می کنید!☺️  ", reply_markup = ReplyKeyboardMarkup(keyboard3, resize_keyboard = True , one_time_keuboard = True))


#تست ها
def bioyek(update,context):
    bioyk = [['کربوهيدرات'],['ليپيدها'],['🔙🔙']]
    update.message.reply_text("بخش مورد نظر خودتون رو انتخاب کنيد!", reply_markup = ReplyKeyboardMarkup(bioyk, resize_keyboard = True, one_time_keyboard = True))

def carb(update, context):
    chat_id = update.message.from_user["id"]
    test = open("carbohydrat.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    carbohydrats[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = carbohydrats[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def biotwo(update,context):
    biotwok = [['گلیکولیز'],['چرخه کربس'],['🔙🔙']]
    update.message.reply_text("بخش مورد نظر خودتون رو انتخاب کنيد!", reply_markup = ReplyKeyboardMarkup(biotwok, resize_keyboard = True, one_time_keyboard = True))

def glicolize(update, context):
    chat_id = update.message.from_user["id"]
    test = open("glicoliz.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    glicolizs[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = glicolizs[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def kereb(update, context):
    chat_id = update.message.from_user["id"]
    test = open("kerebs.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    kerebss[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = kerebss[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

    
def uplimb(update,context):
    uplimbk = [['استخوان اندام فوقانی🦴','عضلات اندام فوقانی🥩'],['عروق اندام فوقانی🩸','اعصاب اندام فوقانی'],['🔙🔙']]
    update.message.reply_text("بخش مورد نظر خودتون رو انتخاب کنيد!", reply_markup = ReplyKeyboardMarkup(uplimbk, resize_keyboard = True, one_time_keyboard = True))

def heartblock(update, context):
    keyheart = [['آناتومي❤','بافت شناسي❤'],['فيزيولوژي ❤','🔙🔙']]
    update.message.reply_text('مبحث موردنظر خودتون رو انتخاب کنید!📚' , reply_markup = ReplyKeyboardMarkup(keyheart, resize_keyboard=True, one_time_keyboard= True))

def heartfizio(update,context):
    heartfizk = [['فيزيولوژي قلب','فيزيولوژي گردش خون'],['منو قلب']]
    update.message.reply_text("درس مدنظر خودتون رو انتخاب کنيد!", reply_markup = ReplyKeyboardMarkup(heartfizk, resize_keyboard = True , one_time_keyboard = True))

def bloodfizio(update, context):
    chat_id = update.message.from_user["id"]
    test = open("bloodfizio.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    bloodfizios[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = bloodfizios[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def hearthistology(update, context):
    chat_id = update.message.from_user["id"]
    test = open("hearthisto.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    hearthistos[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = hearthistos[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def heartanatomy(update, context):
    chat_id = update.message.from_user["id"]
    test = open("heartana.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    heartanas[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = heartanas[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def virology(update, context):
    keyviru = [['پاروويروس','آدنو ويروس'],['🔙🔙']]
    update.message.reply_text('مبحث موردنظر خودتون رو انتخاب کنید!📚' , reply_markup = ReplyKeyboardMarkup(keyviru, resize_keyboard=True, one_time_keyboard= True))

def headandneck(update,context):
    #keyhead = [['استخوان های سروگردن🦴','عضلات سروگردن🥩'],['عروق سروگردن🩸','🔙🔙']]
    keyhead = [['استخوان های سروگردن🦴','عضلات سروگردن🥩'],['🔙🔙']]
    update.message.reply_text('مبحث موردنظر خودتون رو انتخاب کنید!📚' , reply_markup = ReplyKeyboardMarkup(keyhead, resize_keyboard=True, one_time_keyboard= True))

def bonehead(update, context):
    chat_id = update.message.from_user["id"]
    test = open("bonehead.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    boneheads[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = boneheads[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def muscleheadvaneck(update,context):
    keybmhn = [['عضلات صورت','عضلات و مثلث هاي گردن'],['🔙🔙']]
    update.message.reply_text("مبحث مدنظر خودتون رو وارد کنيد", reply_markup = ReplyKeyboardMarkup(keybmhn, resize_keyboard = True , one_time_keyboard = True))

def musclehead(update, context):
    chat_id = update.message.from_user["id"]
    test = open("musclehead.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    muscleheads[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = muscleheads[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def muscleneck(update, context):
    chat_id = update.message.from_user["id"]
    test = open("muscleneck.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    musclenecks[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = musclenecks[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def parvo(update, context):
    chat_id = update.message.from_user["id"]
    test = open("parvo.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    parvo[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = parvo[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def adeno(update, context):
    chat_id = update.message.from_user["id"]
    test = open("adenov.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    adenovs[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = adenovs[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

#
#liber

def ketabkhane (update,context):
    update.message.reply_text ("به کتابخونه مديکوهيرو📚 خوش اومدي! \n   از اینجا میتونید به جزوات توپ و گلچین دانشگاه های مختلف و رفرنس های علوم پایه دسترسی پیدا کنید! \n بخش مورد نظر خودتون رو انتخاب کنید 👇🏻👇🏻👇🏻 ", reply_markup = ReplyKeyboardMarkup(liber, one_time_keyboard = True , resize_keyboard  = True))
    
def soon (update, context):
    update.message.reply_text("اين بخش به زودي تکميل ميشه! \n ممنون که با صبر و حوصله همراه ما هستين \n قدردان همراهي شما هستيم ☺️☺️🌺"), ketabkhane(update, context)

def manabe(update,context):
    chat_id = update.message.from_user["id"]
    Bot(TOKEN).forwardMessage(chat_id,channel_id2,22)
    ketabkhane(update,context)
    
def refrens (update, context):
    refrens = [['📗کتب آناتومي','📗کتب بیوشیمی'],['📗کتب فیزیولوژی','📗کتب جنین شناسی'],['📗کتب بافت‌شناسی','📗کتب ایمنی شناسی'],['↩️']]
    update.message.reply_text("درس مورد نظر خودتون رو انتخاب کنيد !✍🏼", reply_markup = ReplyKeyboardMarkup(refrens, one_time_keyboard = True , resize_keyboard = True))

def ketabbaft(update,context):
    keybaftk=[[InlineKeyboardButton("📖جان کوئیرا",callback_data = "junqu"),InlineKeyboardButton("📖اطلس نتر",callback_data = "neterbaft")],[InlineKeyboardButton("🔙",callback_data="backket")]]
    update.message.reply_text("رفرنس مدنظر خودتون رو انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(keybaftk))

def ketabanat(update,context):
    keyanatk=[[InlineKeyboardButton("📖آناتومی گری", callback_data = 'anagry'),InlineKeyboardButton("📖اطلس آناتومی گری",callback_data = 'atlasgry')],[InlineKeyboardButton("📖آناتومی اسنل",callback_data = 'snellana'),InlineKeyboardButton("📖اطلس آناتومی نتر",callback_data = 'neterana')],[InlineKeyboardButton("🔙",callback_data="backket")]]
    update.message.reply_text("رفرنس مدنظر خودتون رو انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(keyanatk))

def ketabbios(update,context):
    keybiosk=[[InlineKeyboardButton("📖لنینجر",callback_data = "leninjer"),InlineKeyboardButton("📖هارپر",callback_data = "harper")],[InlineKeyboardButton("📖دولین",callback_data = "devline")],[InlineKeyboardButton("🔙",callback_data="backket")]]
    update.message.reply_text("رفرنس مدنظر خودتون رو انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(keybiosk))

def ketabfizio(update,context):
    keyfiziok1=[[InlineKeyboardButton("📖برن و لوی", callback_data = "bernva"),InlineKeyboardButton("📖گایتون",callback_data = "guyton")],[InlineKeyboardButton("🔙",callback_data="backket")]]
    update.message.reply_text("رفرنس مدنظر خودتون رو انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(keyfiziok1))

def ketabjanin(update,context):
    keyjanink=[[InlineKeyboardButton("📖لانگمن ",callback_data = "longman"),InlineKeyboardButton("📖اطلس جنین نتر",callback_data = "janinneter")],[InlineKeyboardButton("🔙",callback_data="backket")]]
    update.message.reply_text("رفرنس مدنظر خودتون رو انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(keyjanink))

def ketabimeni(update,context):
    keyimenik=[[InlineKeyboardButton("📖ابوالعباس ",callback_data = "imenabbas")],[InlineKeyboardButton("🔙",callback_data="backket")]]
    update.message.reply_text("رفرنس مدنظر خودتون رو انتخاب کنيد!", reply_markup = InlineKeyboardMarkup(keyimenik))


#
#آموزش
def teaching(update, context):

    teach = [['جمع بندی آناتومی قلب❤️','🦴جمع بندی استخوان hip'],['ويس جمع بندي ويروس شناسي(VIP)'],['بازگشت']]
    update.message.reply_text("مطلب آموزشی مدنظرت رو انتخاب کن!🎦", reply_markup = ReplyKeyboardMarkup(teach, resize_keyboard = True , one_time_keyboard = True))

def virujam(update, context):
    global vaz
    chat_id = update.message.from_user["id"]
    file = open("vip.txt", "r")
    codes = json.loads(file.read())
    file.close()
    users = list (codes.values())
    if (chat_id in users):
        #اگر vip بود همه چي رو اينجا بايد بذاري 
        update.message.reply_text("تو ميتوني ببيني")        
    else:
        update.message.reply_text("شما اجازه دسترسي به اين بخش را نداريد! \n براي دسترسي بايد اکانت خودتون رو به VIP تغيير بدين \n 🆔 يا کد کاربري خودتون رو وارد کنيد")
        vaz[chat_id]="check"
        
def vipcheck(update, context):
    global vaz
    chat_id = update.message.from_user["id"]

    file = open("vip.txt","r")   
    codes = json.loads(file.read())
    file.close()
    if (update.message.text in codes) and (codes[update.message.text]==0):
        codes[update.message.text] = chat_id
        file = open("vip.txt","w")
        file.write(json.dumps(codes))
        file.close()
        ss.sendMessage(chat_id = 176567087 ,text="#vip \n"+"کاربري با آيدي زير وارد ليست VIPهاشد: \n {}".format(update.message.from_user.first_name)+"\n"+str(chat_id)+"\n"+"@"+update.message.from_user['username']+"\n"+"\n"+"تاريخ: \n"+datetime.today().strftime('%Y-%m-%d %H:%M'))
        ss.sendMessage(chat_id = 1148003554 ,text="#vip \n"+"کاربري با آيدي زير وارد ليست VIPهاشد: \n {}".format(update.message.from_user.first_name)+"\n"+str(chat_id)+"\n"+"@"+update.message.from_user['username']+"\n"+"\n"+"تاريخ: \n"+datetime.today().strftime('%Y-%m-%d %H:%M'))
        update.message.reply_text("باتشکر از خرید شما! \n ثبت نام شما در تاریخ :{} با موفقیت انجام شد! ✅🎖\n از این به بعد می توانید به تمامی محتوای بات دسترسی داشته باشید.🔓 \n از جمله مطالب آموزشی ویژه، رفرنس های و جزوات خاص، فایل های جمع بندی توپ مدیکو و در آخر و مهم تر از همه ساخت کوئیز با کارنامه  وکلی چیز دیگه که قراره اضافه بشه😁🧐😎 \n ما رو به دوستاتون هم معرفی کنید😘".format(datetime.today().strftime('%Y-%m-%d %H:%M')))
        welcome(update,context)
    elif(update.message in codes)and(codes[update.message.text]==chat_id):
        update.message.reply_text("gabla vip shodi!")
    else:
        update.message.reply_text("کد وارد شده صحيح نمي باشد! \n براي پيگيري از ادمين اقدام کنيد")
    vaz[chat_id]=""


learnk = [[InlineKeyboardButton("📽فیلم آموزش", callback_data = 'hipf'),InlineKeyboardButton("❓تست مروری"  ,callback_data = "hips"),InlineKeyboardButton("تحلیل سوالات",callback_data='hipt')],[InlineKeyboardButton("بازگشت",callback_data='bkl')]]
def hipbone(update, context):
    update.message.reply_text("سلام مجدد🙃! \n به آموزش ما خوش اومدی! \n اینجا قراره خیلی حرفه ای مبحث رو جمعش کنیم! 👊🏻 \n پس اول. فیلم رو ببین \n دوم. تست هایی که برات درنظر گرفتیم رو بزن \n و در آخر. بیا تا باهم تست ها رو تحلیل کنیم \n\n موفق باشی!🧨", reply_markup = InlineKeyboardMarkup(learnk))

learnkh = [[InlineKeyboardButton("📽فیلم آموزش", callback_data = 'heartf'),InlineKeyboardButton("❓تست مروری"  ,callback_data = "hearts"),InlineKeyboardButton("تحلیل سوالات",callback_data='heartt')],[InlineKeyboardButton("بازگشت",callback_data='bkl')]]
def heartl(update, context):
    update.message.reply_text("سلام مجدد🙃! \n به آموزش ما خوش اومدی! \n اینجا قراره خیلی حرفه ای مبحث رو جمعش کنیم! 👊🏻 \n پس اول. فیلم رو ببین \n دوم. تست هایی که برات درنظر گرفتیم رو بزن \n و در آخر. بیا تا باهم تست ها رو تحلیل کنیم \n\n موفق باشی!🧨", reply_markup = InlineKeyboardMarkup(learnkh))


    #                          
def ghotbes98shahrivar(update, context):
    chat_id = update.message.from_user["id"]
    test = open("es98clasicshah.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    es98clasicshahs[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = es98clasicshahs[chat_id]
    update.message.reply_text("#اصفهان #98 #شهریور #کلاسیک".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))

def shahrivarq8new(update, context):
    chat_id = update.message.from_user["id"]
    test = open("shahrivarq8new.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    shahrivarq8news[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = shahrivarq8news[chat_id]
    update.message.reply_text("#قطب8 #98 #شهریور #ریفرم".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))


def ghotbi(update, context):
    update.message.reply_text("آزمون مد نظر خودتون رو انتخاب کنيد! \n خيلي ممنونيم که مارو همراهي مي کنيد☺️☺️🙏🏻",reply_markup =ReplyKeyboardMarkup(ghotb,resize_keyboard=True,one_time_keyboard = True))
ghotb = [["اصفهان 98 -شهریور(کلاسیک)","قطب8-98شهریور-ریفرم"],['🔙']]

def kerman98rif(update, context):
    chat_id = update.message.from_user["id"]
    test = open("boneheads.txt", encoding="UTF-8")
    qs = json.loads(test.read())
    boneheads[chat_id] = qs
    global nomtest
    nomtest[chat_id] = 0
    listest[chat_id] = boneheads[chat_id]
    update.message.reply_text("محتوا: \n تعداد تست ها🔥: {} \n موفق باشيد!".format(len(listest[chat_id])))
    update.message.reply_poll(question=listest[chat_id][nomtest[chat_id]][0],options=listest[chat_id][nomtest[chat_id]][1],correct_option_id=int(listest[chat_id][nomtest[chat_id]][2]),type="quiz", reply_markup = InlineKeyboardMarkup(shishe))


#quiz
esmq = [[InlineKeyboardButton("آناتومي سروگردن",callback_data='headvaneckq'),(InlineKeyboardButton("ويروس شناسي", callback_data = 'virusq'))],[InlineKeyboardButton("بیوشیمی2",callback_data='bio2q'),InlineKeyboardButton("بیوشیمی1",callback_data='bio1q')],[InlineKeyboardButton("بلوک قلب", callback_data='heart')]]

noeq = [[InlineKeyboardButton("زمان دار(45ثانيه)",callback_data='timedar'),(InlineKeyboardButton("بدون زمان", callback_data = 'nontime'))],[InlineKeyboardButton("بازگشت", callback_data='bazt')]]

tedad = [[InlineKeyboardButton("10", callback_data = "10"),InlineKeyboardButton("20", callback_data = "20")],[InlineKeyboardButton("25", callback_data = "25")],[InlineKeyboardButton("30", callback_data = "30"),InlineKeyboardButton("40", callback_data = "40")],[InlineKeyboardButton("50", callback_data = "50")],[InlineKeyboardButton("برگشت", callback_data = "bazt")]]


def quiz0 (update, context):
    global vaz
    chat_id = update.message.from_user["id"]
    if (chat_id not in liging):
        file = open("vip.txt", "r")
        codes = json.loads(file.read())
        file.close()
        users = list (codes.values())
        if (chat_id in users):
            vaz[chat_id]="quizing"
            update.message.reply_text("تعداد سوالات کوئيز مدنظر رو انتخاب کنيد! 🖌", reply_markup = InlineKeyboardMarkup(tedad))
        
        else:
            update.message.reply_text("شما اجازه دسترسي به اين بخش را نداريد! \n براي دسترسي بايد اکانت خودتون رو به VIP تغيير بدين \n 🆔 يا کد کاربري خودتون رو وارد کنيد")
            vaz[chat_id]="check"
    elif liging[chat_id]=="":
        file = open("vip.txt", "r")
        codes = json.loads(file.read())
        file.close()
        users = list (codes.values())
        if (chat_id in users):
            vaz[chat_id]="quizing"
            update.message.reply_text("تعداد سوالات کوئيز مدنظر رو انتخاب کنيد! 🖌", reply_markup = InlineKeyboardMarkup(tedad))
        
        else:
            update.message.reply_text("شما اجازه دسترسي به اين بخش را نداريد! \n براي دسترسي بايد اکانت خودتون رو به VIP تغيير بدين \n 🆔 يا کد کاربري خودتون رو وارد کنيد")
            vaz[chat_id]="check"
            
    elif liging[chat_id]=="l":
        update.message.reply_text("اول ليگ خودتون رو به پايان برسونيد بعد ادامه بديد", reply_markup = dk)

shisheq=[[         InlineKeyboardButton("بعدي", callback_data = 'nextq')],[InlineKeyboardButton("🔚پایان آزمون" ,callback_data ="end")]]
shisheql=[[         InlineKeyboardButton("بعدي", callback_data = 'nextql')],[InlineKeyboardButton("🔚پایان آزمون" ,callback_data ="end")]]


def quizi(update,context):
    chat_id = update.from_user["id"]
    if (chat_id in tedadquiz) and (chat_id in quiztype):
        n=tedadquiz[chat_id]
        global users_quiz,quiz_ids
    #tedad test ha
        qids[chat_id]=random.sample(esmquiz[chat_id],n)
        update.message.reply_text("آزمون شروع شد")
        #print("$",type(qids[chat_id]))
        LL = []
        for i in qids[chat_id]:
            LL+=[esmquiz[chat_id].index(i)]
        users_quiz[chat_id]=[LL,[-1]*n]
        
        shomare[chat_id] = 0
        if (n<=len(esmquiz[chat_id])):
      #      print(chat_id,quiz_ids,qids)
            dpoll=update.message.reply_poll(question=(qids[chat_id])[shomare[chat_id]][0],options=(qids[chat_id])[shomare[chat_id]][1],correct_option_id=(qids[chat_id])[shomare[chat_id]][2],open_period =quiztype[chat_id], type="quiz",is_anonymous=False,reply_markup = InlineKeyboardMarkup(shisheq))
            quiz_ids[dpoll.poll.id]=esmquiz[chat_id].index(qids[chat_id][shomare[chat_id]])
    #        print(users_quiz)
        if (n>>len(esmquiz[chat_id])):
            update.message.reply_text("تعداد سوالات اين مبحث کمتر از تعداد انتخابي شماست!"), quiz0(update,context)
    else:
        update.message.reply_text("زمان اامه کوئيز قبلي به اتمام رسيده1 \n براي ساخت کوئيز جديد مجددا اقدام کنيد"), pgtwo(update,context)

liging={}

def quizender(update,context):
    chat_id=update.from_user["id"]
    n=tedadquiz[chat_id]
    global users_quiz,quiz_ids,vaz_quiz,quiztype
    #print('#',users_quiz[chat_id],user_vaz(chat_id))
    #print ('@', (user_vaz(chat_id)=="quizing"), chat_id in users_quiz)
    if(user_vaz(chat_id)=="quizing")and(chat_id in users_quiz):
        correct=0
        wrong=0
        blank=0
        for x in range(n):
            #print(chat_id, users_quiz, x)
            qid=users_quiz[chat_id][0][x]
            ans=users_quiz[chat_id][1][x]
            #print(qid,ans)
            if(ans==-1):blank+=1
            elif(str(ans)==esmquiz[chat_id][qid][2]):correct+=1
            else:wrong+=1

        users_quiz[chat_id]=""
        vaz[chat_id]=""
        quiztype[chat_id] = ""
        update.message.reply_text("تعداد سوالات🔸:    "+str(n)+"\n"+"پاسخ صحيح✅:      "+str(correct)+"\n"+"پاسخ غلط❌:          "+str(wrong)+"\n"+"نزده💤:                   "+    str(blank))
        update.message.reply_text("درصد📊:        "+ str(round(correct/n*100))+"%")
        pgtwo(update,context)
        tedadquiz[chat_id] = ""
        esmquiz[chat_id]=""

    elif(user_vaz(chat_id)!="quizing")and(chat_id in users_quiz):
        if liging[chat_id]=="l":
            global yekbar
            yekbar[chat_id]="1"
            correct=0
            wrong=0
            blank=0
            for x in range(n):
                #print(chat_id, users_quiz, x)
                qid=users_quiz[chat_id][0][x]
                ans=users_quiz[chat_id][1][x]
                #print(qid,ans)
                if(ans==-1):blank+=1
                elif(str(ans)==esmquiz[chat_id][qid][2]):correct+=1
                else:wrong+=1

            users_quiz[chat_id]=""
            vaz[chat_id]=""
            update.message.reply_text("تعداد سوالات🔸:    "+str(n)+"\n"+"پاسخ صحيح✅:      "+str(correct)+"\n"+"پاسخ غلط❌:          "+str(wrong)+"\n"+"نزده💤:                   "+    str(blank))
            update.message.reply_text("درصد📊:        "+ str(round(correct/n*100))+"%")
            welcome(update,context)
            tedadquiz[chat_id] = ""
            esmquiz[chat_id]=""
            liging[chat_id] = ""
            d=round(correct/n*100)
            rotbelig[chat_id] = [e[chat_id],d]
            print(rotbelig[chat_id])


    else:
        update.message.reply_text("در حال حاضر آمون فعالي وجود ندارد! \n از کيبورد زير کوئيز خودتون رو شروع کنيد!👇🏻"), pgtwo(update,context)
        users_quiz[chat_id]=""
        vaz_quiz[chat_id]=""


def javabdad(update,context):
    global users_quiz,quiz_ids
    quizid=update.poll_answer.poll_id
    userans=update.poll_answer.option_ids[0]
    chat_id=update.poll_answer.user.id
#    print(quiz_ids[quizid] , users_quiz[chat_id])
    if(chat_id in users_quiz)and(quizid in quiz_ids)and(quiz_ids[quizid] in users_quiz[chat_id][0]):
        #print(8989)
        qid=quiz_ids[quizid]
        #print(qid)
        ind=users_quiz[chat_id][0].index(qid)
        users_quiz[chat_id][1][ind]=userans
        quiz_ids.pop(quizid)

updater.dispatcher.add_handler(PollAnswerHandler(javabdad))

##lig
ligkey = [[InlineKeyboardButton("آمار ليگ", callback_data = "amar"),InlineKeyboardButton("شروع ليگ", callback_data = 'startlig')],[InlineKeyboardButton("بازگشت", callback_data='baz')]]




admin = {1:"close"}
yekbar={}

def lig0 (update, context):
    update.message.reply_text("يادت نرفته که ليگ هامون پنج شنبه ها برگذار میشن👀! \n زیاد عجله نکن و فعلا از بقیه امکانات بات استفاده کن!"),welcome(update,context)


def ligi(update,context):
    update.message.edit_text("آزمون شروع شد")

def adminlig(update,context):            
    chat_id = update.message.from_user["id"]
    if(update.message.from_user["id"] == 176567087):
        global admin,rotbelig,lig,yekbar,liging
        if update.message.text == 'strtlig':
            admin[1] = 'open'
            update.message.reply_text("حله! باز شد.")


        if update.message.text == 'clslig':
            afrad = list(rotbelig.values())
            decind = sorted(afrad,key= lambda k:k[1],reverse = True)
            s = ""
            n=0
            for x in decind:
                n = n+1
                tartibi =str(n)+". "+ x[0]+"  =  "+str(x[1])+"\n"
                s = s+ tartibi
            ss.sendMessage(chat_id = 176567087 ,text="آمار ليگ: \n"+s)
            ss.sendMessage(chat_id = 1148003554 ,text="آمارليگ: \n"+s)
            update.message.reply_text("بسته شد ادمين")
            admin[1] = 'close'
            rotbelig={}
            liging[chat_id]=""
            lig = {}
            yekbar = {}


##

keyboard2=[[InlineKeyboardButton("🔚پایان آزمون",callback_data="end")]]
dk=InlineKeyboardMarkup(keyboard2,resize_keyboard=True)
boneheadsquiz = {}
muscleheadquiz = {}
muscleneckquiz = {}
kerequiz = {}
es98clasicshahs = {}
heartanas = {}
parvoquiz = {}
kerebss = {}
heartfiziosquiz = {}
adenovs = {}
heartanasquiz = {}
hearthistosquiz = {}
adenoquiz = {}
carbsquiz = {}
shahrivarq8news = {}
gliquiz = {}
glicolizs = {}
carbohydrats = {}
hearthistos = {}
tedadquiz = {}
esmquiz = {}
shomare = {}
qids = {}
vaz_quiz = {}
users_quiz = {}
quiz_ids = {}



#dics
vaz={}
tedadquiz = {}
L = {}
listest = {}
nomtest = {}
vaz_dict={"check":vipcheck,"quizing":quizing}
users_quiz={}
quiz_ids={}
diction = {'اصفهان 98 -شهریور(کلاسیک)':ghotbes98shahrivar,"قطب8-98شهریور-ریفرم":shahrivarq8new,
            'گلیکولیز':glicolize,'چرخه کربس':kereb,'🧪بیوشیمی1':bioyek,'کربوهيدرات':carb,'بافت شناسي❤':hearthistology,'آدنو ويروس':adeno,'جمع بندی آناتومی قلب❤️':heartl,'آناتومي❤':heartanatomy,
            'فيزيولوژي':heartfizio,'منو قلب':heartblock,'فيزيولوژي ❤':heartfizio,'فيزيولوژي قلب':bloodfizio,'🦴جمع بندی استخوان hip':hipbone,'آناتومی اندام فوقانی💪🏻':uplimb,'بیوشیمی2 🧪':biotwo,
            'strtlig':adminlig,'clslig':adminlig,'لیگ هفتگی 🎰':lig0,'عضلات صورت':musclehead,'عضلات و مثلث هاي گردن':muscleneck,'📚کتابخونه 📚':ketabkhane,'coming soon...':soon,'منابع آزمون علوم پایه✍🏼':manabe,'/start':welcome,
           'کرمان-شهريور98(ريفرم)':kerman98rif,'↩️':ketabkhane, 'رفرنس هاي انگليسي':refrens,'📗کتب بافت‌شناسی':ketabbaft,'📗کتب آناتومي':ketabanat,'📗کتب بیوشیمی':ketabbios, '📗کتب فیزیولوژی':ketabfizio, '📗کتب جنین شناسی':ketabjanin, '📗کتب ایمنی شناسی':ketabimeni,
           'ويس جمع بندي ويروس شناسي(VIP)':virujam,'تست های مبحثی':pgthree,'بلوک قلب❤️':heartblock,'🔙':pgtwo,'🔙🔙':pgthree,'استخوان های سروگردن🦴':bonehead,'عضلات سروگردن🥩':muscleheadvaneck,
           'ارتقاء به  VIP🎖':ertegha,'فیلم و نکات آموزشی🎓':teaching, 'ارتباط با ما📞':ertebat,"کوییز(+کارنامه)":quiz0,"آزمون هاي قطبي":ghotbi,'آناتومی سروگردن💀':headandneck,'ویروس شناسی🦠':virology,'پاروويروس':parvo,
            "مديکوسايت":site,"بازگشت ":pgtwo,"بازگشت":welcome,"مديکوگروپ":group,"ارتقاء حساب کاربري 💎":ertegha,"مديکوکانال":chanel,"تست هاي علوم پايه⛑":pgtwo}
boneheads = {}
muscleheads = {}
musclenecks = {}
bloodfizios = {}
parvo = {}
kermanshah98rif = {}



@app.route('/'+TOKEN,methods=['POST'])
def respond():
    update=Update.de_json(request.get_json(force=True),ss)
    print("SALAAAM")
    updater.dispatcher.process_update(update)

    return 'ok'
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    print("set")
    s = ss.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
@app.route('/')
def index():
    print("!")
    return 'I feel alive!'


updater.dispatcher.add_handler(MessageHandler(Filters.text,reaction))
updater.dispatcher.add_handler(CallbackQueryHandler(glassing))
updater.dispatcher.add_handler(CommandHandler('start', welcome))


if __name__=='__main__':app.run()

