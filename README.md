# 🎮 Gyro Controller for PC

### ❓ Mi ez?
Ez egy nyílt forráskódú rendszer, amivel az Android telefonodat egy giroszkópos **Xbox 360 kontrollerré** alakíthatod PC-n. Kifejezetten autós játékok kormányzásához, valamint FPS/TPS játékok (pl. **Roblox Rivals**) giroszkópos célzásához készült.

---

### 📁 A projektben található fájlok
* **`GyroController.apk`** – A telefonra telepítendő alkalmazás.
* **`server.py`** – A PC-s szerver program, ami fogadja a telefon jelét.

---

### ⚠️ Mire figyelj a telepítésnél? (NAGYON FONTOS!)

1. **Python telepítése:**
   * Töltsd le a Python 3.14-et innen: **[python-3.14.6-amd64.exe Letöltése](https://www.python.org/ftp/python/3.14.6/python-3.14.6-amd64.exe)**
   * 🚨 **MINDENKÉPP PIPÁLD BE** a telepítő legelső ablakának alján az **"Add python.exe to PATH"** opciót! Ha ez kimarad, a szerver nem fog tudni elindulni.
2. **ViGEmBus Driver:**
   * Töltsd le és telepítsd a drivert innen: **[ViGEmBus_1.22.0_x64_x86_arm64.exe Letöltése](https://github.com/nefarius/ViGEmBus/releases/download/v1.22.0/ViGEmBus_1.22.0_x64_x86_arm64.exe)** *(Ez szükséges a virtuális Xbox kontroller működéséhez)*.
3. **Szükséges Python csomag:**
   * Nyiss egy Parancssort (CMD), és írd be ezt a parancsot:
     ```cmd
     pip install vgamepad
     ```

---

### 🚀 Hogyan kell elindítani? (Lépésről lépésre)

1. **Telepítsd az appot:** Másold át a **`GyroController.apk`** fájlt a telefonodra, és telepítsd fel.
2. **Ellenőrizd a Wi-Fi-t:** Győződj meg róla, hogy a telefonod és a PC-d **ugyanarra a Wi-Fi hálózatra** csatlakozik.
3. **Indítsd el a PC-s szervert:** Nyiss egy Parancssort (CMD) a PC-n abban a mappában, ahol a `server.py` fájl található, és futtasd a következő parancsot:
   ```cmd
   python server.py
