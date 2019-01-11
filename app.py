import csv

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    # 1. Open the post html and get the contents as a string
    post_file = open('post.html', 'r')
    post_html = post_file.read()
    post_file.close()

    # 2. Create a new list that will hold all the html for your blog posts

    # 3. Open the csv file and read it using the CSV library. This will give you a list of rows.
    # See: https://docs.python.org/3/library/csv.html#csv.DictReader

    # 4. Loop over each row in the CSV. Each row is a blog post.

    # 5. Take post_html and replace {{title}} {{body}} {{author}} with the data in each blog post csv row

    # 6. Add the post_html to the new list you created above.

    # 7. Join all the items in your new list together into a single string. Name this string "blog_post_html".

    # 8. Open the index.html file and replace {{blog_posts}} with the blog post string you just created.
    index_file = open('index.html', 'r')
    index_html = index_file.read()

    index_html.replace('{{blog_posts}}', blog_post_html)

    index_file.close()

    return index_html
