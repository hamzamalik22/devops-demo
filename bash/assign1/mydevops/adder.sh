if [[ $# -lt 2 ]]; then
	echo "Usage: $0 num1 num2"
	exit 1
fi
result=$(($1+$2))
echo "Result is $1 + $2 = $result."

pwd
