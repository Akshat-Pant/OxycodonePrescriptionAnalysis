    #!/usr/bin/env python3

import sys


def reducer_oxycodone_city():
    """Reducer1 is responsible for reducing the <key,value> pairs generated by Mapper1 into aggregated output"""

    # Initializing useful parameters
    current_city = None
    city_drug_total_cost = 0
    
    print("city\tDrug\tTotal Drug Cost")
    print("====\t====\t===============")
    for l in sys.stdin:
    
        l = l.strip()
        #print(l)

        # Parse the <k,v>
        #city,drug_total = l.split("\t",1)
        city, drug, drug_total = l.split("\t")

        # Convert the drug_total into an integer so that it can be increased
        try:
            drug_total = float(drug_total)
        except:
            drug_total = 0.0


        ####### Aggregation Logic
        # The most common case when we're trying to add total_drug_cost of the
        # same city
        if current_city == city:
            city_drug_total_cost = city_drug_total_cost + drug_total

        # Cases when the current_city changes
        else:

            # Case when the current_city is not the first in the list
            if current_city:
                city_drug_total_cost = round(city_drug_total_cost,2)
                print(current_city + "\t" + drug + "\t$"+str(city_drug_total_cost))

            # Case when the current customer is the first one in the list
            else:
                pass
            current_city = city
            city_drug_total_cost = 0
            city_drug_total_cost = city_drug_total_cost + drug_total

    city_drug_total_cost = round(city_drug_total_cost,2)
    print(current_city + "\t" + drug + "\t$"+str(city_drug_total_cost))








if __name__=="__main__":
    reducer_oxycodone_city()



