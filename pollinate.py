import yaml
import pyautogui
import os
import time
import copy 
import clipboard
import weed
import os

def main(**kwargs):   
    if "view" in kwargs:
        cross_post = kwargs.get("cross_post", [])
        for platform in cross_post:
            p3 = copy.deepcopy(kwargs)
            p3["platform"] = platform
            view(**p3)
    else:
        print("pollinating")
        directory = os.getcwd()
        kwargs["directory"] = directory
        weed.process_images(**kwargs)
        cross_post = kwargs.get("cross_post", [])
        print(f"cross posting to {cross_post}")
        for platform in cross_post:
            p3 = copy.deepcopy(kwargs)
            p3["platform"] = platform
            post(**p3)


platform_details = {}


platform = "bluesky"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://bsky.app/"
deets["position_text_box"] = (764, 220)
deets["position_add_image_initial"] = (500, 585)
deets["position_add_image"] = (680, 440)

platform = "instagram"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.instagram.com/"
deets["position_text_box"] = (1185, 280)
deets["position_add_image_initial"] = [(82, 553),(82,600)]
#deets["position_add_image_initial"] = (37, 540)
deets["position_add_image"] = (948, 644)
deets["position_add_image_after"] = [(1290, 190), (1450, 190)]

platform = "linkedin"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.linkedin.com/feed/"
deets["position_text_box"] = (645, 265)
deets["position_add_image"] = (726, 623)
deets["position_add_image_after"] = (1466, 965)


platform = "mastadon"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://mastodon.social/home"
deets["position_text_box"] = (460, 271)
deets["position_add_image"] = (377, 422)

platform = "threads"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.threads.net/"
deets["position_add_image_initial"] = (740, 180)
deets["position_text_box"] = (739, 370)
#deets["position_text_box"] = (739, 357)
#deets["position_add_image"] = (723, 555)
deets["position_add_image"] = (723, 550)


platform = "twitter"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://twitter.com/home"
deets["position_text_box"] = (730, 200)
deets["position_add_image_initial"] = (725, 180)
deets["position_add_image"] = (671, 262)


platform = "cohost"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://cohost.org/"
deets["position_text_box"] = (686, 640)
deets["position_add_image_initial"] = (1685, 120)
deets["position_add_image"] = (690, 410)

platform = "taggr"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://taggr.link/"
deets["position_text_box"] = (1026, 435)
deets["position_add_image_initial"] = (1495, 121)
deets["position_add_image"] = (1435, 317)

platform = "telegram"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "C:\\Users\\Stuart-McFarlan\\AppData\\Roaming\Telegram Desktop\\Telegram.exe"
deets["position_text_box"] = (769, 1018)
deets["position_add_image_initial"] = [(150, 50),"oomlout", (115,110)]
deets["position_add_image"] = (709, 1021)


platform = "signal"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "C:\\Users\\Stuart-McFarlan\\AppData\\Local\\Programs\\signal-desktop\\Signal.exe"
deets["position_text_box"] = (805, 1000)
deets["position_add_image_initial"] = [(30, 182), (315,52)]
deets["position_add_image"] = (306, 74)

platform = "discord"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "C:\\Users\\Stuart-McFarlan\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
deets["position_text_box"] = (390, 996)
deets["position_add_image_initial"] = [(33,111),(163,182),(355, 993)]
deets["position_add_image"] = (402, 850)

platform = "medium"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://medium.com/new-story"
deets["position_add_image_initial"] = [(560,265)]
deets["position_add_image"] = (612, 265)
deets["position_text_box"] = (620, 209)

platform = "livejournal"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.livejournal.com/post"
deets["position_add_image_initial"] = [(555,410)]
deets["position_add_image"] = (604, 410)
deets["position_text_box"] = (598, 907)
deets["position_title_box"] = (598, 271)

platform = "tumblr"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.tumblr.com/"
deets["position_add_image_initial"] = [(763,197)]
deets["position_add_image"] = (827, 438)
deets["position_text_box"] = (738, 650)
deets["position_title_box"] = (746, 712)


