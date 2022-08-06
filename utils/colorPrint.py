ANSI_BLACK = 30
ANSI_RED = 31
ANSI_GREEN = 32
ANSI_YELLOW = 33
ANSI_BLUE = 34
ANSI_PURPLE = 35
ANSI_CYAN = 36
ANSI_WHITE = 37

ANSI_BLACK_BACKGROUND = 40
ANSI_RED_BACKGROUND = 41
ANSI_GREEN_BACKGROUND = 42
ANSI_YELLOW_BACKGROUND = 43
ANSI_BLUE_BACKGROUND = 44
ANSI_PURPLE_BACKGROUND = 45
ANSI_CYAN_BACKGROUND = 46
ANSI_WHITE_BACKGROUND = 47

MOD_DEFAULT = 0
MOD_HIGHLIGHT = 1
MOD_UNDERLINE = 4
MOD_FLICKER = 5
MOD_INVERSE = 7
MOD_HIDE = 8


def mod_print(message, fg=ANSI_RED, bg=ANSI_BLACK_BACKGROUND, mod=MOD_HIGHLIGHT, override: bool = False):
    """
    格式化输出
    :param message:打印的消息
    :param fg:前景色
    :param bg:背景色
    :param mod:打印的模式
    :param override 是否要覆盖掉上一行内容
    :return:无（不会返回内容，只会在控制台打印字符串）
    """
    if override:
        print('\r\033[{};{};{}m'.format(fg, bg, mod) + message + '\033[0m', end='')
    else:
        print('\033[{};{};{}m'.format(fg, bg, mod) + message + '\033[0m')


def red(msg):
    mod_print(msg, fg=ANSI_WHITE, bg=ANSI_RED, mod=MOD_HIGHLIGHT)


def green(msg):
    mod_print(msg, fg=ANSI_WHITE, bg=ANSI_GREEN, mod=MOD_HIGHLIGHT)


def yellow(msg, override: bool = False):
    mod_print(msg, fg=ANSI_WHITE, bg=ANSI_YELLOW, mod=MOD_HIGHLIGHT, override=override)


def blue(msg):
    mod_print(msg, fg=ANSI_WHITE, bg=ANSI_BLUE, mod=MOD_HIGHLIGHT)


def purple(msg):
    mod_print(msg, fg=ANSI_WHITE, bg=ANSI_PURPLE, mod=MOD_HIGHLIGHT)
