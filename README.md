# Internal Dev Web Environment. 

## Set it up
* Clone the repository:

```
git clone https://github.com/BillmanH/dsadventure.git
```

* Install the settings file:

```
cp gamesite/TEMPLATE.bak gamesite/settings.py
```

* Add your domain to the settings under `ALLOWED_HOSTS`

* create two fiels (or remove them from the templates)
```
touch gamesite/templates/gamesite/adsensetag.html
touch gamesite/templates/gamesite/gatag.html
```
* Migrate the data and static files.
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```
In my case I had to sync the databases with `python manage.py migrate --run-syncdb`

* load the data into your database: 
```
python manage.py loaddata game.json
```
These are just the default values. You can make them whatever you want. 

then run:
`serve`


# Docker Version
_not really working yet_

docker build -t dsvm:latest .


