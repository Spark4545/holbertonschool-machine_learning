#!/usr/bin/env python3
"""Neural Network
"""
import numpy as np


class NeuralNetwork:
    """Class that define a neural network with one hidden layer
       performing binary classification"""

    def __init__(self, nx, nodes):
        """Class contructor

        Args:
            nx (integer): number of input features
            nodes (integer): number of nodes in the hidden layer
        """

        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.nx = nx
        if type(nodes) is not int:
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    def evaluate(self, X, Y):
        """Evaluates neural network's predictions

        Args:
            X (numpy.ndarray): shape(nx, m), contains the input data
            Y (numpy.ndarray): shape(1, m), contains the correct
                              label for the input data

        Returns:
            pred (numpy.ndarray): shape(1, m) contains the
                                 prediction label for each examples
            cost (integer): cost
        """

        self.forward_prop(X)
        prediction = np.where(self.__A2 >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A2)
        return prediction, cost

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression

        Args:
            Y (numpy.ndarray): shape(1, m), contains the correct
                              labels for the input data
            A (numpy.ndarray): shape(1, m), contains the activated
                              output of the neuron for each exmaples

        Returns:
            integer: cost
        """

        cost = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        cost = np.sum(cost)
        cost = - cost / A.shape[1]
        return cost

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network

        Args:
            X (numpy.ndarray): shape(nx, m), contains the input data

        Returns:
            integer: private attributes A1 and A2
        """

        preactivation1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-preactivation1))
        preactivation2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-preactivation2))
        return self.__A1, self.__A2

    @property
    def W1(self):
        """Getter function for private attribute W1

        Returns:
            integer: weights vector for the hidden layer
        """

        return self.__W1

    @property
    def b1(self):
        """Getter function for private attribute b1

        Returns:
            integer: bias for the hidden layer
        """

        return self.__b1

    @property
    def A1(self):
        """Getter function for private attribute A1

        Returns:
            integer: activated output for the hidden layer
        """

        return self.__A1

    @property
    def W2(self):
        """Getter function for private attribute W2

        Returns:
            integer: weights vector for the ouput neuron
        """

        return self.__W2

    @property
    def b2(self):
        """Getter function for private attribute b2

        Returns:
            integer: bias for the output neuron
        """

        return self.__b2

    @property
    def A2(self):
        """Getter function for private attribute A2

        Returns:
            integer: activated output for the output neuron
        """

        return self.__A2
