FROM python:3.8

RUN pip3 install gunicorn
RUN pip3 install gevent

ADD requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

ADD ./* ./

CMD ["gunicorn", "-c", "gunicorn_conf.py", "server:app"]
