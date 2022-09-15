#!/usr/bin/env python3
import os
from time import strptime
import dev_aberto
from babel.dates import format_date
from babel.numbers import format_number
import gettext
import datetime
gettext.install('cli', localedir='locale') 
if __name__ == '__main__':
    print(os.getenv('LANGUAGE'))
    date, name = dev_aberto.hello()
    
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    print(_('Last commit made in:'),  format_date( date), _(' by'), name)
