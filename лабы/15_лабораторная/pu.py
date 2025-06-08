import face_recognition
known_image = face_recognition.load_image_file("known.jpg")
unknown_image = face_recognition.load_image_file("unknown_t_2.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)
print("Результат сравнения:", results[0])