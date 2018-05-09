#!/usr/bin/python
##################################################################################
# Author: Huaqin Xu (huaxu@ucdavis.edu)
# Supervisor: Alexander Kozik (akozik@atgc.org)
# Date: May. 15. 2007 	Latest Update: 10/25/2013
# Description:
#
# This python script print a image from input file and confiure file. 
#
# =================================================================================
# input arguments:
#	1.File name of configureation information.
#	2.File name of user-defined color schema.
#	3.File name of Data to draw the image.
#	4.Option: 0 -- draw image; others -- draw color schema
# Output: image file
#
# example:
#	python pixelirator.py config.txt colormap.txt input.txt 0
#
######################################################################################

from PIL import Image,ImageDraw, ImageFont
import sys
import re
import array
import os
from math import *
from os.path import exists, join, basename, splitext


# Please change the fontpath to the complete path where you install the pilfonts
fontpath = "."


# ---------------------------functions ------------------------------------------------
# ---------------- Open and read file functions ---------------------------------------
def open_file(file_name, mode):
	if file_name == "":
		print 'Empty input file name!'
		raw_input("\nPress the enter key to exit.")
		sys.exit(0)

	try:
		the_file = open(file_name, mode)
	except(IOError), e:
		print "Unable to open the file", file_name, "Ending program.\n", e
		raw_input("\nPress the enter key to exit.")
		sys.exit(0)
	else:
		return the_file

def read_file(afile):
	try:
		flines = afile.readlines()
	except:
		print 'Failed to read from: ', afile
		sys.exit(0)
	else:
		return flines

# ------------------- get Data to be displyed------------------------------------
def getData(lines):
	global xlabel
	global ylabel
	global xscale
	global yscale
	global configset

	delimiter=configset['delimiter']
	if(delimiter=="TAB"):
		delimiter="\t"
	rowstart=int(configset['rowstart'])
	colstart=int(configset['colstart'])
	xlabelat=int(configset['xlabelat'])
	ylabelat=int(configset['ylabelat'])

	datalen=len(lines)
	if(datalen == 0):
		print "Empty Data file!"
		sys.exit(0)
	else:
		colcount=lines[rowstart].count(delimiter)+1
	if(rowstart<0 or colstart <0):
		print "Invalid data start position!"
		sys.exit(0)

	table=[]
		
	if(xlabelat<0):
		xlabel=[i for i in range(1, colcount-colstart+1)]
	else:
		xlabel=lines[xlabelat].strip().split(delimiter)[colstart:]

	for i in range(len(xlabel)):
		if(i+1)%5 == 0 or i==0:
			xscale.append(str(i+1))
		else:
			xscale.append(' ')
	# print xlabel

	i=1
	for l in range(rowstart, datalen):

	# check for empty lines and incorrect field numbers
		if lines[l] != '\n':
			if lines[l].count(delimiter)==colcount-1:
				arow=lines[l].rstrip().split(delimiter)
				if(ylabelat<0):
					ylabel.append(str(i))
				else:
#					ylabel.append(arow[ylabelat])
					ylabel.append('-'.join(arow[ylabelat:colstart]))
				table.append(arow[colstart:])
				i=i+1
			else:
				print "Error: Line #%s has inconsistent number of columns.\n" %(l+1)
		else:
			print "Skip an empty line at #%s.\n" %(l+1)
	# print ylabel
	for i in range(len(ylabel)):
		if(i+1)%5 == 0 or i==0:
			yscale.append(str(i+1))
		else:
			yscale.append(' ')

	return table

def synLabel(label_pos, labelList, fillchar=' '):

	maxlen=0
	for i in labelList:	
		if(len(i)>maxlen):
			maxlen=len(i)
	for j in range(len(labelList)):
		if(label_pos =="U" or label_pos == "R"):
			labelList[j] = (fillchar+labelList[j]).ljust(maxlen+1)
		else:
			labelList[j] = (labelList[j]+fillchar).rjust(maxlen+1)
	return labelList
	

