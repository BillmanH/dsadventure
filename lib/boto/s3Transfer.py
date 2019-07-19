from boto.s3.connection import S3Connection
import boto
import yaml
import numpy as np
import pandas as pd
import datetime

#conn = boto.connect_s3()

try:
    conn = S3Connection()
except:
    myKeys = yaml.load(open(r'C:\Users\willi\OneDrive\Documents\keyfile.txt', 'r'))
    AWSSecretKey=myKeys['AWSSecretKey']
    AWSAccessKeyId=myKeys['AWSAccessKeyId']
    conn = S3Connection(AWSAccessKeyId, AWSSecretKey)

def save_world(world,user):
    conn = S3Connection()
    mybucket = conn.get_bucket('dsadventure')
    myKey = mybucket.get_key("world/" + user + "world.p")
    
def get_world(user):
    return world

