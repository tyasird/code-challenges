From debian

# update, install packages, python and pip

RUN apt-get update
RUN apt-get install -y iputils-ping
RUN apt-get install -y default-mysql-client
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install mysql-connector-python

# check connection

CMD python3 /home/check.py && bash