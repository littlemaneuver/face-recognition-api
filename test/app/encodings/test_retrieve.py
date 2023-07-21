from flask import url_for

from lib.test import ViewTestMixin


class TestEncodingRetrieve(ViewTestMixin):
    def test_getting_all_encodings(self):
        self.create_encoding(self.files["file_one_face"])
        self.create_encoding(self.files["file_two_faces"])
        self.create_encoding(self.files["file_three_faces"])

        response = self.client.get(url_for("encodings.get_all"))

        assert response.status_code == 200
        assert response.json == [
            {"id": 1, "encoding": self.encodings["file_one_face"]},
            {"id": 2, "encoding": self.encodings["file_two_faces"]},
            {"id": 3, "encoding": self.encodings["file_three_faces"]},
        ]

    def test_getting_one_by_id(self):
        response = self.client.get(url_for("encodings.get_one", id=2))

        assert response.status_code == 200
        assert response.json == {
            "id": 2,
            "encoding": self.encodings["file_two_faces"],
        }

    def test_getting_count(self):
        response = self.client.get(url_for("encodings.get_count"))

        assert response.status_code == 200
        assert response.json == {"count": 3}

    def test_getting_mean_encoding(self):
        response = self.client.get(url_for("encodings.get_mean_encoding"))

        assert response.status_code == 200
        assert response.json == {"mean_encoding": self.encodings["mean"]}
