<!-- ABOUT THE PROJECT -->
## About The Project

This project is a practical training tutorial for learning about the two popular combinatorics mathematical concepts. In particular this project covers Permutations and Combinations.

| Type       | Sub Type       | Algorithm                                     |
|------------|----------------|-----------------------------------------------|
| Combinatorics | Permutations | [Permutations](permutation_and_combinations/) |
| Combinatorics  | Combinations     | [Combinations](permutation_and_combinations/) |

Cheese, what his friends and coaches call him, is a 12U baseball player in the 

### Built With

This section lists all major frameworks/libraries used to bootstrap this project.

* [![Python][Python.org]][Python-url]
* [![Jupyter][Jupyter.org]][Jupyter-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Following the instructions below should get you up and running and quickly as possible without googling around to run the code.
### Prerequisites

Below is the list things you need to use the software and how to install them.  Note, these instructions assume you are using a Mac OS.  If you are using Windows you will need to go through these instructions yourself and update this READ for future users.

1. pyenv
   ```sh
    brew update
    brew install pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```
2. python
   ```sh
    pyenv install 3.9.5   
    pyenv global 3.9.5 
   ```
   
3. poetry
   ```sh
   cd /tmp
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
   bash Mambaforge-$(uname)-$(uname -m).sh
   ```

4. Restart new terminal session in order to initiate mini conda environmental setup


### Installation

Below is the list of steps for installing and setting up the app. These instructions do not rely on any external dependencies or services outside of the prerequisites above.

1. Clone the repo
   ```sh
   git clone git@github.com:johnsonlarryl/machine_learning_training.git
   ```
2. Install project
   ```sh
   poetry install
   conda env create -f environment.yaml
   conda activate permutation_and_combinations
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In order to view or execute the various notebooks run the following command on any of the sub folders in this directory.

Here is an example to launch the Permutations and Combination Notebook.

```sh
jupyter notebook
```

Once inside the notebook [use the following link](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html) on examples of how to use the notebook.


   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DESIGN -->
## Design
* n = Number of elements in collection or list
* r = Number of elements in each tuple
### Permutation

<img src="https://latex.codecogs.com/gif.latex?\frac{n!}{(n-r)!}\quad" /> 

### Combination

<img src="https://latex.codecogs.com/gif.latex?\frac{n!}{(n-r)!r!}\quad" /> 


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@realfintorian](https://twitter.com/realfintorian) - johnson.larry.l@fintorian.com

Project Link: [https://github.com/johnsonlarryl/machine_learning_training](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Jupyter-url]:https://jupyter.org
[Jupyter.org]:https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white
[Python-url]:https://python.org
[Python.org]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white