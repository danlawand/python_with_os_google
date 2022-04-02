#!/usr/bin/env python3
import psutil


# The function receives a time interval and returns the cpu usage percent in
# that interval

time_interval = 0.1
print(psutil.cpu_percent(time_interval))

