  




from telethon import TelegramClient , events
from telethon.client import chats

Api_Id = 10066580
api_hash = 'd1ec6ebc234cd88e33fea4eb955c6a51'

client = TelegramClient ('anon', Api_Id , api_hash)

@client.on(events. NewMessage)

async def handler(event):

    chats = await event.get_chat()
    chat_id = event.chat_id
    print("{}{}".format(chat_id , chats))

    if chat_id == -1001475250480  :
    

        await client.send_message(5116249669,event.raw_text)
         
    if chat_id == -1001764616724  :
        await client.send_message(5116249669,event.raw_text)

    if chat_id == -1001385004034  :
        await client.send_message(5116249669,event.raw_text)


    if chat_id == -1001357275556 :
        await client.send_message(5116249669,event.raw_text)



    if chat_id == -1001193143102 :
        await client.send_message(5116249669,event.raw_text)




client.start()
client.run_until_disconnected()