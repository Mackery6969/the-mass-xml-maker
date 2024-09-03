import os
from moviepy.editor import VideoFileClip
from PIL import Image
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom
import math

def create_spritesheet(frames, output_path):
    num_frames = len(frames)
    grid_size = math.ceil(math.sqrt(num_frames))
    
    frame_width, frame_height = frames[0].size
    spritesheet_width = grid_size * frame_width
    spritesheet_height = grid_size * frame_height

    spritesheet = Image.new('RGBA', (spritesheet_width, spritesheet_height))

    for index, frame in enumerate(frames):
        x_offset = (index % grid_size) * frame_width
        y_offset = (index // grid_size) * frame_height
        spritesheet.paste(frame, (x_offset, y_offset))

    spritesheet.save(output_path, optimize=True)
    return frame_width, frame_height, spritesheet_width, spritesheet_height, grid_size

def create_sparrow_xml(output_folder, num_frames, frame_width, frame_height, grid_size, base_filename):
    texture_atlas = Element('TextureAtlas')
    texture_atlas.set('imagePath', f'{base_filename}.png') 

    for i in range(num_frames):
        sub_texture = SubElement(texture_atlas, 'SubTexture')
        frame_name = f"video{i:04d}.png"  
        x_offset = (i % grid_size) * frame_width
        y_offset = (i // grid_size) * frame_height
        sub_texture.set('name', frame_name)
        sub_texture.set('x', str(x_offset))
        sub_texture.set('y', str(y_offset))
        sub_texture.set('width', str(frame_width))
        sub_texture.set('height', str(frame_height))

    rough_string = tostring(texture_atlas, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml()

    xml_path = os.path.join(output_folder, f'{base_filename}.xml')
    with open(xml_path, 'w') as xml_file:
        xml_file.write(pretty_xml_as_string)

def extract_frames_audio_and_generate_spritesheet(input_folder, output_folder, gif_frame_rate=24):
    images_folder = os.path.join(output_folder, "images")
    sounds_folder = os.path.join(output_folder, "sounds")
    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(sounds_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_video_path = os.path.join(input_folder, filename)
            base_filename = os.path.splitext(filename)[0]
            
            video_clip = VideoFileClip(input_video_path)
            
            frames = []
            for i, frame in enumerate(video_clip.iter_frames(fps=gif_frame_rate, dtype='uint8')):
                frame_image = Image.fromarray(frame)
                frames.append(frame_image)
            
            if frames:
                spritesheet_path = os.path.join(images_folder, f'{base_filename}.png')
                frame_width, frame_height, spritesheet_width, spritesheet_height, grid_size = create_spritesheet(frames, spritesheet_path)
                create_sparrow_xml(images_folder, len(frames), frame_width, frame_height, grid_size, base_filename)
            
            audio_output_path = os.path.join(sounds_folder, f"{base_filename}.ogg")
            video_clip.audio.write_audiofile(audio_output_path, codec='libvorbis')
            
            video_clip.close()
            print(f"Processed {filename}: Spritesheet and XML saved to 'images', and audio saved to 'sounds'.")

# Usage
input_folder = "input_videos"  
output_folder = "output_files"  
gif_frame_rate = 24  

extract_frames_audio_and_generate_spritesheet(input_folder, output_folder, gif_frame_rate)
