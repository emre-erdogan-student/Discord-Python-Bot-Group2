import discord
from discord.ui import Button, View
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("The bot is ready!")
    print("------------------------------")

@client.command()
async def cold(ctx):
    button = Button(label="Stuffy Nose", style = discord.ButtonStyle.blurple, emoji="👃")
    button2 = Button(label="Fever", style = discord.ButtonStyle.blurple, emoji="🤧") 
    button3 = Button(label="Runny Nose", style = discord.ButtonStyle.blurple, emoji="😢")
    button4 = Button(label="Malaise", style = discord.ButtonStyle.blurple, emoji="😴")
    button5 = Button(label="Yes", style = discord.ButtonStyle.green, emoji="✅")
    button6 = Button(label="No", style = discord.ButtonStyle.red, emoji="👎")

    async def button_callback(interaction):
        await interaction.response.send_message("These symptoms you are experiencing are common side effects of having a cold. The recommended route of action you should take to treat the cold is as follows: \n\nVisit your GP, you may be prescriped medication \nGP May ask you to eat certain foods. \nYou should call ER if you are having trouble breathing or if your fever gets worse. \n\nFor more information visit: https://www.cdc.gov/antibiotic-use/colds.html")
    async def button_callback2(interaction):
        await interaction.response.send_message("If you are not experiencing these symptoms of a cold, we still highly recommend you contact your GP for further information. This BOT can't give an exact diagnosis of your cold and should not be used to self diagnose. \n\nIf you are looking for a GP near you, visit the following site: https://www.hotdoc.com.au/ or If you are in an emergency, contact 000.  ")
    button5.callback = button_callback
    button6.callback = button_callback2


    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    await ctx.send("Hello, for us to determine whether you have a cold, do you have either 3 or 4 of these sypmtoms?. Click either 'YES' or 'NO' ", view=view)

@client.command()
async def migraine(ctx):
    button = Button(label="Visual Aura", style = discord.ButtonStyle.blurple, emoji="👁️")
    button2 = Button(label="One Sided or Two sided Pain", style = discord.ButtonStyle.blurple, emoji="🤦‍♂️")
    button3 = Button(label="Pulsing Type Pain", style = discord.ButtonStyle.blurple, emoji="😨")
    button4 = Button(label="Nausea", style = discord.ButtonStyle.blurple, emoji="🤮")
    button5 = Button(label="Sensitive to Light", style = discord.ButtonStyle.blurple, emoji="☀️")
    button6 = Button(label="Yes", style = discord.ButtonStyle.green, emoji="✅")
    button7 = Button(label="No", style = discord.ButtonStyle.red, emoji="👎")
    
    async def button_callback(interaction):
        await interaction.response.send_message("These symptoms you are experiencing are common side effects of having a Headache type called Migraine. The recommended route of action you should take to ease the migraine is as follows: \n\nHold an ice over your forehead or eyes \nSleep in an area with no light \nVisit GP to get prescriped medication for migraine \nTake breaks if you are stressing heavily  \nYou should call ER if you have severe migraines accompanied by confusion, fever, or your eyesight hasn't recovered from the aura. \n\nFor more information visit: https://www.betterhealth.vic.gov.au/health/conditionsandtreatments/headache-migraine")
    async def button_callback2(interaction):
        await interaction.response.send_message("If you are not experiencing these symptoms of a migraine, we still highly recommend you contact your GP for further information. This BOT can't give an exact diagnosis of your migraine and should not be used to self diagnose. \n\nIf you are looking for a GP near you, visit the following site: https://www.hotdoc.com.au/ or If you are in an emergency, contact 000.")
    button6.callback = button_callback
    button7.callback = button_callback2

    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)
    await ctx.send("Hello, for us to determine whether you have a migraine, do you have either 2 to 5 of these sypmtoms?. Click either 'YES' or 'NO' ", view=view)

