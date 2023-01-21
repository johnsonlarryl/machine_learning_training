import numpy as np
from typing import Tuple


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

    def fit(self, x: np.ndarray, y: np.ndarray) -> object:
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

    def net_input(self, x: np.ndarray) -> np.ndarray:
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
    def activation(x: np.ndarray) -> np.ndarray:
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


class AdaptiveLinearStochasticGradientDescent(object):
    """
     Adaptive Linear Neuron classifier

     Parameters
     ----------
     :param eta: Learning rate (between 0.0 and 1.0)
     :param n_iter: Passes over the training dataset
     :param random_state: Random number generator seed for random weight initialization
     :param shuffle: Modify a sequence in-place by shuffling its contents.

     Returns
     --------
     :returns: None
     """
    def __init__(self, eta: float = 0.01, n_iter: int = 10, random_state: int = 1, shuffle=True):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        self.shuffle = shuffle
        self.w_initialized = False

    def fit(self, x: np.ndarray, y: np.ndarray) -> object:
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
        self._initialize_weights(x.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            if self.shuffle:
                x, y = self._shuffle(x, y)

            cost = []

            for xi, target in zip(x, y):
                cost.append(self._update_weights(xi, target))

            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)

        return self

    def partial_fit(self, x: np.ndarray, y: np.ndarray) -> object:
        """
        Fit training data without reinitializing the weights


        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        :param y: {array-like}, shape = [n_samples] Target values

        Returns
        -------
        :return: self
        """
        if not self.w_initialized:
            self._initialize_weights(x.shape[1])

        if y.ravel().shape[0] > 1:
            for xi, target in zip(x, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(x, y)

        return self

    def _shuffle(self, x: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """

        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        :param y: {array-like}, shape = [n_samples] Target values

        Returns
        -------
        :return: :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
                 y: {array-like}, shape = [n_samples] Target values
        """
        r = self.rgen.permutation(len(y))
        return x[r], y[r]

    def _initialize_weights(self, m: int) -> None:
        """
        Initialize weights to small random numbers

        Parameters
        ----------
        :param m: Output shape

        Returns
        -------
        :return: None
        """
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01, size=1 + m)
        self.w_initialized = True

    def _update_weights(self, xi: np.ndarray, target: np.ndarray) -> float:
        """
        Apply Adaline learning rule to update the weights

        Parameters
        ----------
        :param xi:  {array-like}, shape = [n_samples, n_features]
                    Training vectors, where n_samples is the number of samples and n_features is the number of features
        :param target: {array-like}, shape = [n_samples] Target values

        Returns
        -------
        :return: Cost from the learned weights between the calculated outcome and true class label
        """
        output = self.activation(self.net_input(xi))
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error**2

        return cost

    def net_input(self, x: np.ndarray) -> np.ndarray:
        """
        Calculate the net input

        Parameters
        ----------
        :param x: array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features

        Returns
        -------
        :return: The dot product of linear combinations of input vectors and weighted feature vectors
        """
        return np.dot(x, self.w_[1:]) + self.w_[0]

    @staticmethod
    def activation(x: np.ndarray) -> np.ndarray:
        """
        Compute linear activation

        :param x: array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features

        :return: {array-like}, shape = [n_samples, n_features]
                 Training vectors, where n_samples is the number of samples and n_features is the number of features
        """
        return x

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Return class label after unit step

        Parameters
        ----------
        :param x:

        Returns
        -------
        :return: {array-like}, shape = [n_samples, n_features]
        """
        return np.where(self.activation(self.net_input(x)) >= 0.0, 1, -1)
