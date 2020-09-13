FROM python:3.8-alpine

ADD requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
ADD server.py ./server.py

CMD ["python3", "server.py"]
