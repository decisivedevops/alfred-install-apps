#!/usr/bin/env python3

import os
import glob
import json
import sys

# get the list of installable files in the download folder
dmg_files = glob.glob(os.path.expanduser('~/Downloads/*.dmg'))
archive_files = glob.glob(os.path.expanduser('~/Downloads/*.zip'))

installable_files = dmg_files + archive_files

alfred_results = []

for item in installable_files:
    result = {
        "title": item.split('/')[-1],
        "subtitle": item,
        "arg": item,
        "autocomplete": item,
        "icon": {
            "path": "./icon.png"
        }
    }

    alfred_results.append(result)

response = json.dumps({
    "items": alfred_results
})

sys.stdout.write(response)
