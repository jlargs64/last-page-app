from typing import Annotated
import tempfile
from pathlib import Path
from fastapi import FastAPI, File
from ebooklib import epub
from fastapi.responses import FileResponse
import uuid

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "hello"}


@app.get("/health")
async def health():
    return {"status": "OK"}


@app.post("/create-cover")
async def create_cover(cover_image: Annotated[bytes, File()], author: str):
    book = epub.EpubBook()
    book.set_identifier(uuid.uuid1())
    book.set_title(f"{author}'s cover")
    book.add_author(author)
    book.set_language("en")
    with tempfile.NamedTemporaryFile(delete=True, suffix="png") as tmp:
        tmp.write(cover_image)
        tmp_path = tmp.name
        book.set_cover(f"{author}_cover.png", cover_image)

        # return FileResponse()
        return {"ok": "ok"}
