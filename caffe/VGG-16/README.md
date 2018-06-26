	# wget -c https://raw.githubusercontent.com/davidgengenbach/vgg-caffe/master/model/VGG_ILSVRC_16_layers_deploy.prototxt
	# wget -c http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel

	# mvNCProfile VGG_ILSVRC_16_layers_deploy.prototxt -s 16
	# mvNCCompile -w VGG_ILSVRC_16_layers.caffemodel -o graph -s 16 VGG_ILSVRC_16_layers_deploy.prototxt
	# mvNCCheck -i ../../data/images/nps_electric_guitar.png -metric accuracy_metrics -w VGG_ILSVRC_16_layers.caffemodel VGG_ILSVRC_16_layers_deploy.prototxt -S 255 -M 110 -metric top1 -s 16
	# python3 run.py
