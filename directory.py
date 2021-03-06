# %%
"""
# Prepare Images in Directories for Classification
"""

# %%
"""
## Importing the Libraries
"""

# %%
import numpy as np
import pandas as pd
import os
import ipynb_py_convert
import shutil

# %%
"""
## Importing Data
"""

# %%
dataset = pd.read_csv('english.csv')
# we have path to image, category of image

# %%
dataset.head()

# %%
paths = dataset.iloc[:, 0].values
labels = dataset.iloc[:, 1].values

# %%
print(labels)

# %%
"""
## Creating directories
"""

# %%
# Creating base directory for images
os.makedirs("tmp", exist_ok=True)

# %%
classes_set = set(labels)
res = [char for char in classes_set if char.isupper()] 

# %%
"""
### Replacing Capitals with Letter_c
"""

# %%
capitals = []
for i in res:
    i = i + '_c'
    capitals.append(i)

# %%
y = [] 
for i in labels:
    if(i.isupper()):
        i = i + '_c'
    y.append(i)

# %%
classes_set = classes_set.difference(set(res))
classes_set = classes_set.union(set(capitals))
classes_set = sorted(classes_set)

# %%
"""
## Creating Image Directories
"""

# %%
parent_dir = 'tmp'
for i in classes_set:
    directory = i
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)

# %%
"""
## Moving images to new directory
"""

# %%
destination = "tmp"
source = "Img"

# %%
for i in range(0, len(paths)):
    
    shutil.copy(paths[i], destination + '/' + y[i])