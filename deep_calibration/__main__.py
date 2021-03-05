from argparse import ArgumentParser
from collections import OrderedDict

from deep_calibration.scripts import train
 

COMMANDS = OrderedDict(
    [
        ("train", train),
        # ("test", 'run'),
    ]
)

def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description = "training calibration for UR10 arm"
    )

    all_commands = ", \n".join(map(lambda x: f"    {x}", COMMANDS.keys()))
    subparsers = parser.add_subparsers(
        metavar="{command}",
        dest="command",
        help=f"available commands: \n{all_commands}",
    )
    subparsers.required = True
    
    for key, value in COMMANDS.items():
        value.build_args(subparsers.add_parser(key))

    return parser


def main():
    parser = build_parser()
    args, uargs = parser.parse_known_args()
    COMMANDS[args.command].main(args, uargs)


if __name__ == "__main__":
    main()