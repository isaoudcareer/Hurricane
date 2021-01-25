import math
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#CODE

conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
for i in damages:
  if i == "Damages not recorded":
    updated_damages.append(i)
  if i.find("M") != -1:
    updated_damages.append(float(i[0:len(i)-1]) * 10**6)
  if i.find("B") != -1:
    updated_damages.append(float(i[0:len(i)-1]) * 10**9)
#Dictionary for all hurricanes with info:
def hurricane_name(name, month, year, max_w, areas, damage, death):
  dict_hurricane = {}
  count = 0
  for i in name:
    dict_hurricane[i] = {}
  for i in dict_hurricane:
    dict_hurricane[i] = {"Name": name[count], "Month": month[count], "Year":year[count], "Sustained Wind": max_w[count], "Areas Affected": areas[count], "Damages": damage[count], "Deaths": death[count]}
    count += 1
  return dict_hurricane
hurricanes = hurricane_name(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
#Testing the Hurricane Dict:
#print(hurricanes["Mitch"])
#Sorting Hurricane by year

def hurricane_year(hurricanes):
  hurricane_by_year = {}
  for i in hurricanes:
    current_year = hurricanes[i]["Year"]
    current_cane = [i]
    if current_year not in hurricane_by_year:
      hurricane_by_year[current_year] = [current_cane]
    else:
      hurricane_by_year[current_year].append(current_cane)
  return hurricane_by_year
#Testing hurricane_by_year:
hurricane_by_year = hurricane_year(hurricanes)
#print(hurricane_by_year)

#Hurricane Areas affected:
def count_affected_areas(hurricanes):
  """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""
  affected_areas_count = dict()
  for cane in hurricanes:
    for area in hurricanes[cane]['Areas Affected']:
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      else:
        affected_areas_count[area] += 1
  return affected_areas_count
areas_affected_count = count_affected_areas(hurricanes)
#print(areas_affected_count)
#Area affected the most:

def areas_affected_most(areas_affected_count):
  most_affected_dict = {}
  most_affected = 'Mexico'
  num_hits = 0
  for area in areas_affected_count.keys():
    for num in areas_affected_count.values():
      if num > num_hits:
        most_affected = area
        num_hits = num
  most_affected_dict[most_affected] = num_hits
  return most_affected_dict
#print("Most affected area is:", areas_affected_most(areas_affected_count))

#hurricane that caused greatest deaths:

def hurricane_most_deaths(hurricanes):
  most_deaths_cane = 'Dean'
  num_deaths = 0
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] > num_deaths:
      most_deaths_cane = cane
      num_deaths = hurricanes[cane]["Deaths"]
  return most_deaths_cane, num_deaths

#print(hurricane_most_deaths(hurricanes))

# Mortality rates:
def mortality(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality_rate_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] == 0:
      mortality_rate_dict[0].append(cane)
    if (hurricanes[cane]["Deaths"] > 0) and (hurricanes[cane]["Deaths"] < 100):
      mortality_rate_dict[1].append(cane)
    if (hurricanes[cane]["Deaths"] > 100) and (hurricanes[cane]["Deaths"] < 500):
      mortality_rate_dict[2].append(cane)
    if (hurricanes[cane]["Deaths"] > 500) and (hurricanes[cane]["Deaths"] < 1000):
      mortality_rate_dict[3].append(cane)
    if (hurricanes[cane]["Deaths"] > 1000) and (hurricanes[cane]["Deaths"] < 10000):
      mortality_rate_dict[4].append(cane)
    if (hurricanes[cane]["Deaths"] > 10000):
      mortality_rate_dict[5].append(cane)
  return mortality_rate_dict
#print(mortality(hurricanes))
#Hurricane causing greatest damage & how costly it was:
def greatest_damage_cane(hurricanes):
  greatest_damage_cane : "Dean"
  greatest_cost = 0
  for cane in hurricanes:
    if (hurricanes[cane]["Damages"] == "Damages not recorded"):
      hurricanes[cane]["Damages"] = 0
    if hurricanes[cane]["Damages"] > greatest_cost:
      greatest_damage_cane = cane
      greatest_cost = hurricanes[cane]["Damages"]
  
  return greatest_damage_cane, greatest_cost

greatest_damage = greatest_damage_cane(hurricanes)
#print(greatest_damage)


  
  
  


     



