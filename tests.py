import unittest
from app import app, Question, BingBackground


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_homepage(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_get_question(self):
        response = self.client.get("/search/")
        assert response.status_code == 200

    def test_get_bingbackground(self):
        response = Question()
        assert response is not False

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
