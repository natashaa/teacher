# Teachers App Set up Instructions
The teachers app shows index page with all the teachers available.
You can search by first letter of last name of the teacher or subjects taught.
You can import teachers by providing a csv file with headers(First Name,Last Name,Profile picture,Email Address,Phone Number,Room Number,Subjects taught) and a zip file containing the teachers' images (only for logged-in users).
You can also see the teacher details by clicking on their first name on index page.

### Create new virtualenv
```
python3 -m venv ~/.venv/myenv
```

### Activate the new virtual env
```
source ~/.venv/myenv/bin/activate
```

### go to your projects directory (for me, its projects)
```
cd ~/projects
```

### clone the repo
```
git clone https://github.com/natashaa/teacher.git
```

### Move to teachers directory

```
cd teacher
```

### install requirements

```
pip install -r requirements.txt
```

### Run the migrations
```python manage.py migrate```

### Create django super user (Enter the credentials you wish to create)
```python manage.py createsuperuser```

### Login using the credentials created above so import functionality can work fine
http://127.0.0.1:8000/

### run the local server
```
python manage.py runserver # by default runs on post 8000, otherwise the port number
```

### index page for teachers, can search by first letter of last name or subjects taught
```
http://127.0.0.1:8000/teachers/
```

### detail page for teachers
```
http://127.0.0.1:8000/teachers/6/
```

### import for teachers, expects a csv file and zip file containing images
```
http://127.0.0.1:8000/teachers/import/
```

