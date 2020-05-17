from pyAudioAnalysis import audioTrainTest as aT
import Lib.Co as l1


"""
Function1
"""
def fun1(dirname):
    subdirectories = l1.getSubs(dirname)
    if l1.answer("Are you sure you want to continue?"):
        pass
        aT.featureAndTrain(subdirectories, 0.198061, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False)

def main():
    pass
    #foldername = input("Enter the name of the training data folder : \n>")
    print("Make sure that trls"
          "aining data follows the standers written on www.changeme.com")
    foldername = 'MacBookProTrainingData'
    fun1(foldername)

if __name__ == '__main__':
    main()
