# racipe-app-api
Racipe App API source code
.............
# Commands

Test: sudo docker-compose run app sh -c "python manage.py test"

Test with flake8: sudo docker-compose run app sh -c "python manage.py test && flake8"

# Project Start

create project: sudo docker-compose run app sh -c "django-admin.py startproject app ."

app create: sudo docker-compose run app sh -c "python manage.py startapp core"

# migrations:
1. sudo docker-compose run app sh -c "python manage.py makemigrations core"
2. 