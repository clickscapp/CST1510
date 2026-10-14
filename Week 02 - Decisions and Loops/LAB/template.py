"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  : Cyber      
Date  : 3/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
over_attempts = 0
while True: 

    source_IP = input("Source IP:")    
    """This function gets the users source IP and if they type quit it breaks"""
    if source_IP == "quit":
            break 
    failed_logins = float(input("Failed Logins:"))     
    total_attempts = float(input("Total Attempts:")) 
        

# ================================================================== PROCESS
    difference = total_attempts - failed_logins   
    percent = (failed_logins/total_attempts) * 100       

    status = ""
    """This function assigns a message to percent when it falls in specific ranges"""
    if percent >= 100:
        status = ("OVER LIMIT") 
        over_attempts +=1
    elif percent >=90:
        status = ("WARNING")
    else:
        status = ("OK")

# =================================================================== OUTPUT
    print()
    """Prints the info in the above variables with borders and f string formatting"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_IP}")
    print("=" * 34)

    print(f"Failed Logins     : {failed_logins:>10.2f}")
    print(f"Total Attempts    : {total_attempts:>10.2f}")
    print(f"Difference        : {difference:>+10.2f}")
    print(f"Percent           : {percent:>10.2f}%")
    print(f"Status            : {status:>10}")
    print("=" * 34)

print(f"Attempts over the limit: {over_attempts}")
# ==========================================================================