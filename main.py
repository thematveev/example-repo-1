import time
from threading import Thread


def upload_file(name):
    for i in range(1, 11):
        print(f"Uploading file {name} Part: {i}")
        time.sleep(0.5)




print("End of main")
# end comment
