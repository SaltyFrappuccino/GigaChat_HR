FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8005
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8005"]