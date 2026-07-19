"""Configuration and constants for KING AI Checker."""

import json
import os


class Config:
    def __init__(self, config_path=None):
        self.config_path = config_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "config.json"
        )
        self._data = self._load()

    def _load(self):
        defaults = {
            "min_workout_duration_seconds": 300,
            "xp_per_verified_minute": 10,
            "xp_bonus_completion": 50,
            "data_dir": "data",
            "video_processing_fps": 15,
            "movement_confidence_threshold": 0.4,
            "form_points_to_detect": 17,
            "missed_workout_grace_days": 1,
            "leaderboard_size": 50
        }
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                defaults.update(user_config)
        return defaults

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"Config has no attribute '{name}'")
