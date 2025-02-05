from subprocess import check_output

def call_return(command: str, *args: list[str]):
    return check_output(f"{command}, {str.join(" ", list(args))}").decode()

def call(command: str, *args: list[str]):
    check_output(f"{command}, {str.join(args, " ")}")