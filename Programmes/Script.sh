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
    sudo apt-get install -y 

    sudo apt-get update -y 
    sudo apt-get dist-upgrade -y 
    sudo rpi-update -y 
    sudo apt-get upgrade -y 
    sudo apt update -y 
    echo ""



    printf "%b\n" "${BLUE}     *************************************************\n     *   installation des librarys  *\n     *************************************************${NC}\n"
    echo ""
    sudo apt install pip libopencv-dev python3-opencv git -y 
    sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev -y 
    sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libatlas-base-dev i2c-tools -y 
    sudo pip3 install dlib cvlib 
    sudo pip3 install face_recognition 
    sudo pip3 install smbus2 
    sudo pip3 install Flask 

    echo ""

    printf "%b\n" "${BLUE}     *************************************************\n     *   Mise en place de l'interface WEB  *\n     *************************************************${NC}\n"
    
    sudo git clone https://github.com/Luzgog/ptut_bmo/blob/main/scrip_install.sh
    echo ""
    sudo mv /home/pi/ROV/index.html /var/www/html/
