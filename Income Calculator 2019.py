#!/usr/bin/env python3

import State
import Fed

income = input('Do you get paid hourly or salary? ')

if income == "hourly" or 'Hourly':
    stnum = input('Do you live in the same state that you work in? ')
    if stnum == 'Yes' or 'yes':
        stone = input('What state do you live in? ')
        sttwo = input('What state do you work in? ')
    else:
        stone = input('What state is this for? ')
        