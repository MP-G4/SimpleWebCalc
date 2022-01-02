#!/bin/bash

contaienr_name="database"

db_username="donghaoran43"
db_userpass="a6569009"
db_rootpass="a6569009"
db_name="donghaoran43"

# docker build -t velcom .
docker container stop ${contaienr_name}
docker container rm ${contaienr_name}
sleep 1
docker network create velcome_net
# docker run --name ${contaienr_name} -d -p 18080:80 velcom
docker run \
    --detach \
    --name ${contaienr_name} \
    --env MARIADB_USER=${db_username} \
    --env MARIADB_PASSWORD=${db_userpass} \
    --env MARIADB_ROOT_PASSWORD=${db_rootpass} \
    -p 3306:3306 \
    --network velcome_net \
    mariadb:latest

sleep 5
#不需要建表，sqlAlchemy会自动建立
mysql -u root -h "127.0.0.1" -P 3306 -p${db_rootpass} -e "
CREATE DATABASE ${db_name};
use ${db_name};
CREATE TABLE cal_res (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	num VARCHAR(45), 
	calc VARCHAR(45), 
	PRIMARY KEY (id)
);
"