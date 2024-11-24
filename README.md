# Call of Duty Black Ops 1 Zombies Cheat Script

This Python script allows you to modify various game values for Call of Duty Black Ops 1 Zombies such as health, points, ammo, and grenades. It utilizes the `pymem` library to read and write memory values in real-time while the game is running.

![image](https://github.com/user-attachments/assets/17f46c1a-d5d2-46df-94ea-f31dfacfea48)


## Features:
- Modify Health, Points, Ammo, and more.
- Freeze all values to a custom number (e.g., unlimited health, ammo).
- Easy-to-use menu for selecting values to change.

## Requirements:
- Python 3.x
- `pymem` library (install via `pip install pymem`)

## How to Use:
1. Ensure the game **Call of Duty Black Ops 1 Zombies** is running.
2. Run this Python script. The script will attach to the game's process and allow you to view and modify various in-game values.
3. Use the menu to select which value to change and input the new value.

---

### Cheat Engine Method (Mimicking the Script with Cheat Table)

You can use Cheat Engine to find and modify these values manually by following the steps below:

#### 1. **Find Health**:
   - **Initial Scan**: Start the game and set your health to 100 (or any known value).
   - Open Cheat Engine, attach it to the "BlackOps.exe" process.
   - Scan for **4-byte** values, set the health to a different value (e.g., get hit by a zombie).
   - Perform a **Next Scan** with the new health value. You should narrow down the list to a few values.
   - Once you've found the correct value, modify it to your desired health value (e.g., 999).

*It's easier if you go into Cheat Engine settings and set keybinds for decreased value or increased value..*

#### 2. **Find Points**:
   - **Initial Scan**: Set your points to a known value (e.g., 500).
   - Scan for **4-byte** values in Cheat Engine.
   - Increase your points (e.g., buy a perk or complete a round) and scan again for the new value.
   - When you find the value, change it to your desired number (e.g., 99999).

#### 3. **Find Ammo**:
   - **Initial Scan**: Set your ammo count for a specific weapon (e.g., Pistol Ammo = 12).
   - Scan for **4-byte** values and shoot a few times to change the ammo count.
   - Scan again with the new ammo value (e.g., 9 for Pistol).
   - Repeat the process until you narrow down the ammo count and modify it to any value you want.

#### 4. **Find Grenades**:
   - **Initial Scan**: Set the number of grenades to a known value (e.g., 5).
   - Scan for **4-byte** values and throw a grenade (it should decrease).
   - Scan again for the new grenade count.
   - Once you identify the correct value, change it to the desired amount (e.g., 99).

#### 5. **Freezing Values**:
   To freeze a value (e.g., Ammo or Health), right-click the found value in Cheat Engine, select **"Freeze"**. This will lock the value, preventing it from changing during gameplay.

#### 6. **Advanced Tips**:
   - If you have difficulty finding the correct value, consider scanning for **2-byte** or **Float** values instead of **4-byte** if the results are too broad.
   - If values seem to reset or don't persist, consider using Cheat Engine's **Pointer Scan** to track the base address of the values across different sessions.


