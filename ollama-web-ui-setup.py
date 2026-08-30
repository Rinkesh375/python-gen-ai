"""
===========================================================
        OLLAMA + OPEN WEBUI LOCAL DOCKER SETUP
===========================================================

Purpose
-------
This document explains how to install and run:

1. Ollama
2. Open WebUI
3. Local LLM models

using Docker.

Prerequisites
-------------
- Docker Desktop installed
- Docker Desktop running
- Internet connection for downloading Docker images/models

Architecture
------------

Browser
   |
   | http://localhost:3000
   v
Open WebUI
   |
   | Ollama API
   v
Ollama
   |
   v
Local LLM Model


===========================================================
1. START OLLAMA
===========================================================

Run:

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama


Explanation:

-d
    Runs the container in detached/background mode.

-v ollama:/root/.ollama
    Creates a Docker volume named "ollama".
    Downloaded models are stored here.

-p 11434:11434
    Exposes Ollama API on port 11434.

--name ollama
    Names the container "ollama".

ollama/ollama
    Official Ollama Docker image.


Check if Ollama is running:

docker ps


Check Ollama logs:

docker logs ollama


Ollama API:

http://localhost:11434


===========================================================
2. DOWNLOAD OPEN WEBUI IMAGE
===========================================================

Run:

docker pull ghcr.io/open-webui/open-webui:main


This downloads the Open WebUI Docker image.


===========================================================
3. START OPEN WEBUI
===========================================================

Run:

docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main


Explanation:

-d
    Runs the container in background mode.

-p 3000:8080
    Maps host port 3000 to Open WebUI port 8080.

-v open-webui:/app/backend/data
    Stores Open WebUI data in a persistent Docker volume.

--name open-webui
    Names the container "open-webui".

ghcr.io/open-webui/open-webui:main
    Open WebUI Docker image.


===========================================================
4. OPEN WEBUI
===========================================================

Open your browser:

http://localhost:3000


Create your Open WebUI account.

After login, Open WebUI can be used as the local UI
for interacting with Ollama models.


===========================================================
5. DOWNLOAD AN OLLAMA MODEL
===========================================================

Ollama does not automatically download a model.

Example:

docker exec -it ollama ollama pull llama3.2


Check installed models:

docker exec -it ollama ollama list


Run a model directly:

docker exec -it ollama ollama run llama3.2


You can replace "llama3.2" with another model supported
by Ollama.


===========================================================
6. RECOMMENDED DOCKER NETWORK SETUP
===========================================================

For reliable communication between Open WebUI and Ollama,
it is recommended to put both containers on the same
Docker network.


Create network:

docker network create ollama-network


Remove the old Ollama container if it already exists:

docker rm -f ollama


Start Ollama on the network:

docker run -d --name ollama --network ollama-network -v ollama:/root/.ollama -p 11434:11434 ollama/ollama


Start Open WebUI on the same network:

docker run -d --name open-webui --network ollama-network -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main


Now both containers can communicate using:

http://ollama:11434


IMPORTANT:

Inside Docker, do NOT use:

http://localhost:11434

because localhost inside the Open WebUI container refers
to the Open WebUI container itself.

Use:

http://ollama:11434


===========================================================
7. CHECK RUNNING CONTAINERS
===========================================================

Show running containers:

docker ps


Show all containers:

docker ps -a


Expected containers:

ollama
open-webui


===========================================================
8. VIEW LOGS
===========================================================

Ollama logs:

docker logs ollama


Follow Ollama logs:

docker logs -f ollama


Open WebUI logs:

docker logs open-webui


Follow Open WebUI logs:

docker logs -f open-webui


===========================================================
9. STOP CONTAINERS
===========================================================

Stop Ollama:

docker stop ollama


Stop Open WebUI:

docker stop open-webui


Stop both:

docker stop ollama open-webui


===========================================================
10. START CONTAINERS AGAIN
===========================================================

Start Ollama:

docker start ollama


Start Open WebUI:

docker start open-webui


Start both:

docker start ollama open-webui


===========================================================
11. RESTART CONTAINERS
===========================================================

Restart Ollama:

docker restart ollama


Restart Open WebUI:

docker restart open-webui


Restart both:

docker restart ollama open-webui


===========================================================
12. CHECK DOCKER VOLUMES
===========================================================

List volumes:

docker volume ls


Expected volumes:

ollama
open-webui


Inspect Ollama volume:

docker volume inspect ollama


Inspect Open WebUI volume:

docker volume inspect open-webui


IMPORTANT:

The "ollama" volume contains downloaded Ollama models.

The "open-webui" volume contains Open WebUI data.

Do NOT delete these volumes unless you want to reset
your data.


===========================================================
13. REMOVE ONLY CONTAINERS
===========================================================

If you want to remove the containers but KEEP your
models and Open WebUI data:

docker rm -f ollama open-webui


The Docker volumes will remain.

You can recreate the containers later using the commands
above.


===========================================================
14. COMPLETE RESET
===========================================================

WARNING:

This will remove:

- Ollama container
- Open WebUI container
- Downloaded Ollama models
- Open WebUI data


Run:

docker rm -f ollama open-webui


Remove volumes:

docker volume rm ollama open-webui


Remove network:

docker network rm ollama-network


After this, the complete setup is reset.


===========================================================
15. DOCKER CLEANUP
===========================================================

To remove unused Docker containers, images, networks,
and volumes:

docker system prune -a --volumes


Without confirmation:

docker system prune -a --volumes -f


WARNING:

This can permanently delete unused Docker volumes.

If you have databases or other important Docker data,
check your volumes before running this command.


===========================================================
16. PORT INFORMATION
===========================================================

Ollama:

Host:
    11434

Container:
    11434

URL:

http://localhost:11434


Open WebUI:

Host:
    3000

Container:
    8080

URL:

http://localhost:3000


===========================================================
17. IF PORT 11434 IS ALREADY IN USE
===========================================================

Check:

docker ps


On Windows:

netstat -ano | findstr :11434


You can use another host port.

Example:

docker run -d -v ollama:/root/.ollama -p 11435:11434 --name ollama ollama/ollama


Then Ollama will be available from the host at:

http://localhost:11435


NOTE:

Inside the Docker network, Open WebUI should still use:

http://ollama:11434


===========================================================
18. IF PORT 3000 IS ALREADY IN USE
===========================================================

Use another host port:

docker run -d -p 3001:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main


Then open:

http://localhost:3001


===========================================================
19. IF CONTAINER NAME ALREADY EXISTS
===========================================================

Example error:

Conflict. The container name "/ollama" is already in use.


Remove the existing container:

docker rm -f ollama


Then create it again.


For Open WebUI:

docker rm -f open-webui


Then recreate the container.


===========================================================
20. CHECK OLLAMA MODELS
===========================================================

List models:

docker exec -it ollama ollama list


Example output:

NAME
llama3.2
mistral
...


Pull another model:

docker exec -it ollama ollama pull mistral


Run model:

docker exec -it ollama ollama run mistral


===========================================================
21. RECOMMENDED FINAL SETUP
===========================================================

Create Docker network:

docker network create ollama-network


Start Ollama:

docker run -d --name ollama --network ollama-network -v ollama:/root/.ollama -p 11434:11434 ollama/ollama


Start Open WebUI:

docker run -d --name open-webui --network ollama-network -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main


Download model:

docker exec -it ollama ollama pull llama3.2


Open WebUI:

http://localhost:3000


Ollama URL for Open WebUI:

http://ollama:11434


===========================================================
22. QUICK START - COPY AND PASTE
===========================================================

docker network create ollama-network

docker run -d --name ollama --network ollama-network -v ollama:/root/.ollama -p 11434:11434 ollama/ollama

docker pull ghcr.io/open-webui/open-webui:main

docker run -d --name open-webui --network ollama-network -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main

docker exec -it ollama ollama pull llama3.2


Then open:

http://localhost:3000


===========================================================
23. FINAL CHECKLIST
===========================================================

[ ] Docker Desktop is running

[ ] Ollama container is running

[ ] Open WebUI container is running

[ ] ollama Docker volume exists

[ ] open-webui Docker volume exists

[ ] ollama-network exists

[ ] Ollama model is downloaded

[ ] Open WebUI is accessible

[ ] Ollama connection is configured

[ ] http://localhost:3000 opens successfully


===========================================================
END OF DOCUMENT
===========================================================
"""