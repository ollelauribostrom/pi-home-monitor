# Raspberry PI Home Monitor
- Monitor movements with Python, Flask & OpenCV
- Chat based UI (Talk to the monitor through SMS using Twilio)
- Subscribe to notifications when the monitor picks up movements

> Also, scare off intruders by turning on some swedish radio!


Installation
------------
```bash
  # Get yourself a Twilio phone number
  # Make sure your webcamera is working
  # Download vlc to your mobile phone (needed due to codec issue)
  # Make sure you have git installed
  # Make sure you have python 3 & pip 3 installed
  # Make sure you have nodejs installed
  # Make sure you have npm package sverigesradio installed globally

  # Clone repo
  git clone https://github.com/ollelauribostrom/pi-home-monitor.git
  cd pi-home-monitor

  # Install dependencies
  make install
  # or
  sudo make install

  # If using ngrok
  ngrok http 5000
  # Configure Twilio webhook
  # Add ngrok tunnel adress to .env as BASE_URL

  # Set up env
  touch .env
  echo "TWILIO_ACCOUNT_SID=<YOUR_TWILIO_SID>" >> .env
  echo "TWILIO_AUTH_TOKEN=<YOUR_TWILIO_TOKEN>" >> .env
  echo "TWILIO_FROM_NUMBER=<YOUR_TWILIO_NUMER>" >> .env
  echo "SHARED_SECRET=<A_STRING_USED_AS_PASSWORD>" >> .env
  echo "BASE_URL=<NGROK_TUNNEL_OR_PUBLIC_ADRESS>" >> .env

  # Run
  # Change camera settings in src/config.py
  make dev 
  # or
  sudo make production 
```

#### Common errors & possible solutions
```bash
  # Locale settings error
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8

  # Codec issues / corrupt files
  apt-get install ffmpeg x264
  # and/or change codec settings in src/config.py

  # Behind a router
  # —> forward port 80 @ router to pi ip-adress

  # OpenCV issues
  # Try installing OpenCV & dependencies from scratch
  # https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
```

Interacting with the monitor
------------------------
-> Hi Monitor!   
> Hi! Your number is not on the list of authorized numbers. Do you know the secret?

-> secret   
> Great, your number is now on the list of authorized numbers

-> Subscribe to notifications
> Cool, you are now reciving notifications from the monitor

... intruder walks in
> Movements @ http://url/video

-> Play radio
> Radio started

... intruder is scared off

#### List of commands
- **Start radio**: Start radio / Play radio
- **Stop radio**: Stop radio / Pause radio
- **Radio status**: Is radio playing? / Radio status
- **Subscribe**: Subscribe to notifications / Start notifying me on movements / Notify me on movements
- **Unsubscribe**: Stop notifying me / End subscription / Unsubscribe from notifications

Todo
---------
| Task                                                | Type        | Priority |
|:----------------------------------------------------|:------------|:---------|
| Each recording is duplicated when saved             | Bug         | High     |
| Videos are unplayable on iOS (codec issue)          | Bug         | High     |
| Make sure it runs without npm package sverigesradio | Test        | Medium   |
| Add more tests                                      | Test        | Medium   |
| Add possibility to turn on radio on movement        | Enhancement | Low      |
| Add possability to tune in on live video stream     | Enhancement | Low      |
| Make the bot smarter                                | Enhancement | Low      |
| Continuously remove old recordings                  | Enhancement | Low      |


Commands
--------
- `make dev`: Start development live-reload server
- `make production`: Start production server
- `make install`: Install dependencies in requirements.txt
- `make test`: Run tests in /tests
- `make build`: Build docker image
- `make run`: Run docker image
- `make inspect`: Inspect docker container
- `make shell`: Open docker container shell
- `make stop`: Stop docker container
- `make clean`: Remove docker container & image

> During dev, use `ngrok http 5000` to tunnel webhooks from Twilio to localhost


Author
------
* Olle Lauri Boström (ollebostr@gmail.com)


License
-------
Licensed under the MIT License.
