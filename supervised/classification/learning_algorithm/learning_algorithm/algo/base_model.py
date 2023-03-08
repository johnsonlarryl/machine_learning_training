import numpy as np


class BaseModel(object):
    def __init__(self, eta: float = 0.01, epoch: int = 50, random_state: int = 1):
        """
        Adaptive Linear Neuron classifier

        Parameters
        ----------
        :param eta: Learning rate (between 0.0 and 1.0)
        :param epoch: Number of passes over the training dataset
        :param random_state: Random number generator seed for random weight initialization

        Returns
        --------
        :returns: None
        """
        self.eta = eta
        self.epoch = epoch
        self.random_state = random_state

    def fit(self, x: np.ndarray, y: np.ndarray) -> object:
        """
          Fit training data

          Parameters
          ----------
          :param x: {array-like}, shape = [n_samples, n_features]
                    Training vectors , where n_samples is the number of samples and n_features is the number of features
          :param y: {array-like}, shape = [n_samples] Target values

          Returns
          --------
          :return: self
        """
        raise NotImplemented(" Must implement fit method.")

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
        raise NotImplemented(" Must implement predict method.")

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


class AdaptiveLinearNeuron(BaseModel):
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

    def predict(self, x) -> np.ndarray:
        return np.where(self.activation(self.net_input(x)) >= 0.0, 1, -1)



