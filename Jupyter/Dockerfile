# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Jupyter
RUN pip install jupyter

# Expose the port Jupyter runs on
EXPOSE 8888

# Run Jupyter notebook when the container launches
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
