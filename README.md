# OxycodonePrescriptionAnalysis

Derived some very specific insights related to the prescription of “OXYCODONE” for the state of Georgia using the dataset Medicare1.csv

Aggregated the total amount reimbursed for “OXYCODONE” prescriptions based on the following parameters: 
1) Speciality of the prescriber.   
2) City.

Found out the top 5 cities with maximum total drug cost and the ratio of the total drug cost of those cities to total population in those cities

## Run the code

Mapper and reducer functions for aggregation by Speciality of prescriber are mapper_oxycodone_speciality.py and reducer_oxycodone_speciality.py

Mapper and reducer functions for aggregation by city are mapper_oxycodone_city.py and reducer_oxycodone_city.py

Mapper and reducer functions for aggregation by city are mapper_oxycodone_city.py and reducer_oxycodone_city.py

Mapper and reducer functions for aggregation by city and and finding maximum total drug cost and the ratio of the total drug cost of those cities are mapper_georgia.py and reducer_georgia.py. Run the sort command to sort the results. 
