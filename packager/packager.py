from archive import Archive
from file import Copy, Move
from npm import Compile, Doc
from shell import Shell
import yaml
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def read_yaml(yaml_file):
    with open(yaml_file, 'r') as stream:
        commands = yaml.load(stream)
    if not commands.has_key('commands'):
        raise Exception('Invalid commands file, commands tag must be provided and be a list')
    return commands['commands']

def get_commands_from_file(yaml_file):
    commands = read_yaml(yaml_file)
    cmds = []
    for command in commands:
        if command.get('archive') != None:
            cmds.append(Archive(command.get('archive')))
        elif command.get('compile') != None:
            cmds.append(Compile(command.get('compile')))
        elif command.get('copy') != None:
            cmds.append(Copy(command.get('copy')))
        elif command.get('doc') != None:
            cmds.append(Doc(command.get('doc')))
        elif command.get('move') != None:
            cmds.append(Move(command.get('move')))
        elif command.get('shell') != None:
            cmds.append(Shell(command.get('shell')))
    return cmds

def package(cmds):
    for command in cmds:
        command.do()

def parse_arguments():
    parser = argparse.ArgumentParser(description='create a software package')
    parser.add_argument('-c', '--config', help='use a different config file than the default package.yaml')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.config:
        config_file = args.config
    else:
        config_file = 'package.yaml'
    logging.info('config file is: ' + config_file)
    package(get_commands_from_file(config_file))
