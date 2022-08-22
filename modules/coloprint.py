'''
coloprint.py
created by NicolasV
version : 1.0

Usage:

    Output colored text or value (work as the print function):
    
        cprint(value,foreground_color,background_color,attribute,eol)

    Change console color :

        console_color(foreground_color,background_color)

    Get a list of the supported colors or effect:

        colors_list() --> colors
        effects_list() --> effects
    
'''
foreground={"black":"\033[30m"
,"red":"\033[31m"
,"green":"\033[32m"
,"yellow":"\033[33m"
,"blue":"\033[34m"
,"magenta":"\033[35m"
,"cyan":"\033[36m"
,"white":"\033[37m"
,"gray":"\033[90m"
,"bright_red":"\033[91m"
,"bright_green":"\033[92m"
,"bright_yellow":"\033[93m"
,"bright_blue":"\033[94m"
,"bright_magenta":"\033[95m"
,"bright_cyan":"\033[96m"
,"bright_white":"\033[97m"}
background={"black":"\033[40m"
,"red":"\033[41m"
,"green":"\033[42m"
,"yellow":"\033[43m"
,"blue":"\033[44m"
,"magenta":"\033[45m"
,"cyan":"\033[46m"
,"white":"\033[47m"
,"gray":"\033[100m"
,"bright_red":"\033[101m"
,"bright_green":"\033[102m"
,"bright_yellow":"\033[103m"
,"bright_blue":"\033[104m"
,"bright_magenta":"\033[105m"
,"bright_cyan":"\033[106m"
,"bright_white":"\033[107m"}
effect={
    "None":"",
    "bold":"\033[1m",
    "italic":"\033[3m",
    "underline":"\033[4m",
    "slow_blink":"\033[5m",
    "fast_blink":"\033[6m",
    "overlined":"\033[53m",
}
def cprint(value,foreground_color="bright_white",background_color="black",attribute="None",eol="\n"):
    try:
        print(foreground[foreground_color]+background[background_color]+effect[attribute]+"{}".format(value)+"\033[0m",end=eol)
    except:
        print("Can't print that")
def console_color(foreground_color="bright_white",background_color="black"):
    print(foreground[foreground_color]+background[background_color])
        
def colors_list():
    for i in foreground:
        print(i)
        
def effects_list():
    for i in effect:
        print(i)
    
