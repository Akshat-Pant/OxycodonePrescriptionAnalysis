#!/usr/bin/env python3

import sys


def mapper_georgia():
    
    file = open('/Users/akshatpant/Desktop/UMD/Sem4/BigData/HW1/INST767/GeorgiaCitiesByPopulation.txt',  'r')
    city_dict = {}
    for c, l in enumerate(file.readlines()):
        if c > 0:
            l = l.strip()
            l = l.split('\t')
            city = l[0]
            pop = l[1].replace(',', '')
            pop = pop.strip('"')
            city_dict[city] = pop
    
    
    for c, l in enumerate(sys.stdin):
        if c > 0:
            l = l.strip()
            l = l.split(",")

            # The key will be the city name since we're trying to
            # find out the total drug cost incurred by each city
            
            drug = l[9]
            city = l[5]
            drug_cost = l[14]
            
            pop = '0'
            if city in city_dict:
                pop = city_dict[city]

            print(city + '\t' + pop + '\t' + drug + '\t' + drug_cost)

        
#        try:
#            print(city + '\t' + city_dict[city] + '\t' + drug + '\t' + drug_cost)
#        except:
#            print(city)


        # The value will be the total_drug_cost associated with
        # that particular entry



if __name__ == "__main__":
    mapper_georgia()
