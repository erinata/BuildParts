# BuildParts (version 0.1.0)

This is a Sublime Text plugin for executing (or building) part of your code. 

## Installation

Install using Package Control (Recommanded)

1. I guess most Sublime Text 2 users are using Sublime Package Control. If not, please install in from here <http://wbond.net/sublime_packages/package_control>
2. Go to Preference > Package Control, and Choose "Install Package"
3. Choose the package named "BuildParts" to install it
4. If BuildParts is not available from Package Control, you can go to Preference > Package Control, and Choose "Add Repository". Put "https://github.com/erinata/BuildParts" (without quotes) to add the repo and try step 2 and 3 again.

Install manually

1. Download the repo
2. Copy everything in the repo to a folder named "BuildParts" under the package folder of SublimeText 2 (create it if it doesn't exist)

## Usage

There is only one command: `BuildParts: Build the selected code`

When you run this command, it will build the code that you have selected using the build system selected by Sublime Text. If you have selected nothing, it will build the whole file.

BuildParts default keybindings are "ctrl+b" (for Windows and Linux) and "super+b" (for Mac). It's the same as the default keybinding for building your code. If you want to invoke the build system for the whole file. Just select nothing and press "ctrl+b".

Example:

Suppose you have a document named `testing.rb`

    Puts("Hello")
    Puts("World")
    Puts("Everyone")

If you select nothing and press "ctrl+b", Sublime Text will build the whole file and the build output console will show:

    Hello
    World
    Everyone

Suppose you select the first 2 lines, and press "ctrl+b", Sublime Text will only build the current selected parts and the build output console will show:

    Hello
    World

As BuildPart utilizes the build system in Sublime Text, it supports any language the Sublime Text can build. It also work with custom build systems that are install via packages.

## Limitation

Currently this plugin can only use the build system automatically chosen by Sublime Text. Therefore it will use the `Ruby` build system when the file extension is `.rb`. And this means you can choose to build parts of code using `Python` build system if those code are in a `.rb` file.

## Operating Systems

I only tested this on Windows, I hope that it works on OSX and Linux.

## License

Copyright (C) 2012 Tom Lam. MIT License.
  
