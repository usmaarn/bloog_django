FROM python:3.12-slim

WORKDIR /src/app

ENV PYTHONDONTWRITEBYTECODE=1

#RUN sudo apt install python3-venv

#RUN python3 -m venv .venv && source .venv/bin/activate

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic

RUN python manage.py migrate

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]