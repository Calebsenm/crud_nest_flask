### Create a venv 
python3 -m venv  .venv 

### Activate 
source .venv/bin/activate

### Install dependency
pip install -r requirements.txt

### For migration:  
install: 
golang-migrate

add ENV: 
export FLASKDB_DSN='postgres://user:password@localhost/db_name'

Run migration: 
migrate -path=./migrations -database=$FLASKDB_DSN up

Create a migration: 
migrate create -seq -ext=.sql -dir=./migrations create_name_table



### Run dev project : 
flask --app src/main.py  run

### Deploy :
gunicorn --bind 0.0.0.0:8000 src.main:app
