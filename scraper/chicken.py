import urllib2, re, time

# Globals
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

search_term = "fried_chicken"
results_wanted = 10

site_url = "https://www.reddit.com"
start_url = "https://www.reddit.com/r/food/top/?sort=top&t=all"

def scrape():
    queued = []
    curr_url = start_url
    while len(queued) < results_wanted:
        response = opener.open(curr_url)
        html = response.read()
        if "data-permalink" in html:
            links = re.findall('data-permalink="(\S+)"', html)
            for link in links:
                if search_term in link:
                    queued.append(clean(site_url + link))
        try:
            curr_url = clean(re.findall('"next-button"><a href="(\S+)"', html)[0])
        except:
            break
    return queued

def get_pictures(queued):
    db = []
    for link in queued:
        response = opener.open(link)
        html = response.read()
        new_link = re.findall('data-url="(\S+)"', html)[0]
        db.append(clean(new_link))
    return db

def clean(input):
    return input.replace("amp;", "")
    
def main():
    queued = scrape()
    db = get_pictures(queued)
    print db

if __name__ == '__main__': 
    main()