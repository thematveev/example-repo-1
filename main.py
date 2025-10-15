import time
from threading import Thread
from assets import hello

def upload_file(name):
    for i in range(1, 11):
        print(f"Uploading file {name} Part: {i}")
        time.sleep(0.5)



hello()
print("End of main")
# end comment
