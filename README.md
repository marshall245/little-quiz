# little-quiz

## Run Locally

###### Basic Setup
*Note : Requires Docker*

1. Get the code
```bash
# in the directory where you want the repository
$ git clone https://github.com/marshall245/little-quiz.git
```


2. Using Docker, build and run the image
```bash
$ cd little-quiz
$ docker build -t little-quiz .
$ docker run -d -p 8000:8000 --name little-quiz -t little-quiz
```


3. Visiting the `http://localhost:8000/admin` should now work


###### Create an Admin User and Manage App
1. Access image at a shell prompt to create an admin user
```bash
$ docker exec -it little-quiz /bin/sh
```


2. From within the container run
```bash
# add an admin user; {USERNAME} :: {EMAIL} :: {PASSWORD}
(inner-prompt)$ python manage.py createsuperuser
```


3. You can now go back to `http://localhost:8000/admin` and log in as an admin user. Here you can add dataabase entries, users, and user groups.


###### Clean Up
6. Use docker to stop and delete the image
```bash
$ docker stop little-quiz
$ docker rm little-quiz
```

