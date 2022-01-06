import numpy as np
import matplotlib.pyplot as plt
import os

# hardcoded path to feature text files
directory = 'C:\\Users\\cogibbo\\Desktop\\us-mri-fusion-data\\phantomCases\\Feature Analysis\\'

# list of ultrasound planes by offset from base of phantom
caseList = ['0cm', '1cm', '2cm', '3cm', '4cm', '5cm']
# actual Z values corresponding with physically realistic probe alignment
actualValues = [101, 89, 77, 65, 53, 41]

# loop through each text file
for textFile in os.listdir(directory):

    path = f'{directory}{textFile}'
    data = np.loadtxt(path, skiprows=1, delimiter=', ')

    textFile = textFile.replace('.txt', '')

    fig = plt.figure()
    plt.title(f'Feature Correlation vs. Z Value, {textFile}')
    plt.ylabel('Calculated Feature Value')
    plt.xlabel('Z Value')
    plt.plot(data[:, 0], data[:, 1], c='red')
    plt.plot(data[:, 0], data[:, 2], c='green')
    plt.plot(data[:, 0], data[:, 3], c='purple')
    plt.axvline(x=89)
    plt.show()

    print('stop')