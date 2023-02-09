import discord as robert
import os
import requests
import time
import test
import test3
import asyncio
import json
import sys
import heapq
from pdf2image import convert_from_path
from termcolor import colored, cprint
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

BING_TOKEN = os.getenv('BING_TOKEN')

intents = robert.Intents.all()

client = robert.Client(command_prefix='>', intents=intents)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("logged in as {0.user}".format(client))
    # client.loop.create_task(my_background_task())
    game = robert.Game("type foody help me")
    await client.change_presence(status=robert.Status.online, activity=game)
    

@client.event
async def on_message(message): 
    if message.author == client.user or isFile(message.content) or message.content == "":
        return

    content_lower = message.content.lower()
    items = content_lower.split()
    
    curr = time.time()
    curr_string = time.ctime(curr)
    print(color.BOLD + "[{0}] {1}:{2} {3}".format(curr_string[4:], str(message.author.display_name), color.END, str(message.content)))

    if content_lower == "foody help me":
        await help(message)
        return
    
    if message.content == "do the thing":

        words = ["<:sadparabola:1035768053859885107>", "<:lasdrogas:1037254091686031422>", "<:die:1036053649782227084>", "<:panik:1069542403582742568>", "<:pepega:1069752783382790175>", "<:theyaskyouifyourefine:1036723056703459328>", "<:thunj:1039084760372351047>"]
        with open('users.json','r+') as file:
          # First we load existing data into a dict.
            file_data = json.load(file)
            for user in file_data["users"]:
                for word in words:
                    if word not in file_data["counter"]["donovan#4520"]:
                        file_data["counter"][file_data["users"].get(user)].update({word:0})
                    # file_data["counter"].update({file_data["users"].get(user):{}})

            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

    if message.content == "foody do the work":
        with open('users.json','r+') as file:
            file_data = json.load(file)
            for user in file_data["users"]:
            
                file_data["counter"][file_data["users"].get(user)].pop("penis")

                # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

    if message.content == "get all users":
        x = '{"users" : []}'
        with open('users.json','r+') as file:
          # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details

            print(file_data)
            for user in client.users:
                if user != client.user:
                    file_data["users"][user.display_name] =  user.name + "#" +user.discriminator
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
        return

    if message.content == "emote test":
        await message.add_reaction("<:kekw:1035768498313502791>")
        await message.channel.send(file = robert.File('pepega3.jpg'))

    if items[0] == "-food" and items[1] == "chat" and items[2] != "clear":
        with open("chat.txt", "a") as file:
            file.write("Human: " + message.content[11:] + "\nAI: ")
        with open("chat.txt", "r") as file:
            # print("This is the prompt: " + file.read())
            # output = test3.generate_response("how do i make an espresso")

            output = test3.generate_response(file.read())
            print(output)
        with open("chat.txt", "a") as file:
            file.write(output + "\n")
            await message.channel.send(output)

    if items[0] == "-food" and items[1] == "chat" and items[2] == "clear":
        os.remove("chat.txt")
        file = open("chat.txt", "x")
        file.close()


    if str(message.author) == "koko_#0605":
        await hannah(message)

    # if str(message.author) == "donovan#4520":
    #     await hannah(message)

    if str(message.author) == "linguini#8976":
        await hannah(message)

    await booty(message)

    await generate(message, items)
    
    await request(message, items)

    await cookie(message, content_lower)

    await zaddy(message, content_lower)
    
    await claire(message, content_lower)

    await chill(message)

    await homework(message, content_lower, items)

    await food(message, content_lower)

    if await addToCount(message, items) == True:
        return

    with open('users.json','r') as file:
        file_data = json.load(file)

        if await wordCounterOutput(message, items, file_data) == True:
            return

        if await wordCountLeaderBoard(message, items, file_data) == True:
            return
        await getTypoCount(message, items, file_data)

    await wordCounter(message, content_lower)


# # bot tells robert to stop playing his games
# @client.event
# async def on_presence_update(before, after):
#     # if before.name == "SWu" or after.name == "SWu":
#     #     return
#     if after.activity != None and (after.activity).type == robert.ActivityType.playing:
#         channel = client.get_channel(1033081170080038953)
#         await channel.send("%s STOP PLAYING GAMES" % after.mention)

# bot generates image based off the user's prompt
async def generate(message, items):
    if items[0] == "-generate":
        input = message.content.split("-generate")
        test.make_image(input[1])
        await message.channel.send(file = robert.File('temp.png'))
        os.remove("temp.png")
        
