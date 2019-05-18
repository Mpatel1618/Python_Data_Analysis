# import pandas library as pd and matplotlib.pyplot linrary as plt
import pandas as pd
import matplotlib.pyplot as plt


#Part 2: graphs and relationships with time series
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the company data in the dataframe
apple_data = df.loc[df['company'] == 'apple']

def no_none(stars_1):
    '''gets rid of all of the nones in the data'''
    stars_2 = []
    for i in stars_1:
        if i != 'none':
            stars_2.append(float(i))
    return stars_2


#plt.plot(x,y)  
#this is very time consuming and python is hard to handle this big amount of data, so we decide to divide the dates by years

#for apple
app1=apple_data['dates']
years=[]
for d in app1:
    y=d.split('/')[2] #find only the years
    years.append(int(y))

apple_data['years']=years #create another column called 'years' which only contains the years

def graph(category):
    '''this function makes a graph for each of the categories that is inputted by calculating the average of that category from a certain year'''
    app2008=apple_data[apple_data.years==2008] 
    app2008_fixed = no_none(app2008[category])
    apple_y2008=float(sum(app2008_fixed))/(float(len(app2008_fixed)))
    
    app2009=apple_data[apple_data.years==2009] 
    app2009_fixed = no_none(app2009[category])
    apple_y2009=float(sum(app2009_fixed))/(float(len(app2009_fixed)))
    
    app2010=apple_data[apple_data.years==2010] 
    app2010_fixed = no_none(app2010[category])
    apple_y2010=float(sum(app2010_fixed))/(float(len(app2010_fixed)))
    
    app2011=apple_data[apple_data.years==2011]  
    app2011_fixed = no_none(app2011[category])
    apple_y2011=float(sum(app2011_fixed))/(float(len(app2011_fixed)))
    
    app2012=apple_data[apple_data.years==2012]  
    app2012_fixed = no_none(app2012[category])
    apple_y2012=float(sum(app2012_fixed))/(float(len(app2012_fixed)))
    
    app2013=apple_data[apple_data.years==2013]  
    app2013_fixed = no_none(app2013[category])
    apple_y2013=float(sum(app2013_fixed))/(float(len(app2013_fixed)))
    
    app2014=apple_data[apple_data.years==2014]  
    app2014_fixed = no_none(app2014[category])
    apple_y2014=float(sum(app2014_fixed))/(float(len(app2014_fixed)))
    
    app2015=apple_data[apple_data.years==2015] 
    app2015_fixed = no_none(app2015[category])
    apple_y2015=float(sum(app2015_fixed))/(float(len(app2015_fixed)))
    
    app2016=apple_data[apple_data.years==2016] 
    app2016_fixed = no_none(app2016[category])
    apple_y2016=float(sum(app2016_fixed))/(float(len(app2016_fixed)))
    
    app2017=apple_data[apple_data.years==2017]  
    app2017_fixed = no_none(app2017[category])
    apple_y2017=float(sum(app2017_fixed))/(float(len(app2017_fixed)))
    
    app2018=apple_data[apple_data.years==2018]  
    app2018_fixed = no_none(app2018[category])
    apple_y2018=float(sum(app2018_fixed))/(float(len(app2018_fixed)))
    
    #doing the plot
    xapple=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    yapple=[apple_y2008,apple_y2009,apple_y2010,apple_y2011,apple_y2012,apple_y2013,apple_y2014,apple_y2015,apple_y2016,apple_y2017,apple_y2018]
    plt.plot(xapple,yapple)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Apple')

#calls the graph function to plot the points
graph('overall-ratings')
graph('work-balance-stars')
graph('carrer-opportunities-stars')
graph('comp-benefit-stars')
graph('senior-mangemnet-stars')

#special case for culture values because there are so many 'none's   
app2012=apple_data[apple_data.years==2012]  
app2012_fixed = no_none(app2012['culture-values-stars'])
apple_y2012=float(sum(app2012_fixed))/(float(len(app2012_fixed)))
    
app2013=apple_data[apple_data.years==2013]  
app2013_fixed = no_none(app2013['culture-values-stars'])
apple_y2013=float(sum(app2013_fixed))/(float(len(app2013_fixed)))
    
app2014=apple_data[apple_data.years==2014]  
app2014_fixed = no_none(app2014['culture-values-stars'])
apple_y2014=float(sum(app2014_fixed))/(float(len(app2014_fixed)))
    
app2015=apple_data[apple_data.years==2015] 
app2015_fixed = no_none(app2015['culture-values-stars'])
apple_y2015=float(sum(app2015_fixed))/(float(len(app2015_fixed)))
    
app2016=apple_data[apple_data.years==2016]  
app2016_fixed = no_none(app2016['culture-values-stars'])
apple_y2016=float(sum(app2016_fixed))/(float(len(app2016_fixed)))
    
app2017=apple_data[apple_data.years==2017]  
app2017_fixed = no_none(app2017['culture-values-stars'])
apple_y2017=float(sum(app2017_fixed))/(float(len(app2017_fixed)))
    
app2018=apple_data[apple_data.years==2018]  
app2018_fixed = no_none(app2018['culture-values-stars'])
apple_y2018=float(sum(app2018_fixed))/(float(len(app2018_fixed)))
    
#doing the plot for culture values
xapple=['2012','2013','2014','2015','2016','2017','2018']
yapple=[apple_y2012,apple_y2013,apple_y2014,apple_y2015,apple_y2016,apple_y2017,apple_y2018]
plt.plot(xapple,yapple)