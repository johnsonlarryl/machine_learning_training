import numpy as np


class AdaptiveLinearBatchGradientDescent(object):
    def __init__(self, eta: float = 0.01, n_iter: int = 50, random_state: int = 1):
        """
        Adaptive Linear Neuron classifier

        Parameters
        ----------
        :param eta: Learning rate (between 0.0 and 1.0)
        :param n_iter: Passes over the training dataset
        :param random_state: Random number generator seed for random weight initialization

        Returns
        --------
        :returns: None
        """
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, x: np.ndarray, y: np.ndarray):
        """
        Fit training data

        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        :param y: {array-like}, shape = [n_samples] Target values

        Returns
        -------
        :return: self
        """
        rgen = np.random.RandomState(self.random_state)

        # Weights after fitting
        self.w_ = rgen.normal(loc=0.0,
                              scale=0.01,
                              size=1 + x.shape[1])

        # Sum-of-squares cost function value in each epoch
        self.cost_ = []

        for _ in range(self.n_iter):
            net_input = self.net_input(x)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * x.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)

        return self

    def net_input(self, x: np.ndarray):
        """
        Calculate net input

        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features

        Returns
        -------
        :return: The dot product of linear combinations of input vectors and weighted feature vectors
        """
        return np.dot(x, self.w_[1:] + self.w_[0])

    @staticmethod
    def activation(x):
        """
        Computer the linear activation

        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        :return: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        """
        return x

    def predict(self, x) -> np.ndarray:
        """
        Return class label after unit step

        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features

        Returns
        -------

        :return: {array-like}, shape = [n_samples, n_features]
        """
        return np.where(self.activation(self.net_input(x)) >= 0.0, 1, -1)
