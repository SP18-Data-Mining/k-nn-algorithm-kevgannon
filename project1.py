# Kevin Gannon
import csv
import math

entryCount = 0
testData = []
trainingData = []

print("Test Data Entries:\n")

with open('fruit_data_with_colors.txt','r') as tsv:

	# Populate training test data and training data list.
	for line in tsv : 
		if entryCount % 5 == 0 :
			testData.append(line.strip().split('\t'))
		else :
			trainingData.append(line.strip().split('\t'))
		entryCount = entryCount + 1

for i in range(1,len(testData)):
	testWidth = float(testData[i][4])
	testHeight = float(testData[i][5])
	
	# Calculate the difference of the first two entries to work as the starting comparison for similarity (minDiff).
	minDiff = math.sqrt(((testWidth - float(trainingData[0][4]))**2) + ((testHeight - float(trainingData[0][5]))**2))
	similarEntryLabel = trainingData[0][0]
	similarEntryName = trainingData[0][1]
		
	# Compare width and height of current test entry with the remaining training entry's.
	for j in range(len(trainingData)):
		trainWidth = float(trainingData[j][4])
		trainHeight = float(trainingData[j][5])
	
		# Calculate difference by calculating the Euclidean difference (test - training) for two entries.
		diff = math.sqrt(((testWidth - trainWidth)**2) + ((testHeight - trainHeight)**2))
		
		if diff < minDiff:
			minDiff = diff
			similarEntryLabel = trainingData[j][0]
			similarEntryName = trainingData[j][1]
			
	print(str(testData[i]))
	print("This entry's label was predicted to be: " + str(similarEntryLabel) + " (" + similarEntryName + ")\n")


