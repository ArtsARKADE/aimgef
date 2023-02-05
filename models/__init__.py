from .transformer import Transformer
from .vae import VAE

CSQ_TIME_QUANTIZATION = [
    1 / 32, 1 / 16, 1 / 12, 1 / 8, 1 / 6, 3 / 16,
    1 / 4, 1 / 3, 3 / 8, 1 / 2, 2 / 3, 3 / 4, 1
]

CPI_TIME_QUANTIZATION = [(t / 100) for t in range(1, 101)]

CSQ_START_DISTRIBUTION = [
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00024224806,
    0.00024224806, 0.00024224806, 0.00048449612, 0.0007267442, 0.0012112403, 0.0012112403,
    0.0016957364, 0.0019379845, 0.0024224806, 0.003633721, 0.004118217, 0.0058139535, 0.00629845,
    0.0067829457, 0.007025194, 0.007751938, 0.009689922, 0.010416667, 0.013081395, 0.013323643,
    0.01501938, 0.017199613, 0.019137597, 0.019137597, 0.020833334, 0.026405038, 0.027858527,
    0.030281007, 0.033430234, 0.034399226, 0.034883723, 0.035610463, 0.038032945, 0.037790697,
    0.037790697, 0.039244186, 0.03754845, 0.03585271, 0.034641474, 0.033430234, 0.029554263,
    0.029796511, 0.028343024, 0.02761628, 0.02374031, 0.021075582, 0.019137597, 0.016472869,
    0.016472869, 0.013323643, 0.0125969, 0.010658915, 0.008963178, 0.007267442, 0.0053294576,
    0.004844961, 0.004118217, 0.003633721, 0.003149225, 0.0024224806, 0.0019379845, 0.0007267442,
    0.0007267442, 0.00048449612, 0.00048449612, 0.00024224806, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0
]

CPI_START_DISTRIBUTION = [
    0.0013410404624277456, 0.0019421965317919076, 0.0024508670520231213, 0.003144508670520231,
    0.004439306358381503, 0.005734104046242775, 0.011930635838150289, 0.016138728323699423,
    0.02423121387283237, 0.03408092485549133, 0.04171098265895954, 0.050589595375722544, 0.059838150289017344,
    0.06113294797687861, 0.0691329479768786, 0.07213872832369943, 0.07764161849710982, 0.07796531791907514,
    0.07986127167630058, 0.07773410404624277, 0.06363005780346821, 0.0524393063583815, 0.04240462427745665,
    0.029919075144508672, 0.021040462427745665, 0.010589595375722544, 0.004763005780346821,
    0.0013410404624277456, 0.0005086705202312139, 0.00018497109826589596, 0.0, 0.0
]
