import os
import subprocess
import uuid
from datetime import datetime

# 📎 The Instagram post, reel, story, or highlight URL goes here
url = "https://www.instagram.com/link/"

# 🍪 Path to your cookies file (required for private or login-restricted content)
cookies_path = "cookies.txt"

# 📁 Create a unique output folder based on today's date and a short ID
folder_name = datetime.now().strftime("%Y%m%d") + "_" + uuid.uuid4().hex[:6]
output_directory = f"./Instagram/{folder_name}"
os.makedirs(output_directory, exist_ok=True)

# 🎞️ Function to detect the video codec of a given file using ffprobe
def get_video_codec(filepath):
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

# 🔄 Function to re-encode the video to H.264 (for compatibility)
def reencode_video(filepath):
    temp_output = os.path.join(output_directory, f"{uuid.uuid4().hex[:8]}.mp4")

    cmd = [
        'ffmpeg', '-y',                 # 📝 Overwrite if needed
        '-i', filepath,                # 🎞️ Input file
        '-c:v', 'libx264',             # 🎬 Encode video to H.264
        '-preset', 'superfast',        # ⚡ Speed-focused preset
        '-crf', '23',                  # 🎚️ Quality setting (lower = better)
        '-c:a', 'aac',                 # 🎧 Audio encoding
        '-b:a', '192k',                # 🔊 Audio bitrate
        temp_output
    ]

    print(f"🔄 Re-encoding video: {filepath} ...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        os.replace(temp_output, filepath)
        print(f"✅ Successfully re-encoded and replaced: {filepath}")
    else:
        print(f"❌ Re-encoding failed:\n{result.stderr}")
        if os.path.exists(temp_output):
            os.remove(temp_output)

# 🚀 Start downloading process
try:
    cmd = [
        'gallery-dl',
        '--cookies', cookies_path,
        '--directory', output_directory,
        url
    ]

    print(f"\n🚀 Starting download from Instagram:\n🔗 {url}")
    print(f"📁 Saving to folder:\n📂 {output_directory}\n")

    # 🔄 Run gallery-dl and stream its output in real time
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print("📥", line.strip())

    process.wait()

    # ✅ Check if gallery-dl completed successfully
    if process.returncode == 0:
        print("\n✅ Download completed successfully!\n")
    else:
        print(f"\n❌ Download failed with exit code: {process.returncode}\n")

    # 🧪 Process downloaded files: only look at .mp4 videos
    for filename in os.listdir(output_directory):
        if not filename.lower().endswith(".mp4"):
            continue  # ❌ Skip non-video files

        filepath = os.path.join(output_directory, filename)
        print(f"\n📂 Checking file: {filename}")

        codec = get_video_codec(filepath)
        if codec:
            print(f"🎞️ Video codec detected: {codec}")
        else:
            print("⚠️ Could not detect codec. Skipping re-encoding.")
            continue

        # 🔁 Re-encode if the codec isn't H.264 or compatible
        if codec not in ["h264", "avc1"]:
            print("⚠️ Incompatible codec detected. Re-encoding...")
            reencode_video(filepath)
        else:
            print("✅ Codec is compatible. No re-encoding needed.")

    print(f"\n🎉 All done! Your videos are saved in:\n📂 {output_directory}\n")

except Exception as e:
    print(f"\n❌ Oops! Something went wrong:\n{e}")
