import os
from PIL import Image
import datetime
import shutil

source = 'C:/Users/kimye/Desktop/Coding/Python/Image_sorting_algorithm/123/'
destination = 'C:/Users/kimye/Desktop/Coding/Python/Image_sorting_algorithm/des/'
count = 0 

def cleaner(filename):
    filename = filename.replace(':', '')
    filename = filename.replace('-', '')
    filename = filename.replace(' ', '')
    filename = filename[0:8]
    return(filename)

images = os.listdir(source)   

for image in images : 
    oldname = source + image   
    created_time = str(datetime.date.fromtimestamp(os.path.getctime(source+image)))  
    modified_time = str(datetime.date.fromtimestamp(os.path.getmtime(source+image)))  
    timelist =[]
    timelist.append(cleaner(created_time))
    timelist.append(cleaner(modified_time))

    try:
        photo = Image.open(source+image)
        meta = photo._getexif()
        taken_time = meta[36867] 
        timelist.append(cleaner(taken_time))
    except:  
        taken_time = 99999999
        
    timelist.sort() 
    newname = destination + timelist[0] + " " + str(count)  + ".jpg"

    shutil.copy2(oldname, newname)   
    count += 1   



