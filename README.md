# Engineers Fortune Cookie 🥠

A simple Flask web app that serves a random engineering wisdom on every refresh. Great for internal team dashboards, office screens, or a moment of reflection between deploys.

---

## Quick Start

### 1. Clone / navigate to the app folder

```bash
cd apps/engineers-fortune-cookie
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Open your browser at **http://localhost:5000**

Refresh the page to crack a new fortune cookie.

---

## Project Structure

```
engineers-fortune-cookie/
├── app.py              # Flask app
├── fortunes.txt        # One fortune per line
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Front-end page
```

---

## Adding Your Own Fortunes

Open `fortunes.txt` and add a new line for each saying. No restarts needed — fortunes are loaded fresh on every request.

```
Your refactor will break things — but more cleanly.
The spec is vague. Your interpretation will be wrong.
Your own saying goes here.
```

---

## Hosting on GitHub Pages (Public)

The Flask app can't run on GitHub Pages (it's static hosting only), so `docs/` contains a static version of the same site. The browser picks a random fortune on each page load, reading the text files in `docs/fortunes/`.

1. Edit the fortune files at the top level (`engineering-fortunes.txt`, `general-fortunes.txt`, `lawyer-fortunes.txt`).
2. Copy them into the Pages folder:
   ```bash
   python build_pages.py
   ```
3. Commit and push. Then in the repo: **Settings → Pages → Build and deployment → Deploy from a branch**, branch `main`, folder `/docs`.

Preview locally before pushing:

```bash
python -m http.server 8000 --directory docs
# open http://localhost:8000
```

Pages URLs: `/` (engineers), `/?mode=general`, `/?mode=lawyer`.

---

## Hosting on AWS (Internal Access)

See the full step-by-step guide in the main repository README, or follow the summary below.

### Deploy to EC2

```bash
# On the EC2 instance
pip install flask gunicorn

# Copy app files to the instance, then run:
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

### Run as a background service

Create `/etc/systemd/system/fortune.service`:

```ini
[Unit]
Description=Engineers Fortune Cookie
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/fortune-cookie
ExecStart=/home/ec2-user/.local/bin/gunicorn -w 2 -b 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable fortune --now
```

### Restrict access

In your EC2 Security Group, allow inbound TCP port `5000` only from your office or VPN IP range — do not open it to `0.0.0.0/0`.

---

## Requirements

- Python 3.8+
- Flask
