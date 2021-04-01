# names of hurricanes
from typing import ValuesView


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 
'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 
'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 
'Matthew', 'Irma', 'Maria', 'Michael']
######################################################################################################
# Creates callable keynames for Hurricanes 
######################################################################################################
keynames = [x.replace(' ','-') for x in names]

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 
'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 
'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 
'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 
1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 
160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 
'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 
'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 
['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 
'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], 
['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 
'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], 
['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 
'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 
'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 
'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 
'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]
######################################################################################################
# one list tallies hurricans, the other attaches all hurricans to a particular area
######################################################################################################
areas_n_hurricanes = {}
hurricane_frequency = {}
c=0
for zones in areas_affected:
    for area in zones:
        if area in hurricane_frequency:
            hurricane_frequency   [area] += 1
            areas_n_hurricanes    [area] +=  ', '+names[c]
        else:
            hurricane_frequency   [area]  = 0
            areas_n_hurricanes    [area]  =  ' ' +names[c]
    c+=1

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', 
'65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', 
'5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
######################################################################################################
# Converted to floats then integers. Could be either or on necessity 
######################################################################################################
new_dmgs = {}
c=0
for item in damages:
    if   'B'                    in item:
        new_dmgs[keynames[c]]= int(float(item.replace('B',''))*1000000000000)
    elif 'M'                    in item:
        new_dmgs[keynames[c]]= int(float(item.replace('M',''))*1000000      )
    elif 'Damages not recorded' in item:
        new_dmgs[keynames[c]]= (0)
    c+=1

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,
603,138,3057,74]

######################################################################################################
# write your construct hurricane dictionary function here:
######################################################################################################

hurricane_dic = {}
def hurrican_dic(hurricane_dic, months, years, max_sustained_winds, areas_affected, damages, deaths):
    new_hurricane_dic = hurricane_dic
    for i in range(len(names)):
        hurricane_dic[str(names[i])] ={
        'month'                    :                              months              [i], 
        'year'                     :                              years               [i], 
        'max sustained winds'      :    ''.join(''           +str(max_sustained_winds)[i]+'mph'), 
        'areas affected'           :                              areas_affected      [i], 
        'damages'                  :                              damages             [i], 
        'deaths'                   :                              deaths              [i]
    }

    hurricane_dic = new_hurricane_dic
    return new_hurricane_dic


######################################################################################################
###################################Class and most related functions###################################
######################################################################################################

class Hurricane:
##############gives the Hurrican a instance, also allows for 'Hurricane_data' to access basic data.
    def __init__(self, name):
        self.name                    =      name

##############gives each Hurricane a biography######################################################################
    def add_info(self, month, year, max_sustained_winds, areas_affected, damages, deaths):       
        self.months                  =      month
        self.years                   =      year
        self.max_winds               =      max_sustained_winds
        self.areas_affected          =      areas_affected
        self.damages                 =      damages
        self.deaths                  =      deaths 

##########returns a list of Hurricans based off the year they happened. Maybe too much information for a basic call#
    def by_year(self, yearsx):
        c, yearsx = -1, yearsx.sort()
        for year in years:
           c+=1
           print('''the year {} had Hurricane {} 
           '''.format(years[c], names[c],))
        return ':)'

##########returns the number of areas a called Hurricane affected###################################################
    def number_area(self):
        return ''+str(len(self.areas_affected))+''

##########returns the most affected area by Hurricanes takes two new lists above helping access/map data.###########
    def most_affected_area(self):    
        k = max(hurricane_frequency, key=hurricane_frequency.get)
        L = k + ' getting hit by a total of ' + str(hurricane_frequency[k]) + '. Hurricanes were chronologically, ' \
            +areas_n_hurricanes.get(k, 0)
        return L

##########returns most recorded deaths for a Hurricane. No arguments and takes the list above 'deaths' using index##
    def mortality(self):
        L = max(deaths)
        return str(L)+ ' deaths from ' +names[deaths.index(L)]

##########returns a sorted list of Hurricane by Mortality.##########################################################
    def by_mortality(self, a):
        ascending = dict(zip(names, deaths))
        x = sorted(ascending.items(), key=lambda x: x[1], reverse=True)
        for i in x:
            print('Hurricane: '+str(i[0])+', Deaths: '+str(i[1]))
        return ':)'

##########returns a list of Hurricans sorted by damage. Intended to combine all of these into one function but...##
    def by_damage(self):
        x = sorted(new_dmgs.items(), key=lambda x: x[1], reverse=True)
        for i in x:
            if i[1] == 0:
                print('Hurricane: '+str(i[0])+', Damages were not recorded')
            else:
                print('Hurricane: '+str(i[0])+', Damages '+str(i[1])+'$')
        return ':)'

##########returns the greatest amount of damage caused by a Hurricane###############################################
    def greatest_damage(self):
        k = max(new_dmgs, key=new_dmgs.get)
        L = str(k) + ' causing a total of ' + str(new_dmgs[k]) + ' $ in damage'
        return L

    def __repr__(self):
        return '{} {} {} {} {} {} {}'.format(self.name, self.months, self.years, self.max_winds, self.areas_affected, self.damages, self.deaths)


######################################################################################################
###################################/Class_and_most_related_functions##################################
######################################################################################################

######################################################################################################
##################Class_Constructur###################################################################
######################################################################################################


for i in range(len(names)):
    namev                                      =                 keynames[i]
    locals()[''+str(namev.replace(' ',''))+''] =                  Hurricane(
        name                                   =                      namev)

for i in range(len(names)):
    namev                =                                       keynames[i]
    monthv               =                                         months[i]
    yearv                =                                          years[i]
    max_sustained_windsv = ''.join(''            +str(max_sustained_winds[i])+'mph')
    areas_affectedv      =                                 areas_affected[i]
    damagesv             =                                        damages[i]
    deathsv              = ''.join(''                         +str(deaths[i])+' dead')
    locals()[''+str(namev)+''].add_info( 
        month               = monthv, 
        year                = yearv, 
        max_sustained_winds = max_sustained_windsv, 
        areas_affected      = areas_affectedv, 
        damages             = damagesv, 
        deaths              = deathsv)

######################################################################################################
##################Instance_Call_for_Updates###########################################################
hurricane_data = Hurricane('hurricane_data')
######################################################################################################
##################/Class Constructur##################################################################
######################################################################################################



######################################################################################################
# write your update damages function here:
######################################################################################################

##written above. called twice for 'before and after'
# print(Camille.deaths)
# Camille.deaths = 300
# print(Camille.deaths)

######################################################################################################
# write your construct hurricane by year dictionary function here:
######################################################################################################

# written above. Called here.
print(hurricane_data.by_year(years))

######################################################################################################
# write your count affected areas function here:
######################################################################################################

# written above called here
print(Janet.number_area())

######################################################################################################
# write your find most affected area function here:
######################################################################################################

#written above called here.
print(' the area hit by the most \'canes is: ' \
    +hurricane_data.most_affected_area())

######################################################################################################
# write your greatest number of deaths function here:
######################################################################################################

#written above called here.
print(hurricane_data.mortality())

######################################################################################################
# write your catgeorize by mortality function here:
######################################################################################################

#written above called here.
print(hurricane_data.by_mortality('a'))


######################################################################################################
# write your greatest damage function here:
######################################################################################################

print(hurricane_data.greatest_damage())


######################################################################################################
# write your catgeorize by damage function here:
######################################################################################################

print(hurricane_data.by_damage())
