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
    sudo apt-get install lolcat -y 
    sudo apt-get update -y |lolcat
    sudo apt-get dist-upgrade -y |lolcat
    sudo rpi-update -y |lolcat
    sudo apt-get upgrade -y |lolcat
    sudo apt update -y |lolcat
    echo ""



    printf "%b\n" "${BLUE}     *************************************************\n     *   installation des librarys  *\n     *************************************************${NC}\n"
    echo ""
    sudo apt-get install pip libopencv-dev python3-pygame python3-opencv git cmake git libgtk2.0-dev libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 libsdl2-ttf-2.0-0 pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libatlas-base-dev i2c-tools -y |lolcat 
    sudo pip3 install pygame dlib requests cvlib face_recognition smbus2 Flask luma.oled pillow|lolcat
    echo ""

    printf "%b\n" "${BLUE}     *************************************************\n     *   Mise en place de l'interface WEB  *\n     *************************************************${NC}\n"
    
    sudo rm -r /home/pi/BMO 
    sudo rm -r /home/pi/ptut_bmo
    sudo git clone https://github.com/Luzgog/ptut_bmo.git |lolcat
    echo ""
    sudo mkdir /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/WEB/static /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/Programmes/PROGRAMME-BMO.py /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/son/boot.wav /home/pi/BMO



else
    whiptail --title "Mise à Jour" --msgbox "Mise a jour en cours" 10 60

    sudo rm -r /home/pi/BMO 
    sudo rm -r /home/pi/ptut_bmo
    echo ""
    cd
    sudo git clone https://github.com/Luzgog/ptut_bmo.git
    echo ""
    sudo mkdir /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/WEB/static /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/WEB/affichage_oled /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/Programmes/PROGRAMME-BMO.py /home/pi/BMO
    sudo mv /home/pi/ptut_bmo/son/boot.wav /home/pi/BMO

fi

echo ""

if (whiptail --title "Installation" --yesno "voulez vous activer BMO ?" --yes-button "oui" --no-button "non" 20 70) then
    clear
    sudo python3 /home/pi/BMO/PROGRAMME-BMO.py 

else
    whiptail --title "Installation" --msgbox "activation annulée !!!" 20 70
fi

echo "n'oublier pas d'activer la camera et le bus i2c via l'interface raspi-config"
echo "Script par Nino Nicolas avec l'aide de Bastien Tabardel"
exit
