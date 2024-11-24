import pymem
import struct
import time
import threading
import os

def read_game_values(pm):
    base_address = pm.base_address
    
    offsets = {
        "Health": 0x167987C,
        "Points": 0x180A6C8,
        "Pistol_Ammo": 0x1808F00,
        "Pistol_Mags": 0x1808E88,
        "Rifle_Ammo": 0x1808F10,
        "Rifle_Mags": 0x1808E98,
        "Grenades": 0x1808F08,
        "Akimbo_Ammo": 0x1808F20
    }
    
    values = {}
    
    for label, offset in offsets.items():
        address = base_address + offset
        value = pm.read_bytes(address, 4)
        unpacked_value = struct.unpack("<I", value)[0]
        values[label] = unpacked_value

    return values

def read_coordinates(pm):
    base_address = pm.base_address

    offsets = {
        "x": 0x18,
        "y": 0x20,
        "z": 0x1C
    }

    coordinates = {}
    
    for label, offset in offsets.items():
        address = base_address + 0x16796F8 + offset
        value = pm.read_bytes(address, 4)
        unpacked_value = struct.unpack("<f", value)[0]
        coordinates[label] = unpacked_value

    return coordinates

def change_value(pm, label, new_value):
    base_address = pm.base_address
    offsets = {
        "Health": 0x167987C,
        "Points": 0x180A6C8,
        "Pistol_Ammo": 0x1808F00,
        "Pistol_Mags": 0x1808E88,
        "Rifle_Ammo": 0x1808F10,
        "Rifle_Mags": 0x1808E98,
        "Grenades": 0x1808F08,
        "Akimbo_Ammo": 0x1808F20
    }

    offset = offsets.get(label)
    if offset is None:
        print("Invalid selection!")
        return

    address = base_address + offset
    packed_value = struct.pack("<I", new_value)

    pm.write_bytes(address, packed_value, len(packed_value))

    print(f"{label} value changed to: {new_value}")

def freeze_values(pm, frozen_value):
    base_address = pm.base_address
    offsets = {
        "Health": 0x167987C,
        "Points": 0x180A6C8,
        "Pistol_Ammo": 0x1808F00,
        "Pistol_Mags": 0x1808E88,
        "Rifle_Ammo": 0x1808F10,
        "Rifle_Mags": 0x1808E98,
        "Grenades": 0x1808F08,
        "Akimbo_Ammo": 0x1808F20
    }

    while freezing_active:
        for label, offset in offsets.items():
            address = base_address + offset
            packed_value = struct.pack("<I", frozen_value)
            pm.write_bytes(address, packed_value, len(packed_value))
        time.sleep(1)

def stop_freezing():
    global freezing_active
    freezing_active = False
    print("Unfreezing all items...")

def display_menu(values):
    print("## Made by Cr0mb ##")
    print("="*40)
    print("Current Game Values:")
    for label, value in values.items():
        print(f"{label}: {value}")
    print("="*40)

    print("\nSelect the value you want to change:")
    print("1. Health")
    print("2. Points")
    print("3. Pistol Ammo")
    print("4. Pistol Mags")
    print("5. Rifle Ammo")
    print("6. Rifle Mags")
    print("7. Grenades")
    print("8. Akimbo Ammo")  
    print("9. Unlimited Everything (Freeze all values to the same custom value)")
    print("10. Unfreeze all items")
    print("11. View Coordinates (Active Updates)")
    print("12. Exit")
    print("="*40)

def display_coordinates(coordinates):
    # This will print the coordinates on the same line
    print(f"Coordinates - X: {coordinates['x']:.2f} Y: {coordinates['y']:.2f} Z: {coordinates['z']:.2f}", end="\r")

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()  # Clear the screen when the script is first started

    global freezing_active
    freezing_active = False

    pm = pymem.Pymem("BlackOps.exe")

    while True:
        game_values = read_game_values(pm)

        display_menu(game_values)

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 11:
                # Continuously display coordinates without clearing the screen
                print("Watching coordinates... Press Ctrl+C to stop.")
                try:
                    while True:
                        coordinates = read_coordinates(pm)
                        display_coordinates(coordinates)
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print("\nStopped watching coordinates.")
                    clear_screen()  # Clear the screen after exiting the coordinate viewer
                


            if choice == 9:
                print("Enter a custom value to apply to all values:")
                try:
                    frozen_value = int(input("Enter the value: "))
                    print(f"Enabling Unlimited Everything (Freezing all values to {frozen_value})...")
                    freezing_active = True
                    freeze_thread = threading.Thread(target=freeze_values, args=(pm, frozen_value))
                    freeze_thread.daemon = True
                    freeze_thread.start()
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if choice == 12:
                clear_screen()
                print("Exiting Safely...")
                time.sleep(1.5)
                clear_screen()
                break

            labels = [
                "Health", "Points", "Pistol_Ammo", "Pistol_Mags", 
                "Rifle_Ammo", "Rifle_Mags", "Grenades", "Akimbo_Ammo"
            ]
            if 1 <= choice <= 8:
                label = labels[choice - 1]
                new_value = int(input(f"Enter the new value for {label}: "))
                change_value(pm, label, new_value)

            if choice == 10:
                stop_freezing()
                    
            else:
                clear_screen()
        except ValueError:
            time.sleep(1)
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()