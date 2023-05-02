import requests
import os
import urllib.parse as up
import psycopg2


from datetime import date
today = date.today().toordinal()
prevsunday = today - (today % 7)
sundaydate = date.fromordinal(prevsunday)
kingdate = sundaydate.strftime("%Y-%m-%d")
godate = sundaydate.strftime("%Y/%m/%d")

comicstrip = {}

patterngo = 'property="og:image" content="'
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
"BABY BLUES by Rick Kirkman and Jerry Scott": "http://www.gocomics.com/babyblues/",
"MOTHER GOOSE & GRIMM by Mike Peters": "http://www.gocomics.com/mother-goose-and-grimm/",
"CRANKSHAFT by Tom Batiuk and Chuck Ayers": "http://www.gocomics.com/crankshaft/",
#"CATHY by Cathy Guisewite": "http://www.gocomics.com/cathy/" #Cathy is too lame
}

patternking = ' name="twitter:image" content="'
comiclistking = {
"FAMILY CIRCUS by Bil and Jeff Keane": "http://comicskingdom.com/family-circus/",
"BLONDIE by Dean Young and John Marshall": "http://comicskingdom.com/blondie/",
"BEETLE BAILEY by Mort Walker": "http://comicskingdom.com/beetle-bailey-1/",
# Funky Winkerbean officially ended on 2022-12-31 - Crankshaft is still going, though!
"FUNKY WINKERBEAN by Tom Batiuk": "http://comicskingdom.com/funky-winkerbean/",
"HAGAR THE HORRIBLE by Chris Browne": "http://comicskingdom.com/hagar-the-horrible/",
"HI AND LOIS by Brian Walker, Greg Walker and Chance Browne": "http://comicskingdom.com/hi-and-lois/",
"ZITS by Jerry Scott and Jim Borgman": "http://comicskingdom.com/zits/",
"SALLY FORTH by Francesco Marciuliano; drawn by Jim Keefe": "http://comicskingdom.com/sally-forth/",
"PRINCE VALIANT by Mark Schultz and Thomas Yeates": "http://comicskingdom.com/prince-valiant/",
"MUTTS by Patrick McDonnell": "http://comicskingdom.com/mutts/",
"MARY WORTH by Karen Moy and Joe Giella": "http://comicskingdom.com/mary-worth/",
}

def adddatesking():
    for name, address in comiclistking.items():
        comiclistking[name] += kingdate

def adddatesgo():
    for name, address in comiclistgo.items():
        comiclistgo[name] += godate

def comicpullking():
    for name, link in comiclistking.items():
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(link, headers=headers).content.decode()

        if page.find(patternking)>0:
            comicstrip.update({name: page.split(patternking)[1].split('"')[0]})
            print('Found and added %s' % name)

        else:
            print('ComicsKingdom: Did not add %s' % name)

def comicpullgo():
    for name, link in comiclistgo.items():
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(link, headers=headers).content.decode()

        if page.find(patterngo)>0:
            comicstrip.update({name: page.split(patterngo)[1].split('"')[0]})
            print('Found and added %s' % name)

        else:
            print('GoComics: Did not add %s' % name)

def htmlcode():
    thecode = '<html><title>The Sunday Comics</title><body><style type="text/css"> .container {width: 600px; margin: 0 auto;} </style><div class="container"><h1>The Sunday Comics</h1>'
    for name, path in comicstrip.items():
        if name=='NON SEQUITUR by Wiley Miller':
            thecode = thecode + '<p>' + name +'</p>' + '<img src="' + path + '" width="400">'
        else:
            thecode = thecode + '<p>' + name +'</p>' + '<img src="' + path + '" width="600">'
    thecode = thecode + '</div></body></html>'
    return thecode

def uploadsql():
        up.uses_netloc.append("postgres")
        url = up.urlparse(os.environ["DATABASE_URL"])
        conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port
                     )
        cursor = conn.cursor()
        cursor.execute('''insert into comicDB VALUES ('%s', '%s')''' % (kingdate, htmlcode()))
        conn.commit()
        cursor.close()

adddatesking()
adddatesgo()
comicpullgo()
comicpullking()
uploadsql()

