#!/bin/sh
proc src/app.pc code=ANSI_C
gcc -o out/app -lclntsh -I$ORACLE_HOME/sdk/include -L$ORACLE_HOME/ src/app.c
out/app
