#!/bin/bash

# This checks if the number of arguments is correct
# If the number of arguments is incorrect ( $# != 2) print error message and exit
if [[ $# != 2 ]]
then
  echo "backup.sh target_directory_name destination_directory_name"
  exit
fi

# This checks if argument 1 and argument 2 are valid directory paths
if [[ ! -d $1 ]] || [[ ! -d $2 ]]
then
  echo "Invalid directory path provided"
  exit
fi

# [TASK 1]
targetDirectory=$1
destinationDirectory=$2

# [TASK 2]
echo "Target directory -> $targetDirectory"
echo "Destination directory -> $destinationDirectory"

# [TASK 3]
currentTS=$(date +%Y-%m-%d-%H-%M-%S)

# [TASK 4]
backupFileName="backup-$currentTS.tar.gz"

# We're going to:
  # 1: Go into the target directory
  # 2: Create the backup file
  # 3: Move the backup file to the destination directory

# To make things easier, we will define some useful variables...

# [TASK 5]
origAbsPath=$(pwd)

# [TASK 6]
cd "$destinationDirectory" # <-
destDirAbsPath=$(pwd)
cd "$origAbsPath"

# [TASK 7]
cd "$targetDirectory" # <-


# [TASK 8]
yesterdayTS=$(date -d "24 hours ago" +%s)

declare -a toBackup

for file in  * # [TASK 9]
do
  # [TASK 10]
  if [[ -f $file ]] # checks if it is a regular file
  then 
    fileModTime=$(date -r "$file" +%s)
    # [TASK 11]
    if (( fileModTime > yesterdayTS ))
    then 
        echo "Adding '$file' to backup list."
        toBackup+=("$file")
    fi 
  fi
done

# [TASK 12]
echo "Creating '$backupFileName'..."
tar -czf "$backupFileName" "${toBackup[@]}"
# [TASK 13]

# Congratulations! You completed the final project for this course!
echo "Moving backup to destination folder"
mv "$backupFileName" "$destinationDirectory"