import webget
import csv

url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
webget.download(url)

filename = './befkbhalderstatkode.csv'
STATISTICS = {}
persons_dic = {}
age_dic = {}
city_dic = {}


with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    year = None
    city = None
    age = None
    zip_code = None
    persons = None
    
    for row in reader:
        if (row[0] == year):
            if (row[1] == city):
                if (row[2] == age):
                    zip_code = row[3]
                    persons = row[4]
                    persons_dic.update({zip_code : persons})
                   # STATISTICS.update({year: { city: {age : { zip_code : persons}}}})
                else :
                    age = row[2]
                    age_dic.update({age : persons_dic})
            else:
                city = row[1]
                city_dic.update({city : age_dic})
        else:
            year = row[0]
            STATISTICS.update({year : city_dic})

    print(STATISTICS)

    