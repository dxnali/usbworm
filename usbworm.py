import os
import time

"""
Lines with # DEBUG at the end are to check if everything is working correctly,
you can remove them if you want.
"""

# Check priveledges
if os.geteuid() != 0:
    print("This works better with sudo.")
    continuescript = input("Continue? [y/N] => ").lower()
    if continuescript != "y" or continuescript != "yes":
        exit(0)
    else:
        print("Continuing...")

# Directory where USB drives are typically mounted in Linux (change accordingly)
MOUNT_DIR = '/media'

def get_usb_drives():
    """Get a list of mounted USB drives."""
    usb_drives = []
    for root, dirs, files in os.walk(MOUNT_DIR):
        for dir in dirs:
            usb_drives.append(os.path.join(root, dir))
    return usb_drives

def write_to_usb(drive_path):
    """Write 'infected.txt' with 'hello world!' to the USB drive."""
    file_path = os.path.join(drive_path, 'infected.txt')
    try:
        with open(file_path, 'w') as f:
            f.write('Your device has been infected with a worm malware. Do not fret, it is harmless.')
        print(f'Written to {file_path}')
    except Exception as e:
        print(f'Error writing to {file_path}: {e}')  # DEBUG

def main():
    seen_drives = set(get_usb_drives())
    while True:
        current_drives = set(get_usb_drives())
        new_drives = current_drives - seen_drives
        if new_drives:
            for drive in new_drives:
                print(f'New USB drive detected: {drive}')  # DEBUG
                write_to_usb(drive)
            seen_drives.update(new_drives)
        else:
            print('No new USB drives detected.')  # DEBUG
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
