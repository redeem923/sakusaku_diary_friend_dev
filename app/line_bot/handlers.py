from linebot import WebhookHandler
from linebot.models import TextMessage, MessageEvent
from app.ai import generate_diary
from app.line_bot.messages import create_carousel_message

line_handler = WebhookHandler(channel_secret="your_line_bot_channel_secret")

@line_handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

    if text.lower() == "日記を書いて":
        reply_token = event.reply_token
        user_id = event.source.user_id
        carousel_message = create_carousel_message(user_id)
        line_bot_api.reply_message(reply_token, carousel_message)

    elif "some_other_command" in text.lower():
        # Handle other commands here
        pass

    else:
        # Generate a diary entry based on the text message
        reply_token = event.reply_token
        user_id = event.source.user_id
        generated_diary = generate_diary(text, user_id)
        line_bot_api.reply_message(reply_token, TextMessage(text=generated_diary))
