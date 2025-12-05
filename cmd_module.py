import cmd
import shlex
import argparse
import time
import sys


# Color codes for a pretty prompt
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    ENDC = "\033[0m"


class DevOpsShell(cmd.Cmd):
    intro = f"{Colors.HEADER}Welcome to the DevOps Commander. Type help or ? to list commands.\n{Colors.ENDC}"
    prompt = f"{Colors.BLUE}(commander){Colors.ENDC} "

    # Fake database of servers for tab-completion
    servers = ["app-server-01", "app-server-02", "db-primary", "db-replica", "cache-01"]

    def __init__(self):
        super().__init__()
        # Initialize an argument parser for the 'deploy' command
        self.deploy_parser = argparse.ArgumentParser(
            description="Deploy artifacts",
            prog="deploy",
            exit_on_error=False,  # Prevent argparse from exiting the whole shell on error
        )
        self.deploy_parser.add_argument("server", help="Target server name")
        self.deploy_parser.add_argument(
            "--version", "-v", default="latest", help="Version to deploy"
        )
        self.deploy_parser.add_argument(
            "--force", "-f", action="store_true", help="Force deployment"
        )

    def precmd(self, line):
        """Hook method executed just before the command line is interpreted."""
        self._start_time = time.time()
        # You could modify 'line' here before it runs (e.g., lowercasing everything)
        return line

    def postcmd(self, stop, line):
        """Hook method executed just after a command dispatch is finished."""
        elapsed = time.time() - self._start_time
        if elapsed > 0.1:  # Only show timing for slow commands
            print(f"{Colors.GREEN}[Command took {elapsed:.2f}s]{Colors.ENDC}")
        return stop

    def do_deploy(self, arg):
        """
        Deploy an application to a server.
        Usage: deploy <server_name> [-v VERSION] [-f]
        """
        try:
            # 1. Split the raw argument string intelligently (handles quotes)
            parsed_args = shlex.split(arg)

            # 2. Parse using argparse
            # We catch SystemExit because argparse tries to exit() on --help or errors
            try:
                args = self.deploy_parser.parse_args(parsed_args)
            except SystemExit:
                return  # Parser printed help/error, return to prompt
            except argparse.ArgumentError as e:
                print(f"Error: {e}")
                return

            # 3. Execution Logic
            print(f"🚀 Deploying version {args.version} to {args.server}...")
            if args.force:
                print("   (Force flag detected: Bypassing safety checks)")

            # Simulate work
            time.sleep(1.5)
            print("✅ Deployment successful.")

        except ValueError as e:
            print(f"Parsing Error: {e}")

    def complete_deploy(self, text, line, begidx, endidx):
        """
        Auto-complete server names for the deploy command.
        """
        if not text:
            completions = self.servers[:]
        else:
            completions = [s for s in self.servers if s.startswith(text)]
        return completions

    def do_shell(self, arg):
        """Run a system command. Example: !ls -la"""
        import os

        os.system(arg)

    def do_exit(self, arg):
        """Exit the application."""
        print("Goodbye!")
        return True  # Returning True breaks the cmdloop


if __name__ == "__main__":
    try:
        DevOpsShell().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")
