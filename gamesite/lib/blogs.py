# from boto.s3.connection import S3Connection
# import boto
import yaml
import os
import re
import yaml
import datetime


def test_connection():
    conn = boto.connect_s3()
    conn.get_bucket('flaskgame')
    return True


def get_notebooks_as_content():
    notebooks = os.listdir("prodweb/templates/prodweb/notebooks/")
    context = []
    for note in notebooks:
        if '.html' not in note:
            continue
        if note == 'article_not_found.html':
            continue
        n = re.sub("_", " ", note)
        n = re.sub(".html", "", n)
        context.append({"title": n,
                        "subtext": "written on a jupyter notebook, transcribed into a Django template",
                        "filename": note,
                        "type": "notebook"})
    return(context)
