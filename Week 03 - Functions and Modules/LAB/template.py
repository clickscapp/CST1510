"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  : Cyber
Date  : 08/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent):
    """The if statement checks if the percents within the sizes mentioned and gives an appropriate message."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(failed_logins,total_attempts):
    """Defining and doing the calculations for difference and percent and then storing it. """
    difference = total_attempts - failed_logins
    percent = (failed_logins/total_attempts) * 100
    return difference, percent

def print_report(source_IP, failed_logins, total_attempts, difference, percent, status):
    """Takes all variables and outputs them in a specific format with borders and f string formatting."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_IP}")
    print("=" * 34)

    print(f"Failed Logins     : {failed_logins:>10.2f}")
    print(f"Total Attempts    : {total_attempts:>10.2f}")
    print(f"Difference        : {difference:>+10.2f}")
    print(f"Percent           : {percent:>10.2f}%")
    print(f"Status            : {status:>10}")
    print("=" * 34)

# ==================================================================== INPUT
over_attempts = 0
while True:

    source_IP = input("Source IP:")
    """All the information, label value and limit, are being put into inputs so users can add them. If they type quit it ends."""
    if source_IP =="quit":
            break
    failed_logins = float(input("Failed Logins:"))
    total_attempts = float(input("Total Attempts:"))
    
    # ================================================================== PROCESS
    difference, percent = check(failed_logins, total_attempts)   
    """The difference, percent and status is being grabbed from the status_of(percent) and check(failed_login, total_attempts)
    calculations i did above so it doesnt need to be redone.)"""
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_attempts += 1

# =================================================================== OUTPUT
    print_report(source_IP, failed_logins, total_attempts, difference, percent, status)
    """Calls the function to print the final report and prints how many of the login attempts were over the limit.."""
    print(f"Attempts over the limit: {over_attempts}")

# ==========================================================================
