import caffe
import numpy as np

net1 = caffe.Net('VGG_ILSVRC_16_layers_deploy.prototxt', 'VGG_ILSVRC_16_layers.caffemodel', caffe.TEST)
net2 = caffe.Net('VGG_ILSVRC_16_layers_deploy_fc2conv.prototxt', caffe.TEST)

for key, val in net1.params.items():
    if key == "fc6": 
        continue
    
    print(key)

    for idx, v in enumerate(val):
        net2.params[key][idx].data[...] = v.data

net2.params["fc6"][0].data[...] = np.reshape(net1.params["fc6"][0].data, (4096, 512, 7, 7))
net2.params["fc6"][1].data[...] = net1.params["fc6"][1].data

net2.save("VGG_ILSVRC_16_layers_fc2conv.caffemodel")
