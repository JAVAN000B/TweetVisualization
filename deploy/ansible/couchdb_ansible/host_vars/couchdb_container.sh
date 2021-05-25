if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ]
then
    docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet)
    docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
fi

docker create\
      --name couchdb${node}\
      --env COUCHDB_USER=${user}\
      --env COUCHDB_PASSWORD=${pass}\
      --env COUCHDB_SECRET=${cookie}\
      --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\""\
      ibmcom/couchdb3:${VERSION}