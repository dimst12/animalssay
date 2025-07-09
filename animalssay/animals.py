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
