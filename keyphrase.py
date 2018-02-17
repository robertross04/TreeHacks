#Puts the key phrases from the text into a list
def generate_keyphrase_list(key_phrases):
    key_phrases_list = []
    for value in key_phrases.values():
        for tmp in value:
            for key in tmp.values():
                for phrases in key:
                    if len(phrases) >= 3: #only want words 3 or larger
                        key_phrases_list.append(phrases)
    return key_phrases_list

#prints keyphrase list: mainly for debugging
def print_phrase_list(key_phrases_list):
	for phrase in key_phrases_list:
		print(phrase)