#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

class EasyEditor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Easy Editor")
        self.set_default_size(800, 600)
        
        # Simple text area
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        
        # Add to window
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.textview)
        self.add(scrolled)

# Create and show window
win = EasyEditor()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
