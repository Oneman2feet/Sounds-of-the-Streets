import utils
import map_utils
import youtube
import json, urllib2
from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key="blah"
Last_key= "0946dbffa1b5b7ad9c4dc855be73398f"
Map_key = "AIzaSyDm3LFbtgPrB8jtcruyGlf9ED-tidYvYrA"

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == 'POST':
        address = request.form['location']
        return search(address)
    else:
        s = map_utils.source()
        address = "default"
        return render_template("map.html", address=address, s=s)



@app.route("/update", methods = ["GET","POST"])
def update():
    address = request.args.get('address', "line goes here")
    useplace = request.args.get('useplace', False)
    print "useplace" + useplace
    #print(address)
    
    listOfAddresses = []
    listOfAddresses = address.split(";")

    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for place in listOfAddresses:
        print(place)
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if useplace:
        song = utils.getSong2(Last_key,address)
    else:
        song = utils.getSong2(Last_key,listOfAddresses)
    url = song[0]
    artist = song[1]
    vidId = youtube.makeParse(artist)
    #print vidId
    r = {'address':listOfAddresses, 'url':url, 'artist':artist, 'vidId':vidId }
    return json.dumps(r)

@app.route("/search", methods = ["GET","POST"])
def search(address):
    names = []
    names.append(address)
    song = utils.getSong2(Last_key,names)
    url = song[0]
    artist = song[1]
    vidIds = youtube.makeParse(artist)
    r = {'address':names[0], 'url':url, 'artist':artist, 'vidId':vidIds }
    return json.dumps(r)

    
if __name__ == '__main__':
    app.run(debug = True, port = 5000)


