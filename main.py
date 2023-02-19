from uplink_python.uplink import Uplink
from uplink_python.module_classes import DownloadOptions, Permission, ListObjectsOptions
from uplink_python.errors import InternalError, BucketNotFoundError, StorjException

# UPLINK WINDOWS OS TUTORIAL
# https://github.com/storj-thirdparty/uplink-python
# WINDOWS ACTIVATE CGO
# set CGO_ENABLED=1

MY_API_KEY = "1dfJRZh8FxYQB3czs1d13ezgpuC8PHGtX6rP7HRi16mqdSeFqTXvC4KfDGopswDua2KNeiTprdAKqSXXzu5rM3URpPaJjBZLySAGHV9PoKdSCTw7kyDs"
MY_SATELLITE = "12L9ZFwhzVpuEKMUNUqkaTLGzwY9G24tbiigLiXpmZWKwmcNDDs@eu1.storj.io:7777"
MY_ENCRYPTION_PASSPHRASE = "xsA9wgE6zTm7uzJ@"
MY_BUCKET = "saugykla"

if __name__ == '__main__':
    try:
        uplink = Uplink()

        # function calls
        # request access using passphrase
        print("\nRequesting Access using passphrase...")
        access = uplink.request_access_with_passphrase(MY_SATELLITE, MY_API_KEY, MY_ENCRYPTION_PASSPHRASE)
        ### some code ###
        project = access.open_project()

        bucket_list = project.list_buckets()
        for bucket in bucket_list:
            # as python class object
            print(bucket.name)
            # as python dictionary
            print(bucket.get_dict())
        print("Buckets listing: COMPLETE!")

        objects_list = project.list_objects(MY_BUCKET, ListObjectsOptions(recursive=True, system=True))
        # print all objects path

        print(objects_list)

        for obj in objects_list:
            print(obj.key, " | ", obj.is_prefix)  # as python class object
            print(obj.get_dict())  # as python dictionary

        # some code
    except StorjException as exception:
        print("Exception Caught: ", exception.details)
