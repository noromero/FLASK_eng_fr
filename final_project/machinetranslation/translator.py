import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-01-20',
    authenticator=authenticator
)

language_translator.set_service_url(url)

""" This function converts english to french"""
def englishToFrench(englishText):
  frenchText=language_translator.translate(
      text=englishText,
      model_id='en-fr').get_result()
  return frenchText

""" This function converts french to english"""
def frenchToEnglish(frenchText):
  englishText=language_translator.translate(
      text=frenchText,
      model_id='fr-en').get_result()
  return englishText
  
  