from .organizer import DirectoryCleaner


def cli() -> None:

    organizer = DirectoryCleaner()
    organizer.create_folders()
    organizer.move_files()
    print(f"Sorted files in {organizer.directory}")


if __name__ == "__main__":
    cli()
