from linebot import (
    LineBotApi, WebhookHandler
)
from shared.database import Database
from shared.ai_engine import AIEngine
from webhook.chatbot import Chatbot
from shared.settings import LINE_CHANNEL_SECRET, LINE_CHANNEL_ACCESS_TOKEN
import azure.functions as func
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)
import logging
logging.info(LINE_CHANNEL_SECRET)
logging.info(LINE_CHANNEL_ACCESS_TOKEN)
print("airmoto")

chatbot = Chatbot()
ai_engine = AIEngine()
db = Database()
handler = WebhookHandler(LINE_CHANNEL_SECRET)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # get x-line-signature header value
    signature = req.headers['x-line-signature']

    # get request body as text
    body = req.get_body().decode("utf-8")
    logging.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        func.HttpResponse(status_code=400)

    return func.HttpResponse('OK')


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    # [シンプルな日常報告、お勧めメニュー紹介、セールスプロモーション、セクシーなシチュエーション、趣味や好きなもの、日常の出来事、悩み]ここら辺を想定している
    # topic = "シンプルな日常報告"
    # past_diary_data = db.get_past_diary_data(topic)
    # generated_text = ai_engine.generate_diary_entry(
    #     topic, past_diary_data)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
