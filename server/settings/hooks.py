from ayon_server.settings import BaseSettingsModel, SettingsField


class InstallOpenTimelineIOToFlameModel(BaseSettingsModel):
    enabled: bool = SettingsField(
        default=True,
        title="Enable"
    )


class FlameHooksModel(BaseSettingsModel):
    InstallOpenTimelineIOToFlame: InstallOpenTimelineIOToFlameModel = \
        SettingsField(
            default_factory=InstallOpenTimelineIOToFlameModel,
            title="Install OpenTimelineIO to Flame"
        )
    project_setup: bool = SettingsField(
        default=True,
        title="Automated Project setup",
        description=(
            "Create and setup a Flame project matching AYON project."
        ),
    )


DEFAULT_HOOKS_SETTINGS = {
    "InstallOpenTimelineIOToFlame": {"enabled": True},
    "project_setup": True,
}
