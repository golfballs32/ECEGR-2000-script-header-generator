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
    
    argLen = len(sys.argv)
    if(argLen != 4):
        print("Invalid Arguments, please make arguments in the form of sctipt assignment-number assignment-name")
        exit()
    
    script = str(sys.argv[1])
    AS = str(sys.argv[2])
    AN = str(sys.argv[3])
    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    
    f = open(script, "r")
    oldText = f.read()
    f.close()
    
    infile = open(script, "w")
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
    print("Done!")
    exit()

if __name__ == "__main__":
    main()
