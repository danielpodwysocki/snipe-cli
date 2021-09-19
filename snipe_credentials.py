import yaml
import os
from stat import ST_MODE
import sys


def check_perms(path):
    """
    returns 1 and prints an error message if the 'others' permission bit
    on the credentials file is not equal to 0
    """
    others_perms = oct(os.stat(os.path.expanduser(path))[ST_MODE])[-1:]
    try:
        if int(others_perms) != 0:
            raise Exception("The 'others' permission bit" +
                            "on the credentials file is not zero!")
    except Exception as e:
        print(e)
        return 1
    return 0


def get_credentials(path):
    """
    takes the path to the credentials as an argument
    get credentials from a file located in ~/.snipe/credentials.yaml
    retruns a dict with the following keys: "url" and "api_key"
    """
    credentials = {}
    if check_perms(path):
        sys.exit(1)

    with open(os.path.expanduser(path), "r") as stream:
        try:
            credentials = yaml.safe_load(stream)
            if "url" not in credentials:
                raise Exception("the " + path + " file " +
                                "is missing the url")
            elif "api_key" not in credentials:
                raise Exception("the " + path + " file " +
                                "is missing the api_key")
            elif credentials["url"][-1] == "/":
                credentials["url"] = credentials["url"][0:-1]
        except (yaml.YAMLError, Exception) as e:
            print(e)
            sys.exit(1)

    return credentials
