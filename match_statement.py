status_code = 200

match status_code:
    case 200:
        print('OK')
    case 404:
        print('Not found')
    case _:
        print('IDK')

import os
