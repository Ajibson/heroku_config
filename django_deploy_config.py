# First in the settigs.py file make take secrete key to envirnoment variable and access it with

SECRET_KEY = os.environ.get('SECRET_KEY')


# Second
'''The value of the DEBUG will be True by default, but will only be False if the value of the DJANGO_DEBUG environment variable is set to False. 
Please note that environment variables are strings and not Python types. We therefore need to compare strings.
The only way to set the DEBUG variable to False is to actually set it to the string False'''

# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False' # set the 'DJANGO_DEBUG' in the environment to False


# Third 
#Create the file Procfile (no extension) in the root of your GitHub repository to declare the application's process types and entry points

web: gunicorn project_name.wsgi --log-file -

# Install gunicon

pip3 install gunicorn

# Database configuration
'''We can't use the default SQLite database on Heroku because it is file-based, 
It would be deleted from the ephemeral file system every time the application restarts (typically once a day, and every time the application or 
its configuration variables are changed).'''

#Using a database add-on which is

pip3 install dj-database-url


#Now to be used put the following lines of code in settings.py file


import dj_database_url
#put the next two line after the database declaration just did itself
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


#Django needs psycopg2 to work with Postgres databases and you will need to add this to the requirements.txt for Heroku to set this up on the remote server 
#(as discussed in the requirements section below).

pip3 install psycopg2-binary


#Serving static files in production, Put the following lines of codes in settings.py file

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'  #. os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

pip3 install whitenoise # for serving the files 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#added line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#The Python requirements of your web application must be stored in a file requirements.txt in the root of your repository.
#Heroku will then install these automatically when it rebuilds your environment.
#You can create this file using pip on the command line (run the following in the repo root)

#run the code on the terminer with the project directory
pip3 freeze > requirements.txt


#The runtime.txt file, if defined, tells Heroku which programming language to use. Create the file in the root of the repo and add the following text:

python-3.8.6

#for saving uploaded files by users 

#First add the cloudinary adds-on to your heroku app
# Second, click on the add-on o see it's configurations
#put these configurations in the heroku environment 

#put the lines of code below into the seetings.py file
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
     'API_KEY': os.environ.get('API_KEY'),
     'API_SECRET': os.environ.get('API_SECRET'),
      }
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
