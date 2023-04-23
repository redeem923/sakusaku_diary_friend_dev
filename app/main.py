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
    for event in payload.events:
        user_id, message_type, message_content = line_handler.parse_payload(
            event)

        if message_type is not None:
            response_message = chatbot.handle_message(
                user_id, message_type, message_content)

            if response_message is not None:
                line_handler.send_message(user_id, response_message)
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Hello World"}

# 開発環境でのみサーバーを起動
if __name__ == "__main__" and settings.ENV == "development":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
