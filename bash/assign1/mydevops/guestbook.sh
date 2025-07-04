logfile="log.txt"
read -p "Enter Your Name: " name
echo "$name : $(date)" >> $logfile
echo "Logged Successfully"
cat $logfile
