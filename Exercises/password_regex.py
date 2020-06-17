# at least 8 char long
# numbers, letters, $%#@
# end with number

import re

password = 'asdfsadf32434'
pattern = re.compile(r'^[a-zA-Z\d$%#@]{8,}\d$')
check = pattern.fullmatch(password)
print(check)
