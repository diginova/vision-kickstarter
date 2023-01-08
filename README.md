# Vision-Kickstarter
Docker based ML / CV project skeleton
## Create Development Environment in PyCharm
Clone new project and create run/debug configurations with below settings in PyCharm
### Add Docker Server
Open Preferences > Build,Execution,Deployment > Docker : Add docker server
### Create Dockerfile Configuration and Build Image 
Create new run/debug configuration from Dockerfile template with below settings: 
(You should change image tag, container name and project root directory name according to repo name)
- Image Tag: vision-kickstarter
- Container name: vision-kickstarter
- Context folder: .
- Bind ports: 8888:8888
- Bind mounts: {project-root-path}:/opt/project
- Run build image: checked  

Run this file to build image
### Creating Container From Image
Create new run/debug configuration Docker Image with below settings: 
- Name : docker container
- Server :Docker
- Image ID or name: vision-kickstarter
- Contanier name : vision-kickstarter
- Bind ports: 8888:8888
- Bind mounts: {project-root-path}:/opt/project

Run this file to build container 
### Create Docker Remote Interpreter
**_Image building should be finished for create docker remote interpreter._**  
Open Preferences > Project > Python interpreter > Add Python Interpreter : Select "Docker" and set "Image name" as "vision-kickstarter" then click "Ok"  
Configure "Path mappings" setting in Python Interpreter: Open "Edit Project Path Mappings" dialog window  
Add new Path Mappings with below settings:
- Local path: {project-root-path}
- Remote path: /opt/project
### Create Flask Server Configuration and Start (api.py)
Create new run/debug configuration from "Flask server" template with below settings:
(You should change Python Interpreter according to image tag)
- Target type: Script path
- Target: {project-root-path}/apps/api.py
- Additional Options: --host=0.0.0.0 --port=5000
- FLASK_ENV: development
- FLASK_DEBUG: checked
- Python Interpreter: vision-kickstarter:latest
- Docker container settings 
    - Port bindings: 
      - Host Port: 5000
      - Container Port: 5000
      - Host IP: 0.0.0.0
      - Protocol: tcp
      - run options : --entrypoint= --rm --name=vision-kickstarter-api
    - Volume bindings: {project-root-path}:/opt/project
  
Run this file to start flask server on container
### Run Python App on Running Container in PyCharm
Right click on running container at "Services" window and then select option to "Create terminal" or "Exec"  
Write that command template for run python app in exec or terminal: "python {path-of-app-file}"
- Run inference.py: python apps/inference.py

## Create Development Environment in Terminal
Clone new project and create new image and container in project root path
### Build Image
```
docker build -t vision-kickstarter .
```
### Create Container
```
docker run -v {project-root-path}:/opt/project -p 8888:8888 --name vision-kickstarter -it vision-kickstarter
```
### Access Jupyter Notebook Server Token and Links
```
docker exec vision-kickstarter jupyter notebook list
```
### Run Python App in Container
```
docker exec {container-name} python {path-of-app-file}
```
Run inference.py app on Flask (apps/api.py) container:
```
docker exec {flask-service-container-id} python apps/inference.py
```
Run train.py app on vision-kickstarter container:
```
docker exec vision-kickstarter python apps/train.py
```