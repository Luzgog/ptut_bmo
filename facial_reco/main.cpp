#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main(){
    VideoCapture cap;
    CascadeClassifier cascade;
    vector<Rect> faces;

    int i=0;

    Scalar color = Scalar(255,0,0);
    bool test = cap.open(0);
    Mat img, grey;
    cascade.load("haarcascade_frontalface_default.xml");
    while (true){
        cap.read(img);
        if (!img.empty()){
            cvtColor(img, grey,COLOR_BGR2GRAY);
            cascade.detectMultiScale(grey, faces);
            for(int i =0; i< faces.size(); i++){
                Point center(faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2);
                ellipse(img, center, Size(faces[i].width/2, faces[i].height/2), 0, 0, 360, Scalar(255, 0, 255), 4);
            }
            imshow("test", img);

        }else{
            break;
        }
        

    }
    cap.release();

}