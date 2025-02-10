import subprocess

def callfunc(n):
    print(f"process {n} finished!")

if __name__ == "__main__":
    lines = []
    for i in range(5, 1):
        lines.append(subprocess.Popen(f"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe sleep {i}", shell=True))
    for i, item in enumerate(lines):
        item.wait(callfunc(i))