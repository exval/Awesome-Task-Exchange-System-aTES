FROM python:3.10-alpine

# set work directory
WORKDIR /app

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev curl build-base libffi-dev


# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# ENTRYPOINT ["/app/entrypoint.sh"]