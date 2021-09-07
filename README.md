# edice Repository

This is a simple demo for using Docker to containerize a normal console Python app.  The Docker image
is [here on Docker Hub](https://hub.docker.com/repository/docker/gchadder3/edice).  To use this (assuming 
you have a working Docker installation on your machine) do the following:
* `docker pull gchadder3/edice` to pull the image from Docker Hub.
* `docker run -i -t gchadder3/edice` to run the application.  (-i = interactive mode, -t = terminal mode)

To install from this repo
* `git clone https://github.com/gchadder3/edice.git` 
* `cd edice`
* `docker build -t edice .` to build the Docker image (`edice`).
* `docker run -i -t edice` to run it.  The beauty is that you don't have to have Python installed on your 
machine to run this Python code.  Of course, if you do have Python installed, you could also do `python edice.py` 
to run it.

The application itself is a simple text console application that may be used for games that require dice, 
including, for example, polyhedral dice such as are used in paper-based role-playing games such as 
Dungeons & Dragons.  It starts the user off with a regular die (1d6) and the user can keep rolling the 
dice or switch to other dice settings (e.g. 3d8: 3 dice of 8 sides each).