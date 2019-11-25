FROM django

RUN mkdir -p /my-project
COPY . /my-project/

RUN pip install --upgrade pip
WORKDIR /my-project
RUN pip install -r requirements.txt

RUN python myapp/manage.py makemigrations
RUN python myapp/manage.py migrate

CMD ["python", "myapp/manage.py", "runserver"]
