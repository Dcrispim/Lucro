
import os
def lucro(days:list, Min_out:int=0)->int:
    Out = 0
    for buy in range(len(days)):
        next_day = [day for day in days[buy+1:] if day>buy]
        for sale in next_day:
            prof = sale - days[buy]
            if prof>= Min_out and prof>Out:
                Out = sale - days[buy]
    return Out


args = os.sys.argv[1] if len(os.sys.argv) else ''

List = args.replace('[','').replace(']','').split(',')
