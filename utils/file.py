from pathlib import Path


def abs_path_from_project(relative_path: str):
    return (
        Path()
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
