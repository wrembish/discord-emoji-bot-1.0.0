# discord-emoji-bot-1.0.0

a bot programmed in python that has commands to take text from messages on discord and convert each letter to an emoji

# main.py
The bot itself is here. A map is created when the bot is first launched that maps individual character to whatever emojis you want it to pick from
(customize the emojis in the letter_to_emoji.txt file)

# keep_alive.py
a file used to keep the bot running on replit without needing it to constantly be used or restarted. Used in junction with uptimerobot.

# letter_to_emoji.txt
text file containing all of the conversions.
the format is:
<character that gets converted>=<first emoji it can be> <another emoji?> ......
for letters, use capital letters for the character that gets converted
  eg. A=:a: :regional_indicator_a>
if you update this file while the bot is still running, you don't have to relaunch the bot just run /update to rebuild the map with the updated conversions
