#!python
import dev_aberto
from babel.dates import format_date
from babel.numbers import format_number
import gettext
gettext.install('cli', localedir='locale') 
if __name__ == '__main__':
    date, name = dev_aberto.hello()
    print(_('Last commit made in:'),  format_date(date,format='full'), _(' by'), name)
