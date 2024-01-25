import os
import shutil
import time
import yaml



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
    #make dir beet absolute
    dir_beet = os.path.abspath(dir_beet) 
    if not os.path.exists(dir_beet):
        os.makedirs(dir_beet)
        #os.makedirs(f"{dir_beet}")

    dir_default = "garden/default"
    yaml_default = f"{dir_default}/beet.yaml"
    #make yaml_default absolute
    yaml_default = os.path.abspath(yaml_default)
    #if default_exists load it to default
    if os.path.exists(yaml_default):
        with open(yaml_default, 'r') as f:
            import yaml
            kwargs_default = yaml.load(f, Loader=yaml.FullLoader)
        #update kwargs with default
        kwargs.update(kwargs_default)
    else:
        print(f"no default beet found at {yaml_default}")
    
    

    

    #commit all kwargstest

    # old no file extension method
    # for key, value in kwargs.items():
    #     with open(f"{dir_beet}/{key}", 'w') as f:
    #         f.write(value)
    #         pass

    dir_beet_default = f"{dir_default}"
    beet_deets = load_details(dir_beet_default)
    beet_deets.update(kwargs)

    import json
    with open(f"{dir_beet}/beet.json", 'w') as f:
        json.dump(beet_deets, f)
    import yaml
    with open(f"{dir_beet}/beet.yaml", 'w') as f:
        yaml.dump(beet_deets, f)

    print(f"beet planted at {dir_beet}")
    #open dir_beet with explorer
    os.startfile(dir_beet)


def get_beet(**kwargs):    
    return_value = input("whats the beet?\n  ")
    return return_value

def load_details(directory):
    #load all files in directory skid directories
    return_value = {}
    file = f"{directory}/beet.yaml"
    if os.path.exists(file):
        with open(file, 'r') as f:
            return_value = yaml.load(f, Loader=yaml.FullLoader)
    return return_value


if __name__ == '__main__':
    kwargs = {}
    kwargs["host"] = "github.com"
    kwargs["user"] = "oomlout"
    kwargs["allotment_name"] = "the_allotment_oomlout"
    main(**kwargs)