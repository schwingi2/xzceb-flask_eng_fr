#This implements a translationservice
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

#This function translates English to French 
def english_to_french(english_text):
    try:
    # Invoke a method
        english_translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
        french_text = english_translation.get("translations")[0].get("translation")
        return french_text

    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return str(ex.code)
    

#This function translates French to English
def french_to_english(french_text):
    try:
        french_translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
        english_text = french_translation.get("translations")[0].get("translation")
        return english_text

    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return str(ex.code)
        