# bot responds saying if the homework has been releeased
async def homework(message, content_lower, items): 
    if 'test' in content_lower:
        target = "test"

        while (items[0] != target and len(items)>0):
            items.pop(0)

        if items[1] == "331":
            await message.channel.send("dont take this class") 
            await asyncio.sleep(0.5)
            await message.channel.send("i would rather look at a slug")
            return
            
        r = ping(items)

        # print(r.content)

        output = r.content.decode('utf-8', errors = "ignore")
        # print(output)
        if output.__contains__("404 Not Found") or output.__contains__("Forbidden"): 
            print("hw" + items[2] + " doesnt exist")
            await message.channel.send(str(items[1]) + " " + items[3] + items[2] + " isn't released")
        else :
            print("hw" + items[2] + " exists")
            await message.channel.send(str(items[1]) + " " + items[3] + items[2] + " is released")
            if items[1] != "333":
                with open("temp.pdf", 'wb') as file:
                    file.write(r.content)
                images = convert_from_path("temp.pdf")
                os.remove("temp.pdf")
                i = 0
                for image in images:
                    image.save("output" + str(i) + ".jpg", "JPEG")
                    i = i + 1
                for j in range(i):
                    await message.channel.send(file = robert.File("output{}.jpg".format(j)))
                    os.remove("output{}.jpg".format(j))



# returns the html for cse course homework sites
def ping(items):

    # 431
    if items[1] == "431":
        return requests.get('https://homes.cs.washington.edu/~anuprao/pubs/CSE431wi23/homework{0}.pdf'.format(items[2]))
    # 333
    elif items[1] == "333":
        if (items[3] == "ex"):
            return requests.get('https://courses.cs.washington.edu/courses/cse333/23wi/exercises/ex0{0}.html'.format(items[2]))
        if (items[3] == "hw"):
            return requests.get('https://courses.cs.washington.edu/courses/cse333/23wi/hw/hw{0}/hw{0}.html'.format(items[2]))
    elif items[1] == "312":
        return requests.get('https://courses.cs.washington.edu/courses/cse312/23wi/files/homework/pset{0}.pdf'.format(items[2]))
    # 311, 312, 421
    else: 
        return requests.get('https://courses.cs.washington.edu/courses/cse{0}/23wi/assignments/homework{1}.pdf'.format(str(items[1]), items[2]))

# dont worry about it
async def booty(message):
    if message.content == "foody slap my booty":
        await message.channel.send("if you say so!")
        await message.channel.send("🫡")
        await message.channel.send("🚶👏")

# replies with a somewhat complete list of commands
async def help(message):
    with open("help.txt") as file:
        await message.channel.send(file.read())
    for i in range(1, 3):
        async with message.channel.typing():
            await asyncio.sleep(2.3)
        with open("help" + str(i) + ".txt") as file:
            await message.channel.send(file.read())

# COOKIE
async def cookie(message, content_lower):
    if content_lower.__contains__("cookie"):
        for i in range(3):
            await message.channel.send("EAT COOKIE")

# user can submit ideas for feature
async def request(message, items):
    if items[0] == "foodbot" and items[1] == "request":
        with open("requests.txt", 'a') as file:
            file.write(message.content.split("foodbot request ")[1] + '\n')
            await message.channel.send("sure man")
        with open("requests.txt", 'r') as file:
            await message.channel.send("**Current Request List:**```" + file.read() + "```")


async def chill(message):
    if message.content.__contains__("FUCK"):
        await message.channel.send("chill")


async def claire(message, content_lower):
    if content_lower == "hi claire!":
        name = str(message.author).split('#')
        await message.channel.send("HI " + name[0].upper())


async def zaddy(message, content_lower):
    if 'woo' in content_lower or 'kevin' in content_lower:
        await message.channel.send('zaddy?')


# tells user to eat
async def food(message, content_lower):
    if client.user.mentioned_in(message):
        await message.channel.send("Go eat your food")
        return

    arr = {'hungry', "i didn't eat", 'not eaten yet', 'haven\'t had lunch yet', 
           "haven't had dinner yet", "haven't had lunch yet", 
           "have not had dinner yet", "have not had lunch yet", 
           "have not had breakfast yet", "haven't had food yet", 
           "have not had food yet", "I did not eat", "hangry"}
    
    for sentence in arr:
        if sentence in content_lower:
            await message.channel.send("<@%s> go eat your food" % message.author.id)
            # await channel.send("<@%s> go eat your food" % message.author.id)
            break

def isFile(content):
    file_extentions = [".jpg", ".png", ".gif", ".pdf", ".jpeg"]
    if any ([x in content for x in file_extentions]):
        print("found file")
        return True
    else: 
        return False

