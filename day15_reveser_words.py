import re
s = re.sub('\s+',' ',s)
return ' '.join(s.strip().split(' ')[::-1]) 