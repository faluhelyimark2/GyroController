import socket
import json
import vgamepad as vg

# Virtuális Xbox 360 kontroller indítása
gamepad = vg.VX360Gamepad()
print("-> Virtuális Xbox Kontroller csatlakoztatva!")

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

HOST_IP = get_local_ip()
PORT = 8765
MAX_TILT_ANGLE = 40.0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", PORT))

print("--------------------------------------------------")
print(f"UDP Szerver fut! IP: {HOST_IP} | Port: {PORT}")
print("--------------------------------------------------")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8', errors='ignore').strip()

        roll = 0.0
        is_drive_pressed = False
        is_camera_pressed = False
        is_jump_pressed = False
        is_shoot_pressed = False

        if "roll" in message:
            try:
                parsed = json.loads(message)
                roll = float(parsed.get("roll", 0))
                is_drive_pressed = bool(parsed.get("drive", False))
                is_camera_pressed = bool(parsed.get("camera", False))
                is_jump_pressed = bool(parsed.get("jump", False))
                is_shoot_pressed = bool(parsed.get("shoot", False))
            except:
                pass

        # Dőlés skálázása
        clamped_roll = max(-MAX_TILT_ANGLE, min(MAX_TILT_ANGLE, roll))
        joystick_x = int((clamped_roll / MAX_TILT_ANGLE) * 32767)

        # --- UGRÁS (Xbox 'A' Gomb) ---
        if is_jump_pressed:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            jump_str = "A"
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            jump_str = "-"

        # --- TÜZELÉS / LÖVÉS (Xbox RT) ---
        if is_shoot_pressed:
            gamepad.right_trigger(value=255)
            shoot_str = "RT"
        else:
            gamepad.right_trigger(value=0)
            shoot_str = "-"

        # --- TENGELYEK (MOZGÁS / KAMERA / INAKTÍV) ---
        if is_drive_pressed:
            gamepad.left_joystick(x_value=joystick_x, y_value=0)
            gamepad.right_joystick(x_value=0, y_value=0)
            mode_str = "MOZGÁS 🟢"
        elif is_camera_pressed:
            gamepad.right_joystick(x_value=joystick_x, y_value=0)
            gamepad.left_joystick(x_value=0, y_value=0)
            mode_str = "KAMERA 🔵"
        else:
            # Ha egyik gombgs sincs nyomva, mindkét kar középállásban marad!
            gamepad.left_joystick(x_value=0, y_value=0)
            gamepad.right_joystick(x_value=0, y_value=0)
            mode_str = "INAKTÍV ⚪"

        gamepad.update()

        print(f"Mód: {mode_str} | Ugrás: {jump_str} | Lövés: {shoot_str} | Dőlés: {round(roll, 1)}°        ", end="\r")

    except Exception as e:
        print(f"\n[Hiba]: {e}")