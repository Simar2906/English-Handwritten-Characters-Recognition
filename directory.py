# %%
"""
## Importing the Libraries
"""

# %%
import numpy as np
import pandas as pd
import os
import ipynb_py_convert

# %%
"""
## Importing Data
"""

# %%
dataset = pd.read_csv('english.csv')
# we have path to iamge, category of image

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
#path = os.path.join(parent_dir, directory) 
os.makedirs("tmp", exist_ok=True)

# %%
classes_set = set(labels)
#classes_set = sorted(classes_set)
print(type(classes_set))

# %%
res = [char for char in classes_set if char.isupper()] 

# %%
print(res)

# %%
capitals = []
for i in res:
    i = i + '_c'
    capitals.append(i)

# %%
print(capitals)

# %%
classes_set = classes_set.difference(set(res))

# %%
classes_set = classes_set.union(set(capitals))

# %%
classes_set = sorted(classes_set)
print(classes_set)

# %%
parent_dir = 'tmp'
for i in classes_set:
    directory = i
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)