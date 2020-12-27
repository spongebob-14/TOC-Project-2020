import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["init", "candle", "spirit",
            "spirit_dawn","spirit_prairie","spirit_forest","spirit_valley","spirit_wasteland","spirit_vault",
            "candle_dawn","candle_prairie","candle_forest","candle_valley","candle_wasteland","candle_vault"
            ],
    transitions=[
        {
            "trigger": "advance",
            "source": "init",
            "dest": "candle",
            "conditions": "is_going_to_candle",
        },
        {
            "trigger": "advance",
            "source": "init",
            "dest": "spirit",
            "conditions": "is_going_to_spirit",
        },
        {
            "trigger": "advance",
            "source": "spirit",
            "dest": "spirit_dawn",
            "conditions": "is_going_to_dawn",
        },
        {
            "trigger": "advance",
            "source": "spirit",
            "dest": "spirit_prairie",
            "conditions": "is_going_to_prairie",
        },
        {
            "trigger": "advance",
            "source": "spirit",
            "dest": "spirit_forest",
            "conditions": "is_going_to_forest",
        },
        {
            "trigger": "advance",
            "source": "spirit",
            "dest": "spirit_valley",
            "conditions": "is_going_to_valley",
        },
        {
            "trigger": "advance",
            "source": "spirit",
            "dest": "spirit_wasteland",
            "conditions": "is_going_to_wasteland",
        },
        {
            "trigger": "advance",
            "source": "spirit",
            "dest": "spirit_vault",
            "conditions": "is_going_to_vault",
        },
        {
            "trigger": "advance",
            "source": "candle",
            "dest": "candle_dawn",
            "conditions": "is_going_to_dawn",
        },
        {
            "trigger": "advance",
            "source": "candle",
            "dest": "candle_prairie",
            "conditions": "is_going_to_prairie",
        },
        {
            "trigger": "advance",
            "source": "candle",
            "dest": "candle_forest",
            "conditions": "is_going_to_forest",
        },
        {
            "trigger": "advance",
            "source": "candle",
            "dest": "candle_valley",
            "conditions": "is_going_to_valley",
        },
        {
            "trigger": "advance",
            "source": "candle",
            "dest": "candle_wasteland",
            "conditions": "is_going_to_wasteland",
        },
        {
            "trigger": "advance",
            "source": "candle",
            "dest": "candle_vault",
            "conditions": "is_going_to_vault",
        },
        {
            "trigger": "advance",
            "source": "*",
            "dest": "init",
            "conditions": "is_going_to_menu",
        },
    ],
    initial="init",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"



@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    print("get graph\n")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
