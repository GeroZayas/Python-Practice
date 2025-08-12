import inspect
import importlib.util


def extract_symbols_with_inspect(filepath):
    module_name = "temp_module_for_inspection"
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if not spec or not spec.loader:
        print(f"Could not load spec for {filepath}")
        return None

    module = importlib.util.module_from_spec(spec)
    # Add to sys.modules temporarily if needed for relative imports within the module
    # sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Could not execute module {filepath}: {e}")
        # Clean up if needed: del sys.modules[module_name]
        return None

    symbols = {"classes": [], "functions": [], "methods": {}}

    for name, obj in inspect.getmembers(module):
        # Check if the member was defined *in this module*
        # to avoid imported symbols
        if inspect.getmodule(obj) == module:
            if inspect.isclass(obj):
                symbols["classes"].append(name)
                symbols["methods"][name] = []
                # Get methods defined within this class
                for method_name, method_obj in inspect.getmembers(obj):
                    # Check if it's a function/method defined in this class's module
                    if (
                        inspect.isfunction(method_obj)
                        and inspect.getmodule(method_obj) == module
                    ):
                        # Further check if it's actually part of this class might be needed
                        # depending on inheritance etc. This is a basic check.
                        symbols["methods"][name].append(method_name)
            elif inspect.isfunction(obj):
                symbols["functions"].append(name)

    # Clean up: remove module from sys.modules if added
    # if module_name in sys.modules:
    #    del sys.modules[module_name]

    return symbols


# Example usage:
file_symbols = extract_symbols_with_inspect("rich")
