#!/bin/bash
FILES=$(ls | grep csv)
for f in $FILES
  do
     echo "Transforming $f"
     t=$(echo $f | tr -d ".csv" | tr -d "-")
     csvsql -i postgresql $f >> ../create.sql
     csvsql --db postgresql:///causa --table $t --insert $f
 done
