import os

import time


def main(**kwargs):
    beet = get_beet(**kwargs)
    kwargs["beet"] = beet
    dir_beets = "beets"
    if not os.path.exists(dir_beets):
        os.makedirs(dir_beets)
    #year/month/date_hour_minute_second/
    date_beet= time.strftime("%Y/%m/%d_%H_%M_%S")
    dir_beet = f"{dir_beets}/{date_beet}"
    if not os.path.exists(dir_beet):
        os.makedirs(dir_beet)
    with open(f"{dir_beet}/beet", 'w') as f:
        f.write(beet)
    



def get_beet(**kwargs):    
    return_value = input("whats the beet?\n  ")
    return return_value



if __name__ == '__main__':
    main()