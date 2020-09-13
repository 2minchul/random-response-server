FROM python:3.8

RUN pip3 install uwsgi

ADD requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

ADD uwsgi.ini ./
RUN echo "processes = $(grep -c processor /proc/cpuinfo)" >> uwsgi.ini

ADD server.py ./

CMD ["uwsgi","uwsgi.ini"]
