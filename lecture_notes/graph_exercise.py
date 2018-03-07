import webget
import numpy as np
import pandas as pd
import random 

family_name_url = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last'
male_names_url = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first'
female_names_url = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first'

family_names_csv = pd.read_csv(webget.download(family_name_url)).as_matrix()
male_names_csv = pd.read_csv(webget.download(male_names_url)).as_matrix()
female_names_csv = pd.read_csv(webget.download(female_names_url)).as_matrix()

family_names = []
female_names = []
male_names = []


for row in family_names_csv:
    names = row[0].split()
    family_names.append(names[0].title())

for row in male_names_csv:
    names = row[0].split()
    male_names.append(names[0].title())   

for row in female_names_csv:
    names = row[0].split()
    female_names.append(names[0].title())     

    
random_males = [random.choice(male_names) + " " + random.choice(family_names) for _ in range(50)]   
random_females = [random.choice(female_names) + " " + random.choice(family_names) for _ in range(50)]   

random_names = random_males + random_females
print(random_names)