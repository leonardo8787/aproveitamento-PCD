import time

def send_frame_sw(frame):
    print(f"Sending frame {frame}")
    time.sleep(1)  # Simulating network delay
    return True  # Simulating successful ACK

def sliding_window(frames, window_size):
    send_base = 0
    next_frame = 0
    while send_base < len(frames):
        while next_frame < send_base + window_size and next_frame < len(frames):
            send_frame_sw(frames[next_frame])
            next_frame += 1

        ack_received = send_base + 1  # Simulating ACK for the next frame
        print(f"ACK received for frame {ack_received}")
        send_base = ack_received
