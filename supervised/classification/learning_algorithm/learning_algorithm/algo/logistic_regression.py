import numpy as np


class LogisticRegressionGradientDescent(object):
    def __init__(self, eta: float = 0.01, n_iter: int = 50, random_state: int = 1):
        """
        Logistic Regression classifier

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
        regen = np.random.RandomState(self.random_state)

        # Weights after fitting
        self.w_ = regen.normal(loc=0.0,
                               scale=0.01,
                               size=1 + x.shape[1])
        # Logarithmic cost function value in each epoch
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(x)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * x.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()

            # Note that we compute the logistic `cost` now
            # instead of the sum of squared errors cost
            cost = (-y.dot(np.log(output)) - ((1 - y).dot(np.log(1 - output))))
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
        return np.dot(x, self.w_[1:]) + self.w_[0]

    def activation(self, x: np.ndarray) -> np.ndarray:
        """
        Computer the linear activation

        Parameters
        ----------
        :param x: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        :return: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features
        """
        return self.sigmoid(-np.clip(x, -250, 250))

    def predict(self, x):
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
        return np.where(self.net_input(x) >= 0.0, 1, 0)

    @staticmethod
    def sigmoid(z: np.ndarray) -> np.ndarray:
        """
        Inverse of logit function helps predicts classes

        Parameters
        ----------
        :param z: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features

        Returns
        -------
        :return: {array-like}, shape = [n_samples, n_features]
        """
        return 1.0 / (1.0 + np.exp(-z))

    @staticmethod
    def cost_1(z: np.ndarray) -> np.ndarray:
        """
        Cost of predicting first class

        Parameters
        ----------
        :param z: {array-like}, shape = [n_samples, n_features]
                  Training vectors, where n_samples is the number of samples and n_features is the number of features

        Returns
        -------
        :return: {array-like}, shape = [n_samples, n_features]
        """
        return -np.log(LogisticRegressionGradientDescent.sigmoid(z))

    @staticmethod
    def cost_0(z: np.ndarray) -> np.ndarray:
        """
        Cost of predicting second class
        :param z:
        :return: {array-like}, shape = [n_samples, n_features]
        """
        return -np.log(1 - LogisticRegressionGradientDescent.sigmoid(z))


