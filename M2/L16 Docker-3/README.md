docker ps

docker run -d -p 8080:80 --name  my_nginx_cont nginx

docker stop  my_nginx_cont

#Загрузить ообраз из репозитория
docker pull redis

docker login

docker push 

docker run -d --name my_pg1  -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=mydb -v pgdata_temp:/var/lib/postgresql/data -p 5431:5432 postgres:17  

