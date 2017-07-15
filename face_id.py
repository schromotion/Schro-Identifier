import face_recognition

picKellen = face_recognition.load_image_file("kellen.jpg")
picEllen = face_recognition.load_image_file("ellen.jpg")
picMackie = face_recognition.load_image_file("mackie.jpg")
picDan = face_recognition.load_image_file("dan.jpg")
picTara = face_recognition.load_image_file("tara.jpg")

pics = [picKellen, picEllen, picMackie, picDan, picTara]

encodeKellen = face_recognition.face_encodings(picKellen)[0]
encodeEllen = face_recognition.face_encodings(picEllen)[0]
encodeMackie = face_recognition.face_encodings(picMackie)[0]
encodeDan = face_recognition.face_encodings(picDan)[0]
encodeTara = face_recognition.face_encodings(picTara)[0]

family = [encodeKellen, encodeEllen, encodeMackie, encodeDan, encodeTara]

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

count = 0
check = False

for member in family:
    results = face_recognition.compare_faces([member], unknown_face_encoding)

    print("It's a picture of")
    if results[0] == True:
        if count == 0:
            print("Kellen")
        else if count == 1:
            print("Ellen")
        else if count == 2:
            print("Mackie")
        else if count == 3:
            print("Dan")
        else if count == 4:
            print("Tara")
        check = True
        print("nope!")

    count++

if check == False:
    print("No family members in this picture!")
