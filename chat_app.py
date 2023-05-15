from fastapi import FastAPI, HTTPException
import chat_service

app = FastAPI()

@app.get("/chat")
def chat(
    humen_input: str | None = None
) -> str:

    chat_response = chat_service.chat(humen_input)

    return chat_response