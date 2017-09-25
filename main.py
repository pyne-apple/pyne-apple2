import math
import sys

def main():
    if len(sys.argv) != 3:
        print ("Please enter two arguments <train.dat> <test.dat>")
        exit()
    # Reading in data just reading in the training file (train.dat)
    with open(sys.argv[1]) as trainingFile, open(sys.argv[2]) as testFile:
        first_line = trainingFile.readline()
        attributes = first_line.split()

        trainingData = []
        for line in trainingFile:
            trainingData.append(list(line.strip().replace('\t', '')))

        # print(trainingData)

        # Calculate most frequent class, set global instead of passing mostFrequentClassOverall or full dataset around to ever function
        total = 0
        for each in trainingData:
            total += int(each[attributes.index("class")])
        global mostFrequentClassOverall
        mostFrequentClassOverall \
            = round(total / len(trainingData))


        # Where the magic happens
        

        # Accuracy on training set
        # trainingAccuracy = getAccuracy(headNode, trainingData)
        # print("Accuracy on training set (" + str(len(trainingData)) + "): " + "{0:.1f}".format(trainingAccuracy) + "%")

        # Parse Test data
        testData = []
        for line in testFile:
            testData.append(line.strip().replace('\t', ''))
        testData.pop(0)  # Remove headers

        # Accuracy on test set
        # testAccuracy = getAccuracy(headNode, testData)
        # print("Accuracy on test set (" + str(len(testData)) + "): " + "{0:.1f}".format(testAccuracy) + "%")


if __name__ == "__main__":
    main()
