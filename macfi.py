# computation know;edge engine library
import wolframalpha

# library to convert text into speech
from gtts import gTTS

#library for wikipedia
import wikipedia

#import webbrowser
import webbrowser

#import natural language processing library required functions
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#operating system libary
import os

#importing user defined module for data sets
import dataset as data

while True:
	#query input
	input = raw_input("Question: ")

	try:
		# if input.lower() in data.general_query:
		# 	answer = data.general_query[input.lower()]
		# elif __stopwords__(input) in data.task_manager:
		# 	check = raw_input("are you sure you want to",__stopwords__(input),"your computer: (y/n)")
		# 	if check.lower() is 'y':
		# 		os.system(data.task_manager[__stopwords__(input).lower])
		# 		answer = "shuting down computer"
		# 	else:
		# 		break
		# else:
		#wolfram computatoional engine
		app_id = "6T3KKV-222Y9EW6A7"
		#get a client object
		client = wolframalpha.Client(app_id)
		#generating response
		res = client.query(input)
		# answer construction
		answer = next(res.results).text
	except Exception as e:
		#wiki query
		answer = wikipedia.summary(input, sentences=2)
	except:
		print 'Sorry sir i could not find anything '
		


	#The text that we have to convert to audio
	print answer

	#Language in which you want to convert
	language = 'en'

	try:
		mytext = answer

		# Passing the text and language to the engine, 
		# here we have marked slow=False. Which tells 
		# the module that the converted audio should 
		# have a high speed
		myobj = gTTS(text=mytext, lang=language, slow=False)


		# Saving the converted audio in a mp3 file named
		# welcome 
		myobj.save("welcome.mp3")

		# Playing the converted file
		os.system("mpg321 welcome.mp3")
	except:
		print 'None to print'

def __stopwords__(text):
	example_sent = text
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(example_sent)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	filtered_sentence = []
	for w in word_tokens:
	    if w not in stop_words:
	        filtered_sentence.append(w)
	return ' '.join(filtered_sentence)
		
	