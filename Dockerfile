FROM python:3
RUN pip install --upgrade pip && \
    pip install flask && \
    pip install requests && \
    pip install redis && \
    pip install pymongo
COPY copy .
EXPOSE 8080
CMD ["python", "./controller.py"]
