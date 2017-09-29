import math
import sys
import pandas as pd
import numpy as np

mostFrequentClassOverall = -1
dictsOfProbsForClass1 = {}
dictsOfProbsForClass0 = {}

# python main.py train.dat test.dat

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
        dictsOfProbsForClass1["totalProbOfClass"] = totalProbOfClass1
        # print(totalProbOfClass1)
        print ("P(C=1)=%.2f"%totalProbOfClass1, end='')
        for attribute in headers:
            if attribute.lower() == "class":
                continue
            else:
                # Extract all rows with the specific attribute A == 1
                attribute1GivenClass1 = class1trainingDF.loc[class1trainingDF[attribute] == '1']
                # P(A | C) = #A&C / #C
                probOfAttribute1GivenClass1 = len(attribute1GivenClass1.index)/len(class1trainingDF)
                # P(A! | C) = 1 - P(A | C)
                probOfAttribute0GivenClass1 = 1 - probOfAttribute1GivenClass1
                print (' P(' +  str(attribute) + '=1|C=1)=%.2f'%probOfAttribute1GivenClass1, end='')
                #storing things into dictionary because we're going to need it in the classification
                dictsOfProbsForClass1[attribute + '1'] = probOfAttribute1GivenClass1
                print (' P(' + str(attribute) + '=0|C=1)=%.2f'%probOfAttribute0GivenClass1, end='')
                dictsOfProbsForClass1[attribute + '0'] = probOfAttribute0GivenClass1
        print()
        print()

        class0trainingDF = trainingDF.loc[trainingDF['class'] == '0']
        totalProbOfClass0 = len(class0trainingDF.index) / len(trainingDF)
        dictsOfProbsForClass0["totalProbOfClass"] = totalProbOfClass0
        # print(totalProbOfClass0)
        print("P(C=0)=%.2f" % totalProbOfClass0, end='')
        for attribute in headers:
            if attribute.lower() == "class":
                continue
            else:
                # Extract all rows with the specific attribute A == 0
                attribute1GivenClass0 = class0trainingDF.loc[class0trainingDF[attribute] == '1']
                # P(A | C!) = #A&C! / #C!
                probOfAttribute1GivenClass0 = len(attribute1GivenClass0.index) / len(class0trainingDF)
                # P(A! | C!) = 1 - P(A | C!)s
                probOfAttribute0GivenClass0 = 1 - probOfAttribute1GivenClass0
                print(' P(' + str(attribute) + '=1|C=0)=%.2f' % probOfAttribute1GivenClass0, end='')
                dictsOfProbsForClass0[attribute + '1'] = probOfAttribute1GivenClass0
                print(' P(' + str(attribute) + '=0|C=0)=%.2f' % probOfAttribute0GivenClass0, end='')
                dictsOfProbsForClass0[attribute + '0'] = probOfAttribute1GivenClass0
                
        print()
        print()

        # Accuracy on training set
        trainingAccuracy = accuracyOfClassifier(trainingDF, dictsOfProbsForClass0, dictsOfProbsForClass1)
        print("Accuracy on training set (" + str(len(trainingDF)) + " instances) : " + "{0:.1f}".format(trainingAccuracy) + "%")

        # Parse Test data
        testLists = []
        for line in testFile:
            testLists.append(line.strip().replace('\t', ''))
        testLists.pop(0)  # Remove headers

        # Convert test data into a pandas dataframe
        testDF = pd.DataFrame.from_records(testLists, columns=headers)

        #print(testDF)

        # print(dictsOfProbsForClass0)

        # Accuracy on test set
        testAccuracy = accuracyOfClassifier(testDF, dictsOfProbsForClass0, dictsOfProbsForClass1)
        print("Accuracy on test set (" + str(len(testDF)) + " instances) : " + "{0:.1f}".format(testAccuracy) + "%")

def accuracyOfClassifier(setDF, dictsOfProbsForClass0, dictsOfProbsForClass1):
    correct = 0
    for index, row in setDF.iterrows():
        probClass0 = probClass1 = 1
        for attribute in setDF.columns.values.tolist(): #getting each argument
            if attribute.lower() == 'class':
                continue
            # Multiply by the P(X|C)
            probClass0 *= dictsOfProbsForClass0[attribute + row[attribute]]
            probClass1 *= dictsOfProbsForClass1[attribute + row[attribute]]

        # Multiply by P(C)
        probClass0 *= dictsOfProbsForClass0["totalProbOfClass"]
        probClass1 *= dictsOfProbsForClass1["totalProbOfClass"]
        
        # Check for correctness
        estimatedClass = '0' if probClass0 > probClass1 else '1'
        if estimatedClass == row['class']:
            correct += 1

    return 100 * correct / len(setDF)





if __name__ == "__main__":
    main()


