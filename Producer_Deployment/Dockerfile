FROM python:3.8
 
RUN pip3 install kafka-python

COPY ./app ./app
 
CMD ["python", "./app/main.py"]

