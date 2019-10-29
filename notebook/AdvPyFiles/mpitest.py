# -*- coding: utf-8 -*-
#
# Simple scatter-gather example using mpi4py
#
# $ mpirun -np 4 python ./mpiex.py
#

import numpy as np
from mpi4py import MPI
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [(i+1)**2 for i in range(size)]
else:
   data = None

print( 'Rank, Data as initialized: ', rank, data)
stdout.flush()

data = comm.scatter(data, root=0)
print('Rank, Data after scatter: ', rank, data)
stdout.flush()

data += 100
data = comm.gather(data, root=0)

print('Rank, Data after gather: ', rank, data)
stdout.flush()
