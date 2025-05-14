from __future__ import annotations


from .humanoid_target_move_env_cfg import HumanoidTargetMoveEnvCfg
from humanoid_target_move.locomotion.locomotion_env import LocomotionEnv




class HumanoidTargetMoveEnv(LocomotionEnv):
    cfg: HumanoidTargetMoveEnvCfg
    def __init__(self, cfg: HumanoidTargetMoveEnvCfg, render_mode: str | None = None, **kwargs):
        super().__init__(cfg, render_mode, **kwargs)