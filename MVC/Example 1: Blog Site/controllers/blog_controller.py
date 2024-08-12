"""
    Explanation:

    list_posts retrieves all blog posts from the model and displays them.
    view_post fetches a single blog post based on its ID and displays its details.
    new_post handles both showing the form for creating a new post and saving a new post when the form is submitted.
"""

from app.models.post_model import PostModel
from flask import render_template, request, redirect, url_for

class BlogController:
    @staticmethod
    def list_posts():
        posts = PostModel.get_all_posts()
        return render_template('posts/post_list.html', posts=posts)

    @staticmethod
    def view_post(post_id):
        post = PostModel.get_post_by_id(post_id)
        return render_template('posts/post_detail.html', post=post)

    @staticmethod
    def new_post():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            PostModel.create_post(title, content)
            return redirect(url_for('list_posts'))
        return render_template('posts/new_post.html')
    
   
   
