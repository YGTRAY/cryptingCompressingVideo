import cv2
import os
import threading

def merge_video():
    # Set the path to the folder containing the frames
    frame_folder_path = "C:/Users/hp/Desktop/piDecrypted_Decompressed"
    
    # Set the path to the output video file
    output_video_path = "C:/Users/hp/Desktop/piEncryptedMerged/output_video.mp4"
    # Get the list of frames sorted by frame number
    frame_names = os.listdir(frame_folder_path)
    frame_names.sort(key=lambda x: int(x.split(".")[0][5:]))
    
   

    height =2160
    width = 3840
    
    # Create the video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))
    
    # Iterate through the frames and write them to the output video
    for frame_name in frame_names:
        frame_path = os.path.join(frame_folder_path, frame_name)
        frame = cv2.imread(frame_path)
        out.write(frame)
    
    # Release the video writer and destroy all windows
    out.release()
    cv2.destroyAllWindows()

def merge_video_thread():
    """
    This function runs the compress_video() function in a separate thread.
    """
    t = threading.Thread(target=merge_video)
    t.start()

def on_merge_button_click():
    """
    This function is called when the user clicks the compress button.
    """
    merge_video_thread()