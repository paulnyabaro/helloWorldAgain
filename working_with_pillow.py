from PIL import Image
example_image = Image.open('example_image_two.png')
example_image.show()
print(example_image)
print(example_image.size)
width, height = example_image.size
print(f'The image dimensions are: height --> {height}, and width --> {width}')