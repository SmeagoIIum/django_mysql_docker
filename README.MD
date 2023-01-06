RESTful API displaying restaurants and their dishes (many to many-relationship)
on the basis of Django, Docker and a mysql db
PREREQUISITES: Docker, Postman
1. run '(sudo) docker-compose up' in the terminal (in the folder which contains the docker-compose file) which
    a) creates a 
2. Navigate to 'http://localhost:8000/REST/restaurants/' respectively 'http://localhost:8000/REST/restaurants/'
to get an overview of all restaurants and their dishes which have been loaded into the db beforehand
3. Use Postman or another API development environment to fire off HTTP requests
4. Alternatively you can navigate to 'http://localhost:9080/' 
   user: mysql-user, pw: mysql-password