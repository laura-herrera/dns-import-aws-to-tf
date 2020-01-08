#!/bin/bash

input_file=$1

while IFS= read -r line
  do
    if ! [[ $line =~ ^# ]]; then
       $line
    fi
  done < $input_file
