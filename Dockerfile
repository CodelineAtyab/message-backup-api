FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install fastapi[all]
RUN pip install prometheus-fastapi-instrumentator

EXPOSE 8000

CMD [ "python", "main.py" ]
