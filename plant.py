import os
import shutil
import time


def main(**kwargs):
    host = kwargs.get("host")
    user = kwargs.get("user")
    allotment_name = kwargs.get("allotment_name")
    
    #get the beet
    beet = get_beet(**kwargs)
    kwargs["beet"] = beet
    
    # time
    #get current time
    time_current = time.time()
    #convert to string and format
    timee = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_current))
    kwargs["time"] = timee

    time_beet = time.strftime("%Y/%m/%d/%H_%M_%S")
    kwargs["time_beet"] = time_beet

    #folder to beet
    folder = f"{host}/{user}/{allotment_name}/{time_beet}"
    kwargs["folder"] = folder

    id = folder.replace("/", "_")
    id = id.replace("-", "_")
    id = id.replace(".", "_")
    id = id.lower()
    kwargs["id"] = id


    #folders
    dir_beets = "garden"
    if not os.path.exists(dir_beets):
        os.makedirs(dir_beets)

    dir_beet = f"{dir_beets}/{time_beet}"
    dir_generated = f"{dir_beet}/generated"
    if not os.path.exists(dir_beet):
        os.makedirs(dir_beet)
        os.makedirs(f"{dir_generated}")

    dir_default = "default"
    #if default_exists
    if os.path.exists(dir_default):
        shutil.copytree(dir_default, dir_beet)


    #commit all kwargstest

    for key, value in kwargs.items():
        with open(f"{dir_beet}/{key}", 'w') as f:
            f.write(value)
            pass

    import json
    with open(f"{dir_generated}/json", 'w') as f:
        json.dump(kwargs, f)
    import yaml
    with open(f"{dir_generated}/yaml", 'w') as f:
        yaml.dump(kwargs, f)


def get_beet(**kwargs):    
    return_value = input("whats the beet?\n  ")
    return return_value



if __name__ == '__main__':
    kwargs = {}
    kwargs["host"] = "github.com"
    kwargs["user"] = "oomlout"
    kwargs["allotment_name"] = "the_allotment_oomlout"
    main(**kwargs)