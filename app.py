import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkSource", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, GtkSource, Vte, GLib

class EditorPane(Gtk.ScrolledWindow):
    def __init__(self):
        super().__init__()
        # Create GtkSource buffer and view
        self.buffer = GtkSource.Buffer()
        self.view = GtkSource.View.new_with_buffer(self.buffer)
        self.view.set_show_line_numbers(True)
        self.add(self.view)

class TerminalPane(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        
        # Create terminal
        self.terminal = Vte.Terminal()
        
        # Add terminal to a scrolled window
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.terminal)
        
        # Set fixed height for terminal area
        self.set_size_request(-1, 200)
        
        self.pack_start(scrolled, True, True, 0)

        # Spawn shell synchronously first (simpler approach)
        try:
            self.terminal.spawn_sync(
                Vte.PtyFlags.DEFAULT,
                GLib.get_home_dir(),
                ["/bin/bash"],
                [],
                GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                None,
                None
            )
        except GLib.Error as e:
            print("Failed to spawn terminal:", e.message)
            # Fallback to simpler shell
            try:
                self.terminal.spawn_sync(
                    Vte.PtyFlags.DEFAULT,
                    GLib.get_home_dir(),
                    ["/bin/sh"],
                    [],
                    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                    None,
                    None
                )
            except GLib.Error as e:
                print("Failed to spawn fallback terminal:", e.message)
