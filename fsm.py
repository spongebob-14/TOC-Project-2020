from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_candle(self, event):
        text=event.message.text()
        return text.lower() == "candle"

    def is_going_to_spirit(self, event):
        text=event.message.text()
        return text.lower() == "spirit"

    def is_going_to_dawn(self, event):
        text=event.message.text()
        return text.lower() == "dawn"

    def is_going_to_prairie(self, event):
        text=event.message.text()
        return text.lower() == "prairie"

    def is_going_to_valley(self, event):
        text=event.message.text()
        return text.lower() == "valley"

    def is_going_to_wasteland(self, event):
        text=event.message.text()
        return text.lower() == "wasteland"

    def is_going_to_wasteland(self, event):
        text=event.message.text()
        return text.lower() == "wasteland"

    def is_going_to_menu(self, event):
        text=event.message.text()
        return text.lower() == "menu"


    def on_enter_spirit(self, event):
        print("I'm entering spirit")
        reply_token = event.reply_token
        send_text_message(reply_token, "Please select the map you want to know!")

    def on_exit_spirit(self):
        print("Leaving spirit")

    def on_enter_candle(self, event):
        print("I'm entering candle")

        reply_token = event.reply_token
        send_text_message(reply_token, "Please select the map you want to know!")

    def on_exit_candle(self):
        print("Leaving candle")

    def on_enter_spirit_dawn(self, event):
        print("I'm entering spirit_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_prairie(self, event):
        print("I'm entering spirit_prairie")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of prairie")

    def on_enter_spirit_dawn(self, event):
        print("I'm entering spirit_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_dawn(self, event):
        print("I'm entering spirit_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")

    def on_enter_spirit_dawn(self, event):
        print("I'm entering spirit_dawn")

        reply_token = event.reply_token
        send_text_message(reply_token, "here is the inf. of dawn")