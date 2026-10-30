# ============================================================
# server.py
# Aplikasi Web Server Sederhana berbasis Python Flask
# Praktikum Pertemuan 1 - Inisiasi Proyek Web Server & GitHub
# ============================================================
import os 
import socket 
import platform 
from datetime import datetime 

from flask import Flask, jsonify 
app = Flask(__name__) 
# Membaca konfigurasi dari Environment Variable 
APP_AUTHOR = os.getenv("APP_AUTHOR", "Belum Diatur") 
APP_ENV = os.getenv("APP_ENV", "development")

APP_PORT = 5000

# Fungsi untuk mengumpulkan informasi perangkat server
def get_server_info():
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

@app.route("/")
def index():
    info = get_server_info()
    html = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Web Server - Praktikum 1</title>
        <style>
            body {{
                font-family: Arial, sans-serif; background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
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
            }}
            h1 {{ color: #4fc3f7; margin-top: 0; }}
            table {{ border-collapse: collapse; width: 100%; }} 
            td {{ padding: 8px 12px; border-bottom: 1px solid 
        rgba(255,255,255,0.15); }}
            td:first-child {{ font-weight: bold; color: #81d4fa; }} 
        </style>
    </head>
    <body>
        <div class="card">
        <h1>Flask Web Server Aktif - 2505110003 (organization fork)</h1>
        <p>Aplikasi berjalan dengan baik pada perangkat berikut:</p>
        <table>
            <tr><td>Author</td><td>{info["author"]}</td></tr>

<tr><td>Environment</td><td>{info["environment"]}</td></tr>
            <tr><td>Hostname</td><td>{info["hostname"]}</td></tr>
            <tr><td>Sistem Operasi</td><td>{info["os"]}
{info["os_release"]}</td></tr>

<tr><td>Arsitektur</td><td>{info["architecture"]}</td></tr>
            <tr><td>Versi
Python</td><td>{info["python_version"]}</td></tr>
            <tr><td>Waktu
Server</td><td>{info["server_time"]}</td></tr>
        </table>
        </div> 
    </body> 
    </html>
    """ 
    return html

@app.route("/api/info")
def api_info():
    return jsonify(get_server_info())

@app.route("/health")
def health(): 
    return jsonify({"status": "ok", "hostname": socket.gethostname()})

if __name__ == "__main__":
    print("=" * 55)
    print(" Flask Web Server - Praktikum Pertemuan 1")
    print(f" Author : {APP_AUTHOR}")
    print(f" Environment : {APP_ENV}")
    print(f" Hostname : {socket.gethostname()}")
    print(f" Platform : {platform.system()} ({platform.machine()})")
    print(f" Akses : http://localhost:{APP_PORT}")
    print("=" * 55)
    app.run(host="0.0.0.0", port=APP_PORT, debug=(APP_ENV == "development"))