#!/bin/bash

# when submitted with qsub -Ix no PBS directives will be processed

# change to the directory from which the script was submitted
cd $PBS_O_WORKDIR

# do a token amount of work; note that the POP variable must have been set
# in the qsub arguments 
wc -l dat/$POP/$POP\_synth_people.txt
