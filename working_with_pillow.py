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
copy_paste_image = example_image.crop((25, 45, 565, 560))
copied_image.paste(copy_paste_image, (0, 0))
copied_image.paste(copy_paste_image, (200, 323))
copy_paste_image.save('copy_paste_image.jpg')
copy_paste_image.show()

# Resizing images --> Returns new image
# quarter_sized_image = catIm.resize((int(width / 2), int(height / 2)))

# Rotating and flipping images --> Counterclockwise rotation
# catIm.rotate(90).save('rotated90.png')
# Notice that the width and height of the image change when the image
# is rotated 90 or 270 degrees. If you rotate an image by some other amount,
# the original dimensions of the image are maintained
# catIm.rotate(6, expand=True).save('rotated6_expanded.png')
# --> to enlarge the dimensions of the image to fit the entire rotated new image

# Flipping images
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# Changing Individual Pixels
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))