"""
This program writes and reads its own csv data
Author: Michael John Andagan Lalim
Description: Modified code for a past ICS3U1 assignment that invovles with "FILE MANIPULATION"
                Modification made: creates own sets of data & more effecient code. (from 90+ lines to 37)
"""
#Writing Section
#-------------------------------------------------------------------------------------------------
import random as r
import names as n
import randomname as rn

#Welcome screen
#-------------------------------------------------------------------------------------------------
print("Welcome to Data Sample Generator")
print("--------------------------------\n")
fileName = input("Enter name of file: ");fileName+=".csv"
iterationNum = int(input("How many 'hypothetical' applicants(please enter a whole number): "))
writeFile = open(fileName,"w+")

# This section of the script generates a 'hypothetical' grades of applicants and puts it in a list
#-------------------------------------------------------------------------------------------------
gradeList = []
for i in range(50,101,1):
    randomGradeGenerator = 0
    randomGradeGenerator += i
    gradeList.append(randomGradeGenerator)
#-------------------------------------------------------------------------------------------------

#Generates 100 random city names
#-------------------------------------------------------------
cityNameList = []
while len(cityNameList) < 10:
    cities = rn.generate('names/cities/canada')
    if cities in cityNameList:
        continue
    else:
        cityNameList.append(cities)
#-------------------------------------------------------------



for i in range(iterationNum):
    firstName=n.get_first_name()
    lastName=n.get_last_name()
    randomCityName = r.randint(0,9)
    randomGrade1 = r.randint(0,50);randomGrade2 = r.randint(0,50);randomGrade3 = r.randint(0,50);randomGrade4 = r.randint(0,50);randomGrade5 = r.randint(0,50);randomGrade6 = r.randint(0,50)
    writeFile.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(firstName,lastName,cityNameList[randomCityName],gradeList[randomGrade1],gradeList[randomGrade2],gradeList[randomGrade3],gradeList[randomGrade4],gradeList[randomGrade5],gradeList[randomGrade6]))

writeFile.close()
#-------------------------------------------------------------------------------------------------


#Reading Section
#-------------------------------------------------------------------------------------------------
myfile = open(fileName,'r+')
fileReader = myfile.readlines()
#Header
print("{0:<15} | {1:<15} | {2:<15} | {3:<10} | {4:>10}".format("FIRST NAME","LAST NAME","CITY","AVERAGE MARK",'STATUS',))
print("-------"*13)
defferedApplicants=0
rejectedApplicant=0
acceptedApplicants=0
count=0
for i in range(len(fileReader)):
    count+=1
    data = fileReader[i].strip('\n')
    element = data.split(',')
    markSum = 0; averageMark = 0; status = ''
    for j in range(3,9,1):
        markSum += int(element[j])
        averageMark = markSum/6
    if averageMark > 90:
        status = 'Accepted'; acceptedApplicants += 1
    elif 90 > averageMark > 80:
        status = 'Deffered';defferedApplicants+=1
    else:
        status = 'Not Accepted';rejectedApplicant+=1
    print("{0:<15} | {1:<15} | {2:<15} | {3:<12} | {4:>10}".format(element[0],element[1],element[2],round(averageMark,2),status,))
    print("-------"*13)
acceptanceRate = 0
acceptanceRate = (acceptedApplicants/iterationNum) * 100
print("The acceptance rate this year is: {0} %.".format(round(acceptanceRate,2)))
print("The total number of applicants this year is {0}".format(iterationNum))
print("There are {0} accepted applicants".format(acceptedApplicants))
print("There are {0} deferred applicants".format(defferedApplicants))
print("There are {0} applicants who did not meet the quota.".format(rejectedApplicant))
#-------------------------------------------------------------------------------------------------

#closing file
myfile.close()
