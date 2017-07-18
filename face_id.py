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

unknown_face_locations = []
unknown_face_encodings = []

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_locations = face_recognition.face_locations(unknown_picture)
unknown_face_encodings = face_recognition.face_encodings(unknown_picture, unknown_face_locations)

print("UNKNOWN")
print(unknown_face_encodings)
print("FAMILY")
print(family)

check = False

print("It's a picture of")
'''
for unknown_face_encoding in unknown_face_encodings:
    count = 0
    for member in family:
        results = face_recognition.compare_faces([member], [unknown_face_encoding])
        if results[0] == True:
            if count == 0:
                print("Kellen")
            elif count == 1:
                print("Ellen")
            elif count == 2:
                print("Mackie")
            elif count == 3:
                print("Dan")
            elif count == 4:
                print("Tara")
                check = True

        count+=1

'''
if check == False:
    print("No family members in this picture!")
