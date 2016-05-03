#set crontab -e to execute this script

import redis,urllib, json, re, os
r_server = redis.Redis("localhost")


#+++++++++ Get IP from external ++++++++++#
url = "http://jsonip.com"
response = urllib.urlopen(url)
data = json.loads(response.read())

myip = data['ip']
myip = myip.split(',')

#+++++++++ Get IP from database ++++++++++#
idxcn = r_server.llen("mywanip")-1
currentip = r_server.lindex("mywanip", idxcn)
myip = myip[0]

if  myip <> currentip:
	
	r_server.rpush("mywanip",myip)
	print "old:%s" % currentip

	#++++++++ Update noip +++++++++++#
	cmd = "/usr/local/bin/noip2"
	os.system(cmd)

print " current:%s" % myip
