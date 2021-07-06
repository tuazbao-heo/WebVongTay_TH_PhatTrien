# use latest mysql image
ARG version="latest"
ARG image="mysql"

# base image
FROM $image:$version

# copy source to base directory
ADD ./* $BASE_DIRECTORY

# environments
ENV BASE_DIRECTORY="/usr/src/base"
ENV MYSQL_ROOT_PASSWORD="123"
ENV requirement_py_path=$BASE_DIRECTORY/craw_data/requirements.txt
ENV crawl_product_py_path=$BASE_DIRECTORY/craw_data/crawl_product.py
ENV database_sql_path=$BASE_DIRECTORY/base_config/database.sql

# install python3 and pip
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y install python3 python3-pip

# create base-directory
RUN mkdir -p $BASE_DIRECTORY

# install requirement lib
RUN pip3 install -r $requirement_py_path

# create database and import pseudo datas into db
RUN mysql -u root -p 123 -e $database_sql_path

#expose ports
EXPOSE 80/TCP
EXPOSE 3333/TCP