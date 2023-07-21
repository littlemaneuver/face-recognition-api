import face_recognition


def image_to_encoding(file):
    img = face_recognition.load_image_file(file)
    unknown_face_encodings = face_recognition.face_encodings(img)

    if len(unknown_face_encodings) == 0:
        return None

    # handle only first found face
    return unknown_face_encodings[0]
