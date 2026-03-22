#!/usr/bin/python3

# INET4031
# Mazin Ahmed
# 3/22/26 created
# 3/22/26 last modified

#Importing the 'os' module to allows Python to run Linux system commands 
#and the 'sys' module to handle input from the command line.
#re helps to find patterns like hashtags in the file
import os
import re
import sys

def main():
    for line in sys.stdin:

        #Looks for a hashtag at the very start of a line
        #it is used so the admin can comment out / skip certain users in the file
        match = re.match("^#",line)

        #removes the extra space and splits the line into pieces whenever it sees
	#a colon
        fields = line.strip().split(':')

        #checks to see if the line was marked to be skipped with a hashtag or if 
        #it is missing any of the 5 data fields. If true, it skips the line.
        if match or len(fields) != 5:
            continue

        #these lines pull the specific user info from the list and format the full
	#name exactly how the passwd file woild expect to see it
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #this splits the group section by commas in a case that a user may belong
	#to more than one group
        groups = fields[4].split(',')

        #this tells the admin which account is being processed.
        print("==> Creating account for %s..." % (username))
        #This builds the Linux command to create the user account without a password initially.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #These lines print the command for the admin to see and then tell the operating system to actually run it to create the user.
        print(cmd)
        os.system(cmd)

        #this tells the admin that the password setup is starting
        print("==> Setting the password for %s..." % (username))
        #This builds a command that pushes the password into the passwd tool so it can be set automatically
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #These lines display the password command and then execute it on the system
	print(cmd)
        os.system(cmd)

        for group in groups:
            #This checks if the group field has a dash. If it does not, it adds the user 
            #to the listed group. 
	    #if there is a dash, it skips the group assignment.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
