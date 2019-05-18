# import pandas library as pd and matplotlib.pyplot linrary as plt
import pandas as pd
import matplotlib.pyplot as plt


#Part 2: graphs and relationships with time series
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the company data in the dataframe
microsoft_data = df.loc[df['company'] == 'microsoft']

def no_none(stars_1):
    '''gets rid of all of the nones in the data'''
    stars_2 = []
    for i in stars_1:
        if i != 'none':
            stars_2.append(float(i))
    return stars_2


#plt.plot(x,y)  
#this is very time consuming and python is hard to handle this big amount of data, so we decide to divide the dates by years

#for microsoft
mic1=microsoft_data['dates']
years=[]
for d in mic1:
    y=d.split('/')[2] #find only the years
    years.append(int(y))

microsoft_data['years']=years #create another column called 'years' which only contains the years

def graph(category):
    '''this function makes a graph for each of the categories that is inputted by calculating the average of that category from a certain year'''
    mic2008=microsoft_data[microsoft_data.years==2008] 
    mic2008_fixed = no_none(mic2008[category])
    microsoft_y2008=float(sum(mic2008_fixed))/(float(len(mic2008_fixed)))
    
    mic2009=microsoft_data[microsoft_data.years==2009] 
    mic2009_fixed = no_none(mic2009[category])
    microsoft_y2009=float(sum(mic2009_fixed))/(float(len(mic2009_fixed)))
    
    mic2010=microsoft_data[microsoft_data.years==2010] 
    mic2010_fixed = no_none(mic2010[category])
    microsoft_y2010=float(sum(mic2010_fixed))/(float(len(mic2010_fixed)))
    
    mic2011=microsoft_data[microsoft_data.years==2011] 
    mic2011_fixed = no_none(mic2011[category])
    microsoft_y2011=float(sum(mic2011_fixed))/(float(len(mic2011_fixed)))
    
    mic2012=microsoft_data[microsoft_data.years==2012] 
    mic2012_fixed = no_none(mic2012[category])
    microsoft_y2012=float(sum(mic2012_fixed))/(float(len(mic2012_fixed)))
    
    mic2013=microsoft_data[microsoft_data.years==2013] 
    mic2013_fixed = no_none(mic2013[category])
    microsoft_y2013=float(sum(mic2013_fixed))/(float(len(mic2013_fixed)))
    
    mic2014=microsoft_data[microsoft_data.years==2014] 
    mic2014_fixed = no_none(mic2014[category])
    microsoft_y2014=float(sum(mic2014_fixed))/(float(len(mic2014_fixed)))
    
    mic2015=microsoft_data[microsoft_data.years==2015] 
    mic2015_fixed = no_none(mic2015[category])
    microsoft_y2015=float(sum(mic2015_fixed))/(float(len(mic2015_fixed)))
    
    mic2016=microsoft_data[microsoft_data.years==2016]
    mic2016_fixed = no_none(mic2016[category])
    microsoft_y2016=float(sum(mic2016_fixed))/(float(len(mic2016_fixed)))
    
    mic2017=microsoft_data[microsoft_data.years==2017] 
    mic2017_fixed = no_none(mic2017[category])
    microsoft_y2017=float(sum(mic2017_fixed))/(float(len(mic2017_fixed)))
    
    mic2018=microsoft_data[microsoft_data.years==2018] 
    mic2018_fixed = no_none(mic2018[category])
    microsoft_y2018=float(sum(mic2018_fixed))/(float(len(mic2018_fixed)))
    
    #doing the plot
    xmicrosoft=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    ymicrosoft=[microsoft_y2008,microsoft_y2009,microsoft_y2010,microsoft_y2011,microsoft_y2012,microsoft_y2013,microsoft_y2014,microsoft_y2015,microsoft_y2016,microsoft_y2017,microsoft_y2018]
    plt.plot(xmicrosoft,ymicrosoft)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Microsoft')

#calls the graph function to plot the points
graph('overall-ratings')
graph('work-balance-stars')
graph('carrer-opportunities-stars')
graph('comp-benefit-stars')
graph('senior-mangemnet-stars')

#special case for culture values because there are so many 'none's
mic2012=microsoft_data[microsoft_data.years==2012] 
mic2012_fixed = no_none(mic2012['culture-values-stars'])
microsoft_y2012=float(sum(mic2012_fixed))/(float(len(mic2012_fixed)))
    
mic2013=microsoft_data[microsoft_data.years==2013] 
mic2013_fixed = no_none(mic2013['culture-values-stars'])
microsoft_y2013=float(sum(mic2013_fixed))/(float(len(mic2013_fixed)))
    
mic2014=microsoft_data[microsoft_data.years==2014] 
mic2014_fixed = no_none(mic2014['culture-values-stars'])
microsoft_y2014=float(sum(mic2014_fixed))/(float(len(mic2014_fixed)))
    
mic2015=microsoft_data[microsoft_data.years==2015]
mic2015_fixed = no_none(mic2015['culture-values-stars'])
microsoft_y2015=float(sum(mic2015_fixed))/(float(len(mic2015_fixed)))
    
mic2016=microsoft_data[microsoft_data.years==2016] 
mic2016_fixed = no_none(mic2016['culture-values-stars'])
microsoft_y2016=float(sum(mic2016_fixed))/(float(len(mic2016_fixed)))
    
mic2017=microsoft_data[microsoft_data.years==2017]
mic2017_fixed = no_none(mic2017['culture-values-stars'])
microsoft_y2017=float(sum(mic2017_fixed))/(float(len(mic2017_fixed)))
    
mic2018=microsoft_data[microsoft_data.years==2018]
mic2018_fixed = no_none(mic2018['culture-values-stars'])
microsoft_y2018=float(sum(mic2018_fixed))/(float(len(mic2018_fixed)))
    
#doing the plot for culture values
xmicrosoft=['2012','2013','2014','2015','2016','2017','2018']
ymicrosoft=[microsoft_y2012,microsoft_y2013,microsoft_y2014,microsoft_y2015,microsoft_y2016,microsoft_y2017,microsoft_y2018]
plt.plot(xmicrosoft,ymicrosoft)