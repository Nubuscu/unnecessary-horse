# Unnecessary Horse

## What is it?
A command-line launcher that can open any application or perform google searches. Other features are planned, such as more specific domain searches - steam store, amazon, etc. 

If you can make a shortcut to it, you can launch it from here.
## Prerequisites
* Windows, probably.
* Python (preferably 3. Untested on 2)
* Autohotkey. This is used to make the app runnable from a keyboard shortcut (ctrl+alt+t by default)
* An unwillingness to just use desktop icons because they look gross
* A willingness to spend some time reskinning powershell to look arguably less gross (not blue)
## How to use
1) ### run `pip install -r requirements.txt`
1) ### Create a shortcuts folder
    Make a folder anywhere on your pc and fill it with shortcuts or files you want to open from the app. The names of these are what you'll need to type to run them. Make sure they're shortened and/or easy to remember as they probably aren't by default. For example, `Titanfall™ 2` should become `tf2` or `titanfall`

2) ### Create a `settings.json`.
    There is a file called `example-settings.json`. Rename that to `settings.json` and fill in the details, including the folder you just created above.

3) ### Run the autohotkey script
    double-clicking `uh-keybinding.ahk` should make it last until you turn the PC off. Add a shortcut to the script to your start-up apps in order to make it bind every time you restart. To do this, press `win+r` and enter `shell:startup`. Place the shortcut in this folder.

4) ### ???

5) ### Profit

## Why the name?
see [here](http://projectcodename.com/#)

## Why use it?
I have a bunch of games and movies scattered around DRMs and network locations. This is an attempt to unify the ones I like. That and I miss bash on my windows machine.