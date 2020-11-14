'''
Installing dependencies:

This Script installs the dependencies needed
to run the potato bot. If this doesn't work
make sure this script is run as administrator

Supported versions:
Python 3.8 or newer
'''
try:
    # Please add all new imports to the script here
    import os
    import platform
    import discord
    import youtube_dl

except ImportError:
    # Python version check
    RAWversion = platform.python_version()
    version = ''
    for i in range(0, len(RAWversion)):
        if i <= 2:
            version = version + RAWversion[i]

    # Please add all new imports to the script here aswell for the install process
    os.system(f'pip{version} install discord.py && pip{version} install youtube_dl && pip{version} install discord[voice] ')