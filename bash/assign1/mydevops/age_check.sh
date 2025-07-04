read -p 'Enter Your Age: ' age
if [[ $age -ge 18 ]]; then
	echo "Eligible to Vote."
elif [[ $age -lt 18 && $age -ge 13 ]]; then
	echo  "Teenager not allowed"
else
	echo "Child, not eligible"
fi

