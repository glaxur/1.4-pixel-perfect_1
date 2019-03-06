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

    blog_posts = []

    # 3. Open the csv file and read it using the CSV library. This will give you a list of rows.
    # See: https://docs.python.org/3/library/csv.html#csv.DictReader

    # With this, I'm saying that I want to open the data.csv file as a csv file
    # Then I'm making a varaiable called data_csv that uses a dictionary reader to read the csvfile/data.csv
    # Then, for each (new var) 'row' in data_csv, I want to print the row called "image", row called
    # category, row called title, etc.

    with open('data.csv') as csvfile:
        data_csv = csv.DictReader(csvfile)
        for row in data_csv:
            print(row['image'], row['category'], row['title'], row['body'], row['author'],
            row['date'])
# 4. Loop over each row in the CSV. Each row is a blog post.

# 5. Take post_html and replace {{title}} {{body}} {{author}} with the data in each blog post csv row
# Here I am making a new variable called columns. This is all a continuation of the function above
# I'm using the keys method to say that columns is equal to a row of dict keys in the csv file
# Then, I'm making a variable called current_post that is equal to post_html (see line 13)
# then, for each col (new var) in columns -row.keys-, I want to take current_post, which is post_html,
# and do the replace method, current_post.replace to replace the thing in post.html
# that is in {{}} with row[col] - row[col] is defined as going through each column,
            columns = row.keys()
            current_post = post_html
            for col in columns:
                current_post = current_post.replace('{{' + col + '}}', row[col])
            blog_posts.append(current_post)

# 6. Add the post_html to the new list you created above.


# 7. Join all the items in your new list together into a single string. Name this string "blog_post_html".

    blog_post_html = ' '.join(blog_posts)


    # 8. Open the index.html file and replace {{blog_posts}} with the blog post string you just created.
    index_file = open('index.html', 'r')
    index_html = index_file.read()

    index_html = index_html.replace('{{blog_posts}}', blog_post_html)

    index_file.close()

    return index_html