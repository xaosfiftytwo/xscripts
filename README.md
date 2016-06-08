### Various scripts to unify looks between GTK and other graphical apps

#### What's the idea of `xappspicker`?

The idea is to give you maximum control over the looks of your desktop, based
on the contents of your current theme folder.  
You can create custom configs for various apps, put them in your theme folder,
and if you change your GTK2 theme, these apps will also change their looks accordingly.

That is, if you don't already use some desktop environment, and prefer to roll 
your own.  
And if you like the minimal looks of apps like `dmenu` or `xpdf` or `xsetroot`.

The current theme folder is chosen through the file `~/.gtkrc-2.0`, which is
typically modified by an application like `lxapearance` (works great on _any_
desktop), but can also be edited manually.

#### What does `xappspicker` do ?

    It grabs some colors from the current gtk2 theme:
     0: base foreground
     1: base background
     2: selected text foreground
     3: selected text background
    and puts them into the fgbg array.
    it then uses these colors to style some apps:
     - adjust_xapps: create an additional file with X resources, and make sure 
       it is sourced (see man xrdb) 
     - adjust_dmenu: define colors for dmenu, if you use a dmenurc file (see 
       the included dmenu wrapper script)
     - adjust_xsetroot: create a root window background with xsetroot.
       xsetroot will utilize a bitmap, if it exists in the theme's root directory,
       and is named "xsetrootbitmap.xbm"
       color adjustments are possible, please see towards the end of the script.
     - do_conky:
       1. a conky running with "-c ./conky/xappspicker.conkyrc" will be killed.
       2. if ./conky/xappspicker.conkyrc exists in the theme's root directory,
       it will be re-started.

*Please read and make your adjustments in the MAIN section at the bottom of
the script!*

#### Requirements:

 - `python 2.x`, and the `gtk` module. I'm not good with python, but I'm fairly 
sure that this is included in a package called `pygtk`. And you most probably
already have it.
 - `xsetroot`
 - a fairly recent version of `bash`, I'd guess.  
 - the optional `do_conky` function relies on `pgrep`.
 
#### Tips

To avoid running the whole script after login, the script creates a file that 
should be sourced instead.
by default, add `. "$HOME/.local/share/xorg/xappspicker_rc"` to your
autostart file (typically `~/.xinitrc` or `~/.config/openbox/autostart`).

You can set up `inotifywatch` to watch for changes in `~/.gtkrc-2.0` by adding
this to your autostart file:  
`( while :; do inotifywait -e modify ~/.gtkrc-2.0 ; xappspicker ; done ) & disown`

With the `bitmap` program you can create .xbm tiles.

Try out the `xappspicker.py` script to see what other color values can be accessed
(un/comment some sections).

also see [this forum thread](https://forums.bunsenlabs.org/viewtopic.php?id=1941).
