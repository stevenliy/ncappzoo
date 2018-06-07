# This is the NCSDK2 branch
    Added caffe/GoogLeNet_BN project. 
    The GoogleNet_BN model file is from https://github.com/lim0606/caffe-googlenet-bn
    
    Test steps:
        # wget -c http://image-net.org/image/ILSVRC2015/ILSVRC2015_devkit.tar.gz
        # tar zxvf ILSVRC2015_devkit.tar.gz
        # wget -P . https://raw.githubusercontent.com/lim0606/caffe-googlenet-bn/master/deploy.prototxt
        # vim deploy.prototxt
           Go to line 5, change "dim: 10" => "dim: 1"
           Go to line 3102, change "layers" => "layer"
        # make
        # python3 run.py


