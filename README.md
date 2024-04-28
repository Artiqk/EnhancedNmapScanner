# Enhanced Nmap Scanner

## Description
This Python script performs a basic scan using Nmap to retrieve all open ports on a target host or IP address. It then performs an advanced scan, focusing only on the open ports identified during the basic scan. The script allows users to specify the target host and an output file name for the scan results.

## Features
- Basic and Advanced scanning modes
- Command-line arguments for specifying the target host and output file name
- Error handling for graceful termination in case of failures
- Automatically deletes temporary XML file generated during the basic scan

## Requirements
- Python 3.x
- Nmap installed (available at https://nmap.org/download.html)

## Usage
```commandline
python3 enhanced_nmap_scanner.py <host> [--output OUTPUT_FILE]
```
- `<host>`: Target host or IP address to scan
- `--output OUTPUT_FILE` or `-o OUTPUT_FILE`: Optional. Specify the output file name for the scan results (default: nmap_out.txt)

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install Nmap from https://nmap.org/download.html if you haven't already.
3. Clone this repository or download the `enhanced_nmap_scanner.py` file.

## Example
```commandline
python3 enhanced_nmap_scanner.py 192.168.1.1 --output scan_results.txt
```