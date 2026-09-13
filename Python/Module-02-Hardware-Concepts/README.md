# 🖥️ Module 2: Hardware Architecture & Python Execution

## 👨‍🏫 Instructor Core Concepts (Dr. Chuck)

To program effectively, you must understand how Python interacts with physical computer hardware:

* **Central Processing Unit (CPU):** The engine of the computer. Executing instructions at billions of cycles per second, it asks continuously: *"What next?"*
* **Main Memory (RAM):** Ultra-fast, temporary workspace used to store data and code currently in use. Data in RAM disappears as soon as power is turned off (volatile).
* **Secondary Memory:** Permanent storage (Hard Drives, SSDs, Flash Drives). Slower than RAM, but retains files, scripts, and datasets across reboots.
* **Input and Output (I/O) Devices:** Hardware that bridges human interaction and system processing (Keyboard, Mouse, Screen, Network interfaces).

```text
       +---------------------------------------------------+
       |                    HARDWARE                       |
       |                                                   |
[Input Devices] ---> [ CPU (Executes Code) ] <---> [RAM / Main Memory]
(Keyboard/Mouse)            |                           (Fast/Volatile)
                            v
                    [Secondary Storage]
                     (SSD/HDD - Permanent)
                            |
                            v
                     [Output Devices]
                      (Screen/Display)