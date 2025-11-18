import os
from pathlib import Path

from . import TerminalProvider as _TProv

try:
    import yaml
except ImportError:
    yaml = None


class ContourProvider(_TProv):
    """Adapter for Contour Terminal emulator."""

    __CONFIG_PATH = Path.home() / ".config" / "contour" / "contour.yml"

    def is_compatible() -> bool:
        """Check if Contour Terminal is installed and configured."""
        if yaml is None:
            return False
        # Check if config file exists
        return ContourProvider.__CONFIG_PATH.exists()

    def change_terminal(path: str):
        """Set the background image in Contour Terminal config."""
        if yaml is None:
            print("PyYAML is required to configure Contour Terminal.")
            print("Install it with: pip install pyyaml")
            return

        try:
            config_path = ContourProvider.__CONFIG_PATH

            # Read the config file
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            if config is None:
                config = {}

            # Ensure color_schemes exists
            if 'color_schemes' not in config:
                config['color_schemes'] = {}

            # Ensure default color scheme exists
            if 'default' not in config['color_schemes']:
                config['color_schemes']['default'] = {}

            # Set the background image
            if 'background_image' not in config['color_schemes']['default']:
                config['color_schemes']['default']['background_image'] = {}

            config['color_schemes']['default']['background_image']['path'] = path

            # Write back the config file
            with open(config_path, 'w') as f:
                yaml.safe_dump(config, f, default_flow_style=False)

        except Exception as e:
            print(f"Failed to set Contour Terminal background: {e}")

    def clear():
        """Clear the background image from Contour Terminal config."""
        if yaml is None:
            print("PyYAML is required to configure Contour Terminal.")
            return

        try:
            config_path = ContourProvider.__CONFIG_PATH

            # Read the config file
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            if config is None:
                return

            # Remove the background image path if it exists
            if ('color_schemes' in config and
                'default' in config['color_schemes'] and
                'background_image' in config['color_schemes']['default']):
                del config['color_schemes']['default']['background_image']['path']

            # Write back the config file
            with open(config_path, 'w') as f:
                yaml.safe_dump(config, f, default_flow_style=False)

        except Exception as e:
            print(f"Failed to clear Contour Terminal background: {e}")

    def __str__():
        return "Contour"
