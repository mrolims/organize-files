import argparse
from .organizer import Directoryorganizer


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean and sort directory files.")
    parser.add_argument('directory', nargs='?', default=None,
                        help='Directory to clean (default: current directory)')
    args = parser.parse_args()

    organizer = Directoryorganizer(args.directory)
    organizer.create_folders()
    organizer.move_files()
    print(f"Sorted files in {organizer.directory}")


if __name__ == '__main__':
    main()
