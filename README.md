webapp
=====
##### 
Dockerized Flask application



setup locally
=====
##### 

* Required
    * python3.7+
    * pip3
* Setup virtual environment (Optional)
	* python3 -m pip install --user virtualenv
	* python3 -m venv env
	* source env/bin/activate
* Download dependencies
  * `$ pip3 install -r requirements.txt`  

running locally
=====
##### 

* `python3 app.py`



setup using docker
=====
##### 
* Build docker container
	* `docker build -t webapp:latest .`


run using docker
=====
##### 
* Run docker container
	* `docker run -it webapp /bin/sh`