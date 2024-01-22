import threading

import cv2

frame_count = 0

def video_to_frames():
    """
    This function reads a video file and saves each frame as an individual image file.
    """
    video_path = "C:/Users/hp/Desktop/pigeon.mp4"
    output_dir = "C:/Users/hp/Desktop/pi"
    
    cam = cv2.VideoCapture(video_path)

    current_frame = 0
    while True:
        ret, frame = cam.read()
        if ret:
            name = f"{output_dir}/frame{current_frame}.jpg"
            print(f"Creating {name}...")
            cv2.imwrite(name, frame)
            current_frame += 1
        else:
            break
    cam.release()





def split_video_thread():
    """
    This function runs the compress_video() function in a separate thread.
    """
    t = threading.Thread(target=video_to_frames)
    t.start()

def on_split_button_click():
    """
    This function is called when the user clicks the compress button.
    """
    split_video_thread()