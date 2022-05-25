FROM python:3

WORKDIR /app

COPY requirements.txt ./

ENV DISPLAY :0

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/menu.py"]
