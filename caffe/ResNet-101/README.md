# wget -c https://deepdetect.com/models/resnet/ResNet-101-deploy.prototxt
# wget -c https://deepdetect.com/models/resnet/ResNet-101-model.caffemodel
# wget -c https://deepdetect.com/models/resnet/ResNet_mean.binaryproto

# vim ResNet-101-deploy.prototxt
Modify from Line 3:
	input: "data"
	input_shape {
	  dim: 1
	  dim: 3
	  dim: 224
	  dim: 224
	}

Modify from Line 4544:
        name:"prob"
        type:"Softmax"
        bottom:"fc1000"
        top:"prob"

# mvNCProfile ResNet-101-deploy.prototxt -s 12
# mvNCCompile -w ResNet-101-model.caffemodel -o graph -s 12 ResNet-101-deploy.prototxt
# mvNCCheck -w ResNet-101-model.caffemodel -i ../../data/images/nps_electric_guitar.png -s 12 -id 546 -S 255 -M ../../data/ilsvrc12/ilsvrc_2012_mean.npy ResNet-101-deploy.prototxt
# python3 run.py
