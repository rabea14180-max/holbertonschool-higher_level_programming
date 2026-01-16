#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util

    file_path = "/tmp/hidden_4.pyc"

    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)

    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
