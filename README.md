#  𝄞Music-Generation

![Music Compose Logo - Generated on Microsoft Designer with Prompt "Music Compose Text in the middle and a music logo on the left with plain blue blurred background, Picture"](/static/music_compose_logo_2by1.jpg)

- Ever had a thought about composing music in your mind with the description you have?
- Well.. I think you have the solution now in front of you.

---

- Create your music that the world had never listened before. It's personalized and only yours.  
- You want a ringtone that is only yours? You have the power in your hands right here.
- You want a intro music for your Podcast? The keyboard is right in front you to ask.
- You want a clean outro for your YouTube Video? You are just a description of your music away.

---

> Try out the project by following the detailed steps provided in the [`Getting Started`](#-getting-started) section below.

## 📑 Getting Started

Steps to Clone, Install, `Run` the project

### Cloning the project locally

For HTTPS Method,

```sh
# Cloning the GitHub Repository
git clone https://github.com/AjayRahul1/Music-Generation.git

# Going into the directory
cd Music-Generation/
```

For SSH Method (Prefer this only if SSH Key was setup on your computer),

```sh
# Cloning the GitHub Repository
git clone git@github.com:AjayRahul1/Music-Generation.git

# Going into the directory
cd Music-Generation/
```

### Create a virtual environment with Python 3.10.x version

#### Python Version 3.10 Installation

- For Windows
  - Go to [Python Official Downloads](https://www.python.org/downloads/) Page (or) Click [here](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe) to download Python 3.10.11 installer directly.
  - Download 3.10.x version (x can be any number you find there)
  - Run the installer file.
  - Check tick the `Add python to PATH`.
  - During installation, make sure to select the option `Customize installation`.
  - Choose a unique installation directory for Python 3.10.x to avoid overwriting your existing Python version 3.x.x installation.
  - If Add Python to Path is `not` checked, open PATH Environment Variables and edit PATH variable by adding Python 3.10 version.

- For Linux (Open Terminal)
  - For Ubuntu
    - ```sudo apt install python3.10```
  - For Fedora
    - ```sudo dnf install python3.10```

#### Verify Python Version after Installation

- Windows
  - ```py -3.10 --version```
- Linux
  - ```python3.10 --version```

#### Creation of Virtual Environment

- Windows
  - ```py -3.10 -m venv venv```
- Linux
  - ```python3.10 -m venv venv```
- Activating Virtual Environment
  - Windows
    - In Windows 10, Open Powershell (or) In Windows 11, Windows Terminal.
    - ```venv\Scripts\Activate```
    - If you face any `error` with this command, it's because Microsoft disables Running Scripts by default.
    - To enable it temporarily, we run following command and try above command again.
      - ```powershell -ExecutionPolicy bypass```
  - Linux (In Terminal):
    - ```source venv/bin/activate```

#### Installing Requirements

- Check whether you can see (venv) in the terminal that gives the sign of successful virtual environment activation
- ```pip install -r requirements.txt```
- Take a moment of rest and comeback later while the requirements gets installed.

### Run the project on LocalHost

- ```uvicorn main:app --reload```
- Open [Localhost](http://127.0.0.1:8000/) on your computer
- `Optional`: You can change the port number as per your wish.
- Now the website is at your hands!
- Go ahead and type your prompt to generate music accordingly.
