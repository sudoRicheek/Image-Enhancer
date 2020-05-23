import cv2
import numpy as np
import shutil

from EnhancerGANModel import DeepLearningGANModels

class GuiFunctions(object):

    def __init__(self):
        self.working_path = "processimage/inputresizedimage.jpg"
        self.displayoutput = ""
        self.finaloutputpath = ""
        self.path_to_file = ""
        self.winwidth = 401
        self.winheight = 401
        self.imgrealwidth = 401
        self.imgrealheight = 401

    def openFile(self, file_path, winwidth, winheight):
        self.path_to_file = file_path
        self.winwidth = winwidth
        self.winheight = winheight
        self.imageFitter(file_path, self.working_path, self.winwidth, self.winheight)

    def saveFile(self, savepath):
        shutil.copy(self.finaloutputpath, savepath)
        
    def imageFitter(self, file_input_path, file_output_path, winwidth, winheight):
        rawimg = cv2.imread(file_input_path, 1)

        self.imgrealwidth = rawimg.shape[1]
        self.imgrealheight = rawimg.shape[0]
        ##Will change the logic below later, for now its been configured for square window shapes :P

        if rawimg.shape[1] >= rawimg.shape[0] :
            newx = winwidth
            newy = (rawimg.shape[0]/rawimg.shape[1])*winwidth
        else:
            newy = winheight
            newx = (rawimg.shape[1]/rawimg.shape[0])*winheight
        
        newdim = (int(newx), int(newy))

        resizedimg = cv2.resize(rawimg, newdim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(file_output_path, resizedimg)

    def superresUpscaler(self, model):
        self.finaloutputpath = "processimage/finalprocessedimage_" + model + ".jpg"
        self.displayoutput = "processimage/downscaled_finalprocessedimage_" + model + ".jpg"
        
        self.ganPredict = DeepLearningGANModels(model, self.path_to_file)
        model_img = self.ganPredict.modelBash()

        array_img = np.array(model_img).astype(np.float32)
        processed_model_img = cv2.cvtColor(array_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(self.finaloutputpath, processed_model_img)

        self.imageFitter(self.finaloutputpath, self.displayoutput, self.winwidth, self.winheight)

        if model_img is not None :
            return True
        else :
            return False