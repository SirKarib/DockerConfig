import os

LOG_PATH = os.getenv("LOG_PATH", "../var/log/web-server/register.log")


def print_logs():
    with open(LOG_PATH, "r") as file:
        for line in file:
            print(line.strip())
    file.close()


if __name__ == "__main__":
    print_logs()
