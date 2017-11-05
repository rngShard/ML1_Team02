import csv
from sklearn import svm

#global lists
trainLabels = []
trainImages = []
testImages = []

#read train data csv file
with open('train.csv','r') as trainDataFile:
    trainDataReader = csv.reader(trainDataFile)
    for row in trainDataReader:
        trainLabels.append(row[0])
        # convert images to binary format (0,1) if the pixel has value != 0 it will be just 1 to simplfy classification
        #idea taken from this source : https://www.kaggle.com/archaeocharlie/a-beginner-s-approach-to-classification
        trainImages.append([1 if pixelValue != '0' else 0 for pixelValue in row[1:]])


#read test data, the same way as train data
with open ('test.csv','r') as testDataFile:
    testDataReader = csv.reader(testDataFile)
    for row in testDataReader:
        testImages.append([1 if pixelValue != '0' else 0 for pixelValue in row[0:] ])    

#delete the first element as its the file header not the data 
del trainLabels[0]
del trainImages[0]
del testImages[0]

# train SVM module with the exetracted train (labels, images)
svmClassifier = svm.SVC()
svmClassifier.fit(trainImages,trainLabels)

#run the classifier against the test data and get predicated labels
predictedLabels = svmClassifier.predict(testImages)

#write results to csv file
with open('output.csv', 'w') as outputDataFile:
    csvWriter = csv.DictWriter(outputDataFile, fieldnames = ['ImageId','Label'])
    csvWriter.writeheader()
    imageId = 1
    for label in predictedLabels:
        csvWriter.writerow({'ImageId' : imageId,'Label' : label})
        imageId += 1

