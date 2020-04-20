from pathlib import Path


def resource_path(target_file: str):
    return Path(Path(__file__).parent,
                f"../../resources/algorithms_fourth_edition/{target_file}")