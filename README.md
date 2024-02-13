## Template setup to use with Pycharm Debugger

- Run docker-compose build (by default pycharm's debugger runs with sudo so run this with sudo too if nothing was changed)
- Add new interpeter -> On Docker Compose:
  - Service: web 
  - Envs: PYTHONUNBUFFERED=1 
  - Rename interpreter
- Select Edit Debug Configuration
  - Open config/main.py file and choose Current File and run debugger
  - Open Edit Configuration of main.py file
    - set correct interpreter on top
    - set work dir to config
    - set env to PYTHONUNBUFFERED=1

- ATTENCION BLYAT: unix://$XDG_RUNTIME_DIR/docker.sock maps to 'sudo docker' on linux, so it might not be shown in Docker Desktop if you dont run it with sudo. Just a note for diff with Windows...
- Note: by default pycharm runs docker-compose as 'sudo'