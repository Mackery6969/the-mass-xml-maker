# The Mass XML Maker
This project is a tool that converts video files (such as .mp4 and .mov) into spritesheets and generates corresponding XML files (in Sparrow v2 format). It also extracts audio from the video and saves it as an OGG file.
By Mackery

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before you can run this project, you need to have the following software installed:

### Python
Python 3.6+: This project is written in Python. Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://python.org).

### Python Packages
MoviePy: A Python module for video editing.
Pillow (PIL): A Python Imaging Library to handle image creation and manipulation.
lxml: A Python library for XML processing.
You can install these packages using pip:
```bash
pip install moviepy Pillow lxml
```

## Installation
1. Clone the Repository:
First, clone this repository to your local machine using Git:
```bash
git clone https://github.com/Mackery6969/the-mass-xml-maker.git
```

2. Navigate to the Project Directory:
```bash
cd the-mass-xml-maker
```

3. Install the Required Python Packages:
Install the necessary Python libraries as described in the Prerequisites section.

## Usage
1. Place Your Video Files:
Add your .mp4 and .mov video files to the input_videos folder. The script will process all video files in this folder.

2. Run the Script:
Execute the script using Python:
```bash
python convert.py
```

### Configure Settings (Optional):
You can adjust the gif_frame_rate and other settings in the script to customize the output.

## Output
Images Folder: The script will generate a spritesheet (.png) and an XML file in the images folder.
Sounds Folder: The audio extracted from the video will be saved as an .ogg file in the sounds folder.

Example Output Structure:
```bash
output_files/
├── images/
│   ├── video1.png
│   ├── video1.xml
│   ├── video2.png
│   └── video2.xml
└── sounds/
    ├── video1.ogg
    └── video2.ogg
```

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and make your changes. Then, submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE file](https://github.com/Mackery6969/the-mass-xml-maker/blob/main/LICENSE) for details.
