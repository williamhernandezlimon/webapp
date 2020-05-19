from alpine:latest

# add python and pip3
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

# set working directory
WORKDIR /webapp

# copy source code into docker container
COPY . /webapp

# no-cache so no extra images are used
RUN pip3 --no-cache-dir install -r requirements.txt

# open port
EXPOSE 5000

# have container running in background
ENTRYPOINT ["python3", "app.py"]