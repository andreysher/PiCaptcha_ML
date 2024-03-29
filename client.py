import requests
import json
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/api/image_classifier'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('test.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.get(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(response)
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}
