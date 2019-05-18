# import pandas library as pd and matplotlib.pyplot linrary as plt
import pandas as pd
import matplotlib.pyplot as plt


#Part 2: graphs and relationships with time series
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the company data in the dataframe
amazon_data = df.loc[df['company'] == 'amazon']

def no_none(stars_1):
    '''gets rid of all of the nones in the data'''
    stars_2 = []
    for i in stars_1:
        if i != 'none':
            stars_2.append(float(i))
    return stars_2


#plt.plot(x,y)  
#this is very time consuming and python is hard to handle this big amount of data, so we decide to divide the dates by years

#for amazon
ama1=amazon_data['dates']
years=[]
for d in ama1:
    y=d.split('/')[2] #find only the years
    years.append(int(y))

amazon_data['years']=years #create another column called 'years' which only contains the years

def graph(category):
    '''this function makes a graph for each of the categories that is inputted by calculating the average of that category from a certain year'''
    ama2008=amazon_data[amazon_data.years==2008]
    ama2008_fixed = no_none(ama2008[category])
    amazon_y2008=float(sum(ama2008_fixed))/(float(len(ama2008_fixed)))
    
    ama2009=amazon_data[amazon_data.years==2009] 
    ama2009_fixed = no_none(ama2009[category])
    amazon_y2009=float(sum(ama2009_fixed))/(float(len(ama2009_fixed)))
    
    ama2010=amazon_data[amazon_data.years==2010] 
    ama2010_fixed = no_none(ama2010[category])
    amazon_y2010=float(sum(ama2010_fixed))/(float(len(ama2010_fixed)))
    
    ama2011=amazon_data[amazon_data.years==2011] 
    ama2011_fixed = no_none(ama2011[category])
    amazon_y2011=float(sum(ama2011_fixed))/(float(len(ama2011_fixed)))
    
    ama2012=amazon_data[amazon_data.years==2012] 
    ama2012_fixed = no_none(ama2012[category])
    amazon_y2012=float(sum(ama2012_fixed))/(float(len(ama2012_fixed)))
    
    ama2013=amazon_data[amazon_data.years==2013] 
    ama2013_fixed = no_none(ama2013[category])
    amazon_y2013=float(sum(ama2013_fixed))/(float(len(ama2013_fixed)))
    
    ama2014=amazon_data[amazon_data.years==2014]
    ama2014_fixed = no_none(ama2014[category])
    amazon_y2014=float(sum(ama2014_fixed))/(float(len(ama2014_fixed)))
    
    ama2015=amazon_data[amazon_data.years==2015] 
    ama2015_fixed = no_none(ama2015[category])
    amazon_y2015=float(sum(ama2015_fixed))/(float(len(ama2015_fixed)))
    
    ama2016=amazon_data[amazon_data.years==2016] 
    ama2016_fixed = no_none(ama2016[category])
    amazon_y2016=float(sum(ama2016_fixed))/(float(len(ama2016_fixed)))
    
    ama2017=amazon_data[amazon_data.years==2017] 
    ama2017_fixed = no_none(ama2017[category])
    amazon_y2017=float(sum(ama2017_fixed))/(float(len(ama2017_fixed)))
    
    ama2018=amazon_data[amazon_data.years==2018] 
    ama2018_fixed = no_none(ama2018[category])
    amazon_y2018=float(sum(ama2018_fixed))/(float(len(ama2018_fixed)))
    
    #doing the plot
    xamazon=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    yamazon=[amazon_y2008,amazon_y2009,amazon_y2010,amazon_y2011,amazon_y2012,amazon_y2013,amazon_y2014,amazon_y2015,amazon_y2016,amazon_y2017,amazon_y2018]
    plt.plot(xamazon,yamazon)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Amazon')

#calls the graph function to plot the points
graph('overall-ratings')
graph('work-balance-stars')
graph('carrer-opportunities-stars')
graph('comp-benefit-stars')
graph('senior-mangemnet-stars')

#special case for culture values because there are so many 'none's
ama2012=amazon_data[amazon_data.years==2012] 
ama2012_fixed = no_none(ama2012['culture-values-stars'])
amazon_y2012=float(sum(ama2012_fixed))/(float(len(ama2012_fixed)))
    
ama2013=amazon_data[amazon_data.years==2013] 
ama2013_fixed = no_none(ama2013['culture-values-stars'])
amazon_y2013=float(sum(ama2013_fixed))/(float(len(ama2013_fixed)))
    
ama2014=amazon_data[amazon_data.years==2014]
ama2014_fixed = no_none(ama2014['culture-values-stars'])
amazon_y2014=float(sum(ama2014_fixed))/(float(len(ama2014_fixed)))
    
ama2015=amazon_data[amazon_data.years==2015] 
ama2015_fixed = no_none(ama2015['culture-values-stars'])
amazon_y2015=float(sum(ama2015_fixed))/(float(len(ama2015_fixed)))
    
ama2016=amazon_data[amazon_data.years==2016] 
ama2016_fixed = no_none(ama2016['culture-values-stars'])
amazon_y2016=float(sum(ama2016_fixed))/(float(len(ama2016_fixed)))
    
ama2017=amazon_data[amazon_data.years==2017] 
ama2017_fixed = no_none(ama2017['culture-values-stars'])
amazon_y2017=float(sum(ama2017_fixed))/(float(len(ama2017_fixed)))
    
ama2018=amazon_data[amazon_data.years==2018] 
ama2018_fixed = no_none(ama2018['culture-values-stars'])
amazon_y2018=float(sum(ama2018_fixed))/(float(len(ama2018_fixed)))
    
#doing the plot
xamazon=['2012','2013','2014','2015','2016','2017','2018']
yamazon=[amazon_y2012,amazon_y2013,amazon_y2014,amazon_y2015,amazon_y2016,amazon_y2017,amazon_y2018]
plt.plot(xamazon,yamazon)
