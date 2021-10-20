#Open new terminal#

cd /home/project

theia@theiadocker-fernandomin1:/home/project$ [ ! -d 'xzceb-flask_eng_fr' ] && git clone https://github.com/fermino79/testrepo.git
Cloning into 'testrepo'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (10/10), done.

cd /home/project/xzceb-flask_eng_fr/final_project

#Create folder named machinetranslation and change to that directory#

mkdir machinetranslation
cd machinetranslation

#Install the packages that you will be using in this code, namely ibm_watson and python-dotenv#
pip3 install flask ibm-watson python-dotenv

#Create a file .env under the machinetranslation directory, which maps the apikey and url of the Language Translator Service that you created in the IBM Cloud#
apikey=cpQ_3wwMej4ir2nGhuJyigEp36ajy05d5ua5ZpeecvbI
url=https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c78a13ac-5e0f-4bc1-979e-0b93d8e076b0
  
