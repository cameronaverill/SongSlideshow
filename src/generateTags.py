from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi()

images = []
currDir = os.getgwd()
imgUrl =  os.path.abspath(os.path.join(currDir, os.pardir))

for i in os.listdir(os.getcwd()):
	images.append("
result = clarifai_api.tag_images(open('
