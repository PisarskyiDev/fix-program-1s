import os
import shutil

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
    os.popen("taskkill /IM 1cv8.exe /F")
    os.popen("taskkill /IM 1cv8s.exe /F")
    give_command()
    exit()


def give_command() -> None:
    check_name = os.popen("echo %userName%")
    read_name = check_name.readlines()
    right_name = take_right_name(read_name[0])
    cmd_local = os.path.join(f"C:", "\\", "Users", right_name, "AppData", "Local", "1C", "1cv8")
    cmd_roaming = os.path.join(f"C:", "\\", "Users", right_name, "AppData", "Roaming", "1C", "1cv8")
    try:
        for command in [cmd_local, cmd_roaming]:
            os.chdir(path="C:\\")
            os.chdir(path=command)

            for file in os.scandir():
                name = file.name
                if file.is_file():
                    continue
                else:
                    shutil.rmtree(command + "\\" + name)
        sleep(5)
    except OSError:
        print("\n")
        print("Возникла ошибка, обратитесь к администратору")
        sleep(5)
        exit()


if __name__ == '__main__':
    print("Запущенно исправление 1С")
    close_program()
