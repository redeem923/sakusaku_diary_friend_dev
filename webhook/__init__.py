from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)
import logging
import azure.functions as func
from shared.settings import LINE_CHANNEL_SECRET, LINE_CHANNEL_ACCESS_TOKEN
from shared.chatbot import Chatbot

from linebot import (
    LineBotApi, WebhookHandler
)
chatbot = Chatbot()
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

    # reply_token = event.reply_token
    # user_id = event.source.user_id
    # message_type = event.message.type
    # message_content = event.message.text

    # if message_type is not None:
    #     response_message = chatbot.handle_message(
    #         user_id, message_type, message_content)
    #     if response_message is not None:
    #         line_bot_api.reply_message(
    #             reply_token=reply_token, messages=TextMessage(text=response_message))
