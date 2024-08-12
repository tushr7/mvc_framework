"""
Explanation:

    get_all_posts returns a list of all blog posts.
    get_post_by_id returns a specific post based on its ID.
    create_post creates a new blog post and adds it to the list of posts.
"""
class PostModel:
    posts = []

    @staticmethod
    def get_all_posts():
        return PostModel.posts

    @staticmethod
    def get_post_by_id(post_id):
        for post in PostModel.posts:
            if post['id'] == post_id:
                return post
        return None

    @staticmethod
    def create_post(title, content):
        post_id = len(PostModel.posts) + 1
        post = {'id': post_id, 'title': title, 'content': content}
        PostModel.posts.append(post)
