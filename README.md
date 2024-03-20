# urlscrapper

Clone the repository and go to the root path of the project:
```
git clone https://github.com/gabrielbevilaqua/urlscrapper.git
cd urlscrapper
```
You can choose running it with Docker or from a virtual environment. See following sections below ``Running with docker`` and ``Running from virtual environment``.

## Running with docker
Build the contianer:
```
docker-compose build
```
Run the container, it will start running the crawler:
```
docker-compose up
```

Database will automatically be outputed to the ``output`` folder in the root after container finishes running.

## Running from virtual environment
Create a python virtual environment:
```
python3 -m venv <environment_name>
```
Activate environment:

For Linux Based OS Or Mac-OS.
```
source <environment_name>/bin/activate
```
For Windows With CMD.
```
.\<environment_name>\Scripts\activate.bat
```
For Windows With Power shell.
```
.\<environment_name>\Scripts\activate.ps1
```
For Windows With Unix Like Shells For Example Git Bash CLI.
```
source <environment_name>/Scripts/activate
```
Install project dependencies:
```
pip install -r urlscrapper/requirements.txt 
```
Move inside crawler folder and start crawller with:
```
cd urlscrapper
scrapy crawl dogimages
```
The dogimages.db file will be created in this same directory.
