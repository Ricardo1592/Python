# import sys 

class TimeErradoError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        # sys.exc_info()

time = input()
if time == 'Bahia':
    raise TimeErradoError('Bahia 0 x 6 Sport')
else:
    print(time)