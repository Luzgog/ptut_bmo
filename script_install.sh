#!/bin/bash

CYAN='\033[1;36m'
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m'

if (whiptail --title "Installation" --yesno "voulez vous lancer l'installation ou la mise à jour de BMO ?" --yes-button "Installation" --no-button "Mise à Jour" 10 60) then  
    printf "%b\n" "   ${GREEN}////////////////////////////////////////////////\n   ${YELLOW}//      Début du programme d'installation      //\n   ${RED}////////////////////////////////////////////////${NC}\n"    
    echo ""



    printf "%b\n" "${BLUE}     ********************************\n     *   Mise a jour du raspberry   *\n     ********************************${NC}\n"
    echo ""
    sudo apt-get install -y lolcat

    sudo apt-get update -y | lolcat
    sudo apt-get dist-upgrade -y | lolcat
    sudo rpi-update -y |lolcat 
    sudo apt-get upgrade -y | lolcat
    sudo apt update -y | lolcat
    echo ""



    printf "%b\n" "${BLUE}     *************************************************\n     *   installation des librarys  *\n     *************************************************${NC}\n"
    echo ""
    sudo apt install pip libopencv-dev python3-opencv git -y | lolcat
    sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev -y | lolcat
    sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libatlas-base-dev i2c-tools -y | lolcat
    sudo pip3 install dlib cvlib | lolcat
    sudo pip3 install face_recognition | lolcat
    sudo pip3 install smbus2 | lolcat
    sudo pip3 install Flask | lolcat

    echo ""

    printf "%b\n" "${BLUE}     *************************************************\n     *   Mise en place de l'interface WEB  *\n     *************************************************${NC}\n"
    
    sudo git clone https://github.com/NinoZore/ROV.git
    echo ""
    sudo mv /home/pi/ROV/index.html /var/www/html/



else
    whiptail --title "Mise à Jour" --msgbox "En cours de developement" 10 60
fi

echo ""

if (whiptail --title "Mjpg Streamer" --yesno "voulez vous lancer mjpg streamer ?" --yes-button "oui" --no-button "non" 20 70) then 
    /usr/local/bin/mjpg_streamer -i "input_raspicam.so -x 640 -y 480 -fps 24 -q 80" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"
else
    whiptail --title "Mjpg Streamer" --msgbox "Lancement annulée !!!" 20 70
fi

echo "n'oublier pas d'activer la camera et le bus i2c via l'interface raspi-config"
echo "Script par Nino Nicolas"
exit
