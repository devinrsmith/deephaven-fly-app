import os

from deephaven import new_table
from deephaven.column import string_col, int_col
from deephaven import csv
from deephaven import parquet


def get_fly_info():
    return new_table([
        string_col("Name", [os.getenv("FLY_APP_NAME")]),
        string_col("Id", [os.getenv("FLY_ALLOC_ID")]),
        string_col("Region", [os.getenv("FLY_REGION")]),
        int_col("MemoryMB", [int(os.getenv("FLY_VM_MEMORY_MB"))]),
        int_col("CpuCount", [int(os.getenv("FLY_VCPU_COUNT"))]),
        string_col("PublicIP", [os.getenv("FLY_PUBLIC_IP")])
    ])

fly_info = get_fly_info()

csv_pirate = csv.read("/mnt/deephaven/20081205_thepiratebay.csv")

parquet_100mm = parquet.read("/mnt/deephaven/parquet/100mm.parquet")
