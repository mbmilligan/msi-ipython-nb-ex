#!/bin/sh

module load python
qsub pbs_engines
ipcontroller --ip="*" 
