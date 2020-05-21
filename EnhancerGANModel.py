import os

from model.srgan import generator as srgangenerator
from model import resolve_single

from model.WDSRFineTuned import wdsr_b

from PIL import Image
import numpy as np


class DeepLearningGANModels(object):
    
    def __init__(self, model, input_path):
        self.modelname = model
        self.input_path = input_path

    def load_image(self, path):
        return np.array(Image.open(path))[:,:,:3]

    def modelBash(self):
        if self.modelname == "srganx4" :
            return self.srganx4Process()
        elif self.modelname == "wdsr-b-finetunedx4" :
            return self.wdsr_b_finetuned()
        else :
            return None
    
    def wdsr_b_finetuned(self):
        weights_dir = 'model/weights/wdsr'
        wdsr_fine_tuned = wdsr_b(scale=4, num_res_blocks=32)
        wdsr_fine_tuned.load_weights(os.path.join(weights_dir, 'weights-wdsr-b-fine-tuned.h5'))

        lr = self.load_image(self.input_path)
        gan_wdsr_finetuned = resolve_single(wdsr_fine_tuned, lr)

        return gan_wdsr_finetuned

    def srganx4Process(self):
        weights_dir = 'model/weights/srgan'
        weights_file = lambda filename: os.path.join(weights_dir, filename)

        gan_generator = srgangenerator()
        gan_generator.load_weights(weights_file('gan_generator.h5'))

        lr = self.load_image(self.input_path)
        gan_sr = resolve_single(gan_generator, lr)

        return gan_sr