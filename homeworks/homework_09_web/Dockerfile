FROM django

RUN mkdir -p /my-project
COPY . /my-project/

RUN pip install --upgrade pip
WORKDIR /my-project/myapp
RUN pip install -r ../requirements.txt

RUN rm -rf flight/migrations/00*

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN rm -rf flight/migrations/00*

CMD ["python", "myapp/manage.py", "runserver"]
