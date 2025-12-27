FROM netboxcommunity/netbox:latest

USER root

# Descarga instalador oficial de pip y lo instala en el venv de NetBox
ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py

RUN /opt/netbox/venv/bin/python /tmp/get-pip.py \
 && /opt/netbox/venv/bin/pip --version

COPY requirements.txt /tmp/requirements.txt

RUN /opt/netbox/venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt

USER unit
