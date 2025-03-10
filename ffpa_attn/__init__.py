from .interface import (
    faster_prefill_attn_func,
    ffpa,
    ffpa_acc_f16_L1,
    ffpa_acc_f32_L1,
    ffpa_mma_acc_f16_L1,
    ffpa_mma_acc_f32_L1,
    LevelType,
    MMAAccType,
)
from .version import __version__


# e.g pyffpa.L1
L1 = LevelType.L1
L2 = LevelType.L2
L3 = LevelType.L3
# e.g pyffpa.FP32
FP32 = MMAAccType.FP32
FP16 = MMAAccType.FP16
