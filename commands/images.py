import commands, utils, os
from discord import File
from PIL import Image, ImageDraw
import random
command = commands.Command()
@command.event(command="rotate", require="self", type="async")
async def rotate(argdict, args):
    assert len(args) == 1
    degr = int(args[0])
    msg = argdict[commands.Locals.message]
    attachment = msg.attachments[0]
    embed = utils.DefaultEmbed("rotate", msg, "Here's new generated image.")
    pathto = "thumbnails/%s" % attachment.filename
    await attachment.save(pathto)
    img = Image.open(pathto)
    rotated = img.rotate(degr)
    rotated.save(pathto)
    await msg.channel.send(embed=embed, file=File(pathto))
    os.remove(pathto)
    return 0
@command.event(command="mirrow", require="self", type="async")
async def mirrow(argdict, args):
    msg = argdict[commands.Locals.message]
    embed = utils.DefaultEmbed("mirrow", msg, "Here's new generated image.")
    attachment = msg.attachments[0]
    pathto = "thumbnails/%s" % attachment.filename
    await attachment.save(pathto)
    img = Image.open(pathto)
    mirrowed = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirrowed.save(pathto)
    await msg.channel.send(embed=embed, file=File(pathto))
    os.remove(pathto)
    return 0
@command.event(command="grayscale", require="self", type="async")
async def grayscale(argdict, args):
    # Saving code
    msg = argdict[commands.Locals.message]
    embed = utils.DefaultEmbed("grayscale", msg, "Here's new generated image.")
    attachment = msg.attachments[0]
    pathto = "thumbnails/%s" % attachment.filename
    await attachment.save(pathto)
    # Operational code
    image = Image.open(pathto)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1] 	
    pix = image.load()
    for i in range(width):
	    for j in range(height):
		    a = pix[i, j][0]
		    b = pix[i, j][1]
		    c = pix[i, j][2]
		    S = (a + b + c) // 3
		    draw.point((i, j), (S, S, S))
    image.save(pathto)
    del draw
    # Sender and finalizer
    await msg.channel.send(embed=embed, file=File(pathto))
    os.remove(pathto)
    return 0
@command.event(command="negativescale", require="self", type="async")
async def negative(argdict, args):
    # Saving code
    msg = argdict[commands.Locals.message]
    embed = utils.DefaultEmbed("negativescale", msg, "Here's new generated image.")
    attachment = msg.attachments[0]
    pathto = "thumbnails/%s" % attachment.filename
    await attachment.save(pathto)
    # Operational code
    image = Image.open(pathto)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1] 	
    pix = image.load()
    for i in range(width):
	    for j in range(height):
		    a = pix[i, j][0]
		    b = pix[i, j][1]
		    c = pix[i, j][2]
		    draw.point((i, j), (255 - a, 255 - b, 255 - c))
    image.save(pathto)
    del draw
    # Sender and finalizer
    await msg.channel.send(embed=embed, file=File(pathto))
    os.remove(pathto)
    return 0
@command.event(command="blackscale", require="self", type="async")
async def blackscale(argdict, args):
    factor = int(args[0]) if args != None else 70
    # Saving code
    msg = argdict[commands.Locals.message]
    embed = utils.DefaultEmbed("blackscale", msg, "Here's new generated image.")
    attachment = msg.attachments[0]
    pathto = "thumbnails/%s" % attachment.filename
    await attachment.save(pathto)
    # Operational code
    image = Image.open(pathto)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1] 	
    pix = image.load()
    for i in range(width):
	    for j in range(height):
		    a = pix[i, j][0]
		    b = pix[i, j][1]
		    c = pix[i, j][2]
		    S = a + b + c
		    if (S > (((255 + factor) // 2) * 3)):
		    	a, b, c = 255, 255, 255
		    else:
		    	a, b, c = 0, 0, 0
		    draw.point((i, j), (a, b, c))
    image.save(pathto)
    del draw
    # Sender and finalizer
    await msg.channel.send(embed=embed, file=File(pathto))
    os.remove(pathto)
    return 0
@command.event(command="addnoise", require="self", type="async")
async def addnoise(argdict, args):
    factor = int(args[0]) if args != None else 20
    # Saving code
    msg = argdict[commands.Locals.message]
    embed = utils.DefaultEmbed("addnoise", msg, "Here's new generated image.")
    attachment = msg.attachments[0]
    pathto = "thumbnails/%s" % attachment.filename
    await attachment.save(pathto)
    # Operational code
    image = Image.open(pathto)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1] 	
    pix = image.load()
    for i in range(width):
	    for j in range(height):
		    rand = random.randint(-factor, factor)
		    a = pix[i, j][0] + rand
		    b = pix[i, j][1] + rand
		    c = pix[i, j][2] + rand
		    if (a < 0):
		    	a = 0
		    if (b < 0):
		    	b = 0
		    if (c < 0):
		    	c = 0
		    if (a > 255):
		    	a = 255
		    if (b > 255):
		    	b = 255
		    if (c > 255):
		    	c = 255
		    draw.point((i, j), (a, b, c))
    image.save(pathto)
    del draw
    # Sender and finalizer
    await msg.channel.send(embed=embed, file=File(pathto))
    os.remove(pathto)
    return 0