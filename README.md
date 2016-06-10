### Various scripts to unify looks between GTK and other graphical apps

#### What's the idea of `xappspicker`?

The idea is to change the looks of your desktop each time you change your GTK2
theme.

That is, if you don't already use some desktop environment, and prefer to roll 
your own.  
And if you like and use apps like `tint2`, `dmenu`, or Xapps like `xpdf`,
`xfontsel`, `xsetroot` (and its use of 2-tone bitmaps).

#### What does `xappspicker` do ?

The current theme folder is chosen through the file `~/.gtkrc-2.0`, which is
typically modified by an application like `lxapearance` (works great on _any_
desktop), but can also be edited manually.

It then grabs some colors from the current gtk2 theme:

0. base foreground
1. base background
2. selected text foreground
3. selected text background

and puts them into the `fgbg` array.

It then executes functions that use these colors to style some apps:
- adjust_xapps: create an additional file with X resources, and make sure 
it is sourced (see man xrdb) 
- adjust_dmenu: define colors for dmenu, if you use a dmenurc file (see 
the included dmenu wrapper script)
- adjust_xsetroot: create a root window background with xsetroot.
xsetroot will use a random bitmap from a defined folder, or use
`xsetrootbitmap.xbm` if it exists in the theme's root directory, or generate
a random -mod pattern (see `man xsetroot`).
color adjustments are possible, please see towards the end of the script.
- adjust_tint2: if the theme folder contains `tint2/tint2rc`, tint2 will be
started with this config file, otherwise tint2 will be started with its
default config file (usually `~/.config/tint2/tint2rc`).
- The script also looks for an executable file called `xappspicker.exec` in
the current theme folder, and executes it if found. It can be anything,
a shell or python script, a C program...

*Please read and make your adjustments in the MAIN section at the bottom of
the script!*

#### Requirements:

 - `python 2.x`, and the `gtk` module. I'm fairly sure that this is included in
   a package called `pygtk`. And you most probably already have it.
 - `xsetroot`
 - a fairly recent version of `bash`, I'd guess.  
 - `bc` (command line calculator).
 - `hexdump` and `shuf` for the posix compliant random functions.
 
#### Tips

It is possible to simply run the script as is at login.

However, the script isn't exactly fast and might create a noticeable lag during
login.

To avoid that, the script generates a file `$HOME/.local/share/xorg/xappspicker_rc`.  
The idea is:

* Instead of executing the script, source `$HOME/.local/share/xorg/xappspicker_rc`
  at login.
* Set up `inotifywatch` (or some such) to watch for changes in `~/.gtkrc-2.0` and
  execute the script only when needed.

You can achieve this by adding something like this to your autostart file (typically
`~/.xinitrc` or `~/.config/openbox/autostart`):

    dash -c '. "$HOME/.local/share/xorg/xappspicker_rc";sleep 5; while :; do inotifywait -e modify $HOME/.gtkrc-2.0; /path/to/xappspicker; done' &

I recommend using dash instead of bash; it is much faster, and everything has
been tested to work with dash's limited capabilities.

You can create .xbm tiles with the `bitmap` program.

You can symlink the script `xappspicker` to somewhere in your `$PATH`; however,
do not copy over the actual script.

Try out the `xappspicker.py` script to see what other color values can be accessed
(un/comment some sections).

also see [this forum thread](https://forums.bunsenlabs.org/viewtopic.php?id=1941).
