from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

putty_context = AppContext(executable="putty")
kitty_context = AppContext(executable="kitty")
virtualbox_context = AppContext(executable="virtualbox")
bash_context = AppContext(executable="bash")
sh_context = AppContext(executable="sh")
conemu64_context = AppContext(executable="ConEmu64")
grammar = Grammar("bash", context=(putty_context | sh_context | bash_context | kitty_context | virtualbox_context | conemu64_context))
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "bash",
    mapping = {
      "watch macros": Text("cd ~/Documents/GitHub/code-by-voice && ./node_modules/.bin/gulp") + Key('enter'),

      "pseudo": Text("sudo "),

      # navigation
      "make der": Text("mkdir ") + noSpaceNoCaps,
      "CD": Text("cd ") + noSpaceNoCaps,
      "push dee": Key("p,u,s,h,d,space"),
      "pop dee": Key("p,o,p,d,enter"),
      "dirs": Key("d,i,r,s,enter"),
      "up directory": Text("cd ..") + Key('enter'),
      "list files": Text("ls -l") + Key("enter"),
      "LS": Text("ls"),
      "LS long": Text("ls -l"),
      "go home": Text("cd ~") + Key("enter"),
      "run": Text("./"),
      "cancel": Key("c-c"),
      "exit": Key("c-d"),

      # particular programs
      "aptitude install" : Text("apt-get install "),
      "pseudo aptitude install" : Text("sudo apt-get install "),
      "them": Text("vim "),
      "W get": Text("wget "),
      "flex": Text("flex "),
      "GCC": Text("gcc "),

      "make": Text("make "),
      "make test": Text("make test") + Key("enter"),
      "make all": Text("make -B") + Key("enter"),
      "windows make": Text("mingw32-make.exe") + Key("enter"),
      "windows make all": Text("mingw32-make.exe -B") + Key("enter"),

      "docker": Text("docker "),
      "docker run": Text("docker run "),

      "NPM": Text("npm "),
      "NPM install": Text("npm install"),

      "ebb": Text("eb "),
      "ebb in it": Text("eb init "),
      "ebb create": Text("eb create "),

      "vagrant upper": Text("vagrant up"),
      "vagrant ssh": Text("vagrant ssh"),
      "vagrant destroy": Text("vagrant destroy"),
      "vagrant reload": Text("vagrant reload"),
      "vagrant reload [dash dash] provision": Text("vagrant reload --provision"),
      "CD slash vagrant": Text("cd /vagrant"),

      # tmux
      "tmux attach": Text("tmux attach") + Key("enter"),
      "tmux attach dash tee": Text("tmux attach -t "),
      "tmux new": Text("tmux new -s "),
      "tmux Ellis": Text("tmux ls") + Key("enter"),
      "tmux": Text("tmux"),

      "term detach": Key("c-b, d"),
      "term prefix": Key("c-b"),
      "term vertical": Key("c-b,percent"),
      "term split": Key("c-b,dquote"),
      "term west": Key("c-b,left"),
      "term east": Key("c-b,right"),
      "term north": Key("c-b,up"),
      "term south": Key("c-b,down"),
      "term create window": Key("c-b,c"),
      "term list windows": Key("c-b,w"),
      "term next window": Key("c-b,n"),
      "term previous window": Key("c-b,p"),
      "term name window": Key("c-b,comma"),
      "term zoom": Key("c-b,z"),
      "term copy": Key("c-b,lbracket"),
      "term pane <n>": Key("c-b,q,%(n)d"),
      "term window <n>": Key("c-b,w,%(n)d"),
      "term reload config": Key("c-b,colon") + Text("source-file ~/.tmux.conf") + Key("enter"),

      # git
      "git": Text("git "),
      "get": Text("git "),
      "status": Text("status"),
      "diff": Text("diff"),
      "commit": Text("commit"),
      "origin": Text("origin "),

      "get add ": Text("git add "),
      "get add [dash dash] patch": Text("git add --patch"),
      "get branch": Text("git branch "),
      "get check out": Text("git checkout "),
      "get check out dash bee": Text("git checkout -b "),
      "get clone": Text("git clone "),
      "get commit": Text("git commit -v") + Key('enter'),
      "get commit amend": Text("git commit -v --amend") + Key('enter'),
      "get diff": Text("git diff") + Key("enter"),
      "get fetch": Text("git fetch "),
      "get log ": Text("git log --decorate") + Key("enter"),
      "get merge": Text("git merge "),
      "get pull": Text("git pull") + Key("enter"),
      "get pull [dash dash] rebase": Text("git pull --rebase") + Key("enter"),
      "get push": Text("git push "),
      "get status": Text("git status -uno") + Key("enter"),
      "get status pipe less": Text("git status | less") + Key('enter'),
      "get short status": Text("git status -sb -uno") + Key("enter"),
      "get stash": Text("git stash "),
      "get stash save": Text("git stash save") + Key('enter'),
      "get stash pop": Text("git stash pop") + Key('enter'),
      "get reset": Text("git reset "),
      "get reset hard": Text("git reset --hard "),
      "get reset hard head": Text("git reset --hard HEAD"),
      "get reset soft": Text("git reset --soft "),

      "gerrit push": Text("git push origin HEAD:refs/for/"),
      "get review": Text("/c/Python27/Scripts/git-review.exe "),
      "get review dash dee": Text("/c/Python27/Scripts/git-review.exe -d "),
      "get review dash dee <n>": Text("/c/Python27/Scripts/git-review.exe -d %(n)d"),

      "get kay": Text("gitk") + Key("enter"),
      },
    extras = [
        Dictation("text"),
        Integer("n", 0, 20000),
      ],
    defaults = {
      "n" : 1
      }
    )

grammar.add_rule(rules)

grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
