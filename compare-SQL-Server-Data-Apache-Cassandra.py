# pass files as arguments to the command
import datacompy
import pandas as pd
import sys
import os

ip_args = sys.argv[1:]
# Declare the two data frame variables
df1 = pd.read_csv(ip_args[0], low_memory=False)
df2 = pd.read_csv(ip_args[1], low_memory=False)


# Perform Compare
compare = datacompy.Compare(
    df1,
    df2,
    join_columns=["contact_number", "country_code"],
    abs_tol=0,  # Optional, defaults to 0
    rel_tol=0,  # Optional, defaults to 0
    df1_name="SQL",  # Optional, defaults to 'df1'
    df2_name="DSE",  # Optional, defaults to 'df2'
)
# Write teport to file
filepath = os.path.join(
    "/data01/compares","reportname.report",
)
if not os.path.exists("/data01/compares"):
    os.makedirs("/data01/compares")
f = open(filepath, "a")
f.truncate(0)
f.write(compare.report(sample_count=1000))
# print(compare.report())
