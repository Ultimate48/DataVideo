# DataVideo
An amazing tool which can convert any file, no matter the extension into a video file and convert it back to the original video

To run the program, follow the steps below:

1. Clone the repository

```
git clone https://github.com/Ultimate48/DataVideo
```

2. Change directory to the project folder

```
cd DataVideo
```

3. Create a virtual environment

```
python -m venv venv
```

4. Activate the virtual environment

For Windows:

```
venv\Scripts\activate
```

For Linux/MacOS:

```
source venv/bin/activate
```
   
5. Install the dependencies

```
pip install -r requirements.txt
```

6. Run the program

```
python encodeData.py <FILE_NAME>
```

7. To run the output video

```
start "" "output_video.avi"
```

The created video file would be approximately 20% bigger than the original file.

To decode the file, just run the decodeData.py file with the output_video.avi still in the directory and it would recreate the original file with the same name and extension before in the same directory with zero data loss.
