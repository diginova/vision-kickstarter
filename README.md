# vision-kickstarter
app.ini içerisindeki chdir'ye projenizin proje klasörünün absolute pathini veriniz. 

`chdir = /home/sinem/Belgeler/DL/vision-kickstarter/`

Gerekli kütüphanelerin kurulumu için :

`pip install -r requirements.txt`

Tensorflow examples kurulumu için:

` pip install -q git+https://github.com/tensorflow/examples.git`

Uwsgi serverını ayağa kaldırmak için:

`uwsgi app.ini `

Post request için:

` python client.py`

