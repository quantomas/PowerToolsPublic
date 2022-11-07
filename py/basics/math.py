
### clean run
# tested on Python 3.7.3 64 bit


## tests
import math

math.ceil(2.4)
math.floor(2.4)


math.ceil(7.5/5) * 5
math.ceil(17.5/5) * 5
math.ceil(123.5/5) * 5


math.floor(7.5/5) * 5
math.floor(37.5/5) * 5
math.floor(-7.5/5) * 5
math.floor(-17.5/5) * 5
math.floor(-123.5/5) * 5




# str to float
# https://stackoverflow.com/questions/6633523/how-can-i-convert-a-string-with-dot-and-comma-into-a-float-in-python

from locale import atof, setlocale, LC_NUMERIC

setlocale(LC_NUMERIC, '') # set to your default locale; for me this is

# 'English_Canada.1252'. Or you could explicitly specify a locale in which floats
# are formatted the way that you describe, if that's not how your locale works :)

atof('123,456') # 123456.0

# To demonstrate, let's explicitly try a locale in which the comma is a
# decimal point:
setlocale(LC_NUMERIC, 'French_Canada.1252')
atof('123,456') # 123.456

