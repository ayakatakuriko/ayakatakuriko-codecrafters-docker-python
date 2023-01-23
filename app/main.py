import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]
    output_f = sys.stdout
    exit_s = 0
    
    if args[0] == "echo_stderr":
        args[0] = "echo"
        output_f = sys.stderr
    elif args[0] == "exit":
        exit_s = int(args[1])
        
    completed_process = subprocess.run([command, *args], capture_output=True)
    
    print(completed_process.stdout.decode("utf-8").strip(), file=output_f)
    exit(exit_s) 


if __name__ == "__main__":
    main()
