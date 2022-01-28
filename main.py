from pypresence import Presence
import time 
import random

clientid = "clientID"
epoch = int(time.time())
RPC = Presence(clientid)
RPC.connect()
photos = ["lainbreakdown","laingun","shizuku", "lofi", "mosic", "read", "study-girl"]



print("i am working!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

while True:
    RPC.update(state="dying", details="ana bamot please fucking help me", large_image=random.choice(photos), large_text="i am studiiiiiiiiiiiiiiiii", start=epoch)
    time.sleep(120)
    print("refreshed")

