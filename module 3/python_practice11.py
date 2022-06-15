counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
#for county in counties_dict:
#    print(county)
# keys output
#for county in counties_dict.keys():
#    print(county)
#values output
#for voters in counties_dict.values():
#    print(voters)
# for county in counties_dict:
#   print(counties_dict[county])
#for county in counties_dict:
#   print(counties_dict.get(county))

#key-values pairs output
for county, voters in counties_dict.items():
    print(county,"county has", voters, "registered voters.")
