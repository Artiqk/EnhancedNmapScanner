#!/usr/bin/python3
import argparse
import subprocess
import logging
import xml.etree.ElementTree as ET

from color_formatter import ColorFormatter

'''
TODO
 - Use $(which nmap) to find nmap path ?
 - Change -A to -sVC ?
'''

__author__ = "artiqk"
__version__ = "1.0"


logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    prog='nmen',
    description=f'NmapEnhanced {__version__} - Simple python script for a quick and complete TCP port enumeration',
    add_help=True
)

parser.add_argument('host', help='Target host or IP address')
parser.add_argument('-v', '--verbose', action='count', default=0, help="Verbosity: -v for INFO, -vv for DEBUG")
parser.add_argument('-o', '--output', default='nmen_result.txt', help='Output file name for the scan results (default: nmen_result.txt)')
parser.add_argument('-d', '--display', action='store_true', help='Display nmap command output to terminal')
parser.add_argument('--no-delete', action='store_true', help="Cancels deletion of the XML file of the primary scan")

args = parser.parse_args()

HOST = args.host
VERBOSITY = args.verbose
FILENAME_TXT = args.output
DISPLAY_NMAP_OUTPUT = args.display
NO_DELETE_XML = args.no_delete
FILENAME_XML = 'nmen_result.xml'

# CHANGE THIS ACCORDING TO YOUR INSTALLATION
NMAP_PATH = '/usr/bin/nmap'


def get_port_list_from_xml(xml_filepath: str) -> list:
    try:
        tree = ET.parse(xml_filepath)
        root = tree.getroot()
    except (ET.ParseError, FileNotFoundError) as e:
        raise ValueError(f"Could not parse XML file '{xml_filepath}'") from e
    
    logging.info("Parsing for open ports in the XML file")
    # Extracting open port numbers from the XML data
    found_ports_list = [port.attrib['portid'] for port in root.findall('.//port')]
    logging.debug(found_ports_list)
    total_ports = len(found_ports_list)
    
    if total_ports == 0:
        logging.info('No open ports found, advanced scan cancelled')
        return []
    
    logging.info(f"Found {total_ports} open ports : {found_ports_list}")

    return found_ports_list


def delete_xml_file(xml_filepath: str) -> None:
    try:
        cmd = f"rm {xml_filepath}"
        split_cmd = cmd.split(' ')

        logging.info(f"Deleting XML file using : {cmd}")
        logging.debug(split_cmd)

        subprocess.run(split_cmd)

    except (FileNotFoundError, PermissionError) as e:
        raise ValueError(f"Could not delete XML file '{xml_filepath}'") from e
    

def setup_logging(verbosity: int) -> None:
    levels = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG
    }

    level = levels.get(verbosity, logging.DEBUG)

    color_handler = logging.StreamHandler()

    color_handler.setFormatter(ColorFormatter())

    logging.basicConfig(
        level=level,
        handlers=[color_handler]
    )



def main():

    setup_logging(VERBOSITY)

    advanced_scan_cancelled = False

    stdout_target = None if DISPLAY_NMAP_OUTPUT else subprocess.DEVNULL

    try:
        cmd = f'{NMAP_PATH} -p- -T4 -oX {FILENAME_XML} {HOST}'
        split_cmd = cmd.split(' ')

        logging.info(f"Starting primary scan using : {cmd}")
        logging.debug(split_cmd)

        # Running the primary scan and suppressing stdout
        subprocess.run(split_cmd, stdout=stdout_target)
        
        logging.info("Primary scan complete")
    except Exception as e:
        logging.error(f"Primary scan failed : {e}")
        exit(1)

    try:
        ports = get_port_list_from_xml(FILENAME_XML)
        if not ports:
            advanced_scan_cancelled = True
    except ValueError as e:
        logging.critical(f"Failed to retrieve open ports from XML: {e}")
        advanced_scan_cancelled = True

    try:
        if not NO_DELETE_XML:
            delete_xml_file(FILENAME_XML)
    except ValueError as e:
        logging.critical(f"Failed to delete XML file : {e}")

    if advanced_scan_cancelled:
        exit(1)

    try:
        formatted_port_list = ','.join(ports)
        cmd = f'{NMAP_PATH} -sV -A -T4 -p{formatted_port_list} {HOST} -oN {FILENAME_TXT}'
        split_cmd = cmd.split(' ')

        logging.info(f"Starting advanced scan using : {cmd}")
        logging.debug(split_cmd)
        
        subprocess.run(split_cmd, stdout=stdout_target)

        logging.info(f"Advanced scan completed, results saved in {FILENAME_TXT}")
    except Exception as e:
        logging.error(f"Advanced scan failed : {e}")


if __name__ == '__main__':
    main()