# BuildParts (version 0.1.0)

This is a Sublime Text plugin for executing (or building) part of your code. 

## Installation

Install using Package Control (Recommanded)

1. I guess most Sublime Text 2 users are using Sublime Package Control. If not, please install it from here <http://wbond.net/sublime_packages/package_control>
2. Go to Preference > Package Control, and Choose "Install Package"
3. Choose the package named "BuildParts" to install it
4. If BuildParts is not available from Package Control, you can go to Preference > Package Control, and Choose "Add Repository". Put "https://github.com/erinata/BuildParts" (without quotes) to add the repo and try step 2 and 3 again.

Install manually

1. Download the repo
2. Copy everything in the repo to a folder named "BuildParts" under the package folder of SublimeText 2 (create it if it doesn't exist)

## Usage

There is only one command: `BuildParts: Build the selected code`

When you select some code and invoke this command, this package will build the selected code using the currently chosen build system. If you have selected nothing, this package will build the whole file. (So that you still get the default Sublime Text build system behaviour)

BuildParts default keybindings are "ctrl+b" (for Windows and Linux) and "super+b" (for Mac). It's the same as the default keybinding for building your code. If you want to invoke the build system for the whole file. Just select nothing and press "ctrl+b".

Example:

Suppose you have a document named `hello.rb`

    Puts("Hello")
    Puts("World")
    Puts("Everyone")

Suppose you select the first 2 lines, and press "ctrl+b", the package will only build the currently selected parts (which are first 2 lines in this case). The build output console will show:

    Hello
    World

It is useful when you want to execute several lines of your code (especially for interpreted language say Ruby) and see how it works.

If you select nothing and press "ctrl+b", the package will involve the default behaviour in Sublime Text and build the whole file. The build output console will show:

    Hello
    World
    Everyone

As BuildParts utilizes the build system in Sublime Text, it supports any language that Sublime Text can build. It also work with custom build systems that are installed via packages.

## Limitation

BuildParts is not supporting multiple selections for now.

## Operating Systems

I only tested this on Windows, I hope that it works on OSX and Linux.

## License

Copyright (C) 2012 Tom Lam. MIT License.
  
