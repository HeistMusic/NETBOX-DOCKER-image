# NetBox Custom Script – Technical Exercise

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
The script is automatically loaded by NetBox from the configured SCRIPTS_ROOT.
No database registration or additional configuration is required.

### How to Execute Exercise 1

1. Start NetBox using Docker Compose
2. Log in to the NetBox UI
3. Navigate to:
```Admin → Extras → Scripts```
4. Select Device Inventory Report
5. Choose:
- Device Status (required)
- Site or Rack (at least one required)
6. Execute the script

### Output of Exercise 1

- UI Log: One log entry per processed device
- Output Field: YAML-formatted device data
- File Output: PDF report generated with a timestamped filename in:
```
reports/device_inventory_report_YYYYMMDD_HHMMSS.pdf
```
PDF files are persisted using a Docker-mounted volume.

## Exercise 2 – NetBox API Device Count Script

### Description

This exercise provides a standalone Python script that queries the NetBox REST API to retrieve device counts based on their status.

The script supports:

- Counting devices with a specific status
- Counting devices grouped by status if no filter is provided

The script interacts exclusively with the NetBox API and does not depend on NetBox internals.

### API Endpoint Used
```
GET /api/dcim/devices/
```
Optional query parameter:

- status=<device_status>

### Script Location
```
api/device_count.py
```

### How to Execute Exercise 2

Prerequisites

- NetBox running and accessible
- A valid NetBox API token

### Count devices with a specific status
```
python api/device_count.py \
  --url http://localhost:8000 \
  --token <API_TOKEN> \
  --status active
```
Example output:
```
Devices with status 'active': 12
```

### Count devices grouped by status
```
python api/device_count.py \
  --url http://localhost:8000 \
  --token <API_TOKEN>
```
Example output:
```
Device count by status:
  active: 12
  offline: 6
  planned: 2
```

### Error Handling

- HTTP errors are detected and reported
- Invalid tokens or unreachable endpoints produce clear error messages
- API pagination is handled automatically

### Initial Data Setup

For the purpose of this exercise, initial data (Sites, Racks, Devices and admin user)
is created manually in the NetBox UI after deployment.

The dataset used for testing follows the exercise requirements:

- 2 Sites
- 4 Racks (2 per Site)
- 20 Devices (10 per Site)
- One empty Rack per Site
- Status assigned to each Device

This approach avoids coupling the repository to a specific database state and ensures reproducibility across environments.

### Notes

- Custom Scripts are loaded from the filesystem and are not stored in the database
- No NetBox core files are modified
- Docker volumes are used for persistent report storage
- The repository focuses on code and configuration, not runtime data

### Conclusion

This repository provides a complete and reproducible solution for both exercises,
demonstrating correct usage of NetBox Custom Scripts, API interaction, and Docker-based deployment practices.