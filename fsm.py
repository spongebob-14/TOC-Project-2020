from transitions.extensions import GraphMachine

from utils import send_text_message


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

    def is_going_to_valley(self, event):
        text=event.message.text
        return text.lower() == "valley"

    def is_going_to_wasteland(self, event):
        text=event.message.text
        return text.lower() == "wasteland"

    def is_going_to_wasteland(self, event):
        text=event.message.text
        return text.lower() == "wasteland"

    def is_going_to_menu(self, event):
        text=event.message.text
        return text.lower() == "menu"

    
    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_text_message(reply_token, "Please select the topic you want to know!")


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
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_prairie(self, event):
        print("I'm entering spirit_prairie")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of prairie")

    def on_enter_spirit_forest(self, event):
        print("I'm entering spirit_forest")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_valley(self, event):
        print("I'm entering spirit_valley")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_wasteland(self, event):
        print("I'm entering spirit_wasteland")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_vault(self, event):
        print("I'm entering spirit_vault")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")
    
#####################################################################################

    def on_enter_candle_dawn(self, event):
        print("I'm entering candle_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for dawn:https://www.youtube.com/watch?v=FkzpNHTANfs")

    def on_enter_candle_prairie(self, event):
        print("I'm entering candle_prairie")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for prairie:https://www.youtube.com/watch?v=sSxMKaOSm5U")

    def on_enter_candle_forest(self, event):
        print("I'm entering candle_forest")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for forest on Mon.,Wed.,Fri.,Sun.:https://www.youtube.com/watch?v=9WU8KHntBks \ncandle run for forest on Tue.,Thu.,Sat.:https://www.youtube.com/watch?v=iDkMlVjObXc")

    def on_enter_candle_valley(self, event):
        print("I'm entering candle_valley")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for valley:https://www.youtube.com/watch?v=swP1Pc1pZlE")

    def on_enter_candle_wasteland(self, event):
        print("I'm entering candle_wasteland")

        reply_token = event.reply_token
        send_text_message(reply_token, "candle run for wasteland on Mon.,Wed.,Fri.:https://www.youtube.com/watch?v=swP1Pc1pZlE \ncandle run for wasteland on Tue.,Thu.,Sat.:https://www.youtube.com/watch?v=ULr1JlOV1eU \ncandle run for wasteland on Sun.:https://www.youtube.com/watch?v=y7H8C5uGW0o \ncandle run for ark in wasteland:https://www.youtube.com/watch?v=DJhBqg5fWks")

    def on_enter_candle_vault(self, event):
        print("I'm entering candle_vault")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")