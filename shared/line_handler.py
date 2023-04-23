from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent
from chatbot import Chatbot


class LineHandler:

    def __init__(self, channel_access_token, channel_secret):
        self.chatbot = Chatbot()
        self.line_bot_api = LineBotApi(channel_access_token)
        self.handler = WebhookHandler(channel_secret)

    def parse_payload(self, payload):
        """webhookから送られてきたpayloadをパースする"""
        try:
            # self.handler.handle(payload, payload.get("signature"))
            return payload['replyToken'], payload['source']['userId'], payload['message']['type'], payload['message']['text']
        except InvalidSignatureError:
            print(
                "Invalid signature. Please check your channel access token/channel secret.")
            return None, None, None

    def handle_message(self, user_id, message_type, message_content):
        """メッセージを受け取ったときの処理"""
        return self.chatbot.handle_message(user_id, message_type, message_content)

    def send_message(self, reply_token, user_id, response_message):
        """メッセージを送信する"""
        try:
            self.line_bot_api.reply_message(
                reply_token=reply_token, messages=TextMessage(text=response_message))
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
