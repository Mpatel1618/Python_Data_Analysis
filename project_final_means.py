# import pandas library as pd
import pandas as pd

#Part 1: find the average of each category in each company
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the companies data in the dataframe
apple_data = df.loc[df['company'] == 'apple']
google_data = df.loc[df['company'] == 'google']
amazon_data = df.loc[df['company'] == 'amazon']
microsoft_data = df.loc[df['company'] == 'microsoft']
facebook_data = df.loc[df['company'] == 'facebook']
netflix_data = df.loc[df['company'] == 'netflix']

#this function takes the data and then sends back the mean by putting the data into a new list and then dividng by the length of the data
def gather_mean(stars_1):
	stars_2 = []
	for i in stars_1:
		if i != 'none':
			stars_2.append(float(i))
	return sum(stars_2) / len(stars_2)

#this function organizes the data in a more meaningful way
def append_means(data,list_names):
	d = {}
	for c in list_names:
		try: d[c] += gather_mean(data[c]) #adds to the list if it is repeated (hopefully not)
		except: d[c] = gather_mean(data[c])	#adds new character to dictionary
	return d

#sets the columns for the data to be more organized			
columns = ['overall-ratings', 'work-balance-stars', 'culture-values-stars', 'carrer-opportunities-stars', 'comp-benefit-stars', 'senior-mangemnet-stars']

#calls the append means functions to prganize the data
apple_data_means = append_means(apple_data,columns)
google_data_means = append_means(google_data,columns)
amazon_data_means = append_means(amazon_data,columns)
microsoft_data_means = append_means(microsoft_data,columns)
facebook_data_means = append_means(facebook_data,columns)
netflix_data_means=append_means(netflix_data,columns)

#print out all of the data that was made
print('Apple:'); print(apple_data_means); print()
print('Google:'); print(google_data_means); print()
print('Amazon:'); print(amazon_data_means); print()
print('Microsoft:'); print(microsoft_data_means); print()
print('Facebook:'); print(facebook_data_means);print()
print('Netflix:');print(netflix_data_means);print()