from typing import Annotated

from fastapi import FastAPI, Form, UploadFile, APIRouter
from pypdf import PdfReader

pdf_router = APIRouter(prefix="/pdf", tags=['PDF Stuff'])

@pdf_router.post("/")
async def get(file: Annotated[UploadFile, Form()]):
    reader = PdfReader(file.file)
    data = ""
    for i in range(0, reader.get_num_pages()):
        data += reader.get_page(i).extract_text()
    return data