# ------------------- get Configurate parameter and Color shcema -------------------
def setInt(t):
	for i in range(len(t)):
		t[i]=int(t[i])
	return t

def getConfig(configlines):
	global configset
	global infbase

	configset['cell_size'] = 15, 15
	configset['cell_space'] = "1"
	configset['cell_shape'] = "rectangle"
	configset['border_exist'] = 255, 255, 255
	configset['background_color'] = "Y"
	configset['border_color'] = 0, 0, 0
	configset['space_size'] = 20, 20

	configset['title_pos'] = "N"
	configset['title_text'] = infbase
	configset['bar_pos'] = "N"
	configset['bar_size'] = 5, 20
	configset['xlabel_pos'] = "N"
	configset['ylabel_pos'] = "N"
	configset['xlabel_type'] = "header"
	configset['ylabel_type'] = "header"
	configset['label_color'] = 0, 0, 0
	configset['print_value'] = "N"

	configset['colortype'] = "RGB"
	configset['maptype'] = "Rainbow"
	configset['mapfunc'] = "1"

	configset['delimiter'] = "TAB"
	configset['rowstart'] = "1"
	configset['colstart'] = "1"
	configset['xlabelat'] = "0"
	configset['ylabelat'] = "0"

	if(len(configlines) == 0):
		print "Empty configuration file!"
		exit(0)

	for l in configlines:

		if l != "\n" and l[0] != "#":
			set=l.strip().split("=")
			avalue=set[1].strip()
			if(avalue != ''):		
				if(avalue.count(',')>0):
					avalue=tuple(setInt(avalue.split(',')))
				configset[set[0].strip()]=avalue
	# print configset

# ------------------- get Configurate parameter and Color shcema -------------------

def covertColor(colortype, acolor):
	if(colortype=="RGB"):
		return (int(acolor[1]),int(acolor[2]),int(acolor[3]))
	else:
		return (int(acolor[1][0:2], 16), int(acolor[1][2:4], 16), int(acolor[1][4:6], 16))


def getColorMap(colorlines):
	global colorset
	global configset
	global colordefault
	global maptype

	colortype=configset['colortype']
	maptype=configset['maptype']


	for i in range(1, len(colorlines)):
		acolor=colorlines[i].rstrip().split('\t')
		if((len(acolor)!=4 and colortype == "RGB") or (len(acolor)!=2 and colortype == "HEX")):
			print 'Invalid color map file'
			sys.exit(0)

		if(maptype == "Fixed"):
			if(acolor[0] in colorkeys):
				print "Duplicate data value in the color map"
				sys.exit(1)
			else:
				colorkeys.append(acolor[0])
		elif(maptype == "Rainbow"):
			if(i>1):
				if float(acolor[0])<=float(last):
					print "Data value should be ascend in the color map"
					sys.exit(1)
				else:
					colorkeys.append(acolor[0])
			else:
				colorkeys.append(acolor[0])
			last=acolor[0]
		else:
			if(acolor[0] != "min" and acolor[0] != "max"):
				if(i>2 and float(acolor[0])<= float(last)):
					print "Data value should be ascend in the color map"
					sys.exit(1)
				else:
					colorkeys.append(acolor[0]+"~")
					last=acolor[0]
			else:
				colorkeys.append(acolor[0])				
				
	
		if(acolor[0]=="Default"):
			colordefault=covertColor(colortype, acolor)
		elif(acolor[0]=="min" or acolor[0]=="max"):
			colorset[acolor[0]]=covertColor(colortype, acolor)
		else:
			if(maptype=="Fixed"):
				colorset[acolor[0]]=covertColor(colortype, acolor)
			else:
				colorset[float(acolor[0])]=covertColor(colortype, acolor)		
	# print colorkeys

