# Flask init template wit MongoDB
---------------------
This is a simple init template base to start building services with Python Flask and MongoDB.

N.B. Requires Docker to be installed and Python3

---

### Env variables
--------------------
```bash
export FLASK_APP=api
export FLASK_DEBUG=1
export APP_SETTINGS=Local
export SECRET_KEY=this-really-needs-to-be-changed
export MONGODB_DATABASE_HOST=mongodb://0.0.0.0:27018/?retryWrites=true&w=majority
export MONGODB_USER=loki
export MONGODB_USER_PASSWORD=d0nt4get
export MONGODB_DATABASE=notes

```

---

### Run the API
---------------
## In Docker containers
Start both the services (DB & API) with following commands
```bash
docker-compose build
docker-compose up -d
```
API will be available at ```localhost:8080/swagger```

## Locally
Start the DB in  container
```bash
docker-compose up -d mongo
```

and the API (DB is in the container)
```bash
docker-compose up -d mongo
python -m venv venv && . venv/bin/activate
pip install -r requirements/dev.txt
flask run -p 8080
```
then the API will be available at ```localhost:8080```

---

### MongoDB Compass connection string
```bash
mongodb://0.0.0.0:27018/?retryWrites=true&w=majority
```

---

### Documentation
-----------------
The Swagger documentation is available @```localhost:<port>/swagger```

---

### Optimizations
-----------------
A more optimized setup with [uWSGI-NGINX](https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/).

Standalone [WSGI Containers](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/).