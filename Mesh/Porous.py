import numpy as np
from scipy.optimize import brentq
import geomdl
# Importing NURBS module
from geomdl import NURBS
# Importing visualization module
from geomdl.visualization import VisMPL as vis
# If there is an error saying: "AttributeError: module 'numpy' has no attribute 'float'.", we need to degrade numpy to 1.23.5
# conda install numpy==1.23.5
import gmsh

N = 4

r = np.sqrt(5) / 10
fp=[]
for i in range(N):
   fp.append([r * np.cos(i * 2 * np.pi / N), r * np.sin(i * 2 * np.pi / N), i / N]) 
fp.append([r , 0.0, 1.0]) 

lc = np.pi * 2.0 * r / N

idx = 1

gmsh.model.geo.addPoint(-1, -1, 0, lc, idx)
idx = idx + 1
gmsh.model.geo.addPoint(0.5 - r, -1, 0, lc, idx)
idx = idx + 1