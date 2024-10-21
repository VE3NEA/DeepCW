import os
import sys

for folder_name in ['data_generation', 'model', 'validation']:
    path = os.path.abspath(os.path.join(folder_name))
    os.makedirs(path, exist_ok=True)
    if path not in sys.path: sys.path.append(path)
