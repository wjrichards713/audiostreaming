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
    mkdir systemd
    cd systemd
    mkdir user
    cd user
    cp /home/pi/Desktop/audiostreaming/script.service /home/pi/.config/systemd/user/script.service
    cd ..

#reload the auto start demon

    systemctl --user daemon-reload 

#enable the autostart service

    systemctl --user enable script.service 

#start the system

    systemctl --user restart script.service 

#check the status of the system

    systemctl --user status script.service 

