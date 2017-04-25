#!/bin/bash
FILES=$(ls | grep csv)
for f in $FILES
  do
     t=$(echo $f | sed "s/\.csv//" | tr -d "-" | tr -d "_")
     echo "Transforming $f into $t"
     # csvsql -i postgresql --tables $t $f >> ./create.sql
     csvsql --db postgresql:///causa_natura --table $t --insert $f
 done
