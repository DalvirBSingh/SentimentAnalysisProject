# SentimentAnalysisProject

# Setting up on your local machine 
# Python Library Depenndencies
- pip3 install django==2.2.4
- pip3 install jupyter notebook
- pip3 install numpy pandas sklearn joblib
- pip3 install djangorestframework
- pip3 install markdown       # Markdown support for the browsable API.
- pip3 install django-filter  # Filtering support
- ipython kernel install --user --name=venv (Set Jupyter to use local virtualenv) (Note to self: add the jupyter depedencies)
- cd research # start Jupyter "jupyter notebook"
- # please run it in backend/server directory
- python manage.py makemigrations
- python manage.py migrate
python manage.py runserver
