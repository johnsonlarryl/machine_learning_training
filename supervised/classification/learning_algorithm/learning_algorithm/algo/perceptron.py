import numpy as np

from base_model import BaseModel


class Perceptron(BaseModel):
    def __init__(self, eta: float = 0.01, epoch: int = 50, random_state: int = 1):
        """ Perceptron classifier """
        super.__init__(eta, epoch, random_state)

    def fit(self, x: np.ndarray, y: np.ndarray) -> object:
        regen = np.random.RandomState(self.random_state)

        # 1d-array weights after fitting
        self.w_ = regen.normal(loc=0.0,
                               scale=0.01,
                               size=1 + x.shape[1])

        # Number of misclassifications (updates) in each epoch.
        self.errors_ = []

        for _ in range(self.epoch):
            errors = 0

            for xi, target in zip(x, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)

            self.errors_.append(errors)

        return self

    def predict(self, x) -> np.ndarray:
        """
        Return class label after unit step function5

        Parameters
        ----------
        :param x: Training vectors , where n_samples is the number of samples and n_features is the number of features

        Returns
        -------
        :return: {array-like}, shape = [n_samples, n_features]
        """
        return np.where(self.net_input(x) >= 0.0, 1, -1)


