import urllib2, re, time

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

test_url = "https://www.reddit.com/r/food/top/?sort=top&t=all&count=75&after=t3_82y0pj"

search_str = "tendies"
base_url = "https://www.reddit.com/r/food/top/?sort=top&t=all"
reddit_url = "https://www.reddit.com"
curr_url = base_url
visited = []
queued = []
db = []
initial_search = "data-permalink"


while len(queued) < 10:
    print curr_url
#response = opener.open(test_url)
    response = opener.open(curr_url)
    html = response.read()
    if initial_search in html:
        links = re.findall('data-permalink="(\S+)"', html)
        for link in links:
            if search_str in link:
                queued.append(reddit_url + link)
    #print html
    try:
        curr_url = re.findall('"next-button"><a href="(\S+)"', html)[0]
    except:
        print "done with top 1000"
        break
    
print queued

for link in queued:
    time.sleep(2)
    print "Link:", link 
    response = opener.open(link)
    html = response.read()
    db.append(re.findall('data-url="(\S+)"', html)[0])

for item in db:
    if "reddituploads" in item:
        item = item.replace("amp;", "")

print db