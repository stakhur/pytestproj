import os
import json
import shutil
import sys

from subprocess import PIPE, run


GAME_DIR_PATTERN = "game"


def find_all_game_paths(source):
    game_paths = []

    for _, dirs, _ in os.walk(source): # root, dirs, files
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break # we need to look only in top level structure

    return game_paths


def create_dir_or_remove_context(path):
    if not os.path.exists(path):
        os.mkdir(path)
    elif "twt_21_advanced" in path: # for the security reason
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(os.path.join(root, file))

            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
    else:
        print("Skip removing structure.")


def copy_and_rename(game_paths, target):
    new_game_paths = []
    for path in game_paths:
        dir_name = os.path.basename(path)
        dir_name = dir_name.replace("_" + GAME_DIR_PATTERN, "")
        new_path = os.path.join(target, dir_name)
        shutil.copytree(path, new_path)
        new_game_paths.append(new_path)

    return new_game_paths


def compile_code(game_paths):
    for path in game_paths:
        game = os.path.basename(path)
        os.chdir(path)
        for root, _, files in os.walk(path):
            for file in files:
                result = run(
                    ["go", "build", "-o", game, os.path.join(root, file)],
                    stdout=PIPE,
                    stderr=PIPE,
                    text=True
                )
                if result.returncode != 0:
                    print("Compilation failed!", result.stderr)
                else:
                    game_path = os.path.join(root, game)
                    run_result = run(
                        [game_path],
                        stdout=PIPE,
                        stderr=PIPE,
                        text=True
                    )

                    print("Program output:")
                    print(run_result.stdout)

                    if run_result.stderr:
                        print("Program errors:")
                        print(run_result.stderr)



def main(source, target):
    cwd = os.getcwd() # current working directory
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    create_dir_or_remove_context(target_path)
    game_paths = copy_and_rename(game_paths, target_path)
    compile_code(game_paths)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")

    source, target = args[1:]

    main(source, target)