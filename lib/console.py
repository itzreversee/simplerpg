
color = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'
}

background = {
    'black': '\033[40m',   
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'purple': '\033[45m',
    'cyan': '\033[46m',
    'white': '\033[47m',
    'reset': '\033[0m'
}

decoration = {
    'none': '',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[2m',
    'blink': '\033[5m',
    'reverse': '\033[7m',
}

def out(text, color_ = 'white', decoration_ = 'none', no_newline = False, alt_newline = None):
    end = '\n' if not no_newline else ''
    if alt_newline: end = alt_newline
    print(color[color_] + decoration[decoration_] +  text + color['reset']+ decoration['reset'], end=end)

def list(items: list, color_ = 'white', decoration_ = 'reset'):
    for item in items:
        print(color[color_] + " - " + decoration[decoration_] + item + color['reset'] + decoration['reset'])