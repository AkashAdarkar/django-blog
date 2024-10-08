# Django Blog
[![](https://img.shields.io/pypi/pyversions/Django.svg)](https://python.org/downloads/)
[![](https://img.shields.io/badge/django-2.0%20%7C%202.1%20%7C%202.2-success.svg)](https://djangoproject.com/)
[![](https://img.shields.io/apm/l/vim-mode.svg)](https://choosealicense.com/licenses/mit/)



Full-Featured Blog with Django web framework. 

Screenshots

![](./screenshots/Index%20Page.png)
![](./screenshots/Comments.png)
![](./screenshots/Login%20Page.png)
![](./screenshots/create%20post%20page%20.png)
![](./screenshots/Register%20Page.png)
![](./screenshots/users%20total%20posts.png)
![](./screenshots/update%20profile%20page.png)
![](./screenshots/drop-menu%20navigation%20bar.png)
![](./screenshots/password%20reset%20page.png)

Features 
=
- User Registration
- User Login & Logout
- User Profile
- Create, Update, Edit & Delete Posts
- Comments
- Search
- User Change Password
- Password Reset
- Customized admin panel

How To Use
=
## Clone project & Install Requirements
> Make sure you have already installed python3 and git.
```
$ git clone https://github.com/aregret01/django-blog.git && cd django-blog
$ pip install -r requirements.txt
```
## Migrate & Collect Static
```
$ python manage.py migrate
$ python manage.py collectstatic
```
## Create Admin User
```
$ python manage.py createsuperuser
```
## Run Server
```
$ python manage.py runserver
```
> Enter your browser http://localhost:8000/. You can login via admin in http://localhost:8000/admin/.

## Add Some Fake Posts
> First add one another user from blog register page or admin panel.
```
$ python manage.py shell
>>> from blog.models import Post
>>> import json
>>> with open('posts.json') as f:
...     json_posts = json.load(f)
...
>>> for post in json_posts:
...     Post(title=post['title'], content=post['content'], author_id=post['user_id']).save()
...
>>> exit()
```
> You can edit posts via admin panel or from corrent user added post.

TODOS
=
- Change Style
- More Options For New Post
- Sidebar
- Reply comment
- Search for post any pages
- Create following system
- Read later post
- Like post
- Coursel Photos
- ..
