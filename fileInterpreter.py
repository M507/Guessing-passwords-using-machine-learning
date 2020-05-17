"""
Add samples

This script takes a wav file that must have n peaks and create n different files for each peak.
"""

import numpy as np
from scipy.io.wavfile import read,write
import peakutils, os


# average
# 3169 / 2 = 1584.5
side = 10000

# The stander for the peaks
stander = 0

"""
Write the .wav file
"""
def exportFile(filename,rate,data):
    write(filename, rate, data)
    pass
    # try:
    #     write(filename, rate, data)
    # except:
    #     print("exportFile(filename,rate,data)")

"""
Get a peak by its index from a list
Return: a list (a peak)
"""
def getPeak(source,index,side):
    if side <= 10:
        return None
    try:
        leftSide = source[index - side :index]
        rightSide = source[index:index + side]
        #print(len(leftSide),len(rightSide))
        return leftSide + rightSide
    except:
        getPeak(source,index,side-10)


"""
This function takes a peak as an input and and gets it from the main list (audio)
"""
def fun1(source,rate,peaksList,filename):
    for peak in peaksList:
        # Every peak is [value,index]
        value = peak[0]
        index = peak[1]
        tmpList = getPeak(source,index,side)
        if type(tmpList) == np.ndarray:
            # save each peak
            filename = str(index)+filename
            exportFile(filename,rate,tmpList)
        else:
            print("Else fun1()")

"""
Import the audio
"""
def importFile(filenmae):
    print(filenmae)
    rate, raw = read(filenmae)
    data = np.array(raw, dtype=np.int16)
    return rate, raw, data

"""
Lambda 
"""
def takeOne(elem):
    return elem[0]

"""
filter the peaks next to each other
"""
def filter1(peaksList):
    # Sort list with key.
    # Explanation: Since the peaks that are near to each other usually are
    peaksListLength = len(peaksList)
    peaksList.sort(key=takeOne,reverse=True)
    i = 0
    # Filter the close peaks
    while ((i + 1) < peaksListLength):
        currentElement = peaksList[i]
        nextElement = peaksList[i+1]
        currentValue = currentElement[0]
        currentIndex = currentElement[1]
        nextValue = nextElement[0]
        nextIndex = nextElement[1]
        # If the difference is less than 1000 index
        if abs(currentIndex-nextIndex) < 10:
            # Remove the next one since it should be less than the value of the current
            # Because it's already sorted, duh!
            peaksList.remove(peaksList[i+1])
            peaksListLength -= 1
            break
        i += 1
    # Filter the short False positive peaks
    # TODO

    return peaksList

"""
inset the highest peaks in a list and checks for other conditions.
"""
def getTheHighestNPeaksHelper(value, index, peaksList, N):
    # If the list has less than the number of the peaks.
    # And if it is higher than the stander, which is a stander can be configured above.
    if len(peaksList) < N & value > stander:
        peaksList.append([value,index])
        return peaksList
    else:
        # If the list already has more than 10 peaks.
        # Then starts a comparison/filtration process using filter1()
        peaksList = filter1(peaksList)
        print(peaksList)

        # After the comparison/filtration function
        # Check if the current value is
        for element in peaksList:
            highestValue = element[0]
            highestValueIndex = element[1]
            if value > highestValue:
                peaksList.remove(element)
                peaksList.append([value,index])
                return peaksList
    return peaksList

"""
Get the highest peaks in a list
data: a list represents the audio.
N: the number if peaks.

Return: A list of [value,index]s
where, value is the number of how high is the peak in "data",
and index is the index of the value in "data".
"""
def getTheHighestNPeaks(data,N):
    peaksList = []
    length = len(data)
    index = 0
    while (index < length):
        value = data[index]
        peaksList = getTheHighestNPeaksHelper(value,index,peaksList,N)
        index += 1
    return peaksList

def print1():
    print("Menu")
    pass


"""
A debugging function, it shows the differences between the peaks as percentages.
"""
def debug1(peaksList,length):
    for e in peaksList:
        index = e[1]
        print(index * 100 / length)

"""
Using peakutils library
"""
def findpeaks(time_series,N):
    cb = time_series
    indexes = peakutils.indexes(cb, thres=0.02 / max(cb), min_dist=(int(len(time_series)/int(N))))
    sList=[]
    print(indexes)
    for i in indexes:
        sList.append([time_series[i],i])
        print(i)
    return sList


def derive(filePath,N):
    rate, raw, data = importFile(filePath)
    sList = findpeaks(data, N)
    debug1(sList, len(data))
    data = fun1(data, rate, sList, filePath)

"""
Main
"""
def main():

    print1()

    # Dynamic
    # filename = input("Enter the file name: \n>")
    # howManyPeaks = input("Enter how many peaks: \n>")

    # Static values are always better :)
    filename = 'ready1.wav'
    howManyPeaks = '4'


    cwd = os.getcwd()
    fullfilename = cwd + '/'+filename


    rate, raw, data = importFile(fullfilename)

    sList = findpeaks(data,howManyPeaks)
    # peaksList = getTheHighestNPeaks(data,int(howManyPeaks))
    # print(len(data))
    # print(peaksList)
    # test1(peaksList,len(data))
    debug1(sList, len(data))
    # data = fun1(data,rate,peaksList,filename)
    data = fun1(data, rate, sList, filename)

if __name__ == '__main__':
    main()
