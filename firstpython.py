#Open new terminal#

cd /home/project

theia@theiadocker-fernandomin1:/home/project$ [ ! -d 'xzceb-flask_eng_fr' ] && git clone https://github.com/fermino79/testrepo.git

cd /home/project/xzceb-flask_eng_fr/final_project

#Create folder named machinetranslation and change to that directory#

mkdir machinetranslation
cd machinetranslation

#Install the packages that you will be using in this code, namely ibm_watson and python-dotenv#
pip3 install flask ibm-watson python-dotenv

#Create a file .env under the machinetranslation directory, which maps the apikey and url of the Language Translator Service that you created in the IBM Cloud#
apikey=cpQ_3wwMej4ir2nGhuJyigEp36ajy05d5ua5ZpeecvbI
url=https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c78a13ac-5e0f-4bc1-979e-0b93d8e076b0
  
#In the explorer, go to the machinetranslation directory and create a new file called translator.py. Enter the following lines of code.#
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

#Lines of code#
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

apikey = os.environ['apikey']
url = os.environ['url']
  
#Add code to create an instance of the IBM Watson Language translator in translator.py. > Hint : You may refer to the IBM Watson Language Translation API documents here#

