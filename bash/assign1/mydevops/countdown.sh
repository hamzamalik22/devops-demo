read -p "Enter your number: " countdown
stop=0
while [[ $stop -ne $countdown ]]; do
	echo "$countdown"
	((countdown--))
done
