from lib.test import ViewTestMixin


class TestEncodingUpload(ViewTestMixin):
    def test_encoding_creation_for_one_face(self):
        response = self.create_encoding(self.files["file_one_face"])

        assert response.status_code == 201
        assert isinstance(response.json["id"], int) == True
        assert response.json["encoding"] == self.encodings["file_one_face"]

    def test_encoding_creation_for_two_faces(self):
        response = self.create_encoding(self.files["file_two_faces"])

        assert response.status_code == 201
        assert isinstance(response.json["id"], int) == True
        assert response.json["encoding"] == self.encodings["file_two_faces"]

    def test_encoding_creation_for_three_faces(self):
        response = self.create_encoding(self.files["file_three_faces"])

        assert response.status_code == 201
        assert isinstance(response.json["id"], int) == True
        assert response.json["encoding"] == self.encodings["file_three_faces"]

    def test_unsupported_file_returns_bad_request(self):
        response = self.create_encoding(self.files["file_unsupported"])

        assert response.status_code == 400
        assert response.json["message"] == "not allowed file"

    def test_no_face_found_bad_request(self):
        response = self.create_encoding(self.files["file_apple"])

        assert response.status_code == 400
        assert response.json["message"] == "no face was found"
