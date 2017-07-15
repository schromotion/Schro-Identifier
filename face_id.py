import face_recognition

picKellen = face_recognition.load_image_file("kellen.jpg")
picEllen = face_recognition.load_image_file("ellen.jpg")
picMackie = face_recognition.load_image_file("mackie.jpg")
picDan = face_recognition.load_image_file("dan.jpg")
picTara = face_recognition.load_image_file("tara.jpg")

encodeKellen = face_recognition.face_encodings(picKellen)[0]
encodeEllen = face_recognition.face_encodings(picEllen)[0]
encodeMackie = face_recognition.face_encodings(picMackie)[0]
encodeDan = face_recognition.face_encodings(picDan)[0]
encodeTara = face_recognition.face_encodings(picTara)[0]
