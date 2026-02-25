FROM python:3.12-slim
WORKDIR /app
COPY . ./
CMD pip install -r requirements.txt && python app.py
EXPOSE 5000