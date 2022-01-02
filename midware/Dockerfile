FROM python:3.9

RUN mkdir -p midware/templates

COPY requirements.txt /midware
COPY start.sh /midware
COPY calculator.py /midware
COPY uwsgi.ini /midware
#COPY ./conf/ /midware
COPY ./templates/ /midware/templates

WORKDIR /midware

CMD [ "/midware/start.sh" ]