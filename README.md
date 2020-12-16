# SentimentAnalysisProject

# Setting up on your local machine 
# Python Library Depenndencies
- pip3 install django==2.2.4
- pip3 install jupyter notebook
- pip3 install numpy pandas sklearn joblib
- pip3 install djangorestframework
- pip3 install markdown       # Markdown support for the browsable API.
- pip3 install django-filter  # Filtering support

# To connect to virtual environment to run on local machine
- . venv/bin/activate # to get python virtual environment activated
- ipython kernel install --user --name=venv (Set Jupyter to use local virtualenv) (Note to self: add the jupyter depedencies)

# To run Jupyter Notebook 
- cd research # start Jupyter "jupyter notebook"      # please run it in backend/server directory

# To Create migration file and migrate database

- python manage.py makemigrations
- python manage.py migrate
python manage.py runserver

# To clear sql 
- python manage.py sqlflush | python manage.py dbshell

