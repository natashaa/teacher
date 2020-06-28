### Teachers App Set up Instructions

# Creating new virtualenv
```
python3 -m venv ~/.venv/myenv
```

# Activating the new virtual env
```
source ~/.venv/myenv/bin/activate
```

# go to your projects directory (for me, its projects)
```
cd ~/projects
```

# clone the repo
```
git clone https://github.com/natashaa/teacher.git
```

# install requirements
```
pip install -r requirements.txt
```

## run the local server
```
python manage.py runserver # by default runs on post 8000, otherwise the port number
```

# index page for teachers
```
http://127.0.0.1:8000/teachers/
```

# detail page for teachers
```
http://127.0.0.1:8000/teachers/6/
```

# import for teachers, expects a csv file and zip file containing images
```
http://127.0.0.1:8000/teachers/import/
```

