#!/usr/bin/env bash

for FILE in validate_exhaustive_radon_sub.sh.o*;
do
    #echo `grep 'Best group structure:' $(file)`
    grep 'Best group structure:' ./$FILE
done


# Reference: Regular Expressions for file name matching
# http://stackoverflow.com/questions/4307770/regular-expressions-for-file-name-matching