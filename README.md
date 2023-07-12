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

git clone for the file 

    cd Desktop/
    git clone https://github.com/wjrichards713/audiostreaming.git
run test.py and check if everything works well

    cd audiostreaming/
    python3 test.py
give access to script
    
    sudo chmod +x script.sh
    cd

run in auto start:

    cd .config/
    
    nano .config/systemd/user/script.service
    systemctl --user daemon-reload
    journalctl --user -u script.service
    cd .config/systemd/user/
    systemctl --user enable script.service
    systemctl --user status script.service

