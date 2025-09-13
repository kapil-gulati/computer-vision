## Steps to get ubuntu ready for Open CV


```

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


```

# don't do this, as it installed older version of numpy, instead use uv or pip to install the latest using venv, and then activate venv and run make
sudo apt-get install -y python3-numpy python3-scipy


## Once all dependecies are installed, then download the Open CV code and run make using following command

## also have to change the include path to include Python headers which are only available in global environment

```

cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_EXAMPLES=ON -D WITH_OPENNI2=ON -D BUILD_opencv_python2=OFF -D BUILD_opencv_python3=ON -D PYTHON3_EXECUTABLE=/usr/bin/python3.12 -D PYTHON3_INCLUDE_DIR=/usr/include/python3.12 -D PYTHON3_LIBRARY=/usr/lib/python3.12/config-3.12-x86_64-linux-gnu/libpython3.12.so -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -D OPENCV_ENABLE_NONFREE=ON ../opencv

cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_EXAMPLES=ON -D WITH_OPENNI2=ON -D BUILD_opencv_python2=OFF -D BUILD_opencv_python3=ON -D PYTHON3_EXECUTABLE=../computer-vision/.venv/bin/python3.12 -D PYTHON3_INCLUDE_DIR=/usr/include/python3.12 -D PYTHON3_LIBRARY=../computer-vision/.venv/lib/python3.12/config-3.12-x86_64-linux-gnu/libpython3.12.so -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -D OPENCV_ENABLE_NONFREE=ON ../opencv

make -j8

sudo make install

```
__* Note that it will create open cv package. In order to use it into virtual env, I had to copy the module into the site-packages are below:
cp ../build/lib/python3/cv2.cpython-312-x86_64-linux-gnu.so .venv/lib/python3.12/site-packages/


## Autoremove removed filliwubf libs
```
Removing libgl1-amber-dri:amd64 (21.3.9-0ubuntu2) ...
Removing libdrm-nouveau2:amd64 (2.4.122-1~ubuntu0.24.04.1) ...
Removing libdrm-radeon1:amd64 (2.4.122-1~ubuntu0.24.04.1) ...
Removing libglapi-mesa:amd64 (24.2.8-1ubuntu1~24.04.1) ...
Removing python3-pil:amd64 (10.2.0-1ubuntu1) ...
Removing libimagequant0:amd64 (2.18.0-1build1) ...
Removing liblbfgsb0:amd64 (3.0+dfsg.4-1build1) ...
Removing libllvm19:amd64 (1:19.1.1-1ubuntu1~24.04.2) ...
Removing libraqm0:amd64 (0.10.1-1build1) ...
Removing libxcb-dri2-0:amd64 (1.15-1ubuntu2) ...
Removing python3-decorator (5.1.1-5) ...
Removing python3-olefile (0.46-3) ...
Processing triggers for libc-bin (2.39-0ubuntu8.5) ...
```