
#will probably have to run "pip install requests" to get requests library to work
import requests #https requests library
from pprint import pprint #pretty print
from keyphrase import generate_keyphrase_list #Calls keyphrase.py to get a list of keyphrase names
from keyphrase import print_phrase_list #Calls keyphrase.py to print the phrase list
from readfile import create_list

#subscription key for the Text Analytics
subscription_key="867d6db86b5745c3a9fa1b8c1766134d"
assert subscription_key

#API endpoint
text_analytics_base_url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/"
"""
#find the languages associated with the text
language_api_url = text_analytics_base_url + "languages"
print(language_api_url)


documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Espanol.' },
    { 'id': '3', 'text': 'This is Chinese' }
]}

#This uses the API to get the language
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages) #prints the detected language 

#finds the sentiments associated with the text
sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

#docuemnts dictionary: with documents as key that maps to a list of documents
documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Habia mucho trafico el dia de ayer.'}
]}

dictionary = {'documents': create_list()}
#This uses the API to get the sentiments
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=dictionary)
sentiments = response.json()
pprint(sentiments) #sentiment gives the documents a rating between 1 and 0, with closer to 1 meaning positive sentiment and closer to zero is negative sentiment
"""

#finds the keyphrases associated with the text
key_phrase_api_url = text_analytics_base_url + "keyPhrases"


dictionary = {'documents': create_list()}


#This uses the API to get the key phrases
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=dictionary)
key_phrases = response.json()

key_phrases_list = generate_keyphrase_list(key_phrases)
print_phrase_list(key_phrases_list)

