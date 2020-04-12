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

### Usage

```
# Run the environment
sudo docker-compose -f docker/dev/docker-compose.yaml up -d
```

#### Teacher

```
# Authenticate
# POST /login
curl -i -X POST localhost:5000/login -d '{"username": "teacher1", "password": "password1"}' --header "Content-Type: application/json"

# Insert a course
# POST /course
curl -i -X POST localhost:5000/course -H "Authorization: Bearer <token>" -d '{"title": "Flask: An API micro-framework"}' --header "Content-Type: application/json"

```

--------------------------------------------------------------------------------

## Authors

- **Simone Adelchino** - [github](https://github.com/claclacla)
