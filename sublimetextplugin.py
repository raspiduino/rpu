'''
rpu - The stupid realtime Python updater
Copyright @raspiduino 2021
Date created 27/1/2021
----------------------------------------
This is the plugin for sublimetext for
auto saving.
'''

import sublime
import sublime_plugin

class AutoSaveCommand(sublime_plugin.EventListener):
    def on_modified(self, view):
        view.run_command('save')