platform = "facebook_business"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.facebook.com/profile.php?id=61553257906517"
deets["position_add_image_initial"] = [(1200,530)]
#deets["position_add_image_initial"] = [(1200,525)]
deets["position_add_image"] = (953, 600)
deets["position_text_box"] = (774, 350)
#deets["position_text_box"] = (774, 376)


def view(**kwargs):
    #open twittier in chrome
    platform = kwargs.get("platform")
    details = platform_details[platform]
    webpage = details["webpage"]    
    print(f"viewing {platform}")
    if "https" in webpage:
        os.system(f"start chrome {webpage}")
    else:
        os.system(f'"{webpage}"')

def post(**kwargs):
    #open twittier in chrome
    platform = kwargs.get("platform")
    details = platform_details[platform]
    beet = kwargs.get("beet")
    webpage = details["webpage"]
    folder_full = kwargs.get("folder_full")
    print(f"posting to {platform}")
    if "https" in webpage:
        os.system(f"start chrome {webpage}")
    else:
        os.system(f'"{webpage}"')
    print("     waiting for page to load")
    time.sleep(15)
    #add image
    print("     adding image")
    file_image = f"{folder_full}/image.png"
    #replace /
    file_image = file_image.replace("/", "\\")
    folder_image = os.path.dirname(file_image)
    if "position_add_image_initial" in details:
        initial_point = details["position_add_image_initial"]
        #if a string
        mouse_click(details["position_add_image_initial"])  
    
    mouse_click(details["position_add_image"])
    send_text(folder_image)
    send_enter()    
    send_text("image.jpg")
    send_enter()    
    if "position_add_image_after" in details:
        mouse_click(details["position_add_image_after"])
    #click the textbox button
    print("     adding beet")
    mouse_click(details["position_text_box"])
    mouse_click(details["position_text_box"])
    send_text(beet)
    if "position_title_box" in details:
        mouse_click(details["position_title_box"])
        mouse_click(details["position_title_box"])
        send_text(beet)
    post_confirm(platform)

def post_confirm(platform):
    pass
    #input("click the post button then click enter here")

def mouse_click(pos):
    #if pos isn't a list make it one
    if not isinstance(pos, list):
        pos = [pos]
    for p in pos:
        if isinstance(p, str):
            send_text(p)
        else:
            print(f"     moving to {p}")
            pyautogui.moveTo(p)
            pyautogui.click()
            time.sleep(4)

def send_enter():
    pyautogui.press("enter")
    time.sleep(4)

def send_text(text):
    if "#" in text:
        text = text.split("#")    
    else:
        text = [text]
    for t in text:
        pyautogui.typewrite(t)
        #don't include last time through
        if t != text[-1]:
            clipboard.copy("#")
            pyautogui.hotkey('ctrl', 'v')
    
    pyautogui.typewrite(text)
    time.sleep(2)
    
if __name__ == "__main__":
    kwargs = {}
    #if theres a generated folder
    #folder_full = "C:/GH/the_allotment/data/follow/github.com/oomlout/the_allotment_oomlout/garden/2023/10/25/20_49_58"    
    folder_full = os.getcwd()
    if os.path.exists(f"{folder_full}/beet.yaml"):
        #load the yaml details
        with open(f"{folder_full}/beet.yaml", 'r') as f:
            kwargs = yaml.load(f, Loader=yaml.FullLoader)
        kwargs["folder_full"] = folder_full
        folder_base = "C:/GH/the_allotment"
        kwargs["folder_base"] = folder_base            
        main(**kwargs)
    else:
        kwargs["view"] = True
        kwargs["cross_post"] = ["twitter", "instagram", "mastadon", "linkedin", "bluesky", "threads", "cohost", "taggr", "telegram", "signal", "discord", "medium", "livejournal", "tumblr", "facebook_business"]
        print("cant beet from here viewing")
        main(**kwargs)
        
    