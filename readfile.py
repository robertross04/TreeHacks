import json

CHAR_MAX_COUNT = 5000 #largest character count that Microsoft Text Analytics API can handle as text input 
pieces_of_text = []
def create_list():
	filename = raw_input("Enter the name of the file: ")
	file_object = open(filename, "r")

	count = 1
	while(True):
		chunk = file_object.read(CHAR_MAX_COUNT)
		if chunk == '': #breaks when the chunck is empty
			break
		str_id = str(count)
		tmp_dict = {}
		tmp_dict['id'] = str_id
		tmp_dict['text'] = chunk
		s = json.dumps(tmp_dict) #Conversts it to a string
		pieces_of_text.append(json.loads(s)) #json.loads converts it to a 
		count += 1
	file_object.close()
	return pieces_of_text
