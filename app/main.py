import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]
    output = sys.stdout
    
    if args[0] == "echo_stderr":
        args[0] = "echo"
        output = sys.stderr
    completed_process = subprocess.run([command, *args], capture_output=True)
    
    print(completed_process.stdout.decode("utf-8"), file=output)
    


if __name__ == "__main__":
    main()
