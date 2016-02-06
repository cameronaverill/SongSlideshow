from SimpleCV import Image

#change this to process multiple images
img = Image('../images/beach.jpeg')
histogram = img.histogram()

print histogram.getFieldNames