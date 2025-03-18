
---

### CHANGELOG.md

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- Planned: Add more robust unit tests and refactor common decryption routines.
- Planned: Enhance error handling and logging for better traceability.

## [0.2.0] - 2025-03-18
### Added
- Integrated ADB module for listing files on connected Android devices.
- Added detailed logging across all modules.
- Expanded extraction for Chrome browser data (passwords, history, autofill data).

### Changed
- Refactored system information extraction using psutil and WMI.
- Updated Discord webhook integration for data packaging.

### Fixed
- Minor bugs in temporary file handling and cleanup routines.

## [0.1.0] - 2025-01-10
### Added
- Initial release featuring:
  - Basic system and hardware information extraction.
  - Chrome password and history decryption.
  - Microsoft Edge credential extraction.
  - Network (WiFi) profile extraction.
- Initial version of the orchestration script (`main.py`) to package and send data.
