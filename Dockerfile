FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .

CMD [ "python", "./mysite/manage.py", "runserver", "0.0.0.0:8000"]
