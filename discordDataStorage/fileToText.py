from moviepy.editor import VideoFileClip
import pytesseract
from PIL import Image

video_path = 'D:/Videos/shotcut/output.mp4'

def videoToText():
    print("started")
    clip = VideoFileClip(video_path)
    print("clip extracted")
    frames = [frame for frame in clip.iter_frames(fps=10)]  # Extract frames every second
    print("frames extracted")

    text_content = ''

    for frame in frames:
        frame_image = Image.fromarray(frame)
        frame_text = pytesseract.image_to_string(frame_image)
        text_content += frame_text
    print("converted")
    
    with open("videoTextOutput.txt", "w", encoding='utf-8') as f:
        f.write(text_content)
    print("finsihed")

videoToText()