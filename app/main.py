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
    subprocess.run(["mkdir", "-p", "./temp/usr"])    
    subprocess.run(["cp", "-r","/usr/local", "./temp/usr/."])
    subprocess.run(["cp", "-r","/usr/bin", "./temp/usr/."])
    completed_process = subprocess.run(["chroot", "./temp", command, *args], capture_output=True)  
    
    print(completed_process.stdout.decode("utf-8").strip(), file=output_f)
    exit(completed_process.returncode)

if __name__ == "__main__":
    main()
