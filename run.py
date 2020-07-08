from AppWindowQt import Ui_MainWindow
import tensorflow as tf
import os

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

main_ui = Ui_MainWindow()
main_ui.execute()