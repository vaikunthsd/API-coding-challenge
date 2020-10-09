import unittest
from ApiHandler import ApiHandler


class ApiTest(unittest.TestCase):

    def test_get(self):
        api_handler = ApiHandler()
        result = api_handler.get("posts", 99)
        self.assertDictEqual(
            result, {"title": "temporibus sit alias " +
                     "delectus eligendi possimus magni",
                     "userId": 10, "id": 99,
                     "body": "quo deleniti praesentium " +
                     "dicta non quod\n" +
                     "aut est molestias\n" +
                     "molestias et officia quis nihil\nitaque dolorem quia"})

    def test_get_error(self):
        api_handler = ApiHandler()
        result = api_handler.get("post", 99)
        self.assertDictEqual(result, {"title": "N/A"})

    def test_post(self):
        api_handler = ApiHandler()
        newData = {"userId": 500,
                   "title": "Security Interview Post",
                   "body": "This is an insertion test with a known API"}
        result = api_handler.post("posts", newData)
        self.assertTupleEqual(result, (101, 201, "Express"))

    def test_post_error(self):
        api_handler = ApiHandler()
        newData = {"userId": 500,
                   "title": "Security Interview Post",
                   "body": "This is an insertion test with a known API"}
        result = api_handler.post("post", newData)
        self.assertTupleEqual(result, ("Error", "Not Found"))

    def test_delete(self):
        api_handler = ApiHandler()
        result = api_handler.delete("posts", 101)
        self.assertTupleEqual(result, (200, "nosniff"))

    def test_delete_error(self):
        api_handler = ApiHandler()
        result = api_handler.delete("post", 101)
        self.assertTupleEqual(result, ("Error", "Not Found"))


if __name__ == "__main__":
    unittest.main()
