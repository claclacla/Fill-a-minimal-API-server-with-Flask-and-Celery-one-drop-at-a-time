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
# Get the latest snapshot
git clone https://github.com/claclacla/Fill-a-minimal-API-server-with-Flask-and-Celery-one-drop-at-a-time

# Change directory
cd Fill-a-minimal-API-server-with-Flask-and-Celery-one-drop-at-a-time

# Create a .env file with your local playground folder
echo "APP_FOLDER=/path-to-this-directory" > .env

```

--------------------------------------------------------------------------------

### Usage

```
# Run the environment
sudo docker-compose -f docker/dev/docker-compose.yaml up -d
```

#### Teacher

```
# Signup
# POST /user/signup
curl -i -X POST localhost:5000/user/signup -d '{"username": "teacher1@email.com", "password": "password1"}' --header "Content-Type: application/json"

# Authenticate
# POST /user/login
curl -i -X POST localhost:5000/user/login -d '{"username": "teacher1@email.com", "password": "password1"}' --header "Content-Type: application/json"

# Insert a course
# POST /course
curl -i -X POST localhost:5000/course -H "Authorization: Bearer <token>" -d '{"title": "Flask: An API micro-framework"}' --header "Content-Type: application/json"

```

--------------------------------------------------------------------------------

## Authors

- **Simone Adelchino** - [github](https://github.com/claclacla)
