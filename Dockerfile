FROM python:3
RUN pip install --upgrade pip && \
    pip install flask
COPY copy .
VOLUME ./var/log/server.log
RUN python3 server.py
