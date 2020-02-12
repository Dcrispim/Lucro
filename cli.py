
import os
from lucro import lucro

os_args = os.sys.argv[1:]
sys_args = {}

_exclude = []
responses=[]
def parseArgs(list_args: list) -> dict:
    """get a list of args and convert do dict of all args and values
    """    
    _args = {}
    for i in range(len(list_args)):
        if list_args[i][0] == "-":
            try:
                if list_args[i + 1][0] != "-":
                    _args[list_args[i]] = list_args[i + 1]
                    _exclude.append(list_args[i + 1])
                else:
                    _args[list_args[i]] = True

            except IndexError:
                _args[list_args[i]] = True

        elif list_args[i] not in _exclude:
            _args[i] = list_args[i]

    return _args


def runLucroInArgs():
    """try run the current operaiton with the args without keys 
    """ 
    _del = []
    for i in sys_args.keys():
        if str(i).isdigit():
            List = sys_args[i].replace('[','').replace(']','').split(',')
            Min_out = 0 if "-m" not in sys_args.keys() else int(sys_args["-m"])
            op = lucro([float(n) for n in List ], Min_out)
            responses.append(op)
            print(op)
            _del.append(i)

    for i in _del:
        del sys_args[i]

sys_args.update(parseArgs(os_args))
runLucroInArgs()