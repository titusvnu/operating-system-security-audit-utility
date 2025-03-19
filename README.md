 # Malware Simulation & System Information Extraction Tool



**Description:**  
This project simulates malware behavior by extracting sensitive information from a Windows system. It gathers system hardware details, browser data (Chrome and Microsoft Edge), WiFi network credentials, and even interfaces with Android devices via ADB. 

> **Disclaimer:**  
> Unauthorized use of this tool is illegal and unethical. Use it only on systems you own or for which you have explicit permission. The author is not responsible for any misuse of this software.

## Features
- **Browser Data Extraction:**  
    - Extracts encrypted sensitive passwords using Powershell scripting (Edge) and SQL decryption methods (Chrome)
   ![Untitled design (1)](https://github.com/user-attachments/assets/f0323e96-a784-463f-8201-f44a5a439445)

    - Retrieves browsing history by decrypting locally saved SQL databases
    ![Screenshot 2025-03-18 210737](https://github.com/user-attachments/assets/56a7781c-9142-4f0d-91f4-e1c63bf4939b)

  - Retrieves encrypted autofill data  
![Untitled design (3)](https://github.com/user-attachments/assets/27b6a8ba-0a9f-4fc6-8bac-50858fdf5d00)

- **Network Credential Extraction:**  
  - Extracts saved WiFi profiles and passwords.
    ![Untitled design (4)](https://github.com/user-attachments/assets/30d3d035-27cb-4fcb-b64f-0ef3a328d93b)

```
 "system_network_passwords": {
    "NETGEAR68_EXT": "greatunicorn941",
    "TPLINK_42": "greatunicorn333"
  },
  "system_network_count": 2
```
- **Android Device Interface:**  
  Uses ADB to retrieve file listings from connected Android devices.
  
- **System & Hardware Information:**  
  Collects detailed data about CPU, memory, disk storage, GPU, motherboard, and OS information using WMI, psutil, and WMIC commands.
  
  ![Untitled design (5)](https://github.com/user-attachments/assets/00c34f40-4e52-4ff9-b87d-69863d0c9c64)

- **Data Packaging & Exfiltration:**  
    - Packages the collected data (logs, CSVs, etc.) and sends it via Discord webhooks for demonstration.
  
- **Logging:**  
    - Implements comprehensive logging to track the extraction process.
```
08/14 07:30 PM | chromedata | DEBUG |: Attempting to generate data files
08/14 07:30 PM | main | INFO |: Libraries imported successfully!
08/14 07:30 PM | main | DEBUG |: Public IP 
08/14 07:30 PM | main | DEBUG |: Webhook element successfully sent
08/14 07:30 PM | main | DEBUG |: Webhook element successfully sent
08/14 07:30 PM | main | DEBUG |: Webhook element successfully sent
08/14 07:30 PM | main | DEBUG |: Webhook element successfully sent
08/14 07:30 PM | main | DEBUG |: Webhook element successfully sent
08/14 07:30 PM | main | DEBUG |: Webhook element successfully sent
```

### Requirements
- **Operating System:** Windows 7, 8, 10, 11
- **Python Version:** 3.6x+
- **Other:**  
  - Chrome & Microsoft Edge must be installed for browser data extraction.  
  - An active ADB server for Android device interfacing.

## Project History

This project was originally developed in **July 2022**, the summer after my freshman year of high school, fascinated with pushing the limits of malware behavior with Python. 

Although this early version reflects the learning curve of a beginner, this repository serves as a milestone in my journey—demonstrating both my initial creativity and my ongoing evolution in the Computer Science field.


### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/titusvnu/system-credentials-profiling-malware.git
   cd system-credentials-profiling-malware



