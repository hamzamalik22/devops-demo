#!/bin/bash

echo "📅 Current Date : $(date)"
sleep 2

echo -e "\n📂 Current Working Directory:"
pwd
sleep 2

echo -e "\n📄 Files and Folders:"
ls
sleep 2

count=$(ls | wc -l)
echo -e "\n📊 Total items: $count"

