# This part of the code is to gather the most common 5-word structured phrase, and count them 

# General importing
import pandas as pd

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Get the 'employee_reviews' CSV file
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

# List the type of companies available 
companies = ['Apple', 'Google', 'Amazon', 'Microsoft','Facebook', 'Netflix']

# These would be the stop words in the English dictionary
stop_words = set(stopwords.words('english'))

def common_sentences(data,column):
	d = {}
	for string in data[column]:
		# Try to limit unnecessary characters
		string = string.replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(';',' ').replace('-',' ').replace('(',' ').replace(')',' ').lower()
		# Split the sentences into a list to later create sentences
		word_list = string.split()
		# Try to use certain points in a list to create a sentence again
		for i in range(len(word_list)):
			# Check if the word is not a stop word
			if word_list[i] not in stop_words:
				try:
					# Creating a sentence
					sentence = word_list[i] + ' ' + word_list[i+1] + ' ' + word_list[i+2] + ' ' + word_list[i+3] + ' ' + word_list[i+4] 	
					try: d[sentence] += 1	# Adds 1 if sentence is repeated
					except: d[sentence] = 1 # Adds 1 if the sentence is new
				except: d[word_list[i]] = 1	# Adds new word to dictionary if the above statement fails
	# Print the results sorted by their count type
	for k, v in sorted(d.items(), key=lambda value: value[1]):
		print ("%s: %d" % (k, d[k]))
	return 0

def main():
	for company in companies:
		# Tell user what company is about to happen
		print("**"*20)
		print (company)
		print("**"*20)
		# Select the company
		data = df.loc[df['company'] == company.lower()]
		# Common pro words
		u = input("About to print 'pros' in %s . . ." %company)
		common_sentences(data,'pros')
		print("--"*20)
		print("Finished printing 'pros' in %s" %company)
		# Common con words
		u = input("About to print 'cons' in %s. . ." %company)
		common_sentences(data,'cons')
		print("Finished printing 'cons' in %s" %company)
		print("--"*20)

				
if __name__ == '__main__':
	main()


