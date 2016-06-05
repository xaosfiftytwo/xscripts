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
  and is named "xsetrootbitmap.xbm". Or, if `$bitmapdir` is defined, it will
  choose a random .xbm from there. Some simple tiles are provided in the `xbm`
  directory.
- if `$conkydir` is defined, `$conkydir/xappspicker.conkyrc` will be started.
  Else, if `./conky/xappspicker.conkyrc` exists in the theme's root directory,
  it will be started.
- another option is to invert particular colors, and use them for xsetroot.
   
Adjustments are made in the MAIN section (the last 25 or so lines of the script).

#### Requirements:

- a fairly recent version of `bash`, I'd guess.  
- `python 2.x`, and the `gtk` module. I'm not good with python, but I'm fairly 
  sure that this is included in a package called `pygtk`. And you most probably
  already have it.
- `xsetroot`
- `bc` command line calculator.
- the optional `do_conky` function relies on `pgrep`.
 
#### Tips

You can set up `inotifywatch` to watch for changes in `~/.gtkrc-2.0` by adding
this to your `~/.xinitrc` or `~/.config/openbox/autostart` or some such:  
`( xappspicker ; while :; do inotifywait -e modify ~/.gtkrc-2.0 ; xappspicker ; done ) & disown`

With the `bitmap` program you can create .xbm tiles.

Try out the `xappspicker.py` script to see what other color values can be accessed
(un/comment some sections).

[1]: https://gist.githubusercontent.com/dcat/896ff92229de70e4e5ca/raw/7399f404afbf5159758cf11a6a3e6117e7acf748/tile.xbm