@client.command()
async def otitis(ctx):
    button = Button(label="Middle Ear Pain", style = discord.ButtonStyle.blurple, emoji="🤕")
    button2 = Button(label="Ear Has Discharge", style = discord.ButtonStyle.blurple, emoji="👂")
    button3 = Button(label="Loss Of Balance", style = discord.ButtonStyle.blurple, emoji="⚖️")
    button4 = Button(label="Temporary loss of hearing", style = discord.ButtonStyle.blurple, emoji="🙉")
    button5 = Button(label="Poor Hearing", style = discord.ButtonStyle.blurple, emoji="🙅‍♂️")
    button6 = Button(label="Yes", style = discord.ButtonStyle.green, emoji="✅")
    button7 = Button(label="No", style = discord.ButtonStyle.red, emoji="👎")
    
    async def button_callback(interaction):
        await interaction.response.send_message("These symptoms you are experiencing are common side effects of having Otitis also known as Middle Ear Infection. The recommended route of action you should take to treat middle ear infection: \n\nVisit GP to get prescriped antibiotics or other medication for Otitis  \nEat certain foods recommended by GP  \nYou should call ER if you have pain or swelling at ear and high fever  \n\nFor more information visit: https://www.healthdirect.gov.au/ear-infection#:~:text=Outer%20ear%20infections%20(otitis%20externa,the%20bone%20behind%20the%20ear.")
    async def button_callback2(interaction):
        await interaction.response.send_message("If you are not experiencing these symptoms of a Otitis (Middle Ear Infection), we still highly recommend you contact your GP for further information. This BOT can't give an exact diagnosis of your Otitis (Middle Ear Infection) and should not be used to self diagnose. \n\nIf you are looking for a GP near you, visit the following site: https://www.hotdoc.com.au/ or If you are in an emergency, contact 000.")
    button6.callback = button_callback
    button7.callback = button_callback2

    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)
    await ctx.send("Hello, for us to determine whether you have Otitis (Middle ear infection), do you have either 3 to 5 of these sypmtoms?. Click either 'YES' or 'NO' ", view=view)

@client.command()
async def shingles(ctx):
    button = Button(label="Tingling, Itching or Burning Sensation", style = discord.ButtonStyle.blurple, emoji="🔥")
    button2 = Button(label="Headache", style = discord.ButtonStyle.blurple, emoji="🤯")
    button3 = Button(label="Upset Stomach", style = discord.ButtonStyle.blurple, emoji="🙇‍♂️")
    button4 = Button(label="Fever and Chills", style = discord.ButtonStyle.blurple, emoji="🤒")
    button5 = Button(label="Muscles feel Weak", style = discord.ButtonStyle.blurple, emoji="💪")
    button6 = Button(label="Yes", style = discord.ButtonStyle.green, emoji="✅")
    button7 = Button(label="No", style = discord.ButtonStyle.red, emoji="👎")
    
    async def button_callback(interaction):
        await interaction.response.send_message("These symptoms you are experiencing are common side effects of having Shingles. As shingles can be highly dangerous, you should first contact a doctor immediately. If you want to know what what to do when symptoms of Shingles appears: \n\nGet Chicken Pox Vaccination \nEat certain foods recommended by GP \nPrescribed Medication by GP to treat Shingles  \nYou should call ER if you have a sense of confusion, high fever (38*C or higher) \n\nFor more information and clarification visit: https://www.healthdirect.gov.au/shingles")
    async def button_callback2(interaction):
        await interaction.response.send_message("If you are not experiencing some of these sypmtoms of Shingles, we still highly recommend you contact your GP for further assistance. This BOT can't give an exact diagnosis of your Shingles and should not be used to self diagnose. \n\nIf you are looking for a GP near you, visit the following site: https://www.hotdoc.com.au/ or If you are in an emergency, contact 000.")
    button6.callback = button_callback
    button7.callback = button_callback2

    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)
    await ctx.send("Hello, for us to determine whether you have Shingles , do you have either 3 to 5 of these sypmtoms?. Click either 'YES' or 'NO' ", view=view)

