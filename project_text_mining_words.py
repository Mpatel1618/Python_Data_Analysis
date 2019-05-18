# This part of the code is to count the most common used when describing 

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

def common_words(data,column):
	d = {}
	for string in data[column]:
		# Try to limit unnecessary characters
		string = string.replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace(';',' ').replace("'",' ').replace('(',' ').replace(')',' ').replace('-',' ').lower()
		# Split the sentences
		for word in string.split():
			# Check if the word is not a stop word
			if word not in stop_words:
				try: d[word] += 1	# Adds 1 if word is repeated
				except: d[word] = 1	# Adds new word to dictionary
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
		common_words(data,'pros')
		print("--"*20)
		print("Finished printing 'pros' in %s" %company)
		# Common con words
		u = input("About to print 'cons' in %s. . ." %company)
		common_words(data,'cons')
		print("Finished printing 'cons' in %s" %company)
		print("--"*20)
		
if __name__ == '__main__':
	main()


