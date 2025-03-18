# Malware Simulation & System Information Extraction Tool

## Project History

This project was originally developed in **July 2022**, the summer after my freshman year of high school. Back then, I was deeply fascinated by cybersecurity and eager to explore what I could achieve with Python. I challenged myself to simulate aspects of malware behavior, such as extracting system information, decrypting browser data, retrieving network credentials, and interfacing with Android devices via ADB.

Although this early version reflects the learning curve of a beginner, it remains a testament to my long-standing passion for cybersecurity and my commitment to continuous growth. Over the years, I have honed my skills further, and this repository serves as a milestone in my journey—demonstrating both my initial creativity and my ongoing evolution in the field.

**Description:**  
This project simulates malware behavior by extracting sensitive information from a Windows system. It gathers system hardware details, browser data (Chrome and Microsoft Edge), WiFi network credentials, and even interfaces with Android devices via ADB. **This tool is provided for educational and research purposes only.**

> **Disclaimer:**  
> Unauthorized use of this tool is illegal and unethical. Use it only on systems you own or for which you have explicit permission. The author is not responsible for any misuse of this software.

## Features
- **System & Hardware Information:**  
  Collects detailed data about CPU, memory, disk storage, GPU, motherboard, and OS information using WMI, psutil, and WMIC commands.
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
- **Operating System:** Windows (this project relies on Windows-specific libraries and commands)
- **Python Version:** 3.8x+
- **Other:**  
  - Chrome & Microsoft Edge must be installed for browser data extraction.  
  - An active ADB server for Android device interfacing.

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/titusvnu/system-credentials-profiling-malware.git
   cd system-credentials-profiling-malware
