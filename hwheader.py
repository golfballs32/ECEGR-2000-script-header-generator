#   Seattleu ECEGR-2000 homework header generator script  
#   Copyright (C) 2020 Lucas Efcavitch

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#########################################################################################################
# Seattleu ECEGR-2000 homework header generator script                                                  #
# Written by Lucas Efcavitch 2020                                                                       #
#                                                                                                       #
# Automatically prepends required header to a python script based on configuration below                #
#                                                                                                       #
# To use, navigate to working directory and call:                                                       #
# python hwheader (script to be edited) (assignment number) (assignment name)                           #
#                                                                                                       #
# IMPORTANT NOTE: edit config lines below with your information                                         #
#########################################################################################################


firstName = "Rudy"     #enter your first name
lastName = "Redhawk"   #enter your last name


import sys
from datetime import date

def main():
    
    argLen = len(sys.argv)  #check arguments passed by user
    if(argLen != 4):
        print("Invalid Arguments, please make arguments in the form of script assignment-number assignment-name")
        exit()
    
    script = str(sys.argv[1]) #assign arguments to variables, get date
    AS = str(sys.argv[2])
    AN = str(sys.argv[3])
    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    
    f = open(script, "r")   #ensure target script doesn't already have header
    if("# File Name: " in f.readline()):
        print("Header already in file")
        exit()
    f.seek(0)
    oldText = f.read()
    f.close()
    
    infile = open(script, "w") #write header to script
    infile.seek(0)
    infile.write("# File Name: " + lastName + "_" + firstName + "_AS" + AS + ".py\n")
    infile.write("# File Path:  /home/python/userName/" + lastName + "_" + firstName + "_AS" + AS + ".py\n")
    infile.write("# Run Command: sudo python3 /home/python/userName/" + lastName + "_" + firstName + "_AS" + AS + ".py\n")
    infile.write("\n")
    infile.write("# " + firstName + " " + lastName + "\n")
    infile.write("# Date " + d3 + "\n")
    infile.write("# AS." + AS + "\n")
    infile.write("# " + AN + "\n" + "\n")
    infile.write(oldText)
    infile.close()
    
    print("\n# File Name: " + lastName + "_" + firstName + "_AS" + AS + ".py")
    print("# File Path:  /home/python/userName/" + lastName + "_" + firstName + "_AS" + AS + ".py")
    print("# Run Command: sudo python3 /home/python/userName/" + lastName + "_" + firstName + "_AS" + AS + ".py\n")
    print("# " + firstName + " " + lastName)
    print("# Date " + d3)
    print("# AS." + AS)
    print("# " + AN)
    
    print("\nDone!")
    exit()

if __name__ == "__main__": #idk it doesn't work without this. try googling it
    main()
