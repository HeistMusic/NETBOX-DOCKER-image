# NetBox Custom Script – Technical Exercise

## 1. Overview

This repository contains the solution to a technical exercise involving the
development of a custom NetBox script.

The goal of the exercise is to demonstrate:
- Understanding of NetBox Custom Scripts
- Proper filtering and validation logic
- Structured output generation
- Basic reporting and export capabilities
- Docker-based setup awareness

---

## 2. Exercise Requirements

The exercise required implementing a NetBox Custom Script with:

- Filters for Site, Rack and Device Status
- Mandatory Device Status selection
- At least one additional filter (Site or Rack)
- Iteration over matching devices
- Output in YAML format
- Log output in the NetBox UI
- Optional export of results to PDF

---

## 3. Solution Location

The core solution is implemented in:

scripts/device_inventory_report.py


Generated reports are stored in:

reports/

---

## 4. How to Review the Solution (Quick)

To review the exercise without deep setup:

1. Open `scripts/device_inventory_report.py`
2. Review the filter validation logic
3. Review the YAML output generation
4. Review the PDF export logic

This is sufficient to validate the exercise requirements.

---

## 5. Running the Script (Optional)

If execution is required:

1. Start NetBox using Docker Compose
2. Log in to NetBox
3. Navigate to **Admin → Extras → Scripts**
4. Execute **Device Inventory Report**

PDF reports will be generated in:

reports/

yaml
Copiar código

---

## 6. Notes & Design Decisions

- Custom Scripts do not access Django global settings
- File generation is handled via Docker-mounted volumes
- PDF filenames include timestamps to avoid overwrites
- The solution respects NetBox Custom Script constraints

---

## 7. Conclusion

The solution fulfills all the exercise requirements while maintaining
compatibility with NetBox production constraints and Docker best practices.