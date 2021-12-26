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
    Scalar color = Scalar(255,0,0);
    cap.open(0);
    Mat img, grey;
    cascade.load("haarcascade_frontalface_default.xml");
    while (true){
        cap.read(img);
        cvtColor(img, grey,COLOR_BGR2GRAY);
        cascade.detectMultiScale(grey, faces, 1.1, 4);
        for(int i =0; i< faces.size(); i++){
            Rect r = faces[i];
            rectangle(img, r,color );
        }
        imshow("result", img);

    }
    cap.release();

}