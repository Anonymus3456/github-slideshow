import telepot
import time
import random

def on_chat_message(msg):
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        ora = time.ctime()
        g = "cosa sai fare?" , "Cosa sai fare?"
        cose_che_sai_fare = "Sono ancora molto stupido ma il mio creatore mi sta allenando a fare tante cose, per adesso so fare: \n- ti posso dire l'ora; \n- posso dirti lo stato di salute del mio creatore; \n- posso dirti come sto io; "
        c = "come sta Francesco", "Come sta Francesco", "come se la passa Francesco"
        f = "come stai?" "Come stai?", "Come va?", "come va?"
        # Stato bot

        if txt in f:
            bot.sendMessage(chat_id, 'bene e tu?')
        # Cose che sa fare il bot

        elif txt in g:  
            bot.sendMessage(chat_id, name + " ecco cosa so fare: " + cose_che_sai_fare)
        # Orario

        elif txt == "che ore sono ?" or txt == "che ore sono?" or  txt == "ora?":
            bot.sendMessage(chat_id, name +" Questa è l'ora: " + ora[10: 19] )
        # Stato creatore

        elif txt == c :
            stato_Francesco = "Sta abbastanza bene, è molto contento che lo chiedi", "Vive come tutti gli esseri umani :) "," Penso stia bene, non sono il suo bot personale :( " 
            # Ancora da aggiornare
            bot.sendMessage(chat_id, name + random.choice(stato_Francesco))


TOKEN = '1873684255:AAHBK5C2D8-d37HjqpCGpBZaCUws6Kybd2s'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print ('Listening ...')


while 1:
    time.sleep(10)
