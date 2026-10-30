# ============================================================
# server.py
# Aplikasi Web Server Sederhana berbasis Python Flask
# Praktikum Pertemuan 1 - Inisiasi Proyek Web Server & GitHub
# ============================================================
import os
import socket
import platform
from datetime import datetime

# Mengimpor pustaka Flask. Pastikan sudah diinstal dengan 'pip install flask'
from flask import Flask, jsonify

# Inisiasi Aplikasi Flask
# Perbaikan: Pastikan baris ini TIDAK memiliki indentasi ilegal
app = Flask(__name__)

# === KONFIGURASI ===
# Membaca konfigurasi dari Environment Variable dengan nilai default
# Anda bisa menyetel nama Anda dengan perintah terminal:
# export APP_AUTHOR="Nama Lengkap - NIM" (di Git Bash)
APP_AUTHOR = os.getenv("APP_AUTHOR", "Belum Diatur")
APP_ENV = os.getenv("APP_ENV", "development") # Opsi: development, production

# Port server, default 5000
APP_PORT = int(os.getenv("APP_PORT", 5000))

# === FUNGSI PEMBANTU ===
# Fungsi untuk mengumpulkan informasi perangkat server
def get_server_info():
    """Mengembalikan dictionary berisi detail informasi server."""
    return {
        "author": APP_AUTHOR,
        "environment": APP_ENV,
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

# === RUTE APLIKASI (ROUTES) ===

# 1. Rute Utama (/) - Menampilkan halaman dashboard HTML sederhana
@app.route("/")
def index():
    """Menampilkan halaman dashboard HTML yang rapi."""
    # Ambil informasi server terbaru
    info = get_server_info()
    
    # Template HTML menggunakan f-string Python
    # Perbaikan: Memperbaiki typo 'initialscale' dan merapikan CSS/HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Web Server - Praktikum 1</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                padding: 32px 48px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
                backdrop-filter: blur(4px);
            }}
            h1 {{ color: #4fc3f7; margin-top: 0; text-align: center; }}
            p {{ text-align: center; color: rgba(255, 255, 255, 0.8); }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 16px; }}
            td {{ padding: 10px 15px; border-bottom: 1px solid rgba(255,255,255,0.1); }}
            td:first-child {{ font-weight: bold; color: #81d4fa; width: 40%; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Flask Web Server Aktif - 2505110003 (Organization Fork)</h1>
            <p>Aplikasi berjalan dengan baik pada perangkat berikut:</p>
            <table>
                <tr><td>Author</td><td>{info["author"]}</td></tr>
                <tr><td>Environment</td><td>{info["environment"]}</td></tr>
                <tr><td>Hostname</td><td>{info["hostname"]}</td></tr>
                <tr><td>Sistem Operasi</td><td>{info["os"]} {info["os_release"]}</td></tr>
                <tr><td>Arsitektur</td><td>{info["architecture"]}</td></tr>
                <tr><td>Versi Python</td><td>{info["python_version"]}</td></tr>
                <tr><td>Waktu Server</td><td>{info["server_time"]}</td></tr>
            </table>
        </div>
    </body>
    </html>
    """
    return html

# 2. Rute API (/api/info) - Mengembalikan informasi server dalam format JSON
@app.route("/api/info")
def api_info():
    """Endpoint API untuk mendapatkan data server dalam format JSON."""
    return jsonify(get_server_info())

# 3. Rute Health Check (/health) - Untuk memantau status server
@app.route("/health")
def health():
    """Endpoint sederhana untuk pengecekan kesehatan aplikasi."""
    return jsonify({
        "status": "ok", 
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    })

# === MENJALANKAN APLIKASI ===
if __name__ == "__main__":
    # Mencetak banner informasi ke terminal saat startup
    print("=" * 60)
    print(f"{'Aplikasi Flask Web Server - Praktikum Pertemuan 1':^60}")
    print("-" * 60)
    print(f" Author      : {APP_AUTHOR}")
    print(f" Environment : {APP_ENV}")
    print(f" Hostname    : {socket.gethostname()}")
    print(f" Platform    : {platform.system()} ({platform.machine()})")
    print("-" * 60)
    print(f" Akses Web   : http://localhost:{APP_PORT}")
    print(f" Akses API   : http://localhost:{APP_PORT}/api/info")
    print("=" * 60)
    print("Menunggu permintaan...\n")

    # Menjalankan server Flask
    # Perbaikan: Tanda kurung debug diperbaiki dan dirapikan
    # Debug mode otomatis aktif jika APP_ENV adalah 'development'
    app.run(host="0.0.0.0", port=APP_PORT, debug=(APP_ENV == "development"))