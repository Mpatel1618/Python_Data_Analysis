# import pandas library as pd and matplotlib.pyplot linrary as plt
import pandas as pd
import matplotlib.pyplot as plt


#Part 2: graphs and relationships with time series
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the company data in the dataframe
google_data = df.loc[df['company'] == 'google']

def no_none(stars_1):
    '''gets rid of all of the nones in the data'''
    stars_2 = []
    for i in stars_1:
        if i != 'none':
            stars_2.append(float(i))
    return stars_2


#plt.plot(x,y)  
#this is very time consuming and python is hard to handle this big amount of data, so we decide to divide the dates by years

#For google
goo1=google_data['dates']
years=[]
for d in goo1:
    y=d.split('/')[2] #find only the years
    years.append(int(y))

google_data['years']=years #create another column called 'years' which only contains the years

def graph(category):
    '''this function makes a graph for each of the categories that is inputted by calculating the average of that category from a certain year'''
    goo2008=google_data[google_data.years==2008] 
    goo2008_fixed = no_none(goo2008[category])
    google_y2008=float(sum(goo2008_fixed))/(float(len(goo2008_fixed)))
    
    goo2009=google_data[google_data.years==2009]  
    goo2009_fixed = no_none(goo2009[category])
    google_y2009=float(sum(goo2009_fixed))/(float(len(goo2009_fixed)))
    
    goo2010=google_data[google_data.years==2010] 
    goo2010_fixed = no_none(goo2010[category])
    google_y2010=float(sum(goo2010_fixed))/(float(len(goo2010_fixed)))
    
    goo2011=google_data[google_data.years==2011]  
    goo2011_fixed = no_none(goo2011[category])
    google_y2011=float(sum(goo2011_fixed))/(float(len(goo2011_fixed)))
    
    goo2012=google_data[google_data.years==2012]  
    goo2012_fixed = no_none(goo2012[category])
    google_y2012=float(sum(goo2012_fixed))/(float(len(goo2012_fixed)))
    
    goo2013=google_data[google_data.years==2013]  
    goo2013_fixed = no_none(goo2013[category])
    google_y2013=float(sum(goo2013_fixed))/(float(len(goo2013_fixed)))
    
    goo2014=google_data[google_data.years==2014]  
    goo2014_fixed = no_none(goo2014[category])
    google_y2014=float(sum(goo2014_fixed))/(float(len(goo2014_fixed)))
    
    goo2015=google_data[google_data.years==2015]  
    goo2015_fixed = no_none(goo2015[category])
    google_y2015=float(sum(goo2015_fixed))/(float(len(goo2015_fixed)))
    
    goo2016=google_data[google_data.years==2016]  
    goo2016_fixed = no_none(goo2016[category])
    google_y2016=float(sum(goo2016_fixed))/(float(len(goo2016_fixed)))
    
    goo2017=google_data[google_data.years==2017]  
    goo2017_fixed = no_none(goo2017[category])
    google_y2017=float(sum(goo2017_fixed))/(float(len(goo2017_fixed)))
    
    goo2018=google_data[google_data.years==2018]  
    goo2018_fixed = no_none(goo2018[category])
    google_y2018=float(sum(goo2018_fixed))/(float(len(goo2018_fixed)))
    
    #doing the plot
    xgoogle=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    ygoogle=[google_y2008,google_y2009,google_y2010,google_y2011,google_y2012,google_y2013,google_y2014,google_y2015,google_y2016,google_y2017,google_y2018]
    plt.plot(xgoogle,ygoogle)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Google')

#calls the graph function to plot the points
graph('overall-ratings')
graph('work-balance-stars')
graph('carrer-opportunities-stars')
graph('comp-benefit-stars')
graph('senior-mangemnet-stars')

#special case for culture values because there are so many 'none's   
goo2012=google_data[google_data.years==2012]  
goo2012_fixed = no_none(goo2012['culture-values-stars'])
google_y2012=float(sum(goo2012_fixed))/(float(len(goo2012_fixed)))
    
goo2013=google_data[google_data.years==2013]  
goo2013_fixed = no_none(goo2013['culture-values-stars'])
google_y2013=float(sum(goo2013_fixed))/(float(len(goo2013_fixed)))
    
goo2014=google_data[google_data.years==2014]  
goo2014_fixed = no_none(goo2014['culture-values-stars'])
google_y2014=float(sum(goo2014_fixed))/(float(len(goo2014_fixed)))
    
goo2015=google_data[google_data.years==2015]  
goo2015_fixed = no_none(goo2015['culture-values-stars'])
google_y2015=float(sum(goo2015_fixed))/(float(len(goo2015_fixed)))
    
goo2016=google_data[google_data.years==2016]  
goo2016_fixed = no_none(goo2016['culture-values-stars'])
google_y2016=float(sum(goo2016_fixed))/(float(len(goo2016_fixed)))
    
goo2017=google_data[google_data.years==2017]  
goo2017_fixed = no_none(goo2017['culture-values-stars'])
google_y2017=float(sum(goo2017_fixed))/(float(len(goo2017_fixed)))
    
goo2018=google_data[google_data.years==2018]  
goo2018_fixed = no_none(goo2018['culture-values-stars'])
google_y2018=float(sum(goo2018_fixed))/(float(len(goo2018_fixed)))
    
#doing the plot for culture values
xgoogle=['2012','2013','2014','2015','2016','2017','2018']
ygoogle=[google_y2012,google_y2013,google_y2014,google_y2015,google_y2016,google_y2017,google_y2018]
plt.plot(xgoogle,ygoogle)