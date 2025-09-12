sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y build-essential cmake git pkg-config

sudo apt-get install -y libjpeg-dev libtiff-dev libpng-dev

sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev

sudo apt-get install -y libv4l-dev v4l-utils

sudo apt-get install -y libxvidcore-dev libx264-dev

sudo apt install -y libgtk2.0-dev libgtk-3-dev libcanberra-gtk-module libcanberra-gtk3-module

sudo apt install -y libopenblas-dev libatlas-base-dev liblapack-dev gfortran

sudo apt install -y libhdf5-dev libprotobuf-dev protobuf-compiler

sudo apt-get install python3-dev

sudo apt-get install -y python3-numpy python3-scipy

cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_EXAMPLES=ON -D WITH_OPENNI2=ON -D BUILD_opencv_python2=OFF -D BUILD_opencv_python3=ON -D PYTHON3_EXECUTABLE=/usr/bin/python3.12 -D PYTHON3_INCLUDE_DIR=/usr/include/python3.12 -D PYTHON3_LIBRARY=/usr/lib/python3.12/config-3.12-x86_64-linux-gnu/libpython3.12.so -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -D OPENCV_ENABLE_NONFREE=ON ../opencv

make -j8

sudo make install