def interpolatefunc(start, end, point, mapfunc):
	
	if(mapfunc=='1'):
		return int(start*(1-point)+end*point)
	elif(mapfunc=='2'):
		base=10
		return int(start*(1-log(point*base, base))+end*log(point*base, base))
	elif(mapfunc=='3'):
		base=e
		return int(start*(1-log(point*base, base))+end*log(point*base, base))
	elif(mapfunc=='4'):
		base=2
		return int(start*(1-log(point*base, base))+end*log(point*base, base))
	elif(mapfunc=='5'):
		return int(start*(1-sqrt(point))+end*sqrt(point))
	elif(mapfunc=='6'):
		base=2
		return int(start*(1-pow(point, base))+end*pow(point, base))
	elif(mapfunc=='7'):
		base=e
		return int(start*(1-pow(point, base))+end*pow(point, base))
	elif(mapfunc=='8'):
		base=3
		return int(start*(1-pow(point, base))+end*pow(point, base))
	else:
		return int(start*(1-point)+end*point)


def getColor(data):
	global colorset
	global colordefault
	global maptype
	global mapfunc

	if(maptype == "Fixed"):
		if(colorset.has_key(data)):
			return colorset[data]
		else:
			return colordefault
	else:
		if(data.strip() == "-"):
			return colordefault
		elif(data.strip() == "min"):
			return colorset["min"]
		elif(data.strip() == "max"):
			return colorset["max"]
		else:
			data=float(data)
		keylist=colorset.keys()
		if(maptype == "Range"):
			keylist.remove("min")
			keylist.remove("max")
		keylist.sort()
		keylen=len(keylist)
		if(data in keylist):
			return colorset[data]
		if(data < keylist[0]):
			if(maptype == "Range"):
				return colorset["min"]
			else:
				return colorset[keylist[0]]
		elif(data > keylist[keylen-1]):
			if(maptype == "Range"):
				return colorset["max"]
			else:
				return colorset[keylist[keylen-1]]
		else:
			for i in range(keylen-1):
				if(data > keylist[i] and data < keylist[i+1]):
					if(maptype == "Range"):
						return colorset[keylist[i]]
					else:
					#	mapfunc=7
						point=float((data-keylist[i])/(keylist[i+1]-keylist[i]))
						R=interpolatefunc(colorset[keylist[i]][0], colorset[keylist[i+1]][0], point, mapfunc)
						G=interpolatefunc(colorset[keylist[i]][1], colorset[keylist[i+1]][1], point, mapfunc)
						B=interpolatefunc(colorset[keylist[i]][2], colorset[keylist[i+1]][2], point, mapfunc)
						return (R, G, B)
		return colordefault

