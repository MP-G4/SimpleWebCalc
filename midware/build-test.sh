#!/bin/bash

#!/bin/bash

contaienr_name="midware"

db_name="database"

docker build -t ${contaienr_name} .
docker container stop ${contaienr_name}
docker container rm ${contaienr_name}
sleep 1
docker run \
    --name ${contaienr_name} \
    -d \
    -p 5000:5000 \
    --network velcome_net \
    --env DB_HOST=${db_host_name} \
    ${contaienr_name}



