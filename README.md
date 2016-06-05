## Xscripts

### Various scripts trying to homogenize looks between GTK and other graphical apps

#### Right now, only `xappspicker` is fully working.

#### What does `xappspicker` do ?
It grabs the background, foreground and highlight colors from the current GTK2
theme (now with python! much easier!), and sets them as back or foreground 
for the Xapps. (they can be customized only by Xresources)
also see forums.bunsenlabs.org/viewtopic.php?id=1941

- additionally, it defines colors for dmenu.
- it will set the brightness of the highlight color to two defined values,  
  and use the 2 resulting colors to create a root window background with xsetroot.
- xsetroot will utilize a bitmap, if it exists in the theme's root directory,
  and is named "xsetrootbitmap.xbm"
- if ./conky/theme.conkyrc exists in the theme's root directory, it will be
  started - but only if it isn't already running. The idea is to have conky
  display something that visually enhances the wallpaper, e.g. an emblem, but 
  of course it can be anything...
- another option is to invert particular colors, and use them for xsetroot.
   
if you don't want some particular function, it is easy to comment it out in the
MAIN section (line 181 =>)

#### Requirements:

- `python 2.x`, and the `gtk` module. I'm not good with python, but I'm fairly 
  sure that this is included in a package called `pygtk`. And you most probably
  already have it.
- `xsetroot`
- `bc` command line calculator.
- a fairly recent version of `bash`, I'd guess.  
- the optional `do_conky` function relies on `pgrep`.
 
#### Tips

You can set up `inotifywatch` to watch for changes in `~/.gtkrc-2.0` by adding
this to your `~/.xinitrc` or `~/.config/openbox/autostart` or some such:  
`( xappspicker ; while :; do inotifywait -e modify ~/.gtkrc-2.0 ; xappspicker ; done ) & disown`

With the `bitmap` program you can create .xbm tiles. Here's one [example][1]
(right-click and save as `xsetrootbitmap.xbm` in the current theme folder).

[1]: https://gist.githubusercontent.com/dcat/896ff92229de70e4e5ca/raw/7399f404afbf5159758cf11a6a3e6117e7acf748/tile.xbm