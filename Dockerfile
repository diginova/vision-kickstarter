FROM python:3.8

WORKDIR /opt/project
ADD . /opt/project
RUN apt update -y && apt install -y cmake
RUN pip install -r requirements.txt
CMD ["jupyter","notebook","--ip=0.0.0.0","--no-browser","--allow-root"]