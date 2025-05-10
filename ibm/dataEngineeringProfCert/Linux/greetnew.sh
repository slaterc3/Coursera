#! /bin/bash 
# This script accepts the user\'s name and prints 
# a message greeting the user

# Print the prompt message on screen
echo -n "Enter your first name :"	  	

# Wait for user to enter a first and last name, and save the entered name into the variable \'name\'
read firstname				
echo -n "Enter your last name: "
read lastname
# Print the welcome message followed by the name	
echo "Welcome, $firstname $lastname"

# The following message should print on a single line. Hence the usage of \'-n\'
echo -n "Congratulations, $firstname $lastname! You just created and ran a shell script "
# echo "using Bash on IBM Skills Network"