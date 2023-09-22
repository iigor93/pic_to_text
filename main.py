import os
import re
import random
import pytesseract
from PIL import Image


file_names = os.listdir('pic/')
file_names_list = []

for file in file_names:
    ext = file.split('.')[1]

    with Image.open(f'pic/{file}') as image:
        w, h = image.size

        area = (w*0.05, 0, w*0.5, h*0.2)
        image = image.crop(area)
        # image.show()

        string = pytesseract.image_to_string(image)

        string = string.replace(" ", "")
        start = string.find('AA')
        finish = string.find('AA', start + 1)

        if start == -1 and finish == -1:
            print('Text not found')
        else:
            complaint_number = string[start + 2: finish].strip()
            regex = re.compile('[a-zA-Z]|[а-яА-Я]')
            complaint_number = regex.sub('', complaint_number)

            while complaint_number in file_names_list:
                # print(file_names_list)
                # print('string: ', string)
                complaint_number = complaint_number + '_' + str(random.randint(0, 20))

            file_names_list.append(complaint_number)

            os.rename(f'pic/{file}', f'pic/{complaint_number}.{ext}')
