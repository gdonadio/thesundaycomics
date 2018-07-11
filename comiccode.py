import re
import urllib2
import glob


from datetime import date
today = date.today().toordinal()
prevsunday = today - (today % 7)
sundaydate = date.fromordinal(prevsunday)
kingdate = sundaydate.strftime("%Y-%m-%d")
godate = sundaydate.strftime("%Y/%m/%d")

comicstrip = {}

patterngo = '"og:image" content="'
comiclistgo = {
"CALVIN AND HOBBES by Bill Watterson": "http://www.gocomics.com/calvinandhobbes/",
"DOONESBURY by Garry Trudeau": "http://www.gocomics.com/doonesbury/",
"NON SEQUITUR by Wiley Miller": "http://www.gocomics.com/nonsequitur/",
"PICKLES by Brian Crane": "http://www.gocomics.com/pickles/",
"ADAM@HOME by Rob Harrell": "http://www.gocomics.com/adamathome/",
"PEARLS BEFORE SWINE by Stephan Pastis": "http://www.gocomics.com/pearlsbeforeswine/",
"FOR BETTER OR FOR WORSE by Lynn Johnston": "http://www.gocomics.com/forbetterorforworse/",
"CUL DE SAC by Richard Thompson": "http://www.gocomics.com/culdesac/",
"JUMPSTART by Robb Armstrong": "http://www.gocomics.com/jumpstart/",
"MARMADUKE by Brad Anderson": "http://www.gocomics.com/marmaduke/",
"ROSE IS ROSE by Don Wimmer and Pat Brady": "http://www.gocomics.com/roseisrose/",
"BALDO by Hector D. Cantu and Carlos Castellanos": "http://www.gocomics.com/baldo/",
"B.C. by Mastroianni and Hart": "http://www.gocomics.com/bc/",
"PEANUTS by Charles Schultz" : "http://www.gocomics.com/peanuts/",
"GARFIELD by Jim Davis": "http://www.gocomics.com/garfield/",
"FOXTROT by Bill Amend": "http://www.gocomics.com/foxtrot/",
"DILBERT by Scott Adams": "http://www.gocomics.com/dilbert-classics/",
"GET FUZZY by Darby Conley": "http://www.gocomics.com/getfuzzy/",
#"CATHY by Cathy Guisewite": "http://www.gocomics.com/cathy/" #Cathy is too lame
}


patternking = '" name="twitter:image:src"'
comiclistking = {
"FAMILY CIRCUS by Bil and Jeff Keane": "http://comicskingdom.com/family-circus/",
"BLONDIE by Dean Young and John Marshall": "http://comicskingdom.com/blondie/",
"BEETLE BAILEY by Mort Walker": "http://comicskingdom.com/beetle-bailey-1/",
"CRANKSHAFT by Tom Batiuk and Chuck Ayers": "http://comicskingdom.com/crankshaft/",
"FUNKY WINKERBEAN by Tom Batiuk": "http://comicskingdom.com/funky-winkerbean/",
"HAGAR THE HORRIBLE by Chris Browne": "http://comicskingdom.com/hagar-the-horrible/",
"HI AND LOIS by Brian Walker, Greg Walker and Chance Browne": "http://comicskingdom.com/hi-and-lois/",
"ZITS by Jerry Scott and Jim Borgman": "http://comicskingdom.com/zits/",
"SALLY FORTH by Francesco Marciuliano; drawn by Jim Keefe": "http://comicskingdom.com/sally-forth/",
"PRINCE VALIANT by Mark Schultz and Thomas Yeates": "http://comicskingdom.com/prince-valiant/",
"MUTTS by Patrick McDonnell": "http://comicskingdom.com/mutts/",
"MARY WORTH by Karen Moy and Joe Giella": "http://comicskingdom.com/mary-worth/",
"BABY BLUES by Rick Kirkman and Jerry Scott": "http://comicskingdom.com/baby-blues/",
"MOTHER GOOSE & GRIMM by Mike Peters": "http://comicskingdom.com/mother-goose-grimm/",
}

def adddatesking():
	for name, address in comiclistking.items():
		comiclistking[name] += kingdate
	
def adddatesgo():
	for name, address in comiclistgo.items():
		comiclistgo[name] += godate	

def comicpullking():
	for name, link in comiclistking.items():
		request = urllib2.Request(link)
		request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5")

		f = urllib2.urlopen(request)
		page = f.read()


		for match in re.finditer(patternking, page):
			s = match.start()	
			if page[s-21:s-7]=="http://bit.ly/":   #example http://bit.ly/1KPuqPb
				print 'Found "%s" at %d:%d' % (page[s-21:s], s-21, s)
				comicstrip.update({name: page[s-21:s]})
				print 'Added %s' % name
			else:
				print 'No ComicsKingdom this week :( %s' % page[s-21:s]
				print 'Did not add %s' % name
			#print comicstrip
	


def comicpullgo():
	for name, link in comiclistgo.items():
		request = urllib2.Request(link)
		request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5")

		f = urllib2.urlopen(request)
		page = f.read()

		for match in re.finditer(patterngo, page):
			s = match.end()
			if page[s:s+31]=="https://assets.amuniversal.com/":   #example http://bit.ly/1KPuqPb
				print 'Found "%s" at %d:%d' % (page[s:s+63], s, s+63)
				comicstrip.update({name: page[s:s+63]})
				print 'Added %s' % name
			else:
				print 'No GoComics this week :( %s' % page[s:s+31]
				print 'Did not add %s' % name
			


def htmlcode():
	thecode = '<html><title>The Sunday Comics</title><body><style type="text/css"> .container {width: 600px; margin: 0 auto;} </style><div class="container"><h1>The Sunday Comics</h1>'     
	for name, path in comicstrip.items():
		if name=='NON SEQUITUR by Wiley Miller':
			thecode = thecode + '<p>' + name +'</p>' + '<img src="' + path + '" width="400">'
		else:
			thecode = thecode + '<p>' + name +'</p>' + '<img src="' + path + '" width="600">'
	thecode = thecode + '</div></body></html>'
	return thecode
			

import os
TSC_DB = os.environ.get('TSC_DB')
TSC_USER = os.environ.get('TSC_USER')
TSC_SECRET = os.environ.get('TSC_SECRET')
TSC_HOST = os.environ.get('TSC_HOST')
TSC_PORT = os.environ.get('TSC_PORT')

import psycopg2			

def addtosql():
	conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s port=%s" % (TSC_DB,TSC_USER,TSC_SECRET,TSC_HOST,TSC_PORT))
	cursor = conn.cursor()
   	cursor.execute("insert into comicDB VALUES (%s, %s)", (kingdate , htmlcode() ) )
	conn.commit()				

adddatesking()
adddatesgo()
comicpullgo()
comicpullking()
htmlcode()
addtosql()
#
