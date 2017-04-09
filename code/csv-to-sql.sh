#!/bin/bash
FILES=$(ls | grep csv)
for f in $FILES
  do
     echo "Transforming $f"
     csvsql $f >> ../create.sql
 done
