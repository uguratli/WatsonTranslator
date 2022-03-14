import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('api key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/592fed64-a917-4396-8d5f-18d8c341e95f') 
def AR_EN(text):
    text=str(text)
    tr=language_translator.translate(text,model_id='ar-en').get_result()
    return tr["translations"][0]["translation"]
def Identify(text):
    text=str(text)
    lang=language_translator.identify(text).get_result()
    return lang["languages"][0]["language"]