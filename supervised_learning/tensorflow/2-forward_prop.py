#!/usr/bin/env python3
"""summary
"""
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """Function that creates the forward propagation graph for the input layer

    Args:
        x (tf.placeholder): placeholder for the input data
        layer_sizes (list, optional): contains the nulmber of nodes in
            each layer of the network. Defaults to [].
        activations (list, optional): contains the activation functions
            for each layer of the network. Defaults to [].
    """
    for i in range(len(layer_sizes)):
        if i == 0:
            prediction = create_layer(x, layer_sizes[0], activations[0])
        else:
            prediction = create_layer(prediction, layer_sizes[i],
                                      activations[i])
    return prediction
