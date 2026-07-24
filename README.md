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
   * A virtuális Xbox kontroller működéséhez töltsd le és telepítsd a [ViGEmBus Driver-t](https://github.com/nefarius/ViGEmBus/releases) a PC-re!
3. **Szükséges Python csomag:**
   * Nyiss egy Parancssort (CMD), és írd be ezt a parancsot:
     ```cmd
     pip install vgamepad
     ```

---

### 🚀 Hogyan kell használni? (Lépésről lépésre)

1. **Mobil felkészítése:** Telepítsd a **`GyroController.apk`** fájlt az Android telefonodra.
2. **Hálózat:** Győződj meg róla, hogy a telefonod és a PC-d **ugyanarra a Wi-Fi hálózatra** van csatlakozva.
3. **Szerver indítása:** Nyiss egy Parancssort (CMD) a PC-n abban a mappában, ahol a `server.py` van, és írd be:
   ```cmd
   python server.py
