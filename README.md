# diffftp
Simple scripts to monitor/download added files, feel free to fork if you find it useful. 

Developed for my own use to download TV series =)

# Installation
    git clone https://github.com/liusiqi43/diffftp.git

# Usage
Rename settings_common.py to settings.py and config accordingly (comments in settings_common.py).

    python run.py

You will be asked if you want to download all the new files. 
Either way, latest files metadata will be stored and only new files will be downloaded 
when you run the script again in the future.

It might helpful to have an alias in ~/.zshrc and to check for new files:

    alias fetch_files='python /path/to/diffftp/run.py'
