import face_recognition
#Code was inspired by CodingEntrepreneurs and Traversy Media
#This is meant for personal research with face recognition

image = face_recognition.load_image_file('image/path')
face_locations = face_recognition.face_locations(image)#

print (f'there are {len(face_locations)} people in this image')
print(face_locations)
