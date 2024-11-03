import subprocess
import os

def decrypt_file(file_name, password):
    # Command equivalent to the bash script openssl command
    command = [
        "openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-iter", "100000", 
        "-salt", "-in", file_name, "-k", password
    ]
    
    try:
        # Run the command and capture the output
        result = subprocess.run(command, check=True, capture_output=True)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode()}"

if __name__ == "__main__":
    # Replace 'enc' with your actual file name if different
    file_name = '451fd69b'
    password = 'picoCTF'

    if os.path.isfile(file_name):
        decrypted_content = decrypt_file(file_name, password)
        print(decrypted_content)
    else:
        print(f"Error: '{file_name}' is not a valid file.")
