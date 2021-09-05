from random import seed
import random
from datetime import datetime

def build_conversion_map():
  f = open("letter_to_emoji.txt")
  line = f.read()
  f.close()

  isKey = True
  key = 'a'
  value = ""
  values = []
  conversion_map = {}
  for c in line:
    if isKey:
      key = c
      isKey = False
    elif (c == '\r') or (c == '='):
      isKey = False
    elif c == '\n':
      values.append(value)
      conversion_map[key] = values

      value = ""
      values = []
      isKey = True
    elif c == ' ':
      if value != "" and value != " ":
        values.append(value)
      value = ""
    else:
      value = value + c
  
  values.append(value)
  conversion_map[key]=values

  return conversion_map

conversionMap = build_conversion_map()

def convert(astring):
  astring = astring.upper()
  seed(datetime.now())
  output = ""
  for c in astring:
    if(c == ' '):
      output = output + " "
    else:
      i = random.randint(0,len(conversionMap[c])-1)
      output = output + conversionMap[c][i] + " "
  return output

import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from keep_alive import keep_alive

#bot setup
client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
guild_ids=[877555770143698974]

send_it = "send it"

#strings to send specific emoji messages
grit = "<:G_:881974742326857828> <:R_:881975539169120267> <:I_:881975861333606440> <:10:881976704069926943>"

big_oof = ":b: <:I_:881975861333606440> <:G_:881974742326857828>   <:oof:879551416056836106>"

succ = "<:sss:882271624294989834> <:uuu:882671601005494303> <:ccc:882670792582762506> <:ccc:882670792582762506> <:funnyrelatable2:879479344022569000>"

jawn = ":regional_indicator_j: :a: :regional_indicator_w: :regional_indicator_n:"

sf = ":a: :regional_indicator_l: :regional_indicator_l:   :m: :regional_indicator_y:   <:hhh:882271553939722281> :o: :m: <:I_:881975861333606440> :regional_indicator_e: <:sss:882271624294989834>   :regional_indicator_l: :o: :regional_indicator_v: :regional_indicator_e:   <:sss:882271624294989834> :a: :regional_indicator_l: :regional_indicator_e: <:sss:882271624294989834> :regional_indicator_f: :o: <:R_:881975539169120267> <:ccc:882670792582762506> :regional_indicator_e:"

#slash commands
@slash.slash(
  name="update",
  description="update emojis map",
  guild_ids=guild_ids
)

async def _update(ctx:SlashContext):
  global conversionMap
  conversionMap = build_conversion_map()
  await ctx.send(succ + "  cess")

@slash.slash(
  name="grit",
  description="grit",
  guild_ids=guild_ids
)

async def _grit(ctx:SlashContext):
  await ctx.send(grit)

@slash.slash(
  name="jawn",
  description="jawn",
  guild_ids=guild_ids
)

async def _jawn(ctx:SlashContext):
  await ctx.send(jawn)

@slash.slash(
  name="bigoof",
  description="bigoof",
  guild_ids=guild_ids
)

async def _bigoof(ctx:SlashContext):
  await ctx.send(big_oof)

@slash.slash(
  name="succ",
  description="lmao",
  guild_ids=guild_ids
)

async def _succ(ctx:SlashContext):
  await ctx.send(succ)

@slash.slash(
  name="pog",
  description="pog",
  guild_ids=guild_ids
)

async def _pog(ctx:SlashContext):
  await ctx.send("<:cursedpog:882668904281960478>")

@slash.slash(
  name="salesforce",
  description="all my homies love salesforce",
  guild_ids=guild_ids
)

async def _salesforce(ctx:SlashContext):
  await ctx.send(sf)

  #don't catch commands from itself
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#respond to certain messages
@client.event
async def on_message(message):
  global send_it
  content = message.content
  if message.author == client.user:
    return

  if content.startswith('!emoji '):
    textToConvert = message.content.split(" ", 1)
    send_it = convert(textToConvert[1])
    await message.channel.send(send_it)

  if content == '!sendit':
    await message.channel.send(send_it)
  
  if content.find("/grit") != -1:
    await message.channel.send(grit)

  if content.upper().find("SUCK") != -1:
    await message.channel.send(succ)


keep_alive()
client.run(os.environ['TOKEN'])
