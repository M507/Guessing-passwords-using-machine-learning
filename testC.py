from sys import argv
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT
import Lib.Co as l1
import os


def streamTest(filename):
    isSignificant = 0.6  # try different values.
    # R = aT.fileClassification(filename, "svmModel", "svm")
    # print(R)

    # P: list of probabilities
    Result, P, classNames = aT.fileClassification(filename, "svmModel", "svm")
    winner = np.argmax(P)  # pick the result with the highest probability value.

    # is the highest value found above the isSignificant threshhold?
    if float(P[winner]) > isSignificant:
        print(classNames[winner],end='')
        #print("File: " + filename + " is in category: " + classNames[winner] + ", with probability: " + str(
            #float(P[winner])))
    else:
        print("Can't classify sound: " + str(P))


def main():
    cwd = os.getcwd()
    filename = cwd+'/sampleData/tobetested.wav'
    #filename = l1.s_input("Enter the a file name ")
    streamTest(filename)

if __name__ == '__main__':
    main()
