#!/urs/bin/env python

# -*- coding:UTF-8 -*-

import curses

stdscr = curses.initscr()

def display_info(str,x,y,colorpair=2):
    '''using the specific colorpair for display'''
    global stdscr
    stdscr.addstr(y,x,str,curses.color_pair(colorpair))
    stdscr.refresh()

def get_ch_and_continue():
    '''show press any key to continue'''
    global stdscr

    #set nodelay,wating for input 0
    stdscr.nodelay(0)
    #get a char
    stdscr.getch()
    #reset nodelay 
    stdscr.nodelay(1)
    return True


def set_win():
    '''set the console'''
    global stdscr
    #prepare for color
    curses.start_color()
    #set two color_pair for text and backgroud
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    #close the echo
    curses.noecho()
    #respond immed
    curses.cbreak()
    #set nodelay mode
    stdscr.nodelay(1)



def unset_win():
    '''reset the console'''
    global stdscr
    curses.nocbrek()
    curses.kepad(0)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    try:
        set_win()
        display_info('Hola,curses!',0,5)
        display_info('Press any key to continue...',0,10)
        get_ch_and_continue()

    except Exception,e:
        raise e
    finally:
        unset_win()