@client.command()
async def diarrhoea(ctx):
    button = Button(label="Watery, Loose Stools", style = discord.ButtonStyle.blurple, emoji="💧")
    button2 = Button(label="Bloody stools or Fever (Depends on Person)", style = discord.ButtonStyle.blurple, emoji="🩸")
    button3 = Button(label="Cramping or Pain in the Stomach", style = discord.ButtonStyle.blurple, emoji="🙇‍♂️")
    button4 = Button(label="Yes", style = discord.ButtonStyle.green, emoji="✅")
    button5 = Button(label="No", style = discord.ButtonStyle.red, emoji="👎")
    
    async def button_callback(interaction):
        await interaction.response.send_message("These symptoms you are experiencing are common side effects of having Diarrhoea. As these symptoms are a common effect of other bowel related issues, we would recommend contacting a GP. If you want to know what what to do when symptoms of Diarrhoea appears: \n\nPrescribed Medication by GP to treat Diarrhoea  \nDrink plenty of water and find out what to eat by your GP \nGet a treatment plan recomendded by GP \nYou should call ER if you have diarrhoea for longer then 2 days \n\nFor more information visit: https://www.healthdirect.gov.au/diarrhoea")
    async def button_callback2(interaction):
        await interaction.response.send_message("If you are not experiencing some of these sypmtoms of Diarrhoea, we still highly recommend you contact your GP for further assistance. This BOT can't give an exact diagnosis of your Diarrhoea and should not be used to self diagnose. \n\nIf you are looking for a GP near you, visit the following site: https://www.hotdoc.com.au/ or If you are in an emergency, contact 000.")
    button4.callback = button_callback
    button5.callback = button_callback2

    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    await ctx.send("Hello, for us to determine whether you have Diarrhoea , do you have either 2 to 3 of these sypmtoms?. Click either 'YES' or 'NO' ", view=view)

@client.command()
async def mononucleosis(ctx):
    button = Button(label="Skin Rash", style = discord.ButtonStyle.blurple, emoji="🫴")
    button2 = Button(label="Fatigue/Tiredness", style = discord.ButtonStyle.blurple, emoji="😵‍💫")
    button3 = Button(label="Swollen Spleen and Tonsils", style = discord.ButtonStyle.blurple, emoji="😮")
    button4 = Button(label="Sore Throat", style = discord.ButtonStyle.blurple, emoji="😩")
    button5 = Button(label="Yes", style = discord.ButtonStyle.green, emoji="✅")
    button6 = Button(label="No", style = discord.ButtonStyle.red, emoji="👎")
    
    async def button_callback(interaction):
        await interaction.response.send_message("These symptoms you are experiencing are common side effects of having Mononucleosis. If you want to know what what to do when symptoms of Mononucleosis appears: \n\nPrescribed Medication by GP to treat Mononucleosis   \nGet a treatment plan recomendded by GP \nYou should call ER if you have Mononucleosis for longer then 10 days or severe belly pain \n\nFor more information visit: https://www.webmd.com/a-to-z-guides/symptoms-of-mononucleosis")
    async def button_callback2(interaction):
        await interaction.response.send_message("If you are not experiencing some of these sypmtoms of Mononucleosis, we still highly recommend you contact your GP for further assistance. This BOT can't give an exact diagnosis of your Mononucleosis and should not be used to self diagnose. \n\nIf you are looking for a GP near you, visit the following site: https://www.hotdoc.com.au/ or If you are in an emergency, contact 000.")
    button5.callback = button_callback
    button6.callback = button_callback2

    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    await ctx.send("Hello, for us to determine whether you have Mononucleosis , do you have either 2 to 5 of these sypmtoms?. Click either 'YES' or 'NO' ", view=view)


@client.command()
async def pmdinfo(ctx):
    await ctx.send("Hello my name is Pre Med Diagnosis (PMD)! PMD is a discord-only pre-diagnosis chatbot that helps diagnose people based on their symptoms and gives them instructions on what they should do next. \n\nDISCLAIMER: PMD is purely a prototype for our assignment; hence, you should contact your GP for actual medical assistance. \n\nIf you would like further information about me visit our website on: https://emre-erdogan-student.github.io/Artifact-DiscordBot-Assignment3/")
        

#Note! This token will no longer be valid as Discord automatically changes it once it detects anything on the internet of our token. This is to protect our discord bot from getting controlled by hackers and third party
#If you need to test the bot please message me Emre 
client.run('MTAxOTc5NDY2OTMzMDI1NTk1NQ.GSiY6b.3nMtXc0EI6ORd0xU21iScdZ0YOoIxOavITGTnA')

