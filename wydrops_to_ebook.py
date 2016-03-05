#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# author: KevAxe
# email: kevaxe@qq.com

import ConfigParser
import optparse
import os,sys

def check_recipe_dir():
	f = open('wydrops_to_ebook.recipe','r+')
	flist = f.readlines()
	path_arg = "	file_path = '"+os.path.split(os.path.realpath(__file__))[0]+"'\n"
	if flist[10] != path_arg:
		flist[10] = path_arg
		f = open('wydrops_to_ebook.recipe','w+')
		f.writelines(flist)
if __name__ == '__main__':
	check_recipe_dir()
	parser = optparse.OptionParser('usage: %prog [options] argv')
	parser.add_option('-t','--title',dest='title',type='string',default='WooYunDrops',help='Title of your book')
	parser.add_option('-f','--format',dest='format',type='string',default='mobi',help='Book format')
	parser.add_option('-s','--start',dest='start_page',type='int',default=1,help='Start page of the website you want')
	parser.add_option('-e','--end',dest='end_page',type='int',default=0,help='End page of the website you want')
	parser.add_option('-r','--reverse',dest='reverse_article_order',action='store_true',help='From the old to the new article')
	parser.add_option('-k','--key',dest='search_key',type='string',default='',help='The key of WooYunDrops search')
	parser.add_option('-c','--category',dest='category',type='string',default='',help='The category you want')

	(options, args) = parser.parse_args()
	print options
	conf = ConfigParser.ConfigParser()
	conf.read('rule.conf')
	conf.set('info','title',options.title)
	conf.set('info','reverse_article_order',options.reverse_article_order)
	conf.set('info','start_page',options.start_page)
	conf.set('info','end_page',options.end_page)
	conf.set('info','search_key',options.search_key)

	category = ''
	if not options.category.strip() == '':
		category = '/category/' + options.category
	conf.set('info','category',category)
	
	conf.write(open('rule.conf','w'))
	#sys.path[0]
	os.system('ebook-convert wydrops_to_ebook.recipe '+ options.title + '.' + options.format)
