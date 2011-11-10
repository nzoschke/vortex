from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

scan_command = Subcommand('scan', help='scan directory for updates')
def scan(lib, config, opts, args):
    d = config.get("beets", "directory")
    print "Scanning %s..." % d
scan_command.func = scan

class SuperPlug(BeetsPlugin):
    def commands(self):
        return [scan_command]