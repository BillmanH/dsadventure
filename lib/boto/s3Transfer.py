from boto.s3.connection import S3Connection
import boto
import yaml
#note to self, use the Loader=SafeLoader 
import numpy as np
import pandas as pd
import pickle

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
    #save the bucket locally 
    pickled_world = open('pickles/'+ user + 'world.pkl', 'w')
    pickle.dump(world, pickled_world)
    myKey = mybucket.get_key('world/' + user + 'world.pkl')
    

def get_world(user):
    return world

