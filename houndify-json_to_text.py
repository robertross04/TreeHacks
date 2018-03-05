from audio_to_json import result
import json

def parse():
	for text in result["AllResults"]:
		transcript = text["FormattedTranscription"]
	f = open("output.txt","w")
	f.write(transcript)
	f.close()

parse()

