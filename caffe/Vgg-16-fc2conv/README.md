For FC-CONV conversion theory, please refer to this cs231n class page
http://cs231n.github.io/convolutional-networks/#convert


	# wget -c https://raw.githubusercontent.com/davidgengenbach/vgg-caffe/master/model/VGG_ILSVRC_16_layers_deploy.prototxt
	# wget -c http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel
	# cp VGG_ILSVRC_16_layers_deploy.prototxt VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt
	# vim VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt
		Change the fc6 layer defintion From Line 312:
		layer {
		  name: "fc6"
		  type: "Convolution"
		  bottom: "pool5"
		  top: "fc6"
		  convolution_param {
			num_output: 4096
			kernel_size: 7
			stride: 1
			pad: 0
		  }
		}
	# python3 fc2conv.py 
	# mvNCProfile VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt -s 16
	# mvNCCompile -w VGG_ILSVRC_16_layers_fc2conv.caffemodel -o graph -s 16 VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt
	# mvNCCheck -i ../../data/images/nps_electric_guitar.png -metric accuracy_metrics -w VGG_ILSVRC_16_layers_fc2conv.caffemodel VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt -S 255 -M 110 -metric top1 -s 16
	# mvNCCheck -i ../../data/images/nps_electric_guitar.png -metric accuracy_metrics -w VGG_ILSVRC_16_layers_fc2conv.caffemodel VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt -S 255 -M 110 -metric top1 --ma2480
	# python3 run.py
