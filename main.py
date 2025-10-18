import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from app import EditorPane, TerminalPane

class EasyEditor(Gtk.Window):
    def __init__(self):
        super().__init__(title="EasyEditor")
        self.connect("destroy", Gtk.main_quit)
        
        # Set window as resizable
        self.set_resizable(True)
        
        # Set default window size
        self.set_default_size(1200, 800)
        
        # Set minimum window size
        self.set_size_request(600, 400)
        
        # Set window position
        self.set_position(Gtk.WindowPosition.CENTER)

        # Use Paned for resizable split
        self.paned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.paned)

        # Editor pane (top part)
        self.editor = EditorPane()
        self.paned.add1(self.editor)

        # Terminal pane (bottom part, resizable)
        self.terminal = TerminalPane()
        self.paned.add2(self.terminal)

        # Set initial position (terminal starts at 200px height)
        self.paned.set_position(600)

        # Maximize window on start
        self.maximize()

if __name__ == "__main__":
    win = EasyEditor()
    win.show_all()
    Gtk.main()
