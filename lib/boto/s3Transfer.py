# TODO: UPDATE BOTO ASSETS

# from boto3.s3.connection import S3Connection
# import boto3

# from boto3.s3.transfer

import yaml
import numpy as np
import pandas as pd
import pickle
import os


# conn = boto.connect_s3()
# def get_s3():
#     try:
#         conn = S3Connection()
#     except:
#         # for local loading, probably removed in production
#         myKeys = yaml.safe_load(
#             open(r'C:\Users\willi\OneDrive\Documents\keyfile.txt', 'r'))
#         AWSSecretKey = myKeys['AWSSecretKey']
#         AWSAccessKeyId = myKeys['AWSAccessKeyId']
#         conn = S3Connection(AWSAccessKeyId, AWSSecretKey)
#     return conn


def save_world(world, user):
    # Removing S3 functions as they aren't needed at current scale.
    # conn = get_s3()
    # mybucket = conn.get_bucket('dsadventure')
    # save the bucket locally
    pickled_world = open("game/pickles/" + user + "world.pkl", "wb")
    pickle.dump(world, pickled_world)
    # myKey = mybucket.get_key('world/' + user + 'world.pkl')


def get_world(user):
    try:
        with (open("game/pickles/" + user + "world.pkl", "rb")) as pickle_file:
            world = pickle.load(pickle_file)
    except FileNotFoundError:
        return None
    return world
