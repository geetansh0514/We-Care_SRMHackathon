import discord
import requests
import datetime
import os
import sys

def getUserLoc():
        
    fresponse = requests.get('https://freegeoip.app/json/').json()
    loc = [fresponse['latitude'],fresponse['longitude'] ]
    return([fresponse['latitude'],fresponse['longitude']])


def Alert(userLoc):
    client = discord.Client()
    statusdict = {'online': discord.Status.online,
                                'dnd' : discord.Status.dnd,
                                'idle' : discord.Status.idle,
                                'invisible' : discord.Status.invisible}

    swinfo = {}
    #mention function
    def mention(id):
        authorname = "<@!" + str(id) + ">"
        return authorname


    @client.event
    async def on_connect():
        print("Acci-Saver with id",client.user," initialized with latency ",client.latency,"\nListening for new messages.\n")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Get Help",url = "https://acci-saver.herokuapp.com/"))
        general = client.get_channel(909150527022051408)
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
        
        embedhelp1 = discord.Embed(title = "**Alert Recieved** \n*Click to view location on map*",url = "https://maps.google.com/?q=" + str(userLoc[0]) + ","+ str(userLoc[1]))
        embedhelp1.add_field(name = "User Location",value  = str(userLoc[0]) + ","+ str(userLoc[1]) ,inline=False)
        embedhelp1.add_field(name = "Request Time ",value  = now+" - "+ tz  ,inline=False)
        embedhelp1.set_image(url = 'https://media.istockphoto.com/vectors/hand-drawn-doodle-ambulance-illustration-with-cartoon-style-vector-vector-id1196743845')
        embedhelp1.set_footer(text = "----------------------------------------------------------------" ,icon_url="https://www.pngall.com/wp-content/uploads/2017/05/Alert-PNG-Images.png")
        await general.send(embed = embedhelp1)


    client.run(os.environ['TOKEN'])
    client.close()
m = getUserLoc()    

print("User Ip sent through discord - ",sys.argv[1],sys.argv[2])
Alert([sys.argv[1],sys.argv[2]])