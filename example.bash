#!/bin/bash

# when submitted with qsub -Ix no PBS directives will be processed


# do a token amount of work; note that the POP variable must have been set
# in the qsub arguments 
wc -l $POP
