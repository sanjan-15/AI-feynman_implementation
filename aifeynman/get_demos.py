import os
import re
import shutil
import urllib.request
import ssl


def get_demos(dataset="example_data"):
    # Create a less strict SSL context for testing
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    base = "https://space.mit.edu/home/tegmark/aifeynman/" + dataset
    with urllib.request.urlopen(base, context=ssl_context) as base_response:
        string = base_response.read().decode('utf-8')

        # the pattern actually creates duplicates in the list
        pattern = re.compile('>.*\.txt<')
        filelist = map(lambda x: x[1:-1], pattern.findall(string))

        print("downloading...")

        try:
            os.mkdir(dataset)
        except FileExistsError:
            pass

        for fname in filelist:
            print(fname)
            print(base + '/' + fname)
            print(dataset + '/' + fname)
            with urllib.request.urlopen(base + '/' + fname, context=ssl_context) as response, \
                    open(dataset + '/' + fname, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)


if __name__ == "__main__":
    get_demos()
