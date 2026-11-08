"""
RECORD CHECK  -  my version
===========================

Name  : Ryan Crispen
Lane  : Cyber     
Date  : 04/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

from itertools import groupby
from operator import index

import pandas as pd
import matplotlib.pyplot as plt
# ==================================================================== LOAD
with open("cyber_data.csv", "w") as f:
    f.write("source_IP,failed_logins,total_attempts\n")
    f.write("100.4.2.4,100,100\n")
    f.write("33.5.100,190,200\n")
    f.write("40.122.50,3,40\n")
    f.write("100.2.3.4,80,240\n")
    f.write("44.2.4.6,230,400\n")

df = pd.read_csv("cyber_data.csv")

# ================================================================= PROCESS
df["percent"] = (df["failed_logins"]/df["total_attempts"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p>= 100 else "WARNING" if p >= 90 else "OK")

# ================================================================== OUTPUT
print(df)
print(df[(df["status"] == "OVER LIMIT") | (df["status"] == "WARNING")])
grouped = df.groupby("status")
print(grouped.size())

df.to_csv("placeholder.csv", index=False)

df["status"].value_counts().plot(kind="bar")
plt.title("Status Counts")
plt.savefig
plt.show()

# ==========================================================================

