import instaloader

# 🚀 Create an instance of Instaloader
L = instaloader.Instaloader()

# 🔐 Your Instagram credentials
username = 'your_username'
password = 'your_password'

try:
    # 🔐 Log in to Instagram
    print("🔑 Logging in to Instagram...")
    L.login(username, password)
    print("✅ Successfully logged in!")

    # 👤 Define the target user
    target_username = 'target_username'
    print(f"🎯 Target username: {target_username}")

    # 🔗 Instagram post URL
    url = 'https://www.instagram.com/p/shortcode/'  # Replace with actual post URL

    # 🔍 Extract shortcode from the URL
    shortcode = url.strip().split('/')[-2]
    print(f"📎 Extracted post shortcode: {shortcode}")

    # 📥 Load post metadata
    print("📄 Fetching post information...")
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    # 💾 Download the post
    print("📥 Downloading post media...")
    L.download_post(post, target=shortcode)
    print("✅ Post downloaded successfully!")

except Exception as e:
    # ❗ Handle errors
    print("❌ An error occurred:", e)


