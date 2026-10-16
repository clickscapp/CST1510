"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  :  Cyber
Date  : 15/10/2026

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

def check_record(failed_logins,total_attempts):
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

# ====================================================================== STORE
records = [
    {"source_IP": "133.33.43", "failed_logins": 35, "total_attempts": 200},
    {"source_IP": "100.4.33", "failed_logins": 50, "total_attempts": 30},
    {"source_IP": "10.1.1.0.1", "failed_logins": 89, "total_attempts": 80},
    {"source_IP": "21.0.3.21", "failed_logins": 92, "total_attempts": 100}
] 
#i tried to get the excellent but i could not get it to work.
# =============================================================== PROCESS + OUTPUT
over_attempts = 0

for r in records:
    """Checks the data and login status and tracks the over limit count"""
    source_IP = r["source_IP"]
    failed_logins = r["failed_logins"]
    total_attempts = r["total_attempts"]

    difference, percent = check_record(failed_logins, total_attempts)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_attempts +=1

    print_report(source_IP, failed_logins, total_attempts, difference, percent, status)
print(f"Over Limit        : {over_attempts:>10}")
# ==========================================================================
