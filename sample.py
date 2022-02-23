from ast import arguments
from dataclasses import dataclass
from itertools import combinations
import shlex
from typing import List


def run_command(command: str) -> None:
  match command:
    case "quit":
      print("Quitting the program")
    case "reset":
        print("Resetting the system")
    case other:
        print(f"Unknown command: {other!r}")

def run_command2(command: str):
  match command.split():
      case ["load", filename]:
          print(f"Loading file: {filename}.")
      case ["save", filename]:
          print(f"Saving to file: {filename}.")
      case ["quit" | "exit" | "bye"]: #exata palavra
          print("Quitting the program1")
      case ["tchau" | "sair" | "fim", *rest]: #quanlquer coisa que comece com essas palabras
          if 'brasil' in rest or 'br' in rest:
            print('Fechando o brasil')
          else:
              print("Quitting the program2")
      case ["aqui" | "ali" | "aca", '--force']: #comece com qualquer um dessas palabras e depois venha --force
          print("Quitting the program3")
      case _:
        print(f"Unknown command: {command!r}")

def run_command3(command: str):
  match command.split():
      case ["load", filename]:
          print(f"Loading file: {filename}.")
      case ["save", filename]:
          print(f"Saving to file: {filename}.")
      case ["quit" | "exit" | "bye"]: #exata palavra
          print("Quitting the program1")
      case ["tchau" | "sair" | "fim", *rest] if 'brasil' in rest or 'br' in rest: #quanlquer coisa que comece com essas palabras
            print('Fechando o brasil')
      case ["tchau" | "sair" | "fim", *rest]:
              print("Quitting the program2")
      case ["aqui" | "ali" | "aca", '--force']: #comece com qualquer um dessas palabras e depois venha --force
          print("Quitting the program3")
      case _:
        print(f"Unknown command: {command!r}")

@dataclass
class Command:
    command: str
    arguments: List[str]

def run_command4(command: Command):
  match command:
      case Command(command ="load", arguments=[filename]):
          print(f"Loading file: {filename}.")
      case Command(command ="save", arguments=[filename]):
          print(f"Saving to file: {filename}.")
      case Command(command = "quit" | "exit" | "bye" ): #exata palavra
          print("Quitting the program1")
      case Command(command = "tchau" | "sair" | "fim", arguments=["brasil" | "br", *rest] ): #quanlquer coisa que comece com essas palabras
          print('Fechando o brasil')
      case Command(command = "tchau" | "sair" | "fim") :
              print("Quitting the program2")
      case Command(command = "aqui" | "ali" | "aca", arguments=['--force', *rest]): #comece com qualquer um dessas palabras e depois venha --force
          print("Quitting the program3")
      case _:
        print(f"Unknown command: {command!r}")
def main()-> None:
  while True:
    #command = input("$")
    #run_command2(command)
    command, *arguments = shlex.split(input("$ "))
    run_command4(Command(command, arguments))
  
if __name__ == "__main__":
  main()

    #var = 'abcde'
    #print(f"frase: {var!r}")
    #->frase: 'abcde'