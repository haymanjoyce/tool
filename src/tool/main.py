#main.py

#!/usr/bin/python3

# import commands
#
# if __name__ == '__main__':
#     commands.main()

# python main.py test arg

# /Users/richard/PycharmProjects/mt_1.0/src/tool/main.py



import click


@click.command()
def main():
    print("I'm a beautiful CLI ✨")

if __name__ == "__main__":
    main()
