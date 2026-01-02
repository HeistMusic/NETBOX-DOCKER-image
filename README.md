# NetBox Custom Script – Technical Exercise

## Setup

### Environment

This project uses the official NetBox Docker image and is intended to be run using Docker Desktop.
No system-wide installation of Docker Engine or Docker Compose is required, as Docker Desktop already includes both.

### Prerequisites

- Python 3.12
- Docker-desktop [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) (Windows / macOS / Linux)
- Git

### Clone the Repository

```
git clone https://github.com/HeistMusic/NETBOX-DOCKER-image.git NETBOX-DOCKER-image 
cd NETBOX-DOCKER-image
```

### Start NetBox

From the repository root, run:
```
docker compose pull
docker compose up
docker compose down
docker compose build --no-cache
docker compose up -d
```

This will:

- Pull the required NetBox images
- Start NetBox and its dependencies (PostgreSQL, Redis)
- ```docker compose build --no-cache``` This step is required only the first time, or when Python dependencies change

Note:
On the first startup, the NetBox container may temporarily appear as "unhealthy"
while database migrations and initialization tasks are being completed.
This is expected behavior.

Once started, NetBox will be available at: ```http://localhost:8000```

### Create Admin User

After the containers are running, create a NetBox administrator account:
```
docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
```
Follow the prompts to set: ```Username``` , ```Email``` and ```Password```

This user is required to access the NetBox UI and execute Custom Scripts.


### Notes

- Runtime data (database contents, users, devices) is not stored in the repository
- Docker volumes are used for persistence during local execution

## Exercise 1 – NetBox Custom Script

### Description

This exercise implements a NetBox Custom Script that allows filtering devices and generating structured output based on user-selected criteria.

The script demonstrates:

- Usage of NetBox Custom Scripts
- Filter validation logic
- Device iteration using the NetBox ORM
- Structured output generation (YAML)
- Logging execution details in the NetBox UI
- Optional export of results to a PDF file

### Initial Data Setup

For this exercise, the initial dataset (Sites, Racks, Devices, Device Roles and Device Types) can be preloaded automatically using a YAML fixture.

- This approach provides a reproducible and consistent dataset across environments without requiring manual input through the NetBox UI.
- The fixture is located at: ```data/initial_data.yaml```

To load the initial data, run:

```
docker compose exec netbox python manage.py loaddata /opt/netbox/data/initial_data.yaml
```

The dataset created by the fixture follows the exercise requirements:

- 2 Sites
- 4 Racks (2 per Site)
- 20 Devices (10 per Site)
- One empty Rack per Site
- Device Role and Device Type defined
- Status assigned to each Device

Using a declarative fixture avoids coupling the repository to a specific database state while enabling a predictable setup for review and testing.

### Requirements Covered

Filters

- Device Status (required)
- Site (optional)
- Rack (optional)

Validation Rules

- The script cannot be executed if only Device Status is selected
- At least one additional filter (Site or Rack) must be provided

Processing

- Iterates through all devices matching the selected filters

Output

- YAML output displayed in the NetBox Output field
- Log entries displayed in the UI using the format:
```
Site <site_name> (<rack_name>): #<device_id> - <device_name>
```

Optional

- Generation of a PDF report containing the execution results

### Script Location

```
scripts/device_inventory_report.py
```

### How to Execute Exercise 1

1. Start NetBox using Docker Compose
2. Log in to the NetBox UI
3. Navigate to: ```http://localhost:8000/extras/scripts/```
4. Add the script and select ```device_inventory_report.py``` in the ```scripts``` folder located at the repository root
5. Run the Script and Choose: ```Device Status (required) → Site or Rack (at least one required)```
6. Execute the script

### Output of Exercise 1

- UI Log: One log entry per processed device
- Output Field: YAML-formatted device data
- File Output: PDF report generated with a timestamped filename in:
```
reports/device_inventory_report_YYYYMMDD_HHMMSS.pdf
```
- PDF files are persisted using a Docker-mounted volume.

## Exercise 2 – NetBox API Device Count Script

### Description

This exercise provides a standalone Python script that queries the NetBox REST API to retrieve device counts based on their status.

The script supports:

- Counting devices with a specific status
- Counting devices grouped by status if no filter is provided

The script interacts exclusively with the NetBox API and does not depend on NetBox internals.

### Dependencies

- The API script requires the Python ```requests``` library.

If not already installed, it can be installed using:
```
pip install requests
```

### Testing

Unit tests are implemented using Python's built-in ```unittest``` framework.

API responses are simulated using ```unittest.mock```, allowing tests to run without
requiring a running NetBox instance.

Run tests using:

```
python -m unittest discover tests -v
```

Expected output:
```
test_api_error_handling (test_device_count.TestDeviceCountAPI.test_api_error_handling)
Test API error handling when a non-200 response is returned. ... ok
test_get_devices_with_status (test_device_count.TestDeviceCountAPI.test_get_devices_with_status)
Test retrieving devices filtered by status using mocked API response. ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

### How to Execute Exercise 2

Prerequisites

- NetBox running and accessible
- A valid NetBox API token (create one at: ```http://localhost:8000/user/api-tokens/add/```)

### API Endpoint Used

```
GET /api/dcim/devices/
```

Optional query parameter:```status=<device_status>```

### Script Location

```
api/device_count.py
```

### Count devices with a specific status
```
python api/device_count.py --url http://localhost:8000 --token <API_TOKEN> --status active
```
Example output:
```
Devices with status 'active': 12
```

### Count devices grouped by status
```
python api/device_count.py --url http://localhost:8000 --token <API_TOKEN>
```
Example output:
```
Device count by status:
  active: 12
  offline: 8
```

### Error Handling

- HTTP errors are detected and reported
- Invalid tokens or unreachable endpoints produce clear error messages
- API pagination is handled automatically

### Notes

- Custom Scripts are loaded from the filesystem and are not stored in the database
- No NetBox core files are modified
- Docker volumes are used for persistent report storage
- The repository focuses on code and configuration, not runtime data

### Conclusion

This repository provides a complete and reproducible solution for both exercises,
demonstrating correct usage of NetBox Custom Scripts, API interaction, and Docker-based deployment practices.