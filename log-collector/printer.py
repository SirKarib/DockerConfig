import datetime


def print_logs():
    dt_info = datetime.datetime.today().strftime("%A, %d %B %Y, %H:%M:%S")
    request_text = "hello"
    log = dt_info + ' - ' + request_text
    with open("logs.txt", "a") as file:
        file.write(log + '\n')
    file.close()


if __name__ == "__main__":
    print_logs()
