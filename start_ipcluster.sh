#!/bin/sh

module load python
ipcontroller --ip="*" &
qsub pbs_engines