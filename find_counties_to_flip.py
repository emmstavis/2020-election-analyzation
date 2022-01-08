#Election data
#Emma Stavis
#2020

#Finding under 10 counties to flip in 2020 from 2016 for Dem Candidate to Win

import csv
def makedata(dataarray, row):
    dataarray.append([row["State"], row["County"],[row["Republicans 12"],
        row["Democrats 12"], row["Republicans Perc 12"], row["Democrats Perc 12"]],
        [row["Votes Trump"], row["Votes Clinton"],
        row["Republicans Perc 16"], row["Democrats Perc 16"]]])
with open('election_data_simplified.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter = ',')
    linecount = 0
    dataset = []
    lostvote = []
    for row in csv_reader:
        if row["ST"] == "FL":
            linecount +=1
            makedata(dataset, row)
            if int(row["Democrats 12"]) - int(row["Votes Clinton"]) > 1000:
                makedata(lostvote, row)
        if row["ST"] == "MI":
            linecount +=1
            makedata(dataset, row)
        if row["ST"] == "PA":
            linecount +=1
            makedata(dataset, row)
            if int(row["Democrats 12"]) - int(row["Votes Clinton"]) > 6000:
                makedata(lostvote, row)
        if row["ST"] == "WI":
            linecount +=1
            makedata(dataset, row)
            if int(row["Democrats 12"]) - int(row["Votes Clinton"]) > 10000:
                makedata(lostvote, row)
#index numbers for reference
state = 0
county = 1
rvotes12 = 0
dvotes12 = 1
rpercent12 = 2
dpercent12 = 3
rvotes16 = 0
dvotes16 = 1
rpercent16 = 2
dpercent16 = 3

flips = []

for counties in range(len(dataset)):
    #if dem won in 2012 and trump won in 2016, add to array of counties that flipped
    if dataset[counties][2][3] > dataset[counties][2][2] and dataset[counties][3][3] < dataset[counties][3][2]:
        flips.append(dataset[counties])


#arrays of counties with highest percent drops and vote totals (cutoffs determined relatively)
highestpercentdrop = []
highestvoteslost = []
for counties in range(len(flips)):
    dropdpercent = (int(flips[counties][2][1]) - int(flips[counties][3][1]))/int(flips[counties][2][1])
    if dropdpercent > 0.22443267085800578:
        highestpercentdrop.append(flips[counties])
    dropdvotes = int(flips[counties][2][1]) - int(flips[counties][3][1])
    if dropdvotes > 5500:
        highestvoteslost.append(flips[counties])

        

dataset2 = dataset
#dataset2 is 2016 vote with the identified counties changed back to their 2012 vote.
print("Here are the counties to flip:\n")
for counties in range(len(highestvoteslost)):
    for lotscounties in range(len(dataset2)):
        #Michigan would require more counties to flip in order to flip the state, thus I chose to eliminate it from focus
        if dataset[lotscounties][1] == highestvoteslost[counties][1] and dataset[lotscounties][0] !="Michigan":
            dataset2[lotscounties][3][1] = dataset[lotscounties][2][1]
            print(highestvoteslost[counties][1])


#add in PA counties that were not flipped but need to return to 2012 turnout
for lotscounties in range(len(dataset2)):
        if ( dataset[lotscounties][1] == "Philadelphia County, Pennsylvania" or
        dataset[lotscounties][1] == "Mercer County, Pennsylvania" or
        dataset[lotscounties][1] == "Lackawanna County, Pennsylvania" ):
                dataset2[lotscounties][3][1] = dataset[lotscounties][2][1]
                dataset2[lotscounties][3][0] = dataset[lotscounties][2][0]

        
ftotaldemvotes = 0
ftotalrepvotes = 0
mtotaldemvotes = 0
mtotalrepvotes = 0
ototaldemvotes = 0
ototalrepvotes = 0
ptotaldemvotes = 0
ptotalrepvotes = 0
wtotaldemvotes = 0
wtotalrepvotes = 0

for counties in range(len(dataset2)):
    if dataset2[counties][0] == "Florida":
        ftotaldemvotes += int(dataset[counties][3][1])
        ftotalrepvotes += int(dataset[counties][3][0])
    if dataset2[counties][0] == "Michigan":
        mtotaldemvotes += int(dataset[counties][3][1])
        mtotalrepvotes += int(dataset[counties][3][0])
    if dataset2[counties][0] == "Pennsylvania":
        ptotaldemvotes += int(dataset[counties][3][1])
        ptotalrepvotes += int(dataset[counties][3][0])
    if dataset2[counties][0] == "Wisconsin":
        wtotaldemvotes += int(dataset[counties][3][1])
        wtotalrepvotes += int(dataset[counties][3][0])
print("""\nHere would be the total votes if all of the previous counties
were flipped and Philadelphia, Mercer, and Lackawanna PA
returned to 2012 vote: \n\n""")
      
print("Florida total R:", ftotalrepvotes)
print("Florida total D:", ftotaldemvotes)
print(" ")
print("Michigan total R:", mtotalrepvotes)
print("Michgan total D:", mtotaldemvotes)
print(" ")
print("PA total R:", ptotalrepvotes)
print("PA total D:", ptotaldemvotes)
print(" ")
print("Wisconsin total R:", wtotalrepvotes)
print("Wisconsin total D:", wtotaldemvotes)
print("\n")






