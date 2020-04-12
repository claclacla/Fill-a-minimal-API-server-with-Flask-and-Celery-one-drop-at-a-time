# Fill an API server with Flask and Celery one drop at a time

--------------------------------------------------------------------------------

### Prerequisites

What things you need to install the software

```
docker 17+
docker-compose 1.19.0+
```

--------------------------------------------------------------------------------

### Installing

```
# Pull the python image
sudo docker pull python:3.6-slim

# Change the directory to the playground folder
cd path-to-your-playground

# Create a .env file with your local playground folder
echo "APP_FOLDER=/path-to-your-playground" > .env

```

--------------------------------------------------------------------------------

### Executing

```
# Run the environment
sudo docker-compose -f docker/dev/docker-compose.yaml up -d

# Authenticate
curl -i -X POST localhost:5000/login -d '{"username": "teacher1", "password": "password1"}' --header "Content-Type: application/json"

# Insert a course
curl -i -X POST localhost:5000/course -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODY3MjQ1OTgsIm5iZiI6MTU4NjcyNDU5OCwianRpIjoiOWZmYmFkMTktNzc2NC00NWZmLTlmMTctZWM5MWY3MjdkZWViIiwiZXhwIjoxNTg2NzI1NDk4LCJpZGVudGl0eSI6InRlYWNoZXIxIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.sEEC1XiWNU5pBfvnfzZz4MA2z07gkoPsz1ODGp__6TI" -d '{"title": "Flask: An API micro-framework"}' --header "Content-Type: application/json"

```

--------------------------------------------------------------------------------

## Authors

- **Simone Adelchino** - [github](https://github.com/claclacla)
