import json, urllib2
import gdata.youtube
import gdata.youtube.service

key = "0946dbffa1b5b7ad9c4dc855be73398f"

def getSong(k,name):
    #Gets the URL of a song
    #If there is no song for the name sent in, it rickrolls you.
    
    title = name.split()
    track = ""
    #the next line cuts out the first 2 parts of the address so we can see this works when you click on 42nd street
    #title = title[2:4]
    for item in title:
        track = track + item + "+"
    track = track[:-1]
    track = urllib2.quote(track)
    url = 'http://ws.audioscrobbler.com/2.0/?method=track.search&track="%s"&api_key=%s&format=json'%(track,k)
    print url
    request = urllib2.urlopen(url)
    result = json.loads(request.read())
    print result
    try:
        x = result["results"]["trackmatches"]["track"][0]["url"]
    except:
        x = "http://www.last.fm/music/Rick+Astley/_/Never+Gonna+Give+You+Up?ac=never+gonna+give+you+"
    return x


def getSong2(k,names):
    #Gets the URL of a song
    #If there is no song for the name sent in, it rickrolls you.
    for item in names:
        
        title = item.split()
        track = ""
   #the next line cuts out the first 2 parts of the address so we can see this works when you click on 42nd street
    #title = title[2:4]
        for item in title:
            track = track + item + "+"
        track = track[:-1]
        track = urllib2.quote(track)
        url = 'http://ws.audioscrobbler.com/2.0/?method=track.search&track="%s"&api_key=%s&format=json'%(track,k)
        print url
        request = urllib2.urlopen(url)
        result = json.loads(request.read())
        print result
        try:
            x = result["results"]["trackmatches"]["track"][0]["url"]
            break
        except:
            x = "http://www.last.fm/music/Rick+Astley/_/Never+Gonna+Give+You+Up?ac=never+gonna+give+you+"
    return x


###############
#Youtube Stuff#
###############

def initialize():

    yt_service = gdata.youtube.service.YouTubeService()

    # Turn on HTTPS/SSL access.
    # Note: SSL is not available at this time for uploads.
    yt_service.ssl = True

    yt_service.developer_key = "AI39si5ftQAadvFWghwUFyQgZVRXIj_E-J8bmlv1PeQCZ5dQQneayRz1XV822s8phGDKpqknrl7n0HoiSLwaxfd5HlbU4s2iMg"
    yt_service.client_id = key

def getTopVideo( searchTerm):
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = searchTerm
    query.orderby = 'relevance'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)
    return feed.entry[0]

initialize()
print getTopVideo("tonight")

"""
def getVideo(k,name):
    song = name.split()
    track = ""
    for item in song:
        track = track + item + '%20'
    track = track[:-1]
    track = urllib2.quote(track)
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&key=%s"%(track,k)
    request = urllib2.urlopen(url)
    result = json.loads(request.read())
    print result
"""
#getVideo(key, "believe")


