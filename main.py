import sys
import os
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import animation

from PyQt5.QtWidgets import *


class Ui(QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)

        self.setWindowTitle("Z-Slice Visualizer")

        # intialize embedded matplotlib object
        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        # create layout objects for the whole window and the button interface
        windowLayout = QVBoxLayout()
        inputLayout = QHBoxLayout()

        # create interface elements and link them to click events
        self.pushButtonLoadData = QPushButton('Load Data')
        self.pushButtonLoadData.clicked.connect(self.on_pushButtonLoadData_clicked)

        self.pushButtonPrevious = QPushButton('Previous Slice')
        self.pushButtonPrevious.clicked.connect(self.on_pushButtonPrevious_clicked)

        self.pushButtonNext = QPushButton('Next Slice')
        self.pushButtonNext.clicked.connect(self.on_pushButtonNext_clicked)

        self.pushButtonSave = QPushButton('Save Figures')
        self.pushButtonSave.clicked.connect(self.on_pushButtonSave_clicked)

        self.label = QLabel("Current Slice: ")

        self.textEditSliceIndex = QLineEdit('')

        # add interface elements to input layout
        inputLayout.addWidget(self.pushButtonLoadData)
        inputLayout.addWidget(self.label)
        inputLayout.addWidget(self.textEditSliceIndex)
        inputLayout.addWidget(self.pushButtonPrevious)
        inputLayout.addWidget(self.pushButtonNext)
        inputLayout.addWidget(self.pushButtonSave)

        # add sublayouts to window
        windowLayout.addWidget(self.canvas)
        windowLayout.addLayout(inputLayout)

        # make navigation buttons inaccessible until data is loaded
        self.textEditSliceIndex.setReadOnly(False)
        self.pushButtonPrevious.setEnabled(False)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonSave.setEnabled(False)

        # save layout changes
        self.setLayout(windowLayout)

    def on_pushButtonLoadData_clicked(self):
        # let user select directory where Z-slice data is located
        self.projectDirectory = QFileDialog.getExistingDirectory(self, 'Select a folder containing Z-Slice text files')

        # don't crash the program if the user fails to pick a folder
        if not self.projectDirectory:
            return

        # get information about number of files and their names
        self.ZFiles = os.listdir(self.projectDirectory)
        self.index = 1
        self.numFiles = len(self.ZFiles)

        # make directory to store z-slice image representations
        if not os.path.exists(self.projectDirectory.replace('Z-Cases', 'Z-Case-Images/')):
            os.mkdir(self.projectDirectory.replace('Z-Cases', 'Z-Case-Images/'))

        # load in data from the first file and generate/display plot
        self.updatePlot()


        # Enable buttons now that data is loaded
        self.pushButtonPrevious.setEnabled(True)
        self.pushButtonNext.setEnabled(True)
        self.pushButtonSave.setEnabled(True)


    def on_pushButtonPrevious_clicked(self):
        # only update plot if index is not at minimum
        if self.index > 1:
            self.index -= 1
            self.updatePlot()
        else:
            print("Min value reached.")

    def on_pushButtonNext_clicked(self):
        # only update plot if index is not at maximum
        if self.index < self.numFiles:
            self.index += 1
            self.updatePlot()
        else:
            print("Max value reached.")

    def on_pushButtonSave_clicked(self):
        print("Feature has not yet been defined")

    # function that updates the plot, called initially and when previous/next buttons pressed
    def updatePlot(self):
        # get data from appropriate text file

        # get Z-Value for graph title
        ZValue = str(self.ZFiles[self.index - 1])
        ZValue = ZValue.replace('.txt', '')

        currentFilePath = str(self.projectDirectory) + '/' + str(self.ZFiles[self.index - 1])
        data = np.loadtxt(currentFilePath, delimiter='\t', skiprows=1)

        x = []
        y = []
        objective = []

        # sort data into arrays
        for i in range(len(data)):
            if data[i][2] != 1000000:
                x.append(data[i][0])
                y.append(data[i][1])
                objective.append(data[i][2])


        # clear existing figure and replace it with new slice data
        self.figure.clear()

        # initialize 2D scatter plot for data, with color mapping defined by objective function value
        plt.scatter(x, y, c=objective, vmin=0, vmax=1500)
        plt.colorbar()

        # set color map and title/labels
        plt.set_cmap('Spectral')
        plt.title("Z = " + ZValue)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.draw()

        print(self.projectDirectory.replace('Z-Cases', 'Z-Case-Images/') + ZValue + '_plot.txt')
        plt.savefig(self.projectDirectory.replace('Z-Cases', 'Z-Case-Images/') + ZValue + '_plot.png')

        self.canvas.draw()


        self.textEditSliceIndex.setText(str(self.index) + '/' + str(self.numFiles))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Ui()

    main.show()

    sys.exit(app.exec_())




