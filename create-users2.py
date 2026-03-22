#!/usr/bin/python3

# INET4031
# Mazin Ahmed
# 3/22/26 created
# 3/22/26 last modified

# Importing the 'os' module to allows Python to run Linux system commands 
# and the 'sys' module to handle input from the command line.
# re helps to find patterns like hashtags in the file
import os
import re
import sys

def main():
    # This asks the user at the very start if they want a dry-run or a real run
    mode = input("Would you like to run in dry-run mode? (Y to dry-run / N to run normally): ")

    for line in sys.stdin:

        # Looks for a hashtag at the very start of a line
        # it is used so the admin can comment out / skip certain users in the file
        match = re.match("^#",line)

        # removes the extra space and splits the line into pieces whenever it sees a colon
        fields = line.strip().split(':')

        # This checks if the line was marked to be skipped with a hashtag
        if match:
            # If the user chose Y, it prints a message saying the line was skipped
            if mode == 'Y' or mode == 'y':
                print("==> Skipping line marked with #: %s" % line.strip())
            continue

        # This checks if the line is missing any of the 5 data fields
        if len(fields) != 5:
            # If the user chose Y, it prints an error message
            if mode == 'Y' or mode == 'y':
                print("==> ERROR: Line does not have 5 fields: %s" % line.strip())
            continue

        # these lines pull the specific user info from the list and format the full
        # name exactly how the passwd file would expect to see it
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # this splits the group section by commas in a case that a user may belong
        # to more than one group
        groups = fields[4].split(',')

        # Account Creation Section
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        if mode == 'Y' or mode == 'y':
            print("DRY-RUN: Would run command -> %s" % cmd)
        else:
            print("==> Creating account for %s..." % (username))
            os.system(cmd)

        # Password Setup Section
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        if mode == 'Y' or mode == 'y':
            print("DRY-RUN: Would run command -> %s" % cmd)
        else:
            print("==> Setting the password for %s..." % (username))
            os.system(cmd)

        for group in groups:
            # This checks if the group field has a dash. If it does not, it adds the user to the listed group. 
            if group != '-':
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                if mode == 'Y' or mode == 'y':
                    print("DRY-RUN: Would run command -> %s" % cmd)
                else:
                    print("==> Assigning %s to the %s group..." % (username,group))
                    os.system(cmd)

if __name__ == '__main__':
    main()
