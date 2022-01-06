import numpy as np
import matplotlib.pyplot as plt
import os

# hardcoded path to feature text files
directory = 'C:\\Users\\cogibbo\\Desktop\\us-mri-fusion-data\\phantomCases\\Feature Analysis\\'

# list of ultrasound planes by location and "true" Z-offset
caseDict = {
    '0cm': 101,
    '1cm': 89,
    '2cm': 77,
    '3cm': 65,
    '4cm': 53,
    '5cm': 41
}

# loop through each text file
for textFile in os.listdir(directory):

    path = f'{directory}{textFile}'
    file = open(path, 'r')
    # get the feature type and the ultrasound scan it corresponds with from the first line of the text file
    featureType, caseLabel = file.readline().split(', ')
    file.close()
    caseLabel = caseLabel.replace('\n', '')
    # load the numerical data into an array
    data = np.loadtxt(path, skiprows=2, delimiter=', ')

    # set up plot
    fig = plt.figure()
    plt.title(f'{featureType} vs. Z Value, {caseLabel}')
    plt.ylabel(f'Calculated {featureType} Value')
    plt.xlabel('Z Value')
    # plot correlation curves for each of the three tissue types
    plt.plot(data[:, 0], data[:, 1], c='red')
    plt.plot(data[:, 0], data[:, 2], c='green')
    plt.plot(data[:, 0], data[:, 3], c='purple')
    # add a vertical axis line corresponding with the "true" Z-location of this US plane relative to MRI model
    plt.axvline(x=caseDict[caseLabel])
    plt.show()

    print('stop')