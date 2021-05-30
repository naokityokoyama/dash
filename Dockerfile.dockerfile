FROM python:3.6

WORKDIR /usr
COPY ./requirements.txt /usr/requirements.txt

RUN pip install -r requirements.txt

COPY ./dataset /usr/dataset
ENTRYPOINT [ "python" ]

EXPOSE 8888
CMD ["./dashboard.py"]