# spell checks messages
async def hannah(message):
    
    api_key = BING_TOKEN # "<ENTER-KEY-HERE>"
    example_text = message.content # the text to be spell-checked
    endpoint = "https://api.bing.microsoft.com/v7.0/SpellCheck"

    print(example_text)
    data = {'text': example_text}
    
    params = {
    'mkt':'en-us',
    'mode':'spell' #spell/proof
    }

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': api_key
    }

    response = requests.post(endpoint, headers=headers, params=params, data=data)
    json_response = response.json()
    print(json_response)
    has_errors = bool(json_response["flaggedTokens"])

    print("has errors: " + str(has_errors)) 
    # print(json_response["flaggedTokens"])
    
    # if has_errors:
    #     for i in json_response["flaggedTokens"]:
    #         if not i["suggestions"][0]["suggestion"].__contains__('\''):
    #             print("found \'")
    #             await message.add_reaction("<:pepega:1069752783382790175>")
    #     print(json_response["flaggedTokens"][0]["suggestions"][0]["suggestion"])
    if not has_errors:
        return
    
    with open('users.json','r+') as file:
        file_data = json.load(file)

        for i in json_response["flaggedTokens"]:
            if not i["suggestions"][0]["suggestion"].__contains__('\'') and i.get("token") != "staek" and i.get("token") != "-food":
                
                file_data["typos"][str(message.author)] += 1
                await message.add_reaction("<:pepega:1069752783382790175>")

        file.seek(0)
        json.dump(file_data, file, indent = 4)
    
    print(json_response["flaggedTokens"][0]["suggestions"][0]["suggestion"])

async def wordCounter(message, content): 
    # words = ["fuck", "shit", "<:kekw:1035768498313502791>", "<:letsfuckinggo:1035768505485774919>", "<:ughh:1046294416555520000>", "<:hollow:1064666622096326696>", "<:shrunk:1065183547385729044>", "<:diesfrommid:1044704686529327215>"]
    with open('users.json','r+') as file:
        file_data = json.load(file)

        for word in file_data["words"]:
            if content.__contains__(word):
                old_count = file_data["counter"][str(message.author)].get(word)
                file_data["counter"][str(message.author)].update({word:(old_count+1)})

        # Sets file's current position at offset.
        file.seek(0)
        json.dump(file_data, file, indent = 4)

async def wordCounterOutput(message, items, file_data):

    if items[0] != "-food" or items[2] != "#":
        return

    if items[3] not in file_data["words"]:
        await message.channel.send("I don't count the occurences of *"+ items[3] + "*")
        return
    
    with open('users.json','r') as file:
    # First we load existing data into a dict.
        file_data = json.load(file)
        count = file_data["counter"][file_data["users"].get(items[1])].get(items[3])

        await message.channel.send("{0} has said {1} {2} times".format(items[1], items[3], count))

    return True

async def wordCountLeaderBoard(message, items, file_data):
    # words = ["fuck", "shit", "<:kekw:1035768498313502791>", "<:letsfuckinggo:1035768505485774919>", "<:ughh:1046294416555520000>", "<:hollow:1064666622096326696>", "<:shrunk:1065183547385729044>", "<:diesfrommid:1044704686529327215>"]
    words = file_data["words"]

    if items[0] != "-food" or items[2] != "leaderboard":
        return

    if items[1] not in words:
        await message.channel.send("I don't count the occurences of *"+ items[1] + "*")
        return

    output = "**{} Leaderboard**```".format(items[1].capitalize())
    # with open('users.json','r') as file:
    #     file_data = json.load(file)
    counts = []
    
    for user in file_data["users"]:
        count = file_data["counter"][file_data["users"].get(user)].get(items[1])
        counts.append((count, user))
    print("List before: " + str(counts))
    # heapq._heapify_max(counts)
    counts.sort(reverse = True)
    print("List after: + " + str(counts))
    count = 1

    for person in counts:
        if person[0] == 0:
            break
        output += "{}. {}: {}\n".format(count, person[1].capitalize(), person[0])
        count += 1

    await message.channel.send(output + "```")

    return True

async def addToCount(message, items):

    if items[0] != "-food" or items[1] != "start" or items[2] != "counting":
        return

    with open('users.json','r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        if items [3] in file_data["counter"]["donovan#4520"]:
            await message.channel.send("dawg i already count that jawn")
            return True

        file_data["words"].append(items[3])
        for user in file_data["users"]:
            file_data["counter"][file_data["users"].get(user)].update({items[3]:0})

        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        
        await message.channel.send("okie i count")

    return True

async def getTypoCount(message, items, file_data):

    if items[0] != "-food" or items[2] != "typos":
        return
    if items[1] != "luksh" and items[1] != "hannah":
        await message.channel.send("dawg i dont remember")
        return
    count = file_data["typos"].get(file_data["users"].get(items[1]))
    await message.channel.send("They be making " + str(count) + " typos")

client.run(TOKEN)

