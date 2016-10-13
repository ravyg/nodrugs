# nodrugs_demo
social networking data collection 

## To start colaborating:

1. Fork this repo your profile
2. do a `git clone` of your repo
3. `commit and push code` to your repo (fork of this repo)
4. create a `pull request` using github interface

### NOTE: Detailed instruction of each step above is provided by github documentation. Be creative.

### Use instructions at defaultauth.py for intialization.

## To set the collection keywords visit data/FILTER
- add one keyword per line as shown.
- Backup FILTER file for future reference.

## Set data folder path at main_stream.py if needed.
This folder "/data" is used to read FILTER and write tweets collected output per day in batchs.
Sample json output files are located in same folder as 2016-08-30-1.json etc.

## Import json to read file from your code as follows:
move collected files to be processed to folder tweets/raw

```

import json
import os

# Call each file and extract data.
tweet_text = ""
data = ""

for input_filename in os.listdir('tweets/raw'):
  if not input_filename.startswith('.'):
    dirpath = os.path.splitext(os.path.basename(input_filename))[0]
    for line in open("tweets/raw/" + '/' + input_filename,'r').readlines():

```