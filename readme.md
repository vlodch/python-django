# To run Python Django Web App project use the following steps:
## 1. Clone the repo, https://github.com/vlodch/python-django.git
## 2. Chnage the branch to "django_web_app_market_place" and change the directory to "python-django"
## 3. Run the following commands in terminal:
### 
# docker build -t djangowebapp .                   
# docker run -d -p 8000:8000 djangowebapp
## Container ID output should be the following e.g:
```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
1f2ed7cec25a   djangowebapp   "python manage.py ru…"   18 seconds ago   Up 17 seconds   0.0.0.0:8000->8000/tcp   silly_driscoll
(env) (base) user@MacBook-Air market % docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                    PORTS                    NAMES
1f2ed7cec25a   djangowebapp   "python manage.py ru…"   6 minutes ago   Up 6 minutes              0.0.0.0:8000->8000/tcp   silly_driscoll
```

### Navigate in the browser to the localhost: e.g:
http://127.0.0.1:8000/ to see the items in the database and to navigate the site

### To manage the content 
http://127.0.0.1:8000/admin/ link to manage the content should be used 