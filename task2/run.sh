#!/bin/sh
proc src/pro_c.pc code=ANSI_C
gcc -o out/pro_c -lclntsh -I$ORACLE_HOME/sdk/include -L$ORACLE_HOME/ src/pro_c.c
out/pro_c
