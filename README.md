# INET4031 Add Users Script and User List

## Program Description

This script automates the process of adding user accounts to a system. Instead of manually adding each user one at a time, this script reads information from a file and creates the users automatically. Adding these users manually would require the admin to run commands such as adduser to create a new user, passwd to set the password for each user, and adduser to assign users to groups. This script automates all those commands by taking in input from a file and running them automatically, saving time and effort.

## Program User Operation

This script reads from a file that contains the user information and processes it line by line. Any lines that are invalid or are marked with a '#' at the start are skipped, while the rest of the file gets processed. Each valid line will have an account created, a password set, and a specified group it will be assigned to.

### Input File Format

For a line to be valid in the input file, it needs to have exactly 5 fields that are separated by colons.

The format would look like: username:password:lastname:firstname:group1,group2

* Field 1 (username): The login name for the account
* Field 2 (password): The password for the account
* Field 3 (lastname): The user's last name
* Field 4 (firstname): The user's first name
* Field 5 (groups): A comma separated list of groups

If you want to skip a line in the input file, place a # at the start of the line you would like to skip and the script will ignore it.

If you don't want to add a user to any groups, place a - in the groups field.

## Command Execution

To make sure the script is executable, run: `chmod +x create-users.py`

Then run the script with: `sudo ./create-users.py < create-users.input`

## "Dry Run"

To test the script before actually creating any accounts, you can test it through doing a "dry run". To do this, open the script and edit it so that the os.system(cmd) lines are commented out and the print(cmd) lines are uncommented. There are 3 instances of these in the code. Close out of the script and run it. It will print out all the commands it would have run without actually executing those commands. This will allow you to test the script out and verify everything looks correct. Once you are ready to actually run the script, uncomment os.system(cmd) and run the script again.
