from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Playback)
unvanquished = AppContext(title="unvanquished")
grammar = Grammar("unvanquished", context=(unvanquished))

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

# Macros for playing the game Unvanquished (https://github.com/Unvanquished/Unvanquished)
# I made this completely as a joke. It does work well enough to kind of move
# around the maps, but the latency from speech recognition is really high
# (like, 1+ seconds sometimes) so don't expect to get any frags.

rules = MappingRule(
    name = "unvanquished",
    mapping = {
      # open console and set character to constantly fire
      "attack":   Key("backtick") + Text("/+attack") + Key("enter,backtick")

      # start walking forward
      "go go go":  Key("e:down"),

      # walk forward for a short distance
      "advance":   Key("e:down/20, e:up"),

      # release movement to stop moving
      "stop":      Key("e:up,d:up,f:up,s:up"),

      # open buy menu
      "by":        Key("q"),

      # movement keys
      "dough":     Key("e:down"),
      "ray":       Key("d:down"),
      "me":        Key("f:down"),
      "sow":       Key("s:down"),


      # View commands (these replace the mouse)

      # rotate view left
      "yes":       Key("left:down,right:up"),

      # rotate view right
      "hello" :    Key("right:down,left:up"),

      # stop view from rotating
      "very" :     Key("left:up,right:up,up:up,down:up"),
    },

    extras = [
        Dictation("text", format=False),
        Integer("n", 1, 20000),
        Integer("scroll_by", 1, 20000),
      ],
    defaults = {
      "text" : "", 
      "n" : 1,
      "scroll_by" : 10
      }
    )
 
grammar.add_rule(rules)
grammar.load()
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
