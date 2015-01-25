#!/usr/bin/python
# -*- coding: latin-1 -*-

from BeautifulSoup import BeautifulSoup
import urllib2
import os
import sys

"""

PyTube Project (http://www.github.com/sk1m4x/PyTube/)
Copyright (c) 2015 Spade Team - sk1m4x

Thank you, Spade Team Developers. ♠

"""

print "\033[1;37m[ + ]\tWelcome to py\033[41mTube\033[0m"


if len(sys.argv) < 2:
	print "\033[1;31m[ - ]\t\033[0;31mVocê não passou o paramêtro de páginas. (Consulte o README.md em https://github.com/sk1m4x/PyTube/README.md)\033[0m"
	sys.exit()

else:
	search_query = sys.argv[1]
	print "\033[1;33m[sk1]\t\033[0;33mBaixe mais scripts open/closed sources em https://github.com/sk1m4x/"
	print "\n\033[1;36m[...]\033[0;37m\tPesquisando por \033[1;37m'%s'\033[0;37m na pagina \033[1;37m%s." % (search_query, sys.argv[2][-1:])
	for page in sys.argv[2]:
		new_url	=	urllib2.urlopen("https://www.youtube.com/results?page=%s&search_query=%s" % (str(page[0]), search_query.replace(" ", "%20")))

	soup 	=	BeautifulSoup(new_url)

	for each in  soup.findAll('a', attrs={'class' : 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink     spf-link '}):
		print "\033[1;37m\n\n", each.text
		print "\033[0;37myoutube.com"+each.get('href')

	print "\n\n\033[1;32m[ + ]\t\033[0;32mConcluido."
print "\033[0m"