# --------------------------------- draw image  ------------------------------------
def drawImg():
	global configset
	global dataset
	global xlabel
	global ylabel
	global xscale
	global yscale
	global mapfunc
	      
	###### Parameters ##################
	cellx, celly = configset['cell_size']
	cells = int(configset['cell_space'])
	cellshape = configset['cell_shape']
	bdexist = configset['border_exist']
	bgcolor = configset['background_color']
	bdcolor = configset['border_color']
	spacex, spacey = configset['space_size']

	title_pos = configset['title_pos']
	title_text = configset['title_text']
	bar_pos = configset['bar_pos']
	barx, bary = configset['bar_size']
	xlabelpos = configset['xlabel_pos']
	ylabelpos = configset['ylabel_pos']
	xlabeltype = configset['xlabel_type']
	ylabeltype = configset['ylabel_type']
	ftcolor = configset['label_color']

	printval = configset['print_value']
	colortype = configset['colortype']
	maptype = configset['maptype']
	mapfunc = configset['mapfunc']


	####################################
	gapx=cellx+cells
	gapy=celly+cells

	xlabelNum=len(xlabel)
	ylabelNum=len(ylabel)
	imagex=(xlabelNum)*gapx
	imagey=(ylabelNum)*gapy
	
	if(xlabeltype == "scale"):
		xscale=synLabel(xlabelpos, xscale, '-')
		xlabelimg = label2img(xscale, gapx, "courR08.pil", "PNG", ftcolor, bgcolor, 90)
	else:
		xlabel=synLabel(xlabelpos, xlabel)
		xlabelimg = label2img(xlabel, gapx, "courR08.pil", "PNG", ftcolor, bgcolor, 90)
	if(ylabeltype == "scale"):
		yscale=synLabel(ylabelpos, yscale, '-')
		ylabelimg = label2img(yscale, gapy, "courR08.pil", "PNG", ftcolor, bgcolor, 0)
	else:
		ylabel=synLabel(ylabelpos, ylabel)
		ylabelimg = label2img(ylabel, gapy, "courR08.pil", "PNG", ftcolor, bgcolor, 0)

	dataimg = drawData(imagex, imagey, gapx, gapy, cellx, celly, cells, cellshape, bgcolor, bdexist, bdcolor, printval)
	x1, y1=xlabelimg.size
	x2, y2=ylabelimg.size
	img = Image.new("RGBA", (imagex,imagey), bgcolor)
	draw = ImageDraw.Draw(img)


	if(xlabelpos == "N" and ylabelpos == "N"):
		img.paste(dataimg, (0, 0))
	elif(ylabelpos == "N"):
    		img = img.resize((imagex,imagey+y1))		
		if(xlabelpos == "U"):
			img.paste(xlabelimg, (0, 0))
			img.paste(dataimg, (0, y1))
		else:
			img.paste(dataimg, (0, 0))
			img.paste(xlabelimg, (0, imagey))
	elif(xlabelpos == "N"):
    		img = img.resize((imagex+x2,imagey))
		if(ylabelpos == "L"):
			img.paste(ylabelimg, (0, 0))
			img.paste(dataimg, (x2, 0))
		else:
			img.paste(dataimg, (0, 0))
			img.paste(xlabelimg, (imagex, 0))
	else:
		img = img.resize((imagex+x2,imagey+y1))
		if(xlabelpos == "U"):
			if(ylabelpos == "L"):
				img.paste(xlabelimg, (x2,0))
				img.paste(ylabelimg, (0, y1))
				img.paste(dataimg, (x2, y1))
			else:
				img.paste(xlabelimg, (0, 0))
				img.paste(dataimg, (0, y1))
				img.paste(ylabelimg, (imagex, y1))
		else:			
			if(ylabelpos == "L"):
				img.paste(ylabelimg, (0, 0))
				img.paste(dataimg, (x2, 0))
				img.paste(xlabelimg, (x2, imagey))
			else:
				img.paste(dataimg, (0, 0))
				img.paste(xlabelimg, (0, imagey))
				img.paste(ylabelimg, (imagex, 0))
	
	if(bar_pos != "N"):
		barimg = drawBar(barx, bary, ftcolor, bgcolor, maptype)
		bx, by = barimg.size
		imagex, imagey = img.size

		if(imagex>bx):
			imgOut = Image.new("RGBA", (imagex,imagey+by), bgcolor)
			imgOut.paste(barimg, ((imagex-bx)/2, 0))
			imgOut.paste(img,(0, by))
		else:
			imgOut = Image.new("RGBA", (bx,imagey+by), bgcolor)
			imgOut.paste(barimg, (0, 0))
			imgOut.paste(img,(0, by))
	 	img=imgOut

	if(title_pos != "N"):

		imagex, imagey = img.size
		titleimg = drawTitle(title_text, imagex, imagey, "courR10.pil", "PNG", ftcolor, bgcolor, title_pos)
		tx, ty=titleimg.size
		imgOut = Image.new("RGBA", (imagex,imagey), bgcolor)
		draw = ImageDraw.Draw(imgOut)

		if(title_pos == "U" or title_pos == "D"):
			if(imagex>=tx):
    				imgOut = imgOut.resize((imagex,imagey+ty))
			else:	
    				imgOut = imgOut.resize((tx,imagey+ty))
	
			if(title_pos == "U"):
				imgOut.paste(titleimg, (0, 0))
				imgOut.paste(img,(0, ty))
			else:
				imgOut.paste(img,(0, 0))
				imgOut.paste(titleimg, (0, imagey))
		else:
			if(imagey>=ty):
    				imgOut = imgOut.resize((imagex+tx,imagey))
			else:	
    				imgOut = imgOut.resize((imagex+tx,ty))

			if(title_pos == "L"):
				imgOut.paste(titleimg, (0, 0))
				imgOut.paste(img, (tx, 0))
			else:
				imgOut.paste(img, (0, 0))
				imgOut.paste(titleimg, (imagex, 0))
		img=imgOut

	imagex, imagey = img.size
	imgOut = Image.new("RGBA", (imagex+2*spacex,imagey+2*spacey), bgcolor)
	imgOut.paste(img, (spacex, spacey))
	return imgOut


