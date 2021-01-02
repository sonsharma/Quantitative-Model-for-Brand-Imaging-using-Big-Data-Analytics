#!/bin/bash
source /etc/profile.d/modules.sh
module purge
module load python/gnu/3.6.5
python $*