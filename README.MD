RESTful API on the basis of Django, Docker and a mysql db 

PREREQUISITES: Python, Docker, Docker compose

1. run '(sudo) docker-compose build' and '(sudo) docker-compose up' in the terminal (in the folder which contains the docker-compose file)
2. Navigate to 'http://localhost:8000/register/' to create a new user
3. Navigate to 'http://localhost:8000/' to get an overview of all users in the db
4. Alternatively you can navigate to 'http://localhost:9080/' and change the database entries directly
   (server: mysql-airflow, user: root, pw: mysql, db: airflow_db)