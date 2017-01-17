from dragonfly import (MappingRule, Key, Mouse, FocusWindow, Text, Integer, Dictation, IntegerRef, CompoundRule, Grammar)

rules = MappingRule(
    name = "general",
    mapping = {
        # This is redundant with multiedit, but, I break multiedit
        # occasionally and not having this command available drives me crazy.
        # afaik it doesn't cause any problems.
        "slap": Key("enter"),

        "Max when": Key("w-up"),
        "min win": Key("w-down"),
        "window dell": Key("w-d"),

        # Fill half of screen, or shift to next monitor if already on the edge
        "left when": Key("w-left"),
        "right when": Key("w-right"),

        # Move window between monitors
        "Window left": Key("ws-left"),
        "Window right": Key("ws-right"),

        # Volume
        "louder [<n>]": Key("volumeup:%(n)d"),
        "loud": Key("volumeup:20"),
        "quieter [<n>]": Key("volumedown:%(n)d"),
        "quiet": Key("volumedown:100") + Key("volumeup:25"),
        "mute": Key("volumemute"),

        # This is a hack to make the volume slider pop up so you can
        # see the current volume. It will unmute as a side effect.
        "tell volume": Key("volumeup, volumedown"),

        # Voice-activated media keys are the best
        "media play": Key("playpause"),
        "media skip": Key("tracknext"),
        "media back": Key("trackprev"),

        # Note that spoken movement commands defined in multiedit will close
        # this after completing because they release all modifier keys. This
        # can make navigation hard if you haven't memorized how movement keys
        # work in the alt-tab window. But, it's OK because something needs to
        # release the alt key after this executes.
        # You could define alternative movment commands that do not release alt,
        # If you do, the enter command from multiedit is probably the most
        # convenient way to select and release alt.
        "switch apps": Key("alt:down, tab"),

        "switch app": Key("a-tab"),

        # Handy if you have a sore index finger
        "Grab window": Mouse("(0.5,10), left:down"),
        "oink": Mouse("left:down"),
        "boink": Mouse("left:up"),

        # I use this to reload NatLink macros
        "toggle Dragon": Key("np1,np1"),

        "swap gmail": FocusWindow(executable="chrome.exe",title="Gmail"),
        "swap gee vim": FocusWindow(executable="gvim.exe"),
        "task manager": Key("cs-escape"),

        "run command": Key("w-r"),
        "run command MS paint": Key("w-r/10") + Text("mspaint") + Key("enter"),

        # Move mouse to middle of current window
        "mouse center": Mouse("(0.5, 0.5)"),

        # Absolute mouse movement commands assume the following monitor layout:
        #  (from left to right): 1920x1080 1920x1080 1080x1920

        # Middle of left monitor
        "mouse tall": Mouse("[960, 540]"),

        # Middle of middle monitor
        "mouse Venti": Mouse("[2880, 540]"),

        # Middle of right monitor
        "mouse grawnday": Mouse("[4380, 540]"),
    },

    extras = [
        Integer("n", 0, 10),
        Dictation("text"),
        ],
    defaults = { "n": 0, },
)

class VolumeRule(CompoundRule):
    spec = "volume <v>"
    extras = [IntegerRef("v", 0, 100),]
    defaults = { "v": 30 }

    def _process_recognition(self, node, extras):
        # Amount volume changes per volumeup key press.
        # change if "volume X" sets your volume to something other than X
        VOLUME_CHANGE_PER_KEYPRESS = 2
        v = extras["v"]

        # set volume to 0
        Key("volumedown:"+str(int(100/VOLUME_CHANGE_PER_KEYPRESS))).execute()

        # increase to desired amount by pressing the volumeup key multiple times
        # I could set the volume directly with COM automation,
        # but fuuuuuuck that.
        Key("volumeup:"+str(int(v/VOLUME_CHANGE_PER_KEYPRESS))).execute()


grammar = Grammar("general")
grammar.add_rule(rules)
grammar.add_rule(VolumeRule())

grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
