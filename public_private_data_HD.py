import os
import subprocess
import uuid
from datetime import datetime

# The Instagram post, reel, stories, highlights URL should be placed
url = "https://www.instagram.com/link/"

# Path to your Instagram cookies file (needed to access private content)
cookies_path = "cookies.txt"

# Generate a unique folder name for this download session based on date + short random ID
folder_name = datetime.now().strftime("%Y%m%d") + "_" + uuid.uuid4().hex[:6]
output_directory = f"./Instagram/{folder_name}"

# Make sure the output folder exists (create it if not)
os.makedirs(output_directory, exist_ok=True)

def get_video_codec(filepath):
    """
    Use ffprobe to figure out what video codec is used in the given file.
    Returns codec name as a string (e.g., 'h264') or None if it can't tell.
    """
    try:
        cmd = [
            'ffprobe', '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=codec_name',
            '-of', 'default=noprint_wrappers=1:nokey=1',
            filepath
        ]
        codec = subprocess.check_output(cmd).decode().strip()
        return codec
    except subprocess.CalledProcessError:
        return None

def reencode_video(filepath):
    """
    Re-encode the given video to H.264 codec using ffmpeg.
    Saves to a temporary file first, then replaces the original file.
    """
    temp_output = os.path.join(output_directory, f"{uuid.uuid4().hex[:8]}.mp4")

    cmd = [
        'ffmpeg', '-y',               # Overwrite output without asking
        '-i', filepath,               # Input file
        '-c:v', 'libx264',            # Video codec: H.264
        '-preset', 'superfast',       # Speed up encoding (less compression)
        '-crf', '23',                 # Quality level (lower is better)
        '-c:a', 'aac',                # Audio codec: AAC
        '-b:a', '192k',               # Audio bitrate
        temp_output
    ]

    print(f"🔄 Re-encoding video: {filepath} ...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        os.replace(temp_output, filepath)  # Replace original with re-encoded
        print(f"✅ Finished re-encoding and replaced original file.")
    else:
        print(f"❌ Re-encoding failed:\n{result.stderr}")
        if os.path.exists(temp_output):
            os.remove(temp_output)

try:
    cmd = [
        'gallery-dl',
        '--cookies', cookies_path,
        '--directory', output_directory,
        url
    ]

    print(f"\n🚀 Starting download from Instagram:\n{url}")
    print(f"\n📁 Files will be saved in:\n{output_directory}\n")

    # Start gallery-dl and capture its live output
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in process.stdout:
        print("📥", line.strip())

    process.wait()

    if process.returncode == 0:
        print("\n✅ Download completed successfully!\n")
    else:
        print(f"\n❌ Download failed with exit code: {process.returncode}\n")

    # Now check each downloaded mp4 video file
    for filename in os.listdir(output_directory):
        if not filename.lower().endswith(".mp4"):
            continue  # Skip any non-video files

        filepath = os.path.join(output_directory, filename)
        print(f"\n📂 Checking file: {filename}")

        codec = get_video_codec(filepath)
        if codec:
            print(f"🎞️ Video codec detected: {codec}")
        else:
            print("⚠️ Couldn't detect video codec, skipping re-encoding.")
            continue

        # If codec isn't H.264, re-encode it to ensure compatibility
        if codec not in ["h264", "avc1"]:
            print("⚠️ Codec not compatible. Starting re-encoding...")
            reencode_video(filepath)
        else:
            print("✅ Codec is fine. No re-encoding needed.")

    print(f"\n🎉 All done! Check your videos in:\n{output_directory}\n")

except Exception as e:
    print(f"\n❌ Oops, something went wrong:\n{e}")
