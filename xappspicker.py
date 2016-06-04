#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# thanks to this:
# bytes.com/topic/python/answers/748007-pygtk-theme-colors

#~ import pygtk
#~ pygtk.require('2.0')
import gtk
#~ import sys

#~ print 'Number of arguments:', len(sys.argv), 'arguments.'
#~ print 'Argument List:', str(sys.argv[1])

w = gtk.Window()
w.realize()
style=w.get_style()

l=[gtk.STATE_NORMAL,gtk.STATE_ACTIVE,gtk.STATE_PRELIGHT,gtk.STATE_SELECTED,gtk.STATE_INSENSITIVE]
#~ for i in l:
	#~ print "- base",i,style.base[i].to_string()
#~ for i in l:
	#~ print "- text",i,style.text[i].to_string()
#~ for i in l:
	#~ print "- fg",i,style.fg[i].to_string()
#~ for i in l:
	#~ print "- bg",i,style.bg[i].to_string()

#~ for i in l:
	#~ print "- base",i,style.base[i]
#~ for i in l:
	#~ print "- text",i,style.text[i]
#~ for i in l:
	#~ print "- fg",i,style.fg[i]
#~ for i in l:
	#~ print "- bg",i,style.bg[i]

#~ if sys.argv[1] == 'fg':
	#~ print style.fg[gtk.STATE_NORMAL]
#~ if sys.argv[1] == 'bg':
	#~ print style.bg[gtk.STATE_NORMAL]

print style.fg[gtk.STATE_NORMAL].to_string()
print style.bg[gtk.STATE_NORMAL].to_string()
#~ print style.bg[gtk.STATE_SELECTED]

#~ print style.fg[gtk.STATE_NORMAL].to_string()
#~ print style.bg[gtk.STATE_NORMAL].to_string()

