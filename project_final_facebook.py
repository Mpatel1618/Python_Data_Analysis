# import pandas library as pd and matplotlib.pyplot linrary as plt
import pandas as pd
import matplotlib.pyplot as plt


#Part 2: graphs and relationships with time series
df = pd.read_csv('123_employee_reviews.csv', encoding = 'latin-1')

#locating the company data in the dataframe
facebook_data = df.loc[df['company'] == 'facebook']

def no_none(stars_1):
    '''gets rid of all of the nones in the data'''
    stars_2 = []
    for i in stars_1:
        if i != 'none':
            stars_2.append(float(i))
    return stars_2


#plt.plot(x,y)  
#this is very time consuming and python is hard to handle this big amount of data, so we decide to divide the dates by years

#for facebook
fac1=facebook_data['dates']
years=[]
for d in fac1:
    y=d.split('/')[2] #find only the years
    years.append(int(y))

facebook_data['years']=years #create another column called 'years' which only contains the years

def graph(category):
    '''this function makes a graph for each of the categories that is inputted by calculating the average of that category from a certain year'''
    fac2008=facebook_data[facebook_data.years==2008] 
    fac2008_fixed = no_none(fac2008[category])
    facebook_y2008=float(sum(fac2008_fixed))/(float(len(fac2008_fixed)))
    
    fac2009=facebook_data[facebook_data.years==2009] 
    fac2009_fixed = no_none(fac2009[category])
    facebook_y2009=float(sum(fac2009_fixed))/(float(len(fac2009_fixed)))
    
    fac2010=facebook_data[facebook_data.years==2010] 
    fac2010_fixed = no_none(fac2010[category])
    facebook_y2010=float(sum(fac2010_fixed))/(float(len(fac2010_fixed)))
    
    fac2011=facebook_data[facebook_data.years==2011] 
    fac2011_fixed = no_none(fac2011[category])
    facebook_y2011=float(sum(fac2011_fixed))/(float(len(fac2011_fixed)))
    
    fac2012=facebook_data[facebook_data.years==2012] 
    fac2012_fixed = no_none(fac2012[category])
    facebook_y2012=float(sum(fac2012_fixed))/(float(len(fac2012_fixed)))
    
    fac2013=facebook_data[facebook_data.years==2013] 
    fac2013_fixed = no_none(fac2013[category])
    facebook_y2013=float(sum(fac2013_fixed))/(float(len(fac2013_fixed)))
    
    fac2014=facebook_data[facebook_data.years==2014] 
    fac2014_fixed = no_none(fac2014[category])
    facebook_y2014=float(sum(fac2014_fixed))/(float(len(fac2014_fixed)))
    
    fac2015=facebook_data[facebook_data.years==2015] 
    fac2015_fixed = no_none(fac2015[category])
    facebook_y2015=float(sum(fac2015_fixed))/(float(len(fac2015_fixed)))
    
    fac2016=facebook_data[facebook_data.years==2016] 
    fac2016_fixed = no_none(fac2016[category])
    facebook_y2016=float(sum(fac2016_fixed))/(float(len(fac2016_fixed)))
    
    fac2017=facebook_data[facebook_data.years==2017] 
    fac2017_fixed = no_none(fac2017[category])
    facebook_y2017=float(sum(fac2017_fixed))/(float(len(fac2017_fixed)))
    
    fac2018=facebook_data[facebook_data.years==2018] 
    fac2018_fixed = no_none(fac2018[category])
    facebook_y2018=float(sum(fac2018_fixed))/(float(len(fac2018_fixed)))
    
    #doing the plot
    xfacebook=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    yfacebook=[facebook_y2008,facebook_y2009,facebook_y2010,facebook_y2011,facebook_y2012,facebook_y2013,facebook_y2014,facebook_y2015,facebook_y2016,facebook_y2017,facebook_y2018]
    plt.plot(xfacebook,yfacebook)
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Facebook')

#calls the graph function to plot the points
graph('overall-ratings')
graph('work-balance-stars')
graph('carrer-opportunities-stars')
graph('comp-benefit-stars')
graph('senior-mangemnet-stars')

#special case for culture values because there are so many 'none's
fac2012=facebook_data[facebook_data.years==2012] 
fac2012_fixed = no_none(fac2012['culture-values-stars'])
facebook_y2012=float(sum(fac2012_fixed))/(float(len(fac2012_fixed)))
    
fac2013=facebook_data[facebook_data.years==2013] 
fac2013_fixed = no_none(fac2013['culture-values-stars'])
facebook_y2013=float(sum(fac2013_fixed))/(float(len(fac2013_fixed)))
    
fac2014=facebook_data[facebook_data.years==2014] 
fac2014_fixed = no_none(fac2014['culture-values-stars'])
facebook_y2014=float(sum(fac2014_fixed))/(float(len(fac2014_fixed)))
    
fac2015=facebook_data[facebook_data.years==2015] 
fac2015_fixed = no_none(fac2015['culture-values-stars'])
facebook_y2015=float(sum(fac2015_fixed))/(float(len(fac2015_fixed)))
    
fac2016=facebook_data[facebook_data.years==2016] 
fac2016_fixed = no_none(fac2016['culture-values-stars'])
facebook_y2016=float(sum(fac2016_fixed))/(float(len(fac2016_fixed)))
    
fac2017=facebook_data[facebook_data.years==2017] 
fac2017_fixed = no_none(fac2017['culture-values-stars'])
facebook_y2017=float(sum(fac2017_fixed))/(float(len(fac2017_fixed)))
    
fac2018=facebook_data[facebook_data.years==2018] 
fac2018_fixed = no_none(fac2018['culture-values-stars'])
facebook_y2018=float(sum(fac2018_fixed))/(float(len(fac2018_fixed)))
    
#doing the plot for culture values
xfacebook=['2012','2013','2014','2015','2016','2017','2018']
yfacebook=[facebook_y2012,facebook_y2013,facebook_y2014,facebook_y2015,facebook_y2016,facebook_y2017,facebook_y2018]
plt.plot(xfacebook,yfacebook)