# NmapEnhanced

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

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install Nmap from https://nmap.org/download.html if you haven't already.
3. Clone this repository or download the `enhanced_nmap_scanner.py` file.
4. Change the variable NMAP_PATH according to your installation.

**Get nmap PATH**
```bash
$> which nmap
/usr/bin/nmap # PUT THIS IN NMAP_PATH
```

**TIP**

For ease of use you can create a symlink of main.py in ~/.local/bin

```bash
ln -s <PATH TO MAIN.PY> /home/<user>/.local/bin/nmen
```

## Usage
```commandline
python3 enhanced_nmap_scanner.py <host> [--output OUTPUT_FILE]
```
- `<host>`: Target host or IP address to scan
- `--output OUTPUT_FILE` or `-o OUTPUT_FILE`: Optional. Specify the output file name for the scan results (default: nmap_out.txt)

**OR**

If you've added the script to your .local/bin

```bash
nmen <host> [--output OUTPUT_FILE]
```

## Example
```commandline
python3 enhanced_nmap_scanner.py 192.168.1.1 --output scan_results.txt
```
**OR**
```bash
nmen 192.168.1.1 --output scan_results.txt
```