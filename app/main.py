from fastapi import FastAPI, Depends
from app.api.api_v1 import api_router
from app.line_bot.handlers import line_handler, line_bot_api
from app.utils import get_settings

settings = get_settings()

app = FastAPI(title="Sakusaku Diary Friend")

app.include_router(api_router, prefix="/api/v1")

@app.post("/webhook")
async def webhook():
    signature = request.headers["X-Line-Signature"]
    body = await request.body()

    try:
        line_handler.handle(body.decode("utf-8"), signature)
    except Exception as e:
        print(f"Error: {str(e)}")
        return HTTPException(status_code=400)

    return {"message": "OK"}
