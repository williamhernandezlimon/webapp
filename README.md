Webapp


Running locally
* setup
	* without docker
		* required
		    * python3.7+
		    * pip3
		* setup virtual environment (optional)
			* python3 -m pip install --user virtualenv
			* python3 -m venv venv
			* source venv/bin/activate
		* download dependencies
		  * `pip3 install -r requirements.txt`
		* run app
			* `python3 app.py`
	* with docker
		* install docker
			* macos:
				* https://hub.docker.com/editions/community/docker-ce-desktop-mac
		* build docker container
			* `docker build -t webapp:latest .`
		* run docker container
			* `docker run -it -d -p 5000:5000 webapp`
* test
	* `curl --request GET 'http://localhost:5000/api/v1/task'`


Running on AWS Fargate
* setup
	* ecr
		* create ecr
			* `aws ecr create-repository --repository-name webapp --region us-east-2`
				* note `repositoryUri`
		* build image
			* `docker build -t webapp:latest .`
		* create credentials
			* allows docker commands push to ecr
			* `${aws ecr get-login --no-include-email --region us-east-2}`
			* https://youtu.be/Yy9AGt4m0_I?t=187
		* create docker tag
			* `docker tag [docker_image_id] [repositoryUri]/[docker_image_name:version]`
		* push docker image to ecr
			* `docker push [repositoryUri]/[docker_image_name:version]`
	* cloudformation. TODO: create script for automatically uploading
		* upload `aws/ecs.yaml`
			* creates: 
				* cluster
				* ecs
				* task definition
		* upload `aws/vpc.yaml`
			* creates: 
				* internet gateway
				* route table
				* vpc
				* security group
				* subnet
		
* test
	* after cloudformation template was successfully uploaded, look for the public ip address in the new task running on the new ecs cluster/service
	* hit [public_ip_address]/api/v1/task
