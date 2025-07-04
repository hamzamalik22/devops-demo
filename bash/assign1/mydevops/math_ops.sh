multiply() {
	result=$(($1*$2))
	echo $result
}

read -p "Enter Two Numbers : " s1 s2

answer=$(multiply $s1 $s2)

echo "Result is : $answer!"

