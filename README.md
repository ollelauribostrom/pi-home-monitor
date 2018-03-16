# Raspberry PI Home Monitor
- Monitor movements with Python, Flask & OpenCV
- Chat based UI (Talk to the monitor through SMS using Twilio)
- Subscribe to notifications when the monitor picks up movements

> Also, scare off intruders by turning on some swedish radio!


Installation
------------
##### Dependencies
- Python 3
- Twilio phone number
- A web camera
- _optional_ nodejs & npm package [sverigesradio](https://www.npmjs.com/package/sverigesradio) (To play radio)
- _optional_ ngrok (To tunnel webhooks from Twilio to localhost)

#### Local dev installation
```bash
  # Clone repo
  git clone https://github.com/ollelauribostrom/pi-home-monitor.git
  cd pi-home-monitor

  # Install dependencies
  make install

  # Set up env
  touch .env
  echo "TWILIO_ACCOUNT_SID=<YOUR_TWILIO_SID>" >> .env
  echo "TWILIO_AUTH_TOKEN=<YOUR_TWILIO_TOKEN>" >> .env
  echo "TWILIO_FROM_NUMBER=<YOUR_TWILIO_NUMER>" >> .env
  echo "SHARED_SECRET=<A_STRING_USED_AS_PASSWORD>" >> .env
  echo "BASE_URL=<NGROK_TUNNEL_OR_PUBLIC_ADRESS>" >> .env

  # If using ngrok
  ngrok http 5000
  # Configure Twilio webhook
  # Add ngrok tunnel adress to .env as BASE_URL

  # Run
  make dev
```

#### Production on Raspberry PI 3 (Raspbian Jessie)
- Make sure you have Git installed
- Make sure you have Python 3 & pip installed
- Make sure you have nodejs installed

```bash
  # Clone repo
  git clone https://github.com/ollelauribostrom/pi-home-monitor.git
  cd pi-home-monitor

  # Install dependencies
  make install

  # Set up env
  touch .env
  echo "TWILIO_ACCOUNT_SID=<YOUR_TWILIO_SID>" >> .env
  echo "TWILIO_AUTH_TOKEN=<YOUR_TWILIO_TOKEN>" >> .env
  echo "TWILIO_FROM_NUMBER=<YOUR_TWILIO_NUMER>" >> .env
  echo "SHARED_SECRET=<A_STRING_USED_AS_PASSWORD>" >> .env
  echo "BASE_URL=<NGROK_TUNNEL_OR_PUBLIC_ADRESS>" >> .env

  # Run
  make production
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
