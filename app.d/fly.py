import os
import os.path
import shutil

from deephaven import new_table, parquet
from deephaven.column import string_col, int_col
from deephaven.plot import Figure


def get_fly_info():
    return new_table([
        string_col("Name", [os.getenv("FLY_APP_NAME")]),
        string_col("Id", [os.getenv("FLY_ALLOC_ID")]),
        string_col("Region", [os.getenv("FLY_REGION")]),
        int_col("MemoryMB", [int(os.getenv("FLY_VM_MEMORY_MB"))]),
        int_col("CpuCount", [int(os.getenv("FLY_VCPU_COUNT"))]),
        string_col("PublicIP", [os.getenv("FLY_PUBLIC_IP")])
    ])


def get_spy_mid():
    if not os.path.exists('/data/dh-spy-mid.parquet'):
        # Copy from distributed filesystem to local filesystem
        shutil.copyfile('/mnt/deephaven/parquet/dh-spy-mid.parquet', '/data/dh-spy-mid.parquet')
    return parquet.read('/data/dh-spy-mid.parquet')


def get_spy_plot(spy_mid):
    return (Figure()
        .plot_xy(series_name="Spy Mid", t=spy_mid, x="Timestamp", y="Mid")
        .x_axis(label="Timestamp")
        .y_axis(label="Mid")
        .chart_title(title="Spy Mid")
        .show())


fly_info = get_fly_info()

spy_mid = get_spy_mid()

spy_plot = get_spy_plot(spy_mid)
