=====
JWT-AUTH
=====

JWT-AUTH is a simple Django app to achieve JWT Oauth in your Django Project.

It includes the follwing urls:
    url('^token/$', views.token),
    url('^token/refresh/$', views.refresh_token),

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. Install dependencies :
pip install djangorestframework
pip install jwt

2. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
		'rest_framework',
        'jwt-auth',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^auth/', include('jwt-auth.urls')),
	
3. Add following to the settings.py :

AUTH_USER_MODEL = 'useraccounts.UsersModel'

JWT_AUTH = {

    'JWT_SECRET': 'super-secret-key',
    'JWT_ALGORITHM': 'HS256',

}

4. Run `python manage.py migrate` to create the authentication models.