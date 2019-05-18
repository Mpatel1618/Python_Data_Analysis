# Python_Data_Analysis
The code was made to analyze data of customer ratings from a csv file.

The code uses pandas to locate certain companies information and then puts it into a list. There are two functions that go through the data and to figure out the means and the append them a new list. These means are then used to append into the dicitonary with the second function. In the means function, everything that contains 'none' is skipped over in hte appending process.

After everything is sorted out into their dictionary postions the code prints the companies name and then the dictionary containing each categories means.

The other files are there to plot each companies categories time series lines using matplotlib. There is a function to get the years from the whole data, and then it takes the information to create a new column in the csv file so it is easier to check data by year. Once all of the information is collected it graphs the data. Everything before 2012 in culture values is none so those years were skipped over.

The last two files go through the pros and cons of the csv file and looks through what words show up the most for each category using nltk.

Overall the codes purpose was to see what each company needs to improve on when it comes to their employees opinions.
