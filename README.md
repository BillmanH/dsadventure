# Internal Dev Web Environment. 

## Set it up
Clone the repository:

```
git clone https://github.com/BillmanH/dsadventure.git
```

Install the settings file:

```
cp gamesite/TEMPLATE.bak gamesite/settings.py
```

Migrate:
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

then run:
`serve`


# Docker Version
_not really working yet_

docker build -t dsvm:latest .


