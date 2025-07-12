FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

ENV PROJECT_NAME=autoregressive

COPY environment.yml /app

# Install wget and other necessary system packages
RUN apt-get update && apt-get clean

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-p", "/opt/conda_env", "/bin/bash", "-c"]
SHELL ["/bin/bash", "-c"]
RUN conda env create -f environment.yml
RUN . ~/.bashrc
RUN echo "source activate ${PROJECT_NAME}"