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
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
with open("cyber_records.txt", "w") as f:
    f.write("src=10.4.32.3,attempts=70,result=failed\n")
    f.write("src=23.1.3,attempts=2,result=success\n")
    f.write("src=145.1.1,attempts=150,result=failed\n")
    f.write("src=55.12.5.7,attempts=44, result=failed\n")
    f.write("src=34.21.5,attempts=30,result=success\n")


def parse_line(raw_line):
    """ """
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
    """ """
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
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
