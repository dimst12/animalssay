def bubble(text):
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    top = '  ' + '-' * (width + 2)
    middle = '\n'.join(f'< {line.ljust(width)} >' for line in lines)
    bottom = '  ' + '-' * (width + 2)
    return f"{top}\n{middle}\n{bottom}"


def cat_says(text):
    return f"""{bubble(text)}
     \\
      \\
        /\_/\  
       ( o.o ) 
        > ^ <"""


def dog_says(text):
    return f"""{bubble(text)}
     \\
      \\
      / \\__
     (    @\\___
     /         O
    /   (_____/
   /_____/   U"""


def frog_says(text):
    return f"""{bubble(text)}
     \\
      \\
     @..@
    (----)
   ( >__< )
   ^^ ~~ ^^"""


def fox_says(text):
    return f"""{bubble(text)}
     \\
      \\
     /\   /\\
    //\\_//\\\\
    \\_     _/
     / * * \\
     \_\O/_/
     /     \\
    |     |"""


def cow_says(text):
    return f"""{bubble(text)}
     \\
      \\
        ^__^ 
        (oo)\\_______
        (__)\\       )\\/\\
            ||----w |
            ||     ||"""


def pig_says(text):
    return f"""{bubble(text)}
     \\
      \\
      ^-----^
     ( o   o )
     (  (oo)  )
      \\  ^  /
       |||||"""


def owl_says(text):
    return f"""{bubble(text)}
     \\
      \\
     ,_, 
    (O,O)
    (   )
    " \" \" """


def bat_says(text):
    return f"""{bubble(text)}
     \\
      \\
    =/\                 /\=
    / \\'._   (\_/)   _.'/ \\
   / .''._'--(o.o)--'_.''. \\
  /.' _/ |`'=/ " \='`| \_ `.\\
 /` .' `\;-,'\___/',-;/` '. '\\
/.-' jgs   `\(-V-)/`       `-.\\
`            "   "            `"""


def dolphin_says(text):
    return f"""{bubble(text)}
     \\
      \\
                    ;'-. 
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
     `       `'------/_.'----```
                     `"""

def shark_says(text):
    return f"""{bubble(text)}
     \\
      \\
                (`.              
                 \ `.           
                  )  `._..---._
\`.       __...---`         o  )
 \ `._,--'           ,    ___,'
  ) ,-._          \  )   _,-' 
 /,'    ``--.._____\/--''  """


def elephant_says(text):
    return f"""{bubble(text)}
     \\
      \\
                       .---'-    \\
      .-----------/           \\
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\)."""


def bunny_says(text):
    return f"""{bubble(text)}
     \\
      \\
         / \
    / _ \\
   | / \ |
   ||   || _______
   ||   || |\     \\
   ||   || ||\     \\
   ||   || || \    |
   ||   || ||  \__/
   ||   || ||   ||
    \\\\_/ \_/ \_//
   /   _     _   \\
  /               \\
  |    O     O    |
  |   \  ___  /   |                           
 /     \ \_/ /     \\
/  -----  |  --\    \\
|     \__/|\__/ \   |
\\       |_|_|       /
 \_____       _____/
       \     /
       |     |"""


def spider_says(text):
    return f"""{bubble(text)}
     \\
      \\
                  (
               )
              (
        /\  .-\"\"\"-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-\"\"\"-;///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/"""


def horse_says(text):
    return f"""{bubble(text)}
     \\
      \\
                                     |\    /|
                              ___| \,,/_/
                           ---__/ \/    \\
                          __--/     (D)  \\
                          _ -/    (_      \\
                         // /       \_ /  -\\
   __-------_____--___--/           / \_ O o)
  /                                 /   \__/
 /                                 /
||          )                   \_/\\
||         /              _      /  |
| |      /--______      ___\    /\  :
| /   __-  - _/   ------    |  |   \ \\
 |   -  -   /                | |     \ )
 |  |   -  |                 | )     | |
  | |    | |                 | |    | |
  | |    < |                 | |   |_/
  < |    /__\                <  \\
  /__\                       /___\\"""


def monkey_says(text):
    return f"""{bubble(text)}
     \\
      \\
                __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. \\
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \\ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
       '._ '-=-' _.'
           '~---~'"""


def wolf_says(text):
    return f"""{bubble(text)}
     \\
      \\
                         .
                    / V\
                  / `  /
                 <<   |
                 /    |
               /      |
             /        |
           /    \  \ /
          (      ) | |
  ________|   _/_  | |
<__________\______)\__)"""