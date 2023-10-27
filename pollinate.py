import yaml
import pyautogui
import os
import time
import copy 
import clipboard

def main(**kwargs):    
    cross_post = kwargs.get("cross_post", [])
    for platform in cross_post:
        p3 = copy.deepcopy(kwargs)
        p3["platform"] = platform
        post(**p3)


platform_details = {}


platform = "bluesky"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://bsky.app/"
deets["position_text_box"] = (764, 212)
deets["position_add_image_initial"] = (515, 576)
deets["position_add_image"] = (700, 385)

platform = "linkedin"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://www.linkedin.com/feed/"
deets["position_text_box"] = (645, 265)
deets["position_add_image_initial"] = (874, 279)
deets["position_add_image"] = (726, 623)
deets["position_add_image_after"] = (1466, 965)


platform = "mastadon"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://mastodon.social/home"
deets["position_text_box"] = (460, 271)
deets["position_add_image_initial"] = (874, 279)
deets["position_add_image"] = (405, 370)

platform = "twitter"
platform_details[platform] = {}
deets = platform_details[platform]
deets["webpage"] = "https://twitter.com/home"
deets["position_text_box"] = (750, 180)
deets["position_add_image_initial"] = (671, 222)
deets["position_add_image"] = (671, 290)


def post(**kwargs):
    #open twittier in chrome
    platform = kwargs.get("platform")
    details = platform_details[platform]
    beet = kwargs.get("beet")
    webpage = details["webpage"]
    folder_full = kwargs.get("folder_full")
    print(f"posting to {platform}")
    os.system(f"start chrome {webpage}")
    print("     waiting for page to load")
    time.sleep(15)
    #add image
    print("     adding image")
    file_image = f"{folder_full}/image.png"
    #replace /
    file_image = file_image.replace("/", "\\")
    folder_image = os.path.dirname(file_image)
    if platform == "twitter" or platform == "bluesky":
        mouse_click(details["position_add_image_initial"])  
    
    mouse_click(details["position_add_image"])
    send_text(folder_image)
    send_enter()    
    send_text("image.jpg")
    send_enter()    
    #click the textbox button
    print("     adding beet")
    mouse_click(details["position_text_box"])
    send_text(beet)
    post_confirm(platform)

def post_confirm(platform):
    input("click the post button then click enter here")

def mouse_click(pos):
    pyautogui.moveTo(pos)
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
    if os.path.exists(f"{folder_full}/generated"):
        #load the yaml details
        with open(f"{folder_full}/generated/yaml", 'r') as f:
            kwargs = yaml.load(f, Loader=yaml.FullLoader)
        kwargs["folder_full"] = folder_full
        folder_base = "C:/GH/the_allotment"
        kwargs["folder_base"] = folder_base    
        
        main(**kwargs)
    else:
        print("cant beet from here")
        
    