# use latest mysql image
ARG version="latest"
ARG image="mysql"

# base image
FROM $image:$version

# install python3 and pip
RUN apt-get update
RUN apt-get install python3 python3-pip

# create base-directory
ENV base_directory="/urs/src/base"
RUN mkdir $base_directory

# copy source to base directory
ADD ./* /urs/src/base

# install requirement lib
ENV requirement_py_path=$base_directory/craw_data/requirements.txt
RUN pip3 install -r $requirement_py_path

# create database and import pseudo datas into db
ENV MYSQL_ROOT_PASSWORD="123"
ENV crawl_product_py_path=$base_directory/craw_data/crawl_product.py
ENV database_sql_path=$base_directory/base_config/database.sql
RUN mysql -u root -p 123 -e $database_sql_path

#expose ports
EXPOSE 80/TCP
EXPOSE 3333/TCP