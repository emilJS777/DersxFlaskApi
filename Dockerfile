# base image
FROM python:3.10-alpine

# set working directory
WORKDIR /app

# copy source code to working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000

# start app
CMD ["python", "app.py"]