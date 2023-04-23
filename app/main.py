from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import Chatbot
from line_handler import LineHandler
import settings


app = FastAPI()
chatbot = Chatbot()

line_handler = LineHandler(
    settings.LINE_CHANNEL_ACCESS_TOKEN,
    settings.LINE_CHANNEL_SECRET
)


class Payload(BaseModel):
    events: list


@app.post("/webhook")
async def handle_webhook(payload: Payload):
    """webhookから送られてきたpayloadをパースする"""
    for event in payload.events:
        reply_token, user_id, message_type, message_content = line_handler.parse_payload(
            event)
        """メッセージを受け取ったときの処理"""
        if message_type is not None:
            response_message = chatbot.handle_message(
                user_id, message_type, message_content)
            """メッセージを送信する"""
            if response_message is not None:
                line_handler.send_message(
                    reply_token=reply_token,
                    user_id=user_id,
                    response_message=response_message
                )
    return {"status": "ok"}

# 開発環境でのみサーバーを起動
if __name__ == "__main__" and settings.ENV == "development":
    print("Starting development server at http://localhost:8000")
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
