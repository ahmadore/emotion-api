from . import config
from sklearn import svm
import numpy as np

__author__ = "Akas Antony"
__version__ = "1.0.0"
__maintainer__ = "Akas Antony"
__email__ = "antony.akas@gmail.com"

class_map = {
    0: 'ANGRY',
    1: 'HAPPY',
    2: 'EXCITED',
    3: 'SAD',
    4: 'FEAR',
    5: 'ANXIETY'
}

class Classify(object):
    def __init__(self):
        self.raw_data = np.load(config.assets_path+'training_data/data.npy')
        self.raw_target = np.load(config.assets_path+'training_data/target.npy')

    def extract(self):
        X,y = self.raw_data[:-3], self.raw_target[:-3]
        self.pulse_classify(X,y)

    def pulse_classify(self,X,y):
        clf = svm.SVC(gamma=0.001, C=100)
        clf.fit(X,y)
        inp_data = input("Enter the data to be classified in the format [pulse, age]")
        inp_data = inp_data.split()
        inp_data = list(map(int, inp_data))
        inp_data = np.array(inp_data).reshape(1, -1)
        _class = clf.predict(inp_data)[0]
        print("Class: " + class_map[_class])

    def pulse_classify_web(self, inp_data):
        X,y = self.raw_data[:-3], self.raw_target[:-3]
        clf = svm.SVC(gamma=0.001, C=100)
        clf.fit(X,y)
        inp_data = inp_data.split()
        inp_data = list(map(int, inp_data))
        inp_data = np.array(inp_data).reshape(1, -1)
        _class = clf.predict(inp_data)[0]
        return class_map[_class]