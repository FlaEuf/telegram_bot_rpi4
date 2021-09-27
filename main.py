import Constants as C
import telebot
import ytlinkdownload as yt

API_KEY = C.API_KEY
bot = telebot.TeleBot(API_KEY)

def song_request(message):
    if len(message.text) < 3:
        return False
    else:
        return True

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "Welcome to SoundBot! Paste the YT link of the song you want to listen!")

@bot.message_handler(commands=['hello'])
def greet(message):
    bot.send_message(message.chat.id, "Hey! How is it going?")

@bot.message_handler(func=song_request)
def song_response(message):
    id = yt.get_audio_id(message.text)
    yt.download_song(message.text, id)
    vid = yt.get_vid(id)
    try:
        bot.send_audio(message.chat.id, audio=open(f"downloads/{id}/{vid}","rb"))
    except:
        bot.send_message(message.chat.id, "Not found, try again")

bot.delete_webhook()
bot.polling()
