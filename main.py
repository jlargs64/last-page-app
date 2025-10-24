import os
import uuid
from typing import Annotated

from ebooklib import epub
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "hello"}


@app.get("/health")
async def health():
    return {"status": "OK"}


@app.post("/api/create-cover")
async def create_cover(
    cover_image: Annotated[UploadFile, File()], author: Annotated[str, Form()]
):
    cover_image_bytes = await cover_image.read()
    book = epub.EpubBook()
    file_id = str(uuid.uuid1())
    book.set_identifier(file_id)
    book.set_title(f"{author}'s cover")
    book.add_author(author)
    book.set_language("en")
    book.set_cover(f"{author}_cover.png", cover_image_bytes)
    book.spine = ["cover"]
    epub_path = f"{file_id}.epub"
    epub.write_epub(epub_path, book, {})
    return FileResponse(epub_path, background=BackgroundTask(os.unlink, epub_path))
