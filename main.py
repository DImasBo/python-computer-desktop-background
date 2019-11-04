from PIL import Image
import os

# width = 1366
# height = 768
def create_backgrount(name_paste,size= ( 1366,768 ),color_background = (80,20,50),max = 700):
	background = Image.new('RGB', size, color_background)
	im = Image.open(name_paste)

	if im.height > max:
		el = im.height - max
		im.thumbnail((im.width-el,max))
	if im.width > max:
		el = im.width - max
		im.thumbnail((max,im.height-el))

	border = Image.new('RGB',(im.width+20,im.height+20), (67,17,47))
	y = int((size[1] / 2 - im.width/2 )/2 )
	x = size[0] - im.width - y

	background.paste(border,(x-10,y-10))
	background.paste(im,(x,y))

	name_out = name_paste.replace("input/","output/") 
	name_out  =  name_out.split('.')[0] + ".png"
	background.save(name_out, "PNG")

if __name__ == '__main__':
	images = os.listdir("input/")
	for image in images:
		create_backgrount("input/" + image)
	# create_backgrount("input/7P42K.jpg");
