"""
@author: peng

"""
import pandas as pd
import os
import numpy as np
import cv2
import archive.common_config as common_config

from PIL import Image
from StringIO import StringIO
from argparse import ArgumentParser

from pipelines.obj_det import ObjectDet
    
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--movie_name',
        type = str,
        help = 'which movie to process',
    )
    args = parser.parse_args()
    #----------------------------------------
    movie_name = args.movie_name
    module_name = 'archive.config_' + movie_name
    config = importlib.import_module(module_name, package=None)
    print module_name
    
    mode = {
        'output_final': True,
        'segment':{
                    'overwrite':False,
                    'id_st': 2000,
                    'id_ed': 4000
                    }
    }
    
    obj_det = ObjectDet(config, 'resnet')
    obj_det.process_video(mode)
    
    
    
