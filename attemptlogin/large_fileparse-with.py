#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successlogin = 0
hackerz = []
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            #the .split() method takes a string and splits it apart into elements in a list
            #the " " argument says that it should split the string wherever there is a whitespace
            # [-1] would then take the last element in that list ... which would be the IP address
            hackerz.append(line.split(" ")[-1].rstrip("\n"))
    
        elif "-] Authorization failed" in line:
            successlogin += 1

print("The number of failed log in attempts is", loginfail)
print(hackerz)
print("The number of successful log in attempts is", successlogin)

