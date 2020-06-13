def normalize(value, min, max):
    normalized = (value - min) / (max - min)
    return normalized


def denormalize(normalized, min, max):
    denormalized = (normalized * (max - min) + min)
    return denormalized

def normalize_function_paper(value,
                             min_time_window,
                             max_time_window,
                             min_template,
                             max_template):
    return min_template +((value-min_time_window)* (max_template - min_template)/(max_time_window-min_time_window))