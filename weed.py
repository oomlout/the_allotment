import os
import copy

def main(**kwargs):
    directory = kwargs.get("directory", os.getcwd())
    kwargs["directory"] = directory
    #if directory isn't an list make it one iterable make it
    if not isinstance(directory, list):
        directory = [directory]
    
    for dir in directory:
        dir = dir.replace("\\", "/")
        dir = dir.replace("/image.jpg", "")

        print(f"Processing {dir}")
        
        p3 = copy.deepcopy(kwargs)
        p3["directory"] = dir
        process_images(**p3)





def process_images(**kwargs):
    resolutions = kwargs.get("resolutions", [1080, 720, 480, 360, 240, 144])
    crops = kwargs.get("crops", ["16_9", "4_3", "1_1", "original"])
    directory = kwargs.get("directory")
    #if image.jps exists in directory
    image_filename = f"{directory}/image.jpg"
    if os.path.exists(image_filename):
        image_src = f"{directory}/image.jpg"
        #crop and resize images using library not shutil
        from PIL import Image
        image_src = Image.open(image_src)
        for crop in crops:
            width_image = image_src.size[0]
            height_image = image_src.size[1]
            height_crop = width_image
            top_left = (0,0)
            bottom_right = (width_image, height_crop)
            if crop == "16_9":
                width_crop = width_image
                height_crop = width_image * 9 / 16
                top_left = (0,0)
                bottom_right = (width_image, height_crop)                
            elif crop == "4_3":
                width_crop = width_image
                height_crop = width_image * 3 / 4
                top_left = (0,0)
                bottom_right = (width_image, height_crop)
            elif crop == "1_1":
                width_crop = width_image
                height_crop = width_image
                top_left = (0,0)
                bottom_right = (width_image, height_crop)
            elif crop == "original":
                width_crop = width_image
                height_crop = height_image
                top_left = (0,0)
                bottom_right = (width_image, height_crop)
            crop_box = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
            image_crop = image_src.crop(crop_box)
            for resolution in resolutions:
                image_dst = f"{directory}/generated/image_{crop}_{resolution}.jpg"
                image_crop.thumbnail((resolution, resolution))
                image_crop.save(image_dst)
                print(f"   Saved {image_dst}")





if __name__ == '__main__':
    kwargs = {}
    cwd = os.getcwd()
    import glob 
    directories = glob.glob(f"{cwd}/**/image.jpg", recursive=True)

    
    kwargs["directory"] = directories
    main(**kwargs)
    'C:\\gh\\the_allotment\\data\\follow\\github.com\\oomlout\\the_allotment_oomlout\\garden\\2023\\10\\25_20_49_58\\image.jpg'