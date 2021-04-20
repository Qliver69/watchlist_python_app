import requests

def get_video(URL, path):
    try:
            # get the content of the file on the current page
            r = requests.get(URL)
            # write the content got just before and write it in a file
            with open(path, 'wb') as f:
                f.write(r.content)
            print(r.headers['content-typre']+'\t'+r.encoding)
    except:
        print('Error: problem occurs during download, wait for the download to finish and check if it is readable or try again')