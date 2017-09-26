import math
import sys
import pandas as pd
import numpy as np

def main():
    if len(sys.argv) != 3:
        print ("Please execute with two arguments <train.dat> <test.dat>")
        exit()
    # Reading in data just reading in the training file (train.dat)
    with open(sys.argv[1]) as trainingFile, open(sys.argv[2]) as testFile:
        firstLine = trainingFile.readline()
        headers = firstLine.split()

        print(headers)

        trainingLists = []
        for line in trainingFile:
            trainingLists.append(list(line.strip().replace('\t', '')))

        # Convert training data into a pandas dataframe
        trainingDF = pd.DataFrame.from_records(trainingLists, columns=headers)

        print(trainingDF)

        # Calculate most frequent class, set global instead of passing mostFrequentClassOverall or full dataset around to ever function
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

        print(testDF)

        # Accuracy on test set
        # testAccuracy = getAccuracy(headNode, testLists)
        # print("Accuracy on test set (" + str(len(testLists)) + "): " + "{0:.1f}".format(testAccuracy) + "%")


if __name__ == "__main__":
    main()
