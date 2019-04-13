FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
ADD . /code/
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
#CMD python3 manage.py runserver 0.0.0.0:8000