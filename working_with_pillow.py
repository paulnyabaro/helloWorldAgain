from PIL import Image
# example_image = Image.open('example_image_two.png')
example_image = Image.open('example-image.jpg')
example_image.show()
print(example_image)
print(example_image.size)
width, height = example_image.size
print(f'The image dimensions are: height --> {height}, and width --> {width}')
print(example_image.format)
print(example_image.format_description)