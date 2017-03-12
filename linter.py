#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dmitry Tsoy
# Copyright (c) 2013 Dmitry Tsoy
#
# Updated by Kevin Perrine
# Copyyright (c) 2017 Kevin Perrine
#
# License: MIT
#

"""This module exports the Phpcbf plugin class."""

from SublimeLinter.lint import Linter


class Phpcbf(Linter):
    """Provides an interface to phpcbf."""

    syntax = ('php', 'html', 'html 5')
    executable = 'phpcbf'
    defaults = {
        '--standard=': 'PSR2'
    }
    inline_overrides = ('standard')

    def cmd(self):
        """Read cmd from inline settings."""
        settings = Linter.get_view_settings(self)

        if 'cmd' in settings:
            command = [settings.get('cmd')]
        else:
            command = [self.executable_path]

        command.append('*')
        command.append('@')

        return command
