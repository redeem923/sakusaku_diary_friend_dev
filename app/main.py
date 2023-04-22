import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import Chatbot
from app.line_handler import LineHandler


app = FastAPI()
chatbot = Chatbot()

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
channel_secret = os.getenv("LINE_CHANNEL_SECRET")

line_handler = LineHandler(channel_access_token, channel_secret)


class Payload(BaseModel):
    events: list

# エンドポイント: ユーザーからのメッセージを受信


@app.post("/webhook")
async def handle_webhook(payload: Payload):
    for event in payload.events:
        print("=======================================")
        user_id, message_type, message_content = line_handler.parse_payload(
            event)
        print(f"User ID: {user_id}")
        print(f"Message type: {message_type}")
        print(f"Message content: {message_content}")

        if message_type is not None:
            response_message = chatbot.handle_message(
                user_id, message_type, message_content)

            if response_message is not None:
                line_handler.send_message(user_id, response_message)
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Hello World"}

# ローカルで実行する場合は、以下のコマンドを実行してください
# uvicorn app.main:app --reload
