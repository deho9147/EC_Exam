import csv
import math
ecByYear = {}
ecVotesState = {}
usedvotes = {}
with open('/home/derek/ElectoralCollegeChange/ElectoralCollegeVotes - Sheet1 (1).csv') as csvfile:
    ecVotes=csv.reader(csvfile)
    for row in ecVotes:
        if row[0] !="State":
            ecVotesState[row[0]]=int(row[1]);
print(ecVotesState)
#open same file multiple times to reset row to front, gets the data in order
with open('/home/derek/ElectoralCollegeChange/dataneeded.csv') as csvfile:
    ecVotes = csv.reader(csvfile)
    for row in ecVotes:
        if (row[0] and row[1] and row[7] and row[18] and (row[18]!="roundedElec") and ((row[8]=="republican") or row[8]=="conservative") ):
            year = row[0]
            state = row[1]
            candidate = row[7]
            votenumber = math.trunc(float(row[16])*float(ecVotesState[state]))
            if year in usedvotes:
                if state in usedvotes[year]:
                    usedvotes[year][state] = usedvotes[year][state]+votenumber
                else:
                    usedvotes[year][state]=votenumber
            else:
                usedvotes[year]={state:votenumber}
            party = row[8]
            if (votenumber!=1000):
                if (year in ecByYear):
                    if (state in ecByYear[year]):
                        ecByYear[year][state] = ecByYear[year][state] + [candidate, party, votenumber, row[16]]
                    else:
                        ecByYear[year][state] = [candidate,party,votenumber,row[16]]
                else:
                    ecByYear[year]= {state:[candidate,party,votenumber,row[16]]}
with open('/home/derek/ElectoralCollegeChange/dataneeded.csv') as csvfile:
    ecVotes = csv.reader(csvfile)
    for row in ecVotes:
        if (row[0] and row[1] and row[7] and row[18] and (row[18]!="roundedElec") and (row[8]=="democrat" or row[8]=="liberal")):
            year = row[0]
            state = row[1]
            candidate = row[7]
            votenumber = math.trunc(float(row[16])*float(ecVotesState[state]))
            party = row[8]
            if year in usedvotes:
                if state in usedvotes[year]:
                    usedvotes[year][state] = usedvotes[year][state]+votenumber
                else:
                    usedvotes[year][state]=votenumber
            else:
                usedvotes[year]={state:votenumber}
            if (votenumber!=1000):
                if (year in ecByYear):
                    if (state in ecByYear[year]):
                        ecByYear[year][state] = ecByYear[year][state] + [candidate, party, votenumber,row[16]]
                    else:
                        ecByYear[year][state] = [candidate,party,votenumber, row[16]]
                else:
                    ecByYear[year]= {state:[candidate,party,votenumber,row[16]]}
with open('/home/derek/ElectoralCollegeChange/dataneeded.csv') as csvfile:
    ecVotes = csv.reader(csvfile)
    for row in ecVotes:
        if (row[0] and row[1] and row[7] and row[18] and (row[18]!="roundedElec") and row[8]!="democrat" and row[8]!="republican"):
            year = row[0]
            state = row[1]
            candidate = row[7]
            votenumber = math.trunc(float(row[16])*float(ecVotesState[state]))
            party = row[8]
            if year in usedvotes:
                if state in usedvotes[year]:
                    usedvotes[year][state] = usedvotes[year][state]+votenumber
                else:
                    usedvotes[year][state]=votenumber
            else:
                usedvotes[year]={state:votenumber}
            if (votenumber!=0):
                if (year in ecByYear):
                    if (state in ecByYear[year]):
                        ecByYear[year][state] = ecByYear[year][state] + [candidate, party, votenumber, row[16]]
                    else:
                        ecByYear[year][state] = [candidate,party,votenumber, row[16]]
                else:
                    ecByYear[year]= {state:[candidate,party,votenumber, row[16]]}
print(usedvotes)
for year in usedvotes:
    for state in usedvotes[year]:
        votesremaining = ecVotesState[state]-usedvotes[year][state]
        if votesremaining != 0:
            if ecByYear[year][state][3] > ecByYear[year][state][7]:
                ecByYear[year][state][2]=ecByYear[year][state][2] + votesremaining
            else:
                ecByYear[year][state][6] = ecByYear[year][state][6] + votesremaining
for year in ecByYear:
    with open('/home/derek/ElectoralCollegeChange/csvs/'+year+'.csv', 'w') as writefile:
        writer = csv.writer(writefile, delimiter=',')
        for state in ecByYear[year]:
            temp = [year,state]
            count = 0
            for item in ecByYear[year][state]:
                count = count + 1
                temp = temp + [item]
            writer.writerow(temp)



print(ecByYear)
