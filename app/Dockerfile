FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./main.py /app/

ARG PORT
EXPOSE ${PORT}

CMD fastapi run main.py --host 0.0.0.0 --port ${PORT}