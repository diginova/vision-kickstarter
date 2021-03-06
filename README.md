# vision-kickstarter
app.ini içerisindeki chdir'ye projenizin app klasörünün absolute pathini,
virtualenv'a ise virtual envoirementın absolute pathini veriniz. 

`chdir = /home/sinem/Belgeler/app/`

`virtualenv = /home/sinem/Belgeler/app/testenv`

Gerekli kütüphanelerin kurulumu için :

`pip install -r requirements.txt`

Usgwi serverını ayağa kaldırmak için:

`uwsgi app.ini `

Post request için:

` python client.py`

