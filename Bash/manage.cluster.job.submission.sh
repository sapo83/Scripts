### max number of processes - may vary by user
number=480

task() {
  echo $1
  # actual code
}

while read -r line
do
  job_count=$( squeue | grep '<user_name>' | wc -l )
  while [ $job_count -gt $number ]
  do
    sleep 10 # checks job count every 10 seconds
    job_count=$( squeue | grep '<user_name' | wc -l )
  done
  task "$line"
done < list.of.files.txt
wait
