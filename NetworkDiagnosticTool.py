
import platform
import socket
import subprocess

def show_system_info():
    print("\\n--- System Information ---")
    print("Operating System:", platform.system())
    print("OS Version:", platform.release())
    print("Computer Name:", socket.gethostname())

def check_dns(hostname):
    print("\\n--- DNS Lookup ---")
    try:
        address = socket.gethostbyname(hostname)
        print(hostname, "resolves to", address)
    except socket.gaierror:
        print("DNS lookup failed.")
        print("Check your internet or DNS settings.")

def check_ping(hostname):
    print("\\n--- Connectivity Test ---")
    flag = "-n" if platform.system() == "Windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", flag, "1", hostname],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print("Ping successful:", hostname)
        else:
            print("Ping failed or blocked:", hostname)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("Ping unavailable or timed out.")

def main():
    print("NETWORK DIAGNOSTIC TOOL")
    print("======================")
    show_system_info()

    hostname = input(
        "\\nEnter a hostname to test (e.g. example.com): "
    ).strip()

    if hostname:
        check_dns(hostname)
        check_ping(hostname)
    else:
        print("No hostname entered.")

if __name__ == "__main__":
    main()
