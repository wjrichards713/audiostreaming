# audiostreaming
Stream Audio From Raspberry Pi 

  Install library 
  
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3 python3-pip
    pip3 install selenium
    sudo apt-get install chromium-chromedriver
    pip3 install pyvirtualdisplay
    sudo apt-get install xvfb
  
run test.py and check if every things works well

    sudo chmod+x test.py
    python3 test.py
Save create shell script file

    Cd Desktop
    nano script.sh
    Inside script.sh python3 /home/pi/Desktop/test.py
    chmod +x /home/pi/Desktop/script.sh

run in auto start:

    nano .config/systemd/user/script.service
    systemctl --user daemon-reload
    journalctl --user -u script.service
    cd .config/systemd/user/
    systemctl --user enable script.service
    systemctl --user status script.service

