#!/usr/bin/env python3

import sys


def mapper_oxycodone_speciality():
    for l in sys.stdin:
        l = l.strip()
        l = l.split(",")

        # The key will be the city name since we're trying to
        # find out the total drug cost incurred by each city
        
        drug = l[9]
        speciality = l[6]
        drug_cost = l[14]
        
        if 'OXYCODONE' in drug.upper():
            print(speciality + '\t' + drug + '\t' + drug_cost)


        # The value will be the total_drug_cost associated with
        # that particular entry



if __name__ == "__main__":
    mapper_oxycodone_speciality()