# --------------------------------- draw data  ------------------------------------
def drawData(imagex, imagey, gapx, gapy, cellx, celly, cells, cellshape, bgcolor, bdexist, bdcolor, printval):
	global dataset

	if exists(os.path.join(fontpath,"courR08.pil")):
	    font = ImageFont.load(os.path.join(fontpath,"courR08.pil"))
	else:
	    font = ImageFont.load_default()

	dataimg = Image.new("RGBA", (imagex,imagey), bgcolor)
	draw = ImageDraw.Draw(dataimg)

	for i in range(0,imagex,gapx):
		for j in range(0,imagey,gapy):
			color=getColor(dataset[j/gapy][i/gapx])
			x, y, z=color
			txcolor=(255-x, 255-y, 255-z)
			if cellshape == "rectangle":
				if bdexist == 'Y':
        				draw.rectangle([i, j, i+cellx,j+celly], outline=bdcolor, fill=color)
				else:
        				draw.rectangle([i, j, i+cellx,j+celly], fill=color)		
			else:
				if bdexist == 'Y':
					draw.ellipse([i, j, i+cellx,j+celly], outline=bdcolor ,fill=color)
				else:
        				draw.ellipse([i, j, i+cellx,j+celly], fill=color)		
			if(printval=="Y"):
				draw.text((i+cells,j+cells), dataset[j/gapy][i/gapx], fill=txcolor, font=font)

	return dataimg		

# --------------------------------- draw label  ------------------------------------
def label2img(labellist, height, fontname="helvR08.pil", imgformat="PNG", 
            fgcolor=(0,0,0), bgcolor=(255,255,255),
            rotate_angle=0):
	
    if exists(os.path.join(fontpath,fontname)):
    	font = ImageFont.load(os.path.join(fontpath,fontname))
    else:
	font = ImageFont.load_default()
    imgOut = Image.new("RGBA", (20,49), bgcolor)

    # calculate space needed to render text
    draw = ImageDraw.Draw(imgOut)
    sizex, sizey = draw.textsize(labellist[0], font=font)
    labelNum=len(labellist)

    imgOut = imgOut.resize((sizex,height*labelNum))
    draw = ImageDraw.Draw(imgOut)

    # render label into image draw area
    for i in range(labelNum):
    	draw.text((0, i*height), labellist[i], fill=fgcolor, font=font)

    if rotate_angle:
        imgOut = imgOut.rotate(rotate_angle, expand=1)

    return imgOut

# --------------------------------- draw title  ------------------------------------
def drawTitle(title, imagex, imagey, fontname="helvR10.pil", imgformat="PNG", 
            fgcolor=(0,0,0), bgcolor=(255,255,255), title_pos="U"):

    if exists(os.path.join(fontpath,fontname)):
    	font = ImageFont.load(os.path.join(fontpath,fontname))
    else:
	font = ImageFont.load_default()
    img = Image.new("RGBA", (20,49), bgcolor)

    # calculate space needed to render text
    draw = ImageDraw.Draw(img)
    sizex, sizey = draw.textsize(title, font=font)
    img = img.resize((sizex,sizey))
    draw = ImageDraw.Draw(img)

    # render label into image draw area
    draw.text((0, 0), title, fill=fgcolor, font=font)
    imgOut = Image.new("RGBA", (sizex, sizey), bgcolor)
    draw = ImageDraw.Draw(imgOut)

    if title_pos=="L" or title_pos=="R":
	  if(imagey >= sizex):
	  	imgOut = imgOut.resize((imagey, sizey*2))
		imgOut.paste(img, ((imagey-sizex)/2, 0))
	  else: 
	  	imgOut = imgOut.resize((sizex, sizey*2))
		imgOut.paste(img, ((sizex-imagey)/2, 0))

	  imgOut = imgOut.rotate(90)
    else:
	  if(imagex >= sizex):
	  	imgOut = imgOut.resize((imagex, sizey*2))
		imgOut.paste(img, ((imagex-sizex)/2, 0))
	  else: 
	  	imgOut = imgOut.resize((sizex, sizey*2))
		imgOut.paste(img, ((sizex-imagex)/2, 0))

    return imgOut

