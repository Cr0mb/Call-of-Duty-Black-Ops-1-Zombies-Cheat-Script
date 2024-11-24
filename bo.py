import pymem
import struct
import time
import threading
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_game_values(pm):
    base_address = pm.base_address
    
    offsets = {
        "Health": 0x167987C,
        "Points": 0x180A6C8,
        "Pistol_Ammo": 0x1808F00,
        "Pistol_Mags": 0x1808E88,
        "Rifle_Ammo": 0x1808F10,
        "Rifle_Mags": 0x1808E98,
        "Grenades": 0x1808F08
    }
    
    values = {}
    
    for label, offset in offsets.items():
        address = base_address + offset
        value = pm.read_bytes(address, 4)
        unpacked_value = struct.unpack("<I", value)[0]
        values[label] = unpacked_value

    return values

def change_value(pm, label, new_value):
    base_address = pm.base_address
    offsets = {
        "Health": 0x167987C,
        "Points": 0x180A6C8,
        "Pistol_Ammo": 0x1808F00,
        "Pistol_Mags": 0x1808E88,
        "Rifle_Ammo": 0x1808F10,
        "Rifle_Mags": 0x1808E98,
        "Grenades": 0x1808F08
    }

    offset = offsets.get(label)
    if offset is None:
        print("Invalid selection!")
        return

    address = base_address + offset
    packed_value = struct.pack("<I", new_value)

    pm.write_bytes(address, packed_value, len(packed_value))  # Write 4 bytes to memory

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
        "Grenades": 0x1808F08
    }

    while True:
        for label, offset in offsets.items():
            address = base_address + offset
            packed_value = struct.pack("<I", frozen_value)
            pm.write_bytes(address, packed_value, len(packed_value))
        time.sleep(1)

def display_menu(values):
    clear_screen()
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
    print("8. Unlimited Everything (Freeze all values to a custom value)")
    print("9. Exit")
    print("="*40)

def main():
    pm = pymem.Pymem("BlackOps.exe")

    while True:
        game_values = read_game_values(pm)

        display_menu(game_values)

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 9:
                print("Exiting...")
                break

            if choice == 8:
                freeze_value = int(input("Enter the value to freeze all game values to: "))
                print(f"Enabling Unlimited Everything (Freezing all values to {freeze_value})...")
                freeze_thread = threading.Thread(target=freeze_values, args=(pm, freeze_value))
                freeze_thread.daemon = True
                freeze_thread.start()

            labels = [
                "Health", "Points", "Pistol_Ammo", "Pistol_Mags", 
                "Rifle_Ammo", "Rifle_Mags", "Grenades"
            ]
            if 1 <= choice <= 7:
                label = labels[choice - 1]
                new_value = int(input(f"Enter the new value for {label}: "))
                change_value(pm, label, new_value)
            else:
                print("Invalid choice, please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
