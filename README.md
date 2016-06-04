## Xscripts

### Various scripts trying to homogenize colors between GTK and other graphical apps

#### Right now, only `xappspicker` is fully working

```
What does it do ?
It grabs the bg and fg colors from the current theme (now with python! much
easier!), and sets them as back or foreground for the Xapps. (they can be
customized only by Xresources)
also see forums.bunsenlabs.org/viewtopic.php?id=1941

 - additionally, it defines colors for dmenu.
 - it will invert the background color, and slightly darken it, and use the 2
   resulting colors to create a root window background with xsetroot.
 - xsetroot will utilize a bitmap, if it exists in the theme's root directory,
   and is named "xsetrootbitmap.xbm"
 - if ./conky/theme.conkyrc exists in the theme's root directory, it will be
   started - but only if it isn't already running.
   
if you don't want some particular function, it is easy to comment it out in the
MAIN section (line 163 =>)
```
