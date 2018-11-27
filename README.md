# little-quiz

## Run Locally
*Note : Requires Docker*

#### Basic Setup
1. Get the code
```bash
# in the directory where you want the repository
$ git clone https://github.com/marshall245/little-quiz.git
```


2. Using Docker, build and run the image
```bash
$ cd little-quiz
$ docker-compose up --build -d
```


3. Visiting the `http://localhost:8000/admin` should now work


#### Create an Admin User and Manage App
1. Find your container. Search under column name in the output to find it.
```bash
$ docker container ls
```

2. Access image at a shell prompt to create an admin user. Use the name from (1) in {NAME} below
```bash
$ docker exec -it {NAME} /bin/sh
```


2. From within the container run
```bash
# add an admin user; {USERNAME} :: {EMAIL} :: {PASSWORD}
(inner-prompt)$ /venv/bin/python manage.py createsuperuser
```


3. You can now go back to `http://localhost:8000/admin` and log in as an admin user. Here you can add dataabase entries, users, and user groups.


#### Clean Up
1. Use docker to stop and delete the image
```bash
$ docker-compose down
$ docker-compose rm -fv
```


#### Purge
You can thoroughly purge the necessary docker state using the following commands
    
    
###### Containers
    - docker container ls
    - docker container stop [containers]
    - docker container prune

    
###### Volumes
_Do not forget to remove the directories these are pointed to_

    - docker volume ls
    - docker volume rm [volumes]
    
    
###### Images
    - docker image ls
    - docker image rm [images]
