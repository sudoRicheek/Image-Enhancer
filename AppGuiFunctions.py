import cv2
import numpy as np

class GuiFunctions(object):

    def __init__(self):
        self.working_path = "processimage.jpg"
        self.path_to_file = ""

    def openFile(self, file_path, winwidth, winheight):
        self.path_to_file = file_path
        rawimg = cv2.imread(self.path_to_file, 1)

        ##Will change the logic below later, for now its been configured for square window shapes :P
        
        if rawimg.shape[1] >= rawimg.shape[0] :
            newx = winwidth
            newy = (rawimg.shape[0]/rawimg.shape[1])*winwidth
        else:
            newy = winheight
            newx = (rawimg.shape[1]/rawimg.shape[0])*winheight
        
        newdim = (int(newx), int(newy))

        resizedimg = cv2.resize(rawimg, newdim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(self.working_path, resizedimg)

    