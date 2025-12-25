# NETBOX-DOCKER-image

## NETBOX AND DOCKER SETUP

Para realizar esta prueba tecnica he decidido usar  [the official NetBox Docker Image](https://github.com/netbox-community/netbox-docker?tab=readme-ov-file) y el [docker-desktop](https://www.docker.com/products/docker-desktop/) app(Windows) 

### Quickstart
To get NetBox Docker up and running run the following commands.
```
git clone -b release https://github.com/netbox-community/netbox-docker.git
cd netbox-docker
# Copy the example override file
cp docker-compose.override.yml.example docker-compose.override.yml
# Read and edit the file to your liking
docker compose pull
docker compose up
```
The whole application will be available after a few minutes. Open the URL `http://127.0.0.1:8000/`(in my case) or `http://0.0.0.0:8000/` in a web-browser. You should see the NetBox homepage.

To create the first admin user run this command:
```
docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
```

### Project Structure
```
<repository_root>/
├── .github/
├── build-functions/              # Helper scripts for build automation
├── configuration/                # NetBox configuration files
├── docker/                       # Docker-related helper files
├── env/                          # Environment variable templates
├── test-configuration/           # Test and validation configuration
├── .dockerignore
├── .editorconfig
├── .editorconfig-checker.json
├── .flake8
├── .gitignore
├── .hadolint.yaml
├── .markdown-lint.yml
├── .yamllint.yml
├── actionlint.yml
├── build-latest.sh
├── build.sh
├── docker-compose.override.yml   # Local overrides (volumes, custom build)
├── docker-compose.override.yml.example
├── docker-compose.test.override.yml
├── docker-compose.test.yml
├── docker-compose.yml            # 
├── Dockerfile                    # Custom NetBox image extension
├── LICENSE
├── MAINTAINERS.md
├── PRINCIPALS.md
├── pyproject.toml
├── README-SETUP.md               # Setup documentation
├── README.md                     # Project documentation
├── release.sh
├── renovate.json
├── requirements-container.txt
├── test.sh
└── VERSION
```