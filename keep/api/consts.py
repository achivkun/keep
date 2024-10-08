import os

from keep.api.models.db.preset import PresetDto, StaticPresetsId

RUNNING_IN_CLOUD_RUN = os.environ.get("K_SERVICE") is not None
PROVIDER_PULL_INTERVAL_DAYS = int(
    os.environ.get("KEEP_PULL_INTERVAL", 7)
)  # maximum once a week
STATIC_PRESETS = {
    "feed": PresetDto(
        id=StaticPresetsId.FEED_PRESET_ID.value,
        name="feed",
        options=[
            {"label": "CEL", "value": "(!deleted && !dismissed)"},
            {
                "label": "SQL",
                "value": {"sql": "(deleted=false AND dismissed=false)", "params": {}},
            },
        ],
        created_by=None,
        is_private=False,
        is_noisy=False,
        should_do_noise_now=False,
        static=True,
        tags=[],
    ),
    "groups": PresetDto(
        id=StaticPresetsId.GROUPS_PRESET_ID.value,
        name="groups",
        options=[
            {"label": "CEL", "value": "group"},
            {"label": "SQL", "value": {"sql": '"group"=true', "params": {}}},
        ],
        created_by=None,
        is_private=False,
        is_noisy=False,
        should_do_noise_now=False,
        static=True,
        tags=[],
    ),
    "dismissed": PresetDto(
        id=StaticPresetsId.DISMISSED_PRESET_ID.value,
        name="dismissed",
        options=[
            {"label": "CEL", "value": "dismissed"},
            {"label": "SQL", "value": {"sql": "dismissed=true", "params": {}}},
        ],
        created_by=None,
        is_private=False,
        is_noisy=False,
        should_do_noise_now=False,
        static=True,
        tags=[],
    ),
}
