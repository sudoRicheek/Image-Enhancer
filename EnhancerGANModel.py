import os

from model.srgan import generator as srgangenerator
from model import resolve_single
from utils import load_image


class DeepLearningGANModels(object):
    
    def __init__(self, model, input_path):
        self.modelname = model
        self.input_path = input_path

    def modelBash(self):
        if self.modelname == "srganx4" :
            return self.srganx4Process()
        else :
            return None

    def srganx4Process(self):
        weights_dir = 'weights/srgan'
        weights_file = lambda filename: os.path.join(weights_dir, filename)

        pre_generator = srgangenerator()
        gan_generator = srgangenerator()

        pre_generator.load_weights(weights_file('pre_generator.h5'))
        gan_generator.load_weights(weights_file('gan_generator.h5'))

        lr = load_image(self.input_path)
        gan_sr = resolve_single(gan_generator, lr)

        return gan_sr