#!/bin/bash

echo "🧮 Welcome to The Calculator!"

# Check if 3 arguments are given
if [[ $# -lt 3 ]]; then
    echo "Usage : $0 num1 operator num2"
    echo "Example: $0 2 + 3"
    exit 1
fi

# Get arguments
num1=$1
op=$2
num2=$3
result=0

# Perform calculation
if [[ "$op" == "+" ]]; then
    result=$((num1 + num2))
elif [[ "$op" == "-" ]]; then
    result=$((num1 - num2))
elif [[ "$op" == "*" ]]; then
    result=$((num1 * num2))
elif [[ "$op" == "/" ]]; then
    if [[ "$num2" -eq 0 ]]; then
        echo "❌ Cannot divide by zero"
        exit 1
    fi
    result=$((num1 / num2))
else
    echo "❌ Invalid operator: $op"
    echo "Use only +, -, *, /"
    exit 1
fi

# Output result
echo "✅ Result: $num1 $op $num2 = $result"

