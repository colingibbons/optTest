import sys
import os
import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from mpl_toolkits import mplot3d

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

        self.pushButtonCustom = QPushButton('Custom Slice')
        self.pushButtonCustom.clicked.connect(self.on_pushButtonCustom_clicked)

        self.label = QLabel("Current Slice: ")

        self.textEditSliceIndex = QLineEdit('')

        # add interface elements to input layout
        inputLayout.addWidget(self.pushButtonLoadData)
        inputLayout.addWidget(self.label)
        inputLayout.addWidget(self.textEditSliceIndex)
        inputLayout.addWidget(self.pushButtonPrevious)
        inputLayout.addWidget(self.pushButtonNext)
        inputLayout.addWidget(self.pushButtonCustom)

        # add sublayouts to window
        windowLayout.addWidget(self.canvas)
        windowLayout.addLayout(inputLayout)

        # make navigation buttons inaccessible until data is loaded
        self.textEditSliceIndex.setReadOnly(False)
        self.pushButtonPrevious.setEnabled(False)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonCustom.setEnabled(False)

        # save layout changes
        self.setLayout(windowLayout)

    def on_pushButtonLoadData_clicked(self):
        # let user select directory where Z-slice data is located
        self.projectDirectory = QFileDialog.getExistingDirectory(self, 'Select a folder containg Z-Slice text files')

        # don't crash the program if the user fails to pick a folder
        if not self.projectDirectory:
            return

        # get information about number of files and their names
        self.ZFiles = os.listdir(self.projectDirectory)
        self.index = 1
        self.numFiles = len(self.ZFiles)

        # load in data from the first file and generate/display plot
        self.updatePlot()

        # Enable buttons now that data is loaded
        self.pushButtonPrevious.setEnabled(True)
        self.pushButtonNext.setEnabled(True)
        self.pushButtonCustom.setEnabled(True)


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

    def on_pushButtonCustom_clicked(self):
        print("Feature has not yet been defined")

    # function that updates the plot, called for all buttons
    def updatePlot(self):
        # get data from appropriate text file
        currentFilePath = str(self.projectDirectory) + '/' + str(self.ZFiles[self.index - 1])
        data = np.loadtxt(currentFilePath, delimiter='\t', skiprows=1)

        # create arrays for each of the parameters
        x = []
        y = []
        objective = []

        # sort data into arrays
        for i in range(len(data)):
            x.append(data[i][0])
            y.append(data[i][1])
            objective.append(data[i][2])

        # clear existing figure and replace it with new slice data
        self.figure.clear()
        ax = plt.axes(projection='3d')
        ax.scatter3D(x, y, objective, c=objective, cmap='Reds')

        ax.set(xlabel='$X$', ylabel='$Y$', zlabel='$Objective Function$')

        self.canvas.draw()

        self.textEditSliceIndex.setText(str(self.index) + '/' + str(self.numFiles))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Ui()

    main.show()

    sys.exit(app.exec_())




