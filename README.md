# Malware Simulation & System Information Extraction Tool



**Description:**  
This project simulates malware behavior by extracting sensitive information from a Windows system. It gathers system hardware details, browser data (Chrome and Microsoft Edge), WiFi network credentials, and even interfaces with Android devices via ADB. **This tool is provided for educational and research purposes only.**

> **Disclaimer:**  
> Unauthorized use of this tool is illegal and unethical. Use it only on systems you own or for which you have explicit permission. The author is not responsible for any misuse of this software.

## Features
- **System & Hardware Information:**  
  Collects detailed data about CPU, memory, disk storage, GPU, motherboard, and OS information using WMI, psutil, and WMIC commands.
![Untitled design (1)](https://github.com/user-attachments/assets/f0323e96-a784-463f-8201-f44a5a439445)
- **Browser Data Extraction:**  
  - **Chrome:** Retrieves passwords, browsing history, and autofill data using decryption routines.  
  - **Microsoft Edge:** Extracts saved credentials using PowerShell.
- **Network Credential Extraction:**  
  Extracts saved WiFi profiles and passwords.
- **Android Device Interface:**  
  Uses ADB to retrieve file listings from connected Android devices.
- **Data Packaging & Exfiltration:**  
  Packages the collected data (logs, CSVs, etc.) and sends it via Discord webhooks for demonstration.
- **Logging:**  
  Implements comprehensive logging to track the extraction process.

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



