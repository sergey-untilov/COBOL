#!/bin/sh
gcc -c -Wall -Werror -fPIC src/shared.c  
gcc -shared -o out/libshared.so shared.o

cobc -x -o out/app -O src/app.cbl out/libshared.so

if ls *.o 1> /dev/null 2>&1; then
    rm *.o
fi

./out/app Shared print works from COBOL module. > out/result.txt
echo 'See out/result.txt'
head ./out/result.txt
