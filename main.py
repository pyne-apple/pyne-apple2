import math
import sys
import pandas as pd
import numpy as np

mostFrequentClassOverall = -1
dictsOfProbsForClass1 = []
dictsOfProbsForClass0 = []

def main():
    if len(sys.argv) != 3:
        print ("Please execute with two arguments <train.dat> <test.dat>")
        exit()
    # Reading in data just reading in the training file (train.dat)
    with open(sys.argv[1]) as trainingFile, open(sys.argv[2]) as testFile:
        firstLine = trainingFile.readline()
        headers = firstLine.split()

        #print(headers)

        trainingLists = []
        for line in trainingFile:
            trainingLists.append(list(line.strip().replace('\t', '')))

        # Convert training data into a pandas dataframe
        trainingDF = pd.DataFrame.from_records(trainingLists, columns=headers)

        #print(trainingDF)


        # Calculate most frequent class, set global instead of passing mostFrequentClassOverall or full dataset around to ever function
        #Priyanka comment = I break down the df into a smaller one where the class is 1 then 
        # go from there
        class1trainingDF = trainingDF.loc[trainingDF['class'] == '1']
        totalProbOfClass1 = len(class1trainingDF.index)/len(trainingDF)
        print(totalProbOfClass1)
        print ("P(C=1)=%.2f"%totalProbOfClass1, end='')
        for attribute in headers:
            if attribute.lower() == "class":
                continue
            else:
                attribute1GivenClass1 = class1trainingDF.loc[class1trainingDF[attribute] == '1']
                probOfAttribute1GivenClass1 = len(attribute1GivenClass1.index)/len(class1trainingDF)
                probOfAttribute0GivenClass1 = 1 - probOfAttribute1GivenClass1
                print (' P(', attribute, '=1|C=1)=%.2f'%probOfAttribute1GivenClass1, end='')
                #storing things into dictionary because we're going to need it in the classification
                dictsOfProbsForClass1.append({"attribute": attribute, "class" : '1', "probability" :probOfAttribute1GivenClass1})
                print (' P(', attribute, '=0|C=1)=%.2f'%probOfAttribute0GivenClass1, end='')
                dictsOfProbsForClass1.append({"attribute": attribute, "class": '0', "probability": probOfAttribute0GivenClass1})
        print()
        print ()

        class0trainingDF = trainingDF.loc[trainingDF['class'] == '0']
        totalProbOfClass0 = len(class0trainingDF.index) / len(trainingDF)
        print(totalProbOfClass0)
        print("P(C=0)=%.2f" % totalProbOfClass0, end='')
        for attribute in headers:
            if attribute.lower() == "class":
                continue
            else:
                attribute1GivenClass0 = class0trainingDF.loc[class0trainingDF[attribute] == '1']
                probOfAttribute1GivenClass0 = len(attribute1GivenClass0.index) / len(class0trainingDF)
                probOfAttribute0GivenClass0 = 1 - probOfAttribute1GivenClass0
                print(' P(', attribute, '=1|C=0)=%.2f' % probOfAttribute1GivenClass0, end='')
                dictsOfProbsForClass0.append({"attribute" : attribute, "class": '1', "probability" : probOfAttribute1GivenClass0})
                print(' P(', attribute, '=0|C=0)=%.2f' % probOfAttribute0GivenClass0, end='')
                dictsOfProbsForClass0.append({"attribute": attribute, "class": '0', "probability": probOfAttribute1GivenClass0})

        print()



        # total = 0
        # for each in trainingDF:
        #     total += int(each[headers.index("class")])
        # global mostFrequentClassOverall
        # mostFrequentClassOverall \
        #     = round(total / len(trainingDF))


        # Where the magic happens
        

        # Accuracy on training set
        # trainingAccuracy = getAccuracy(headNode, trainingDF)
        # print("Accuracy on training set (" + str(len(trainingDF)) + "): " + "{0:.1f}".format(trainingAccuracy) + "%")

        # Parse Test data
        testLists = []
        for line in testFile:
            testLists.append(line.strip().replace('\t', ''))
        testLists.pop(0)  # Remove headers

        # Convert test data into a pandas dataframe
        testDF = pd.DataFrame.from_records(testLists, columns=headers)

        #print(testDF)

        # Accuracy on test set
        # testAccuracy = getAccuracy(headNode, testLists)
        # print("Accuracy on test set (" + str(len(testLists)) + "): " + "{0:.1f}".format(testAccuracy) + "%")
        probOfClassifying1(trainingDF)

###NOT COMPLETED###
#I'm so sleepy!
def probOfClassifying1(trainingDF):
    multiplyingTotal = 1
    for row in trainingDF:
        for each in trainingDF.columns.values.tolist(): #getting each argument
            if each.lower() == 'class':
                continue






if __name__ == "__main__":
    main()


