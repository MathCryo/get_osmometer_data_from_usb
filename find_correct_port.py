import platform
import os
import serial  # include pySerial 
import serial.tools.list_ports  # tool to find list_ports


def find_harware(hwids):
    port_list=serial.tools.list_ports.comports()
    correct_port=None
    try:
        for name, desc, hwid in sorted(port_list):
            port_name=name
            if hwid in hwids:
                correct_port=port_name
                break
    except Exception as err:
        print(f"An error occured: {err}")
    if correct_port:
        print("CORRECT PORT IS: ", correct_port)
    else:
        print("Correct port not found, check connection and permissions!")
    return correct_port
def main():
    hwids=["n/a", "need_id_1_2"]
    find_harware(hwids)
if __name__ == "__main__":
    main()
