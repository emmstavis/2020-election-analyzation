#Election Data
#Emma Stavis
#2020

#Reports back 2016 vote for inputed county in PA, WI, MI, FL, NC, and GA
#Doesn't check for county correctness, will catch states
#Use state abreviations, type quit as county to quit

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
    for row in csv_reader:
        if row["ST"] == "FL" or row["ST"] == "PA" or row["ST"] == "MI" or row["ST"] == "WI" or row["ST"] == "GA" or row["ST"] == "NC":
            linecount +=1
            makedata(dataset, row)
        

def make_full(input_county):
    valid = False
    while (valid == False) :
        valid = True
        state_entered = input("State: ")
        if state_entered.lower() == "pa":
            end_county = input_county + " County, Pennsylvania"
        elif state_entered.lower() == "wi":
            end_county = input_county + " County, Wisconsin"
        elif state_entered.lower() == "mi":
            end_county = input_county + " County, Michigan"
        elif state_entered.lower() == "fl":
            end_county = input_county + " County, Florida"
        elif state_entered.lower() == "nc":
            end_county = input_county + " County, North Carolina"
        elif state_entered.lower() == "ga":
            end_county = input_county + " County, Georgia"
        else:
            valid = False
    return end_county

def get_data():
    continuation = True
    while (continuation==True):
        county_wanted = input("What county?: ").capitalize()
        if county_wanted != 'Quit':
            county_wanted = make_full(county_wanted)
            print(county_wanted)
            for counties in range(len(dataset)):
                if dataset[counties][1] == county_wanted:
                    county_row = counties
            print("% Rep:", dataset[county_row][3][2])
            print("% Dem:",dataset[county_row][3][3])
            print("Votes Rep:",dataset[county_row][3][0])
            print("Votes Dem:",dataset[county_row][3][1])
        else:
            continuation = False

get_data()





