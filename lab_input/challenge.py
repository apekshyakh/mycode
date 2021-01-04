#!/usr/bin/python3
username = input("Please enter username:")
day_of_week = input("What day of week is it?")
print("Hello, " + username + "! Happy " + day_of_week + "!")

# PRINT OBJECTS
print("Hello ", user,"! Happy ",day,"!",sep="")
# CONCATENATION
print("Hello, " + user + "! Happy " + day + "!")
# MIX AND MATCH!
print("Hello", user +"!","Happy", day +"!")
# FORMAT
print("Hello {}! Happy {}!".format(user,day))
# F-STRING
print(f"Hello {user}! Happy {day}!")

