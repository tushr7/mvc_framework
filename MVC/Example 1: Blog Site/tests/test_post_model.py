"""
Explanation:

    This test file checks if the blog post creation and retrieval functionalities work as expected.
"""
import unittest
from app.models.post_model import PostModel

class TestPostModel(unittest.TestCase):
    def test_create_post(self):
        PostModel.create_post("Test Title", "Test Content")
        posts = PostModel.get_all_posts()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], "Test Title")
        self.assertEqual(posts[0]['content'], "Test Content")

    def test_get_post_by_id(self):
        PostModel.create_post("Another Title", "Another Content")
        post = PostModel.get_post_by_id(1)
        self.assertIsNotNone(post)
        self.assertEqual(post['title'], "Test Title")

if __name__ == '__main__':
    unittest.main()
