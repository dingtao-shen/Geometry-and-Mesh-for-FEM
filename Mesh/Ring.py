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

l = 0.1
L = 0.5

for s in range(1, 11):
    N1 = 5 * s
    N2 = 5 * N1

    CrvNdsIn = []
    for n in range(N1):
        CrvNdsIn.append([l * np.cos(- n * 2 * np.pi / N1), l * np.sin(- n * 2 * np.pi / N1)])
    CrvNdsIn.append([l , 0.0])

    CrvNdsOut = []
    for n in range(N2):
        CrvNdsOut.append([L * np.cos(- n * 2 * np.pi / N2), L * np.sin(- n * 2 * np.pi / N2)])
    CrvNdsOut.append([L , 0.0])

    msh = "ASCIIV4/Ring/RingMesh_" + str(N1) + "_" + str(N2) + ".msh"
    gmsh.initialize()
    gmsh.model.add(msh)

    # the interior boundary
    lc = 2 * np.pi * l / N1 # mesh size
    inner_pt = []
    for i in range(N1):
        gmsh.model.geo.addPoint(CrvNdsIn[i][0], CrvNdsIn[i][1], 0, lc, i+1)
        inner_pt.append(i + 1)

    inner_crv = []
    for i in range(N1 - 1):
        gmsh.model.geo.addLine(i + 1, i + 2, i + 1)
        inner_crv.append(i+1)
    gmsh.model.geo.addLine(N1, 1, N1)
    inner_crv.append(N1)

    gmsh.model.geo.addCurveLoop(inner_crv, 1)
    gmsh.model.addPhysicalGroup(1, inner_crv, name = "Interior boundary")

    # the exterior boundary
    LC = 2 * np.pi * L / N2 # mesh size
    ex_pt = []
    for i in range(N2):
        gmsh.model.geo.addPoint(CrvNdsOut[i][0], CrvNdsOut[i][1], 0, LC, i + 1 + N1)
        ex_pt.append(i + 1 + N1)

    ex_crv = []
    for i in range(N2 - 1):
        gmsh.model.geo.addLine(i + 1 + N1, i + 2 + N1, i + 1 + N1)
        ex_crv.append(i + 1 + N1)
    gmsh.model.geo.addLine(N2 + N1, N1 + 1, N2 + N1)
    ex_crv.append(N2 + N1)

    gmsh.model.geo.addCurveLoop(ex_crv, 2)
    gmsh.model.addPhysicalGroup(1, ex_crv, name = "Exterior boundary")

    gmsh.model.geo.addPlaneSurface([1,2], 1)
    gmsh.model.addPhysicalGroup(2, [1], name = "2D Domain")

    gmsh.model.geo.synchronize()
    #     gmsh.model.mesh.set_size(gmsh.model.getEntities(0), lc)
    gmsh.model.mesh.generate(2)

    gmsh.write(msh)

    gmsh.fltk.run()
    gmsh.finalize()

    InnerBdNds = []
    nbs = "mesh/Ring/NURBSGRID_" + str(N1) + "_" + str(N2) + ".dat"
    for i in range(N1 - 1):
        InnerBdNds.append([i + 1, i + 2, i / N1, (i + 1) / N1])
    InnerBdNds.append([N1, 1,  (N1 - 1) / N1, N1 / N1])

    with open(nbs, 'a') as f:
        f.write('$NURBSGRID_1 \n')
        f.write(str(N1) + '\n')
        for row in InnerBdNds:
            line = '{} {} {:.16f} {:.16f}\n'.format(int(row[0]), int(row[1]), float(row[2]), float(row[3]))
            f.write(line)
        f.write('$ENDNURBSGRID_1 \n')

    ExBdNds = []
    ExBdNds.append([N1 + 1, N1 + N2,  (N2 - N2) / N2, (N2 - N2 + 1) / N2])
    for i in range(N2 - 1, 0, -1):
        ExBdNds.append([i + N1 + 1, i + N1, (N2 - i) / N2, (N2 - i + 1) / N2])

    with open(nbs, 'a') as f:
        f.write('$NURBSGRID_2 \n')
        f.write(str(N2) + '\n')
        for row in ExBdNds:
            line = '{} {} {:.16f} {:.16f}\n'.format(int(row[0]), int(row[1]), float(row[2]), float(row[3]))
            f.write(line)
        f.write('$ENDNURBSGRID_2 \n')