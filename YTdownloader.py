import streamlit as st
from pytubefix import YouTube, Playlist, request
import os

# ------------------------------------------------------------
# Streamlit YouTube Downloader (Stylish UI + Progress Bar)
# ------------------------------------------------------------
# REQUIREMENTS:
#   pip install pytubefix streamlit
# RUN:
#   streamlit run app.py
# ------------------------------------------------------------

# Fix SSL chunk issues for macOS
request.default_range_size = 1024 * 1024   # 1 MB chunks

st.set_page_config(page_title="YouTube Downloader", page_icon="🎬", layout="centered")

st.markdown("""
    <h1 style='text-align:center; color:#ff4b4b;'>🎬 YouTube Video & Audio Downloader</h1>
    <p style='text-align:center; color:gray;'>Fast • Safe • Stylish Streamlit UI</p>
""", unsafe_allow_html=True)

# ------------------------------
# USER INPUTS
# ------------------------------
url = st.text_input("🔗 Paste YouTube Video or Playlist Link")

col1, col2 = st.columns(2)
with col1:
    download_type = st.selectbox("Download Type", ["Video", "Audio Only"])
with col2:
    quality = st.selectbox("Video Quality", ["1080p", "720p", "480p", "360p", "240p", "144p"])

download_folder = st.text_input("📁 Download Location (Folder Path)")
mode = st.radio("Select Mode", ["Video", "Playlist"], horizontal=True)

progress_bar = st.progress(0)
progress_text = st.empty()

# ------------------------------------------------------------
# PROGRESS CALLBACK
# ------------------------------------------------------------
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    downloaded = total_size - bytes_remaining
    percent = downloaded / total_size
    progress_bar.progress(percent)
    progress_text.text(f"Progress: {percent*100:.2f}%")

# ------------------------------------------------------------
# DOWNLOAD FUNCTION
# ------------------------------------------------------------

def safe_download(stream, folder):
    try:
        stream.download(output_path=folder)
    except Exception:
        stream.download(output_path=folder)

def download_video(url, folder, resolution=None, audio_only=False):
    yt = YouTube(url, on_progress_callback=on_progress, use_oauth=False, allow_oauth_cache=False)

    st.info(f"Fetching: {yt.title}")

    if audio_only:
        stream = yt.streams.filter(only_audio=True).first()
    else:
        stream = yt.streams.filter(progressive=True, res=resolution).first()
        if stream is None:
            stream = yt.streams.get_highest_resolution()

    safe_download(stream, folder)
    st.success("Download Complete ✔️")

# ------------------------------------------------------------
# MAIN DOWNLOAD BUTTON
# ------------------------------------------------------------
if st.button("🚀 Start Download"):
    if not url or not download_folder:
        st.error("❌ Please enter both URL and download folder!")
    else:
        if not os.path.exists(download_folder):
            st.error("❌ Download folder does not exist!")
        else:
            progress_bar.progress(0)
            progress_text.text("Starting download...")

            if mode == "Video":
                download_video(url, download_folder, resolution=quality, audio_only=(download_type == "Audio Only"))

            else:
                pl = Playlist(url)
                total = len(pl.video_urls)
                count = 0
                for v in pl.video_urls:
                    download_video(v, download_folder, resolution=quality, audio_only=(download_type == "Audio Only"))
                    count += 1

                st.success("🎉 Playlist Downloaded Successfully!")

st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit & pytubefix</p>
""", unsafe_allow_html=True)
