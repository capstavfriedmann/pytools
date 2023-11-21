import json
import os
import pandas as pd
import hashlib
from functools import wraps


####################################################################
# Caching utility for json and dataframes                          #
#                                                                  #
# Uses a simple hash to store files in a cache folder:             #
#                                                                  #
####################################################################



def cache_json(key_arguments=None):
    if key_arguments is None:
        key_arguments = []
    
    def decorator(func):
        """
        Wrapper for functions making json api calls:
            Usage:
                @cache_json(["remote_addr", "credentials" ...])
                def call_api(connection_object remote_addr=None, credentials=None):
                    ....

            Decription:
                Simple wrapper for making test calls idempotent.
                Avoids the problem of invalid cache as a result of 
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = ""
            for arg in key_arguments:
                key += str(kwargs[arg])

            if not len(key_arguments):
                # if used without key args, simply use all args
                for arg in args:
                    key += str(arg)
                for _, value in kwargs.items():
                    key += str(value)

            if _is_in_cache(key) and \
             os.environ.get("IGNORE_CACHE") is not True:
                return _retrieve_cache_json(key)

            result = func(*args, **kwargs)
            try:
                json.loads(result)
            except:
                print("ERROR: cache_json wrapper recieved a non-json return value")

            _insert_cache_json(key, result)
            return result
        return wrapper
    return decorator


def _insert_cache_dataframe(key, df):
    parent = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(f"{parent}/.cache"):
        os.mkdir(f"{parent}/.cache")

    if _is_in_cache(__deterministic_hash(key)):
        print("---Tried to save to populated cache, please clear cache to overwrite---")
        return
    df.to_csv(f"{parent}/.cache/{__deterministic_hash(key)}")


def _is_in_cache(key):
    parent = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(f"{parent}/.cache"):
        return False

    return __deterministic_hash(key) in os.listdir(f"{parent}/.cache")


def _retrieve_cache_dataframe(key):
    parent = os.path.dirname(os.path.abspath(__file__))
    try:
        return pd.read_csv(f"{parent}/.cache/{__deterministic_hash(key)}", index_col=0)
    except:
        return None


def _insert_cache_json(key, js):
    parent = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(f"{parent}/.cache"):
        os.mkdir(f"{parent}/.cache")
    
    with open(f"{parent}/.cache/{__deterministic_hash(key)}", "w") as f:
        json.dump(js, f, indent=4)


def _retrieve_cache_json(key):
    parent = os.path.dirname(os.path.abspath(__file__))
    cache_value = []
    try:
        with open(f"{parent}/.cache/{__deterministic_hash(key)}", 'r') as f:
            content = f.read()
            if not content.strip():  # Check if the content is a blank string
                return []
            cache_value = json.loads(content)  # Decode the JSON content
    except Exception as e:
        print("Could not load cached config values", str(e))
        return False
    return cache_value
    

def __deterministic_hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()