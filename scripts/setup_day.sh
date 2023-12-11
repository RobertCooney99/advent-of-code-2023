#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <problem_number>"
  exit 1
fi

day=$(printf "%03d" "$1")
if [ "$day" -gt 25 ]; then
  echo "Day must be 25 or less."
  exit 1
fi

input_dir="inputs"
mkdir -p "$input_dir"

input_file="$input_dir/day${day}.txt"
if [ ! -e "$input_file" ]; then
  echo "This is input file for problem ${day}" > "$input_file"
  echo "Input file created: $input_file"
else
  echo "Input file already exists: $input_file"
fi

solutions_dir="solutions"
mkdir -p "$solutions_dir"

skeleton_code="from utils import input

input = input.text_to_string(\"$day\")

answer = 0

print(f\"Solution: {answer}\")"

solution_file_1="$solutions_dir/day${day}part001.py"
if [ ! -e "$solution_file_1" ]; then
  echo -e "$skeleton_code" > "$solution_file_1"
  echo "Solution file created: $solution_file_1"
else
  echo "Solution file already exists: $solution_file_1"
fi

solution_file_2="$solutions_dir/day${day}part002.py"
if [ ! -e "$solution_file_2" ]; then
  echo -e "$skeleton_code" > "$solution_file_2"
  echo "Solution file created: $solution_file_2"
else
  echo "Solution file already exists: $solution_file_2"
fi
