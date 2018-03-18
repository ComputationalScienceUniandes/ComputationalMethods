#!/bin/bash
# ------------------------------------------------------------------
# Title			timer.sh
# Description	Used to compare a C program with bash and python versions.
# Author		Juan David Lizarazo
# Creation Date	Jun 2, 2015
# ------------------------------------------------------------------

starttime=$(date "+%s")
./$1 > theintegers
endtime=$(date "+%s")
timetaken=$(( endtime - starttime ))
echo "Time taken: $timetaken s"