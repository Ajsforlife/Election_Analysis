voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
              {'county':'Denver', 'registered_voters':463353},
              {'county':'Jefferson', 'registered_voters': 432438}]
#for county_dict in voting_data
    #print(county_dict)
#for i in range(len(voting_data)):
    #print(voting_data[i]['county'])
#county and voters output
#for county_dict in voting_data:
#   for value in county_dict.values():
#        print(value)
#just voters output
#for county_dict in voting_data:
 #   print(county_dict['registered_voters'])
for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.")