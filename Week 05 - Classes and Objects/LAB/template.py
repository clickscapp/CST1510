"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  :  Cyber
Date  : 24/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0

    def __init__(self, source_ip, failed_logins, total_attempts):
        """Saves the IP, failed logins and total attempts"""
        self.source_ip = source_ip
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts

    def percent(self):
        return (self.failed_logins / self.total_attempts) * 100

    def difference(self):
        return self.total_attempts - self.failed_logins

    def status(self):
        """Gives a message based on what range the value in calculation"""
        calculation = (self.failed_logins / self.total_attempts) * 100
        if calculation >= 100:
            return "OVER LIMIT"
        elif calculation >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
###i struggled here.

records = [
    Record("10.03.23", 44, 200),
    Record("213.21.55", 90, 100),
    Record("32.122.0.0", 10, 5)
]   

# ==================================================================== OUTPUT
over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.source_ip}")
    print("=" * 34)

    status_p = record.status()

    if status_p == "OVER LIMIT":
        over_limit_count +=1

    print(f"Failed Logins     : {record.failed_logins:>10.2f}")
    print(f"Total Attempts    : {record.total_attempts:>10.2f}")
    print(f"Difference        : {record.difference():>+10.2f}")
    print(f"Percent           : {record.percent():>10.2f}%")
    print(f"Status            : {status_p:>10}")

    print("=" * 34)
print(f"Over Limit        : {over_limit_count:>10.2f}")

# ==========================================================================

