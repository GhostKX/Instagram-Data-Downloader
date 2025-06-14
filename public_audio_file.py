import subprocess
import os
import uuid

# 📎 Asking the user to paste the Instagram post or reel link
video_url = input("📥 Paste the Instagram post or reel URL: ").strip()

# 🧾 Generating a short unique ID to avoid filename collisions
unique_id = uuid.uuid4().hex[:8]

# 📁 Output file paths
video_dir = "Instagram_temp_video"
audio_dir = "Instagram_audio"
video_file = f"{video_dir}/insta_{unique_id}.mp4"
mp3_file = f"{audio_dir}/insta_audio_{unique_id}.mp3"

# 📂 Make sure output folders exist
os.makedirs(video_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

try:
    # ⬇️ Download Instagram video using yt-dlp
    print("⬇️ Downloading video from Instagram...")
    result = subprocess.run([
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",  # Getting the best quality video+audio
        "-o", video_file,  # Output filename
        video_url
    ], text=True)

    # ❌ Checking if download failed or file is missing
    if result.returncode != 0 or not os.path.exists(video_file):
        print("❌ Failed to download the video.")
        exit(1)

    # 🎧 Extract MP3 audio from the video using ffmpeg
    print("🎧 Extracting audio and converting to MP3...")
    result = subprocess.run([
        "ffmpeg", "-y",             # Overwrite if output file exists
        "-i", video_file,          # Input: the downloaded video
        "-vn",                     # No video (extract audio only)
        "-acodec", "libmp3lame",   # Use MP3 codec
        "-ab", "192k",             # Audio bitrate: good quality
        mp3_file,
    ], text=True)

    # ❌ Check if ffmpeg failed or output is missing
    if result.returncode != 0 or not os.path.exists(mp3_file):
        print("❌ Failed to extract audio.")
        exit(1)

    # 🧹 Clean up the original video file
    os.remove(video_file)
    print("🧹 Cleaned up temporary video file.")

    # ✅ Done!
    print(f"✅ Success! MP3 saved as: {mp3_file}")

except Exception as e:
    # ⚠️ Catch unexpected errors and display them
    print(f"⚠️ An unexpected error occurred:\n{e}")
