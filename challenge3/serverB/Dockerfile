From debian

# install packages, python and pip

RUN apt-get update
RUN apt-get install -y iputils-ping
RUN apt-get install -y nginx
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install mysql-connector-python

# change default nginx html file

RUN echo "Hello World"  > /var/www/html/index.nginx-debian.html 


# https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile
# command that will always be executed when the container starts.

ENTRYPOINT service nginx restart && bash
ENTRYPOINT python3 /home/check.py && bash
