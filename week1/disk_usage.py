#!/usr/bin/env python3
import shutil

du = shutil.disk_usage("/")

print(du)

free_disk_percent = du.free/du.total*100

print(free_disk_percent)

