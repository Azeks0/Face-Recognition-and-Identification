import face_recognition
from PIL import Image, ImageDraw
#Code was inspired by CodingEntrepreneurs and Traversy Media
#This is meant for personal research with face recognition

image_of_subject0 = face_recognition.load_image_file('subject/image/path')
subject_face_encoding = face_recognition.face_encodings(image_of_subject0)[0]

image_of_subject1 = face_recognition.load_image_file('subject1/image/path')
steve_face_encoding = face_recognition.face_encodings(image_of_subject1)[0]

image_of_subject2 = face_recognition.load_image_file('subject2/image/path')
elon_face_encoding = face_recognition.face_encodings(image_of_subject2)[0]

#  Create arrays of encodings and names
known_face_encodings = [
    subject0_face_encoding,
    subject1_face_encoding,
    subject2_face_encoding
]

known_face_names = [
    "Subject0",
    "Subject1",
    "Subject2"
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('test_image/path')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 255, 0), outline=(255, 255, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('image.png')