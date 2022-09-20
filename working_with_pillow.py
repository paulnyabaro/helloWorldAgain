from PIL import Image
# example_image = Image.open('example_image_two.png')
example_image = Image.open('example-image.jpg')
# example_image.show()
print(example_image)
print(example_image.size)
width, height = example_image.size
print(f'The image dimensions are: height --> {height}, and width --> {width}')
print(example_image.format)
print(example_image.format_description)

# Saving the image in same or different format
example_image.save('example-image-save.png')

# using the new() method to create images
from PIL import Image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# Cropping image
cropped_image = example_image.crop((355, 345, 565, 560))
cropped_image.save('cropped-image.jpg')
# cropped_image.show()

# Copying image
copied_image = cropped_image.copy()
copied_image.save('copied-image.jpg')

# Copying and pasting image on another image
copy_paste_image = example_image.crop((25, 45, 665, 700))
im.paste(copy_paste_image, (25, 45))
im.paste(copy_paste_image, (200, 323))
copy_paste_image.save('copy_paste_image.jpg')
copy_paste_image.show()