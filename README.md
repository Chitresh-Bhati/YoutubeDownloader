<h1>YouTube Video & Playlist Downloader (Stable macOS Version)</h1>

<p>
This is a Python-based YouTube downloader capable of downloading <strong>videos, audio-only files, or entire playlists</strong>.  
It uses <strong>pytubefix</strong> and includes specific fixes for macOS SSL issues, such as:
</p>

<ul>
  <li><code>ssl.SSLError: DECRYPTION_FAILED_OR_BAD_RECORD_MAC</code></li>
  <li>Certificate verification errors</li>
  <li>Large video downloads failing mid-way</li>
</ul>

<p>
The script supports:
</p>

<ul>
  <li>✔ Downloading single YouTube videos</li>
  <li>✔ Downloading audio-only streams</li>
  <li>✔ Downloading entire playlists</li>
  <li>✔ Choosing video quality (e.g., 720p)</li>
  <li>✔ Safe chunked downloading (prevents SSL failures)</li>
</ul>

<hr>

<h2>📦 Installation</h2>

<p>Install the required package:</p>

<pre><code>pip install pytubefix
</code></pre>

<hr>

<h2>⚙️ Features</h2>

<ul>
  <li>🎥 Download videos in your chosen resolution</li>
  <li>🎵 Download audio-only files</li>
  <li>📂 Download full playlists automatically</li>
  <li>🔐 Mac-safe chunked SSL download system</li>
  <li>🚨 Auto fallback to highest resolution when needed</li>
</ul>

<hr>

<h2>🖥️ Usage</h2>

<p>Edit the values in the <strong>USER INPUT SECTION</strong> of the script:</p>

<ul>
  <li><strong>url</strong> – YouTube video or playlist link</li>
  <li><strong>download_folder</strong> – local folder path</li>
  <li><strong>mode</strong> – <code>"video"</code> or <code>"playlist"</code></li>
  <li><strong>download_type</strong> – <code>"video"</code> or <code>"audio"</code></li>
  <li><strong>resolution</strong> – only required for videos</li>
</ul>

<p>Then simply run the script:</p>

<pre><code>python your_script_name.py
</code></pre>

<hr>

<h2>🛡 macOS SSL Fix</h2>

<p>
This version includes the recommended fix for macOS OpenSSL download errors:
</p>

<pre><code>from pytubefix import request
request.default_range_size = 1024 * 1024  # Safe 1 MB chunks
</code></pre>

<p>
Additionally, the YouTube object is initialized safely:
</p>

<pre><code>YouTube(url, use_oauth=False, allow_oauth_cache=False)
</code></pre>

<hr>

<h2>📁 Download Modes</h2>

<h3>1. Single Video</h3>
<pre><code>mode = "video"
download_type = "video"
resolution = "720p"
</code></pre>

<h3>2. Audio Only</h3>
<pre><code>mode = "video"
download_type = "audio"
</code></pre>

<h3>3. Full Playlist</h3>
<pre><code>mode = "playlist"
</code></pre>

<hr>

<h2>📷 Example Output</h2>

<pre>
🎥 Downloading video: Example Title in 720p  
⚠️ Requested resolution not available. Downloading highest resolution instead.  
✅ Download completed!
</pre>

<hr>

<h2>📜 License</h2>

<p>This project is free to use and modify.</p>

<hr>

<h2>💬 Support</h2>

<p>If you need help or want a Streamlit UI version, feel free to ask!</p>
