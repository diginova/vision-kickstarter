# Vision-Kickstarter
Docker based ML / CV project skeleton
#Build Image
```
docker build -t vision-tensorflow .
```
#Create Container
```
docker run -v {host-path}:/opt/project -p 8888:8888 --name vision-kickstarter -it vision-tensorflow
```
#PyCharm Configurations
Clone project and create run/debug configurations with below settings in PyCharm
## Docker Server
Open Preferences > Build,Execution,Deployment > Docker : Add docker server
## Docker Remote Interpreter
Open Preferences > Project > Python interpreter > Add Python Interpreter : Select Docker  
Configure "Path mappings" setting in Python Interpreter: {project-root} → /opt/project
## Dockerfile
Create new Dockerfile configuration with below settings and run this file to build docker image and container:
- Image Tag: vision-tensorflow
- Container name: vision-kickstarter
- Context folder: .
- Bind ports: 8888:8888
- Bind mounts: {host-path}:/opt/project
- Run build image: checked
## Flask (apps/service.py)
Create new Flask (apps/service.py) configuration with below settings and run this file:
- FLASK_ENV: development
- FLASK_DEBUG: checked
- Docker container settings 
    - Port bindings: 5000:5000
    - Volume bindings: {host-path}:/opt/project
# Jupyter Notebook Server
```
docker exec vision-kickstarter jupyter notebook list
```
# Run Python App in Container
```
docker exec {container-name} python {path-of-app-file}
```
Run for client.py in Flask (apps/service.py) container:
```
docker exec {flask-service-container-id} python client.py
```
Run for main.py in vision-kickstarter container:
```
docker exec vision-kickstarter python main.py
```
