FROM python:3
MAINTAINER Javi Polo <javipolo@drslump.org>

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -r requirements.txt

COPY http-show-headers.py .
CMD ["python", "-u", "http-show-headers.py" ]
