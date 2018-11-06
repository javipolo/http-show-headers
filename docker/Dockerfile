FROM python:2
MAINTAINER Javi Polo <javipolo@drslump.org>

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -r requirements.txt

COPY http-show-headers.py .
CMD ["python", "http-show-headers.py" ]
