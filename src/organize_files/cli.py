import argparse
from .organize_files import DirectoryCleaner


def cli() -> None:
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by moving them into categorized folders."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Target directory to organize (default: current directory).",
    )

    args = parser.parse_args()
    organizer = DirectoryCleaner(directory=args.directory)
    organizer.create_folders()
    organizer.move_files()
    print(f"Sorted files in {organizer.directory}")


if __name__ == "__main__":
    cli()
