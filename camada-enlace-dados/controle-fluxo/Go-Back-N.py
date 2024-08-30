import time

def send_frame_gbn(frame):
    print(f"Sending frame {frame}")
    time.sleep(1) 
    return True 

def go_back_n(frames, window_size):
    send_base = 0
    next_frame = 0
    while send_base < len(frames):
        while next_frame < send_base + window_size and next_frame < len(frames):
            send_frame_gbn(frames[next_frame])
            next_frame += 1

        if next_frame % 3 == 0:
            print(f"ACK lost for frame {send_base + 1}")
        else:
            ack_received = send_base + 1 
            print(f"ACK received for frame {ack_received}")
            send_base = ack_received

        if send_base != next_frame:
            print(f"Timeout, resending frames from {send_base}")
            next_frame = send_base
