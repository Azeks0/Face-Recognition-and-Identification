import face_recognition
#Code was inspired by CodingEntrepreneurs and Traversy Media
#This is meant for personal research with face recognition

image_of_subject = face_recognition.load_image_file('image/path')
subject_face_encoding = face_recognition.face_encodings(image_of_subject)[0]

unknown_image = face_recognition.load_image_file(
    'image/path')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces(
    [subject_face_encoding], unknown_face_encoding)

if results[0]:
    print('results are positive')
else:
    print('results are negative')