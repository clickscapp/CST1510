"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  : Cyber     
Date  : 07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
with open("cyber_records.txt", "w") as f:
    f.write("src=10.4.32.3,attempts=70,result=failed\n")
    f.write("src=23.1.3,attempts=2,result=success\n")
    f.write("src=145.1.1,attempts=150,result=failed\n")
    f.write("src=55.12.5.7,attempts=44, result=failed\n")
    f.write("src=34.21.5,attempts=30,result=success\n")


def parse_line(raw_line):
    """Parses the raw server string into dictionary using hostname used and total values."""
    cleaned_line = raw_line.strip().lower()

    fields = {}
    for piece in cleaned_line.split(","):
        key, value = piece.split("=")
        key = key.strip()
        value = value.strip()

        if key == "attempts":
            fields[key] = int(value)
        else:
            fields[key] = value

    return fields

def status_of(record):
    """Assigns a status based on the number of attempts in the record."""
    return "OVER LIMIT" if record["attempts"] >= 100 else "WARNING" if record["attempts"] >= 90 else "OK"
# ====================================================================== INPUT
raw_records = [] 
with open("cyber_records.txt") as f:
    for line in f:
        raw_records.append(line)

# =============================================================== PROCESS + OUTPUT
total_records = 0
flagged_records = 0

for raw_record in raw_records:
    clean_dict = parse_line(raw_record)
    status = status_of(clean_dict) 

    print(f"{clean_dict} Status: {status}")

    total_records +=1
    if status == "FLAGGED":
       flagged_records +=1

print(f"Summary: {total_records} records, {flagged_records} flagged.")


# ==========================================================================

