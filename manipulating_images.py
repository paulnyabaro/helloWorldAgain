from PIL import ImageColor

# Important info
# CMYK a nd RGB Coloring
# In grade school you learned that mixing red, yellow, and blue paints can
# form other colors; for example, you can mix blue and yellow to make green
# paint. This is known as the subtractive color model, and it applies to dyes, inks,
# and pigments. This is why color printers have CMYK ink cartridges: the Cyan
# (blue), Magenta (red), Yellow, and blacK ink can be mixed together to form any
# color.
# However, the physics of light uses what’s called an additive color model.
# When combining light (such as the light given off by your computer screen),
# red, green, and blue light can be combined to form any other color. This is why
# RGB values represent color in computer programs.

print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
print(ImageColor.getcolor('purple', 'RGBA'))
# Pillow supports more than 100 color name

# y-cordinates increase downwards