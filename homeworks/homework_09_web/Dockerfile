FROM django

RUN mkdir -p /my-project
COPY . /my-project/

RUN pip install --upgrade pip
WORKDIR /my-project
RUN pip install -r requirements.txt

RUN rm -rf myapp/flight/migrations/00*

RUN python myapp/manage.py makemigrations
RUN python myapp/manage.py migrate

RUN rm -rf myapp/flight/migrations/00*

CMD ["python", "myapp/manage.py", "runserver"]
