<!-- ABOUT THE PROJECT -->
## About The Project

This project is a data science and analysis project to compare Statistical Inference to Machine Learning, in particular Supervised Logic Regression.  The data is in the food and nutrition domain.  More specifically, we will be looking at the Starbucks menu dataset, submited to [Kaggle](https://kaggle.com), a data science learning and competition website.

According to the 2015-2020 Dietary Guidelines for Americans, [women are likely to need between 1,600 and 2,400 calories  a day, and women from 2,000 to 3,000 for men.]([https://health.gov/our-work/nutrition-physical-activity/dietary-guidelines/previous-dietary-guidelines/2015)
<br>
<br>
According to the Mayo Clinic [women should try to eat at least 21 to 25 grams of fiber a day, while men should aim for 30 to 38 grams a day](https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/high-fiber-foods/art-20050948#:~:text=Women%20should%20try%20to%20eat,It%20can%20vary%20among%20brands).
<br>
<br>
According to the National Health System (NHS) men should not eat more than 30g of saturated fat a day and women should not eat more than 20g of saturated fat a day.
<br>
<br>
[Acording to the Week&](https://www.weekand.com/healthy-living/article/recommended-intake-grams-carbohydrates-per-day-women-18021277.php) women consuming 1,600-calorie diets need 180 to 260 grams, women following 2,000-calorie diets need 225 to 325 grams and women consuming 2,400 calories per day require 270 to 390 grams of carbohydrates each day. According to the American Academy of Orthopedic Surgeons, women athletes may require 60 to 70 percent of their calories from carbs, which is equivalent to 360 to 420 grams of carbs for a 2,400-calorie meal plan.
<br>
<br>
[According to Healthline men should eat between 338–488 grams for a diet that consists of 3,000 daily calories](https://www.healthline.com/nutrition/3000-calorie-meal-plan#method).  And lastly, Eating Well recommends [approximately 88 g to 122 g for women, 105 g to 145 g for men.](https://www.eatingwell.com/article/290496/this-is-how-much-protein-you-need-to-eat-every-day).  Remember, this research is a generalization for the worldly population.  Please consult a health professional for your personal food intake.

| Type                  | Sub Type       | Algorithm                  |
|-----------------------|----------------|----------------------------|
| Supervised Learning   | Classification | [Logistric Regression](./) |
| Unsupervised Learning | Classification | [K-Means](./)              |
| Statistics            | Inference | [Inference](./)            |


Inference
### Built With

This section lists all major frameworks/libraries used to bootstrap this project.

* [![Python][Python.org]][Python-url]
* [![Jupyter][Jupyter.org]][Jupyter-url]
* [![Miniconda][Miniconda.com]][Miniconda-url]

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
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```
   
4. miniconda
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
   conda env create -f environment.yml
   conda activate learning_algorithm
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

## Design
Here's a rough breakdown of how these factors might contribute to an unhealthy meal, totaling up to 100%. In other words, the higher the individual nutrient score and composite score the more unhealthy the menu item is.

* High in Calories: 35%
* High in Fat: 30%
* High in Carbohydrates: 20%
* Low in Fiber: 10%
* Low in Protein: 5%

```python
CALORIES * .35 + FAT * .30 + CARBOHYDRATES * .20 + FIBER * .10 + PROTEIN * .05
```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENT -->
## Acknowledgements
[Starbucks Nutrition Facts](https://www.kaggle.com/datasets/utkarshx27/starbucks-nutrition)

<!-- CONTACT -->
## Contact

Your Name - [@realfintorian](https://twitter.com/realfintorian) - johnson.larry.l@fintorian.com

Project Link: [https://github.com/johnsonlarryl/machine_learning_training](https://github.com/your_username/repo_name)
References:

[How many calories should I eat a day?](https://www.medicalnewstoday.com/articles/245588#:~:text=Recommended%20calorie%20intake%20depends%20on,men%20and%202%2C000%20for%20women.)

[2015-2020 Dietary Guidelines](https://health.gov/our-work/nutrition-physical-activity/dietary-guidelines/previous-dietary-guidelines/2015)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Jupyter-url]:https://jupyter.org
[Jupyter.org]:https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white
[Python-url]:https://python.org
[Python.org]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Miniconda-url]:https://docs.conda.io/
[Miniconda.com]:https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white
