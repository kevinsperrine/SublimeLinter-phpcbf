SublimeLinter-phpcbf
=========================
Fork of [https://github.com/SublimeLinter/SublimeLinter-phpcs](https://github.com/SublimeLinter/SublimeLinter-phpcs) with changes to support phpcbf within SublimeLinter.

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phpcbf.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phpcbf)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org/) provides an interface to [phpcbf](http://pear.php.net/package/PHP_CodeSniffer/). It will be used with files that have the “PHP”, “HTML” and “HTML5” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `phpcbf` is installed on your system, preferably somewhere in your PATH. To install `phpcbf`, follow the instructions on https://github.com/squizlabs/PHP_CodeSniffer#installation. Once `phpcbf` is installed, you can proceed installing the `SublimeLinter-phpcbf` plugin if you did not already do this (the order does not matter).

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `phpcbf`. Among the entries you should see `SublimeLinter-phpcbf`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

### Project Specific Executable
It is possible to specify the `phpcbf` executable that should be used to lint your code on a per-project level.

**Example:**
```json
{
    "SublimeLinter": {
        "linters": {
            "phpcbf": {
                "cmd": "${project}/vendor/bin/phpcbf"
            }
        }
    }
}
```

### Per-project Standards
You can set up your project settings to use a specific standard using the following:

```json
{
    "SublimeLinter": {
        "linters": {
            "phpcbf": {
                "standard": "${project}/phpcbf.xml"
            }
        }
    }
}
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
