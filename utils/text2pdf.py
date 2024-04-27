from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def text2pdf(text):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    lines = text.split('\n')
    y = 800
    for line in lines:
        c.drawString(50, y, line)
        y -= 12
    c.save()
    return buffer.getvalue()