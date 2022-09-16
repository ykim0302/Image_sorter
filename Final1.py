import os
from PIL import Image
import datetime
import shutil

# The location of the files that you want to sort
source = 'C:/Users/kimye/Desktop/Coding/Python/Image_sorting_algorithm/123/'
# The location where you want to copy them to
destination = 'C:/Users/kimye/Desktop/Coding/Python/Image_sorting_algorithm/des/'

# For photos taken on the same date, add different numbers for each
count = 0 

# Function that removes all other signs from dates
def cleaner(filename):
    filename = filename.replace(':', '')
    filename = filename.replace('-', '')
    filename = filename.replace(' ', '')
    filename = filename[0:8]
    return(filename)

images = os.listdir(source)   

for image in images : 
# Get the created and modified time of the file and put them in a list
    oldname = source + image   
    created_time = str(datetime.date.fromtimestamp(os.path.getctime(source+image)))  
    modified_time = str(datetime.date.fromtimestamp(os.path.getmtime(source+image)))  
    timelist =[]
    timelist.append(cleaner(created_time))
    timelist.append(cleaner(modified_time))

    try:
# Get the meta data of the file
        photo = Image.open(source+image)
        meta = photo._getexif()
        taken_time = meta[36867] 
        timelist.append(cleaner(taken_time))
    except:  
# If a meta data cannot be found, set it as the higest number so that it will be sorted as last in the timelist
        taken_time = 99999999

# The lowest(earliest) time will be selected and be renamed
    timelist.sort() 
    newname = destination + timelist[0] + " " + str(count)  + ".jpg"
    shutil.copy2(oldname, newname)   
    count += 1   



