import time

def send_frame(frame):
    print(f"Sending frame {frame}")
    time.sleep(1)
    return True  

def stop_and_wait(frames):
    for frame in frames:
        while True:
            print(f"Attempting to send frame {frame}")
            if send_frame(frame):
                print(f"ACK received for frame {frame}")
                break
            else:
                print(f"Timeout, resending frame {frame}")
