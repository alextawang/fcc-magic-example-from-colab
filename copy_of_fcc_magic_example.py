# -*- coding: utf-8 -*-
"""Copy of fcc-magic-example.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ta4mJHw4fegrpAPxNLHwpyV_TQU5piuH
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



"""### Dataset
Data are MC generated to simulate registration of high energy gamma particles in an atmospheric Cherenkov telescope

Dataset Characteristics
Multivariate

Subject Area
Physics and Chemistry

Associated Tasks
Classification

Feature Type
Real

# Instances
19020

# Features
10
"""

cols = ["fLength","fWidth","fSize","fConc","Concl","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]
df = pd.read_csv("magic04.data",names=cols)
df.head(-20)

df["class"]=(df["class"]=="g").astype(int)
df.head()
