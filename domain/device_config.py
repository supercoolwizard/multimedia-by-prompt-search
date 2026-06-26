from dataclasses import dataclass
import torch

@dataclass
class DeviceConfig:
    device: str
    dtype: torch.dtype

