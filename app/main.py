import os

from sys import exit
from time import sleep


def take_right_name(bad_name: str) -> (None, str):
    right_name = ""
    for right_letter in bad_name:
        if "\n" in right_letter:
            break
        right_name += right_letter
    return right_name


def close_program() -> None:
    try:
        os.popen("taskkill /IM 1cv8.exe /F")
        give_command()
    except Exception:
        print("Возникла ошибка, процесс не был найден. Обратитесь к администратору")
        sleep(20)
        exit()


def give_command() -> None:
    check_user_name = os.popen("echo %userName%")
    read_user_name = check_user_name.readlines()
    right_user_name = take_right_name(read_user_name[0])
    command_local = os.path.join(f"C:", "Users", right_user_name, "AppData", "Local", "1C", "1cv8")
    command_roaming = os.path.join(f"C:", "Users", right_user_name, "AppData", "Roaming", "1C", "1cv8")

    try:
        for command in [command_local, command_roaming]:
            # result = os.popen(command)
            temp = os.listdir(command)
            print(temp)


    except Exception:
        print("Возникла ошибка, процесс не был найден. Обратитесь к администратору")
        sleep(20)
        exit()


if __name__ == '__main__':
    close_program()
