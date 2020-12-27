import os
from transitions.extensions import GraphMachine

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

from utils import send_text_message,send_flex_message

import flex_template

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_candle(self, event):
        text=event.message.text
        return text.lower() == "candle"

    def is_going_to_spirit(self, event):
        text=event.message.text
        return text.lower() == "spirit"

    def is_going_to_dawn(self, event):
        text=event.message.text
        return text.lower() == "dawn"

    def is_going_to_prairie(self, event):
        text=event.message.text
        return text.lower() == "prairie"

    def is_going_to_forest(self, event):
        text=event.message.text
        return text.lower() == "forest"

    def is_going_to_valley(self, event):
        text=event.message.text
        return text.lower() == "valley"

    def is_going_to_wasteland(self, event):
        text=event.message.text
        return text.lower() == "wasteland"

    def is_going_to_vault(self, event):
        text=event.message.text
        return text.lower() == "vault"

    def is_going_to_menu(self, event):
        text=event.message.text
        return text.lower() == "menu"

    
    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        message = flex_template.main_menu
        message_to_reply = FlexSendMessage("開啟主選單", message)
        line_bot_api.reply_message(reply_token, message_to_reply)
        
        #send_flex_message(reply_token, "Please select the topic you want to know!",flex_template.main_menu)

    def on_enter_spirit(self, event):
        print("I'm entering spirit")
        reply_token = event.reply_token
        send_text_message(reply_token, "Please select the map you want to know!")

    def on_enter_candle(self, event):
        print("I'm entering candle")

        reply_token = event.reply_token
        send_text_message(reply_token, "Please select the map you want to know!")

###################################################################################
    def on_enter_spirit_dawn(self, event):
        print("I'm entering spirit_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the position of spirit in dawn:\nhttps://www.youtube.com/watch?v=pEpTD2MQHII")

    def on_enter_spirit_prairie(self, event):
        print("I'm entering spirit_prairie")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the position of spirit in prairie:\nhttps://www.youtube.com/watch?v=6T9eU6NI40c")

    def on_enter_spirit_forest(self, event):
        print("I'm entering spirit_forest")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the position of spirit in forest:\nhttps://www.youtube.com/watch?v=fS79CNXegoo")

    def on_enter_spirit_valley(self, event):
        print("I'm entering spirit_valley")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the position of spirit in valley:\nhttps://www.youtube.com/watch?v=7dnSrsYnA_4")

    def on_enter_spirit_wasteland(self, event):
        print("I'm entering spirit_wasteland")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the position of spirit in wasteland:\nhttps://www.youtube.com/watch?v=NeKvsyIZT58")

    def on_enter_spirit_vault(self, event):
        print("I'm entering spirit_vault")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the position of spirit in vault:\nhttps://www.youtube.com/watch?v=Ylx05jUcRIc")
    
#####################################################################################

    def on_enter_candle_dawn(self, event):
        print("I'm entering candle_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for dawn:\nhttps://www.youtube.com/watch?v=FkzpNHTANfs")

    def on_enter_candle_prairie(self, event):
        print("I'm entering candle_prairie")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for prairie:\nhttps://www.youtube.com/watch?v=sSxMKaOSm5U")

    def on_enter_candle_forest(self, event):
        print("I'm entering candle_forest")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for forest on Mon.,Wed.,Fri.,Sun.:\nhttps://www.youtube.com/watch?v=9WU8KHntBks \ncandle run for forest on Tue.,Thu.,Sat.:\nhttps://www.youtube.com/watch?v=iDkMlVjObXc")

    def on_enter_candle_valley(self, event):
        print("I'm entering candle_valley")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for valley:\nhttps://www.youtube.com/watch?v=swP1Pc1pZlE")

    def on_enter_candle_wasteland(self, event):
        print("I'm entering candle_wasteland")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for wasteland on Mon.,Wed.,Fri.:\nhttps://www.youtube.com/watch?v=swP1Pc1pZlE \ncandle run for wasteland on Tue.,Thu.,Sat.:\nhttps://www.youtube.com/watch?v=ULr1JlOV1eU \ncandle run for wasteland on Sun.:\nhttps://www.youtube.com/watch?v=y7H8C5uGW0o \ncandle run for ark in wasteland:\nhttps://www.youtube.com/watch?v=DJhBqg5fWks")

    def on_enter_candle_vault(self, event):
        print("I'm entering candle_vault")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for vault:\nhttps://www.youtube.com/watch?v=dCwAZ0PSoB0")