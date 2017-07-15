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

family = [encodeKellen, encodeEllen, encodeMackie, encodeDan, encodeTara]

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]


for members in family:
    result = face_recognition.compare_faces([family[member]], unknown_face_encoding)

    if results[0] == True:
        print("It's a picture of")
        
