#this is the main file.
#this is where you will add all your little projects.
#importing what we need.

import discord
from discord.ext import commands
import json
import os
import random
from discord.ext.commands.cooldowns import BucketType

#this will link your bot to a certain folder.
#this will come in handy when we use databases.
#this is my one but you need to put your path or it wont work.

os.chdir("C:\\Users\\mians\\Desktop\\Bot Making\\Economy Bot")

# sets your bots prefix.
client = commands.Bot(command_prefix = "yourprefixhere")





