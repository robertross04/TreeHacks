
#will probably have to run "pip install requests" to get requests library to work
import requests #https requests library
from pprint import pprint #pretty print

#will probably have to run "pip install ipython" and pip install "ipython[all]"
#from IPython.display import HTML 

#subscription key for the Text Analytics
subscription_key="867d6db86b5745c3a9fa1b8c1766134d"
assert subscription_key

#API endpoint
text_analytics_base_url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/"

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




#renders JSON data as HTML
"""for document in languages["documents"]:
    text  = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
    langs = ", ".join(["{0}({1})".format(lang["name"], lang["score"]) for lang in document["detectedLanguages"]])
    table.append("<tr><td>{0}</td><td>{1}</td>".format(text, langs))
HTML("<table><tr><th>Text</th><th>Detected languages(scores)</th></tr>{0}</table>".format("\n".join(table)))"""


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

#This uses the API to get the sentiments
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments) #sentiment gives the documents a rating between 1 and 0, with closer to 1 meaning positive sentiment and closer to zero is negative sentiment

#finds the keyphrases associated with the text
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)



#This uses the API to get the key phrases
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)


dictionary = {'documents': [{'id': '1', 'text': 'This is a document written in English.'},
               {'id': '2', 'text': 'Este es un document escrito en Espanol.'},
               {'id': '3', 'text': 'Chinese'}]}

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=dictionary)
key_phrases = response.json()
pprint(key_phrases)
