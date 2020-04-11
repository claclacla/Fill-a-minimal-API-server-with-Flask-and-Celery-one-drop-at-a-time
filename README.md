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

# Insert a course
curl -i -X POST localhost:5000/course -d '{"title": "Flask: An API micro-framework"}' --header "Content-Type: application/json"

```

--------------------------------------------------------------------------------

## Authors

- **Simone Adelchino** - [github](https://github.com/claclacla)
