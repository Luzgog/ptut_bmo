#!/bin/bash

CYAN='\033[1;36m'
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m'

if [[ "$EUID" = 0 ]]; then
    echo "Vous etes root"
else
    sudo -k # make sure to ask for password on next sudo
    if sudo true; then
        echo "Mot de passe correct"
    else
        echo "Mot de passe incorrect"
        exit 1
    fi
fi

if (whiptail --title "Installation" --yesno "voulez vous lancer l'installation ou la mise à jour de BMO ?" --yes-button "Installation" --no-button "Mise à Jour" 10 60) then  
    printf "%b\n" "   ${GREEN}////////////////////////////////////////////////\n   ${YELLOW}//      Début du programme d'installation      //\n   ${RED}////////////////////////////////////////////////${NC}\n"    
    echo ""



    printf "%b\n" "${BLUE}     ********************************\n     *   Mise a jour du raspberry   *\n     ********************************${NC}\n"
    echo ""
    apt-get install lolcat -y 
    apt-get update -y |/usr/games/lolcat
    apt-get dist-upgrade -y |/usr/games/lolcat
    rpi-update -y |/usr/games/lolcat
    apt-get upgrade -y |/usr/games/lolcat
    apt-get full-upgrade -y |/usr/games/lolcat
    apt update -y |/usr/games/lolcat
    echo ""



    printf "%b\n" "${BLUE}     *************************************************\n     *   installation des librarys  *\n     *************************************************${NC}\n"
    echo ""
    apt-get install pip libopencv-dev python3-pygame python3-opencv git cmake git libgtk2.0-dev libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 libsdl2-ttf-2.0-0 pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libatlas-base-dev i2c-tools python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy -y |/usr/games/lolcat 
    pip3 install pygame st7789 dlib requests cvlib face_recognition smbus2 Flask pillow|/usr/games/lolcat
    curl -sL https://install.raspap.com | bash -s -- --yes | /usr/games/lolcat
    echo ""

    printf "%b\n" "${BLUE}     *************************************************\n     *   Mise en place de l'interface WEB  *\n     *************************************************${NC}\n"
    
    rm -r /home/pi/BMO 
    rm -r /home/pi/ptut_bmo
    git clone https://github.com/Luzgog/ptut_bmo.git |/usr/games/lolcat
    echo ""
else
    whiptail --title "Mise à Jour" --msgbox "Mise a jour en cours" 10 60
    rm -r /home/pi/ptut_bmo
    git clone https://github.com/Luzgog/ptut_bmo.git |/usr/games/lolcat
    echo ""
fi

echo ""

if (whiptail --title "Installation" --yesno "voulez vous activer BMO ?" --yes-button "oui" --no-button "non" 20 70) then
    clear
    python3 /home/pi/ptut_bmo/Programmes/PROGRAMME-BMO.py 

else
    whiptail --title "Installation" --msgbox "activation annulée !!!" 20 70
fi

echo "n'oublier pas d'activer la camera ,le bus spi et la location wifi via l'interface raspi-config"
echo "Script par Nino Nicolas avec l'aide de Bastien Tabardel"
exit
