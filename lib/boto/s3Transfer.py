from boto.s3.connection import S3Connection
import boto
import yaml
# note to self, use the Loader=SafeLoader
import numpy as np
import pandas as pd
import pickle
import os


#conn = boto.connect_s3()

try:
    conn = S3Connection()
except:
    # for local loading, probably removed in production
    myKeys = yaml.safe_load(
        open(r'C:\Users\willi\OneDrive\Documents\keyfile.txt', 'r'))
    AWSSecretKey = myKeys['AWSSecretKey']
    AWSAccessKeyId = myKeys['AWSAccessKeyId']
    conn = S3Connection(AWSAccessKeyId, AWSSecretKey)


def save_world(world, user):
    conn = S3Connection()
    mybucket = conn.get_bucket('dsadventure')
    # save the bucket locally
    place = os.listdir()
    pickled_world = open('game/pickles/' + user + 'world.pkl', 'wb')
    pickle.dump(world, pickled_world)
    #myKey = mybucket.get_key('world/' + user + 'world.pkl')


def get_world(user):
    with (open('game/pickles/' + user + 'world.pkl', 'rb')) as pickle_file:
        world = pickle.load(pickle_file)
    return world
