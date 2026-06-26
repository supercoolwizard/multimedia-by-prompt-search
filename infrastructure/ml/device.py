import torch

from domain.device_config import DeviceConfig

def get_device_config():
    if torch.cuda.is_available():
        return DeviceConfig(
            device="cuda",
            dtype=torch.float16,
        )

    if torch.backends.mps.is_available():
        return DeviceConfig(
            device="mps",
            dtype=torch.float16,
        )

    return DeviceConfig(
        device="cpu",
        dtype=torch.float32,
    )

