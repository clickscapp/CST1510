"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  : Cyber 
Date  : 23/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
source_ip = input("source IP: ")
failed_logins = float(input("Failed Logins: "))
total_attempts = float(input("Total Attempts: "))
security_flags = int(failed_logins //5)
# ================================================================== PROCESS
difference = total_attempts - failed_logins
percent = (failed_logins/total_attempts) * 100

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)

print(f"Source IP         : {failed_logins:>10.2f}")
print(f"Failed Logins     : {total_attempts:>10.2f}")
print(f"Free              : {difference:>+10.2f}")
print(f"LoginFlags        : {security_flags:>10} ")
print(f"Percent           : {percent:>10.2f}%")
# The idea behind the login flags was to see every 5 login failures as a security risk and it gets flagged. 
# Its useful for an understanding of if someone is trying to access an account they arent allowed to or hack it.
# A high amount of flags requires further actions and it can help prevent any future attacks stop current ones.

print("=" * 34)

# ==========================================================================
