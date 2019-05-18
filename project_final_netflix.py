# import pandas library as pd and matplotlib.pyplot linrary as plt
import pandas as pd
import matplotlib.pyplot as plt


#Part 2: graphs and relationships with time series
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the company data in the dataframe
netflix_data = df.loc[df['company'] == 'netflix']

def no_none(stars_1):
    '''gets rid of all of the nones in the data'''
    stars_2 = []
    for i in stars_1:
        if i != 'none':
            stars_2.append(float(i))
    return stars_2


#plt.plot(x,y)  
#this is very time consuming and python is hard to handle this big amount of data, so we decide to divide the dates by years

#for netflix
net1=netflix_data['dates']
years=[]
for d in net1:
    y=d.split('/')[2] #find only the years
    years.append(int(y))

netflix_data['years']=years #create another column called 'years' which only contains the years

def graph(category):
    '''this function makes a graph for each of the categories that is inputted by calculating the average of that category from a certain year'''
    net2008=netflix_data[netflix_data.years==2008]
    net2008_fixed = no_none(net2008[category])
    netflix_y2008=float(sum(net2008_fixed))/(float(len(net2008_fixed)))
    
    net2009=netflix_data[netflix_data.years==2009] 
    net2009_fixed = no_none(net2009[category])
    netflix_y2009=float(sum(net2009_fixed))/(float(len(net2009_fixed)))
    
    net2010=netflix_data[netflix_data.years==2010] 
    net2010_fixed = no_none(net2010[category])
    netflix_y2010=float(sum(net2010_fixed))/(float(len(net2010_fixed)))
    
    net2011=netflix_data[netflix_data.years==2011] 
    net2011_fixed = no_none(net2011[category])
    netflix_y2011=float(sum(net2011_fixed))/(float(len(net2011_fixed)))
    
    net2012=netflix_data[netflix_data.years==2012] 
    net2012_fixed = no_none(net2012[category])
    netflix_y2012=float(sum(net2012_fixed))/(float(len(net2012_fixed)))
    
    net2013=netflix_data[netflix_data.years==2013] 
    net2013_fixed = no_none(net2013[category])
    netflix_y2013=float(sum(net2013_fixed))/(float(len(net2013_fixed)))
    
    net2014=netflix_data[netflix_data.years==2014] 
    net2014_fixed = no_none(net2014[category])
    netflix_y2014=float(sum(net2014_fixed))/(float(len(net2014_fixed)))
    
    net2015=netflix_data[netflix_data.years==2015] 
    net2015_fixed = no_none(net2015[category])
    netflix_y2015=float(sum(net2015_fixed))/(float(len(net2015_fixed)))
    
    net2016=netflix_data[netflix_data.years==2016]
    net2016_fixed = no_none(net2016[category])
    netflix_y2016=float(sum(net2016_fixed))/(float(len(net2016_fixed)))
    
    net2017=netflix_data[netflix_data.years==2017] 
    net2017_fixed = no_none(net2017[category])
    netflix_y2017=float(sum(net2017_fixed))/(float(len(net2017_fixed)))
  
    net2018=netflix_data[netflix_data.years==2018] 
    net2018_fixed = no_none(net2018[category])
    netflix_y2018=float(sum(net2018_fixed))/(float(len(net2018_fixed)))
    
    #doing the plot
    xnetflix=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    ynetflix=[netflix_y2008,netflix_y2009,netflix_y2010,netflix_y2011,netflix_y2012,netflix_y2013,netflix_y2014,netflix_y2015,netflix_y2016,netflix_y2017,netflix_y2018]
    plt.plot(xnetflix,ynetflix)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Netflix')

#calls the graph function to plot the points
graph('overall-ratings')
graph('work-balance-stars')
graph('carrer-opportunities-stars')
graph('comp-benefit-stars')
graph('senior-mangemnet-stars')

#special case for culture values because there are so many 'none's  
net2012=netflix_data[netflix_data.years==2012] 
net2012_fixed = no_none(net2012['culture-values-stars'])
netflix_y2012=float(sum(net2012_fixed))/(float(len(net2012_fixed)))
   
net2013=netflix_data[netflix_data.years==2013] 
net2013_fixed = no_none(net2013['culture-values-stars'])
netflix_y2013=float(sum(net2013_fixed))/(float(len(net2013_fixed)))
   
net2014=netflix_data[netflix_data.years==2014] 
net2014_fixed = no_none(net2014['culture-values-stars'])
netflix_y2014=float(sum(net2014_fixed))/(float(len(net2014_fixed)))
  
net2015=netflix_data[netflix_data.years==2015] 
net2015_fixed = no_none(net2015['culture-values-stars'])
netflix_y2015=float(sum(net2015_fixed))/(float(len(net2015_fixed)))
  
net2016=netflix_data[netflix_data.years==2016] 
net2016_fixed = no_none(net2016['culture-values-stars'])
netflix_y2016=float(sum(net2016_fixed))/(float(len(net2016_fixed)))
    
net2017=netflix_data[netflix_data.years==2017] 
net2017_fixed = no_none(net2017['culture-values-stars'])
netflix_y2017=float(sum(net2017_fixed))/(float(len(net2017_fixed)))
    
net2018=netflix_data[netflix_data.years==2018] 
net2018_fixed = no_none(net2018['culture-values-stars'])
netflix_y2018=float(sum(net2018_fixed))/(float(len(net2018_fixed)))
    
#doing the plot for culture values
xnetflix=['2012','2013','2014','2015','2016','2017','2018']
ynetflix=[netflix_y2012,netflix_y2013,netflix_y2014,netflix_y2015,netflix_y2016,netflix_y2017,netflix_y2018]
plt.plot(xnetflix,ynetflix)