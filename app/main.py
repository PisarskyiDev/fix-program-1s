from os import popen


def close_program() -> None:
    popen("taskkill /IM 1cv8s.exe /F")
    give_command()

def give_command() -> None:
    command_local = "cd AppData\Local\\1C\\1cv8"
    command_roaming = "cd AppData\Roaming\\1C\\1cv8"
    for command in [command_roaming, command_roaming]:
        result = popen(command)
        for line in result.readlines():
            print(line)
            # if "." not in line[-12:]:


if __name__ == '__main__':
    close_program()
