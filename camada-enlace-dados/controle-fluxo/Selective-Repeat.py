import time


def send_frame_sr(frame):
    print(f"Sending frame {frame}")
    time.sleep(1)  
    return True  

def selective_repeat(frames, window_size):
    send_base = 0
    next_frame = 0
    ack_received = [False] * window_size
    while send_base < len(frames):
        while next_frame < send_base + window_size and next_frame < len(frames):
            send_frame_sr(frames[next_frame])
            next_frame += 1

        ack_number = send_base + (next_frame % window_size) 
        ack_received[ack_number % window_size] = True
        print(f"ACK received for frame {ack_number}")

        while send_base < len(frames) and ack_received[send_base % window_size]:
            send_base += 1

        if send_base == next_frame:
            print(f"All frames up to {send_base} acknowledged")
