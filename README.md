# Corey MS Django Tutorial

A repo to store tutorial code

## 01. Set up virtual enviornment and install Django
set up Python3 virtual enviornment
```bash
sudo pip install virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
echo venv > .gitignore
```

install django and start a django project
```
pip install Django==2.0
echo PROJECT_NAME=django_project >> .bashrc
source ~/.bashrc
django-admin startproject django_project .
```
view the django project 
``` bash
tree
.  
├── django_project  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
└── manage.py  
```
add run alias and add allowed host
```
echo -e \alias run=\"python3 ~/workspace/manage.py runserver '\u0024'IP:'\u0024'C9_PORT\" >> ~/.bash_aliases

source ~/.bash_aliases

sed -i "/ALLOWED_HOSTS/s/\[\]/\['$C9_HOSTNAME'\]/g" ./$PROJECT_NAME/settings.py

echo db.sqlite3 >> .gitignore
```
start the server
```
run
```  

## 02. 
Create a blog app and set up urls folder
```
python manage.py startapp blog
touch blog/blog_urls.py
```
create 2no. basic views that return http responses  
add urls in the blog app to point to the views  
update the project urls to include the blog.blog_urls

