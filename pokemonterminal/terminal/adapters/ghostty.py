import os
from pathlib import Path
from subprocess import run

from . import TerminalProvider as _TProv


class GhosttyProvider(_TProv):
    CONFIG_PATH = Path.home() / ".config" / "ghostty" / "config"
    SETTING_KEY = "background-image"
    FIT_KEY = "background-image-fit"
    OPACITY_KEY = "background-opacity"

    @staticmethod
    def is_compatible() -> bool:
        return os.environ.get("GHOSTTY_RESOURCES_DIR") is not None

    @staticmethod
    def change_terminal(path: str):
        config = GhosttyProvider._ensure_config()
        GhosttyProvider._set_setting(config, GhosttyProvider.SETTING_KEY, path)
        GhosttyProvider._set_setting(config, GhosttyProvider.FIT_KEY, "cover")
        GhosttyProvider._set_setting(config, GhosttyProvider.OPACITY_KEY, "1")
        GhosttyProvider._save_config(config)
        GhosttyProvider._reload()

    @staticmethod
    def clear():
        config = GhosttyProvider._ensure_config()
        GhosttyProvider._remove_setting(config, GhosttyProvider.SETTING_KEY)
        GhosttyProvider._remove_setting(config, GhosttyProvider.FIT_KEY)
        GhosttyProvider._remove_setting(config, GhosttyProvider.OPACITY_KEY)
        GhosttyProvider._save_config(config)
        GhosttyProvider._reload()

    @staticmethod
    def _ensure_config() -> list[str]:
        config = GhosttyProvider.CONFIG_PATH
        config.parent.mkdir(parents=True, exist_ok=True)
        if not config.exists():
            config.touch()
        return config.read_text().splitlines()

    @staticmethod
    def _set_setting(lines: list, key: str, value: str):
        new_line = f"{key} = {value}"
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith(key) and "=" in line:
                lines[i] = new_line
                return
        lines.append(new_line)

    @staticmethod
    def _remove_setting(lines: list, key: str):
        lines[:] = [l for l in lines if not l.strip().startswith(f"{key}=")]

    @staticmethod
    def _save_config(lines: list):
        GhosttyProvider.CONFIG_PATH.write_text("\n".join(lines) + "\n")

    @staticmethod
    def _reload():
        run(["killall", "-SIGUSR2", "ghostty"], check=False)

    def __str__(self):
        return "Ghostty"
