import os
from os.path import exists, join, basename, splitext
import time
import matplotlib
import matplotlib.pyplot as plt
import sys
from IPython.display import YouTubeVideo
import cv2
import torchvision
import cv2
import numpy as np
from types import SimpleNamespace

from tools.test import *

import torch
import torch.nn as nn
import torchvision.models as models
from torchvision import transforms

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from utils.config_helper import load_config
from models import SiamMask


sys.path.append(project_name)
sys.path.append(join(project_name, 'experiments', 'siammask_sharp'))
project_name='SiamMask'
plt.rcParams["axes.grid"] = False


