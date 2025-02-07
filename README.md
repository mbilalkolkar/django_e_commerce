# create project and app steps:
    mkdir e_commerce
    django-admin startproject config e_commerce
    cd e_commerce
    django-admin startapp api

above steps same as :

    mkdir e_commerce
    cd e_commerce
    django-admin startproject config .
    django-admin startapp api


# migrate database steps
    python manage.py makemigrations
    python manage.py migrate
    python manage.py showmigrations

# create superuser
    python manage.py createsuperuser --username admin --email mbk@mail.com

# run server
    python .\manage.py runserver

# generate schema for swagger/redoc 
    - Doc https://drf-spectacular.readthedocs.io/en/latest/settings.html

    ./manage.py spectacular --color --file schema.yml
    <!-- python manage.py graph_models -a -o api/schema.py # came from AI -->

# generating models from already existing db
    - add db config in settings.py
    - run:
        python manage.py inspectdb > models.py
    - update user table
    - change managed to true and run migrations to new db or same one
        managed = True


# Doc ref:
    - ORM:
        https://docs.djangoproject.com/en/3.1/ref/models/fields/

    - Serializers:
        https://www.django-rest-framework.org/api-guide/serializers/

    - View:
        https://www.django-rest-framework.org/api-guide/viewsets/
        https://www.django-rest-framework.org/api-guide/generic-views/

        https://medium.com/@hordunlarmy/understanding-apiview-generic-views-and-viewsets-in-django-rest-framework-0d89ac6b9614
   
    -auth
        https://www.django-rest-framework.org/api-guide/authentication/
        https://medium.com/django-unleashed/django-authentication-from-basic-auth-to-oauth2-and-jwt-a-comprehensive-guide-in-2024-031ad2490d91
        

    - deployment
        https://www.hostinger.com/tutorials/django-tutorial
        https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Deployment

        - static files
            https://docs.djangoproject.com/en/3.1/howto/static-files/
            https://www.django-rest-framework.org/api-guide/settings/#static-root





# ToDo
    - get shopping cart by user_id
    - get order by user_id
    - generate order
        - create Order entry
        - move shopping_cart items to order_items and calculate total price
        - update it in Order 
    - process payment
        - payment services ...
    - update order status in Order and send order confirmation email
    - shopping_cart viewset seems useless as its handled based on its id and not user_id
    - fix fields that are not necessary for request esp in generate-order post method

    
    -  static files stuff while deploying (https://pypi.org/project/whitenoise/)




# Temp
        