# --------------------------------- draw Bar  ------------------------------------
def drawBar(barx, bary, ftcolor, bgcolor, maptype):
	global colorset
	global colorkeys
   	
	if(maptype == "Fixed" or maptype == "Range"):
		bartext = synLabel("R", colorkeys)
		barsize = len(bartext)
		barimg = Image.new("RGBA", (barx,bary), bgcolor)
		bartextimg = label2img(bartext, bary, "courR08.pil", "PNG", ftcolor, bgcolor, 0)
		tx, ty = bartextimg.size
		barimg = Image.new("RGBA", (3*barx + tx, bary*(barsize+2)), bgcolor)
		draw = ImageDraw.Draw(barimg)
		bdcolor=(128, 128, 128)
		for i in range(0, barsize):
			keys=bartext[i].split('~')
			key=keys[0].strip()
			color=getColor(key)
			draw.rectangle([int(barx/2), (i+1)* bary, int(barx/2)+barx, (i+2)*bary], outline=bdcolor, fill=color)
		barimg.paste(bartextimg, (barx*2, bary))
	else:
		if('Default' in colorkeys):
			colorkeys.remove('Default')
		bartext = synLabel("U", colorkeys)
		barsize = len(bartext)
		barlen = int(60/(barsize-1))
		barspace = 20

		barimg = Image.new("RGBA", (barx*(barsize-1)*barlen+60, bary*3), bgcolor)
		draw = ImageDraw.Draw(barimg)
		
		for i in range(0, barsize):
			bartextimg = label2img([bartext[i]], bary, "charR08.pil", "PNG", ftcolor, bgcolor, 0)
			barimg.paste(bartextimg, (i*barx*barlen+barspace, 0))
		for i in range(0, barsize-1):
			for j in range(0, barlen+1):
				data=str((float(bartext[i+1])- float(bartext[i]))*j/barlen + float(bartext[i]))
				color=getColor(data)
				draw.rectangle([(i*barlen+j)*barx+barspace, bary, (i*barlen+j+1)*barx+barspace, 2*bary], fill=color)	
		
	return barimg		


#----------------------------- main ------------------------------------------------------

# ----- get options and file names and open files -----
if len(sys.argv) == 5:
	configfile=sys.argv[1]
	colorfile=sys.argv[2]
	datafile=sys.argv[3]
	choice=sys.argv[4]
else: 
	print len(sys.argv)
	print 'Usage: [1]config file, [2] color map, [3] data file, [4] choice'
	sys.exit(1) 

infbase = splitext(basename(datafile))[0]
outfile = infbase + ".png"

configset={}
configf=open_file(configfile,'r')
configflines = read_file(configf)
getConfig(configflines)

colorset={}
colorkeys=[]
colordefault=(255,255,255)
maptype=""
colorf=open_file(colorfile,'r')
colorlines = read_file(colorf)
getColorMap(colorlines)

tablef=open_file(datafile,'r')
tableflines = read_file(tablef)
xlabel=[]
ylabel=[]
xscale=[]
yscale=[]
dataset=getData(tableflines)

if choice == '0':
	img=drawImg()
else:
	barx, bary = configset['bar_size']
	bgcolor = configset['background_color']
	ftcolor = configset['label_color']
	mapfunc = configset['mapfunc']
	img=drawBar(barx, bary, ftcolor, bgcolor, maptype)		
img.save(outfile, "PNG")

		