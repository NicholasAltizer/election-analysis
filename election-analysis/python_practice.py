counties = ["Arapahoe","Denver","Jefferson"]
#if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#for county in counties:
#    print(county)

#counties_tuple = ("Arapahoe","Denver","Jefferson")
#for i in range(len(counties_tuple)):
#    print(counties_tuple[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict.keys():
    #print(county)
#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#    print(counties_dict[county])

for county, voters in counties_dict.items():
#    print(county,("county has"),voters,("registered voters."))
    print(f"{county} county has {voters} registered voters.")


#voting_data =[]
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict)

#for i in range(len(voting_data)):
#    print(voting_data[i]['county'])

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
        