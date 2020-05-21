def normalize(value, min, max):
    normalized = (value - min) / (max - min)
    return normalized


def denormalize(normalized, min, max):
    denormalized = (normalized * (max - min) + min)
    return denormalized
