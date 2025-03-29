g_current_task = ""
g_config = None


def gl_init():
    ...


def gl_set(k, v):
    globals()[k] = v


def gl_get(k, d=None):
    try:
        return globals()[k]
    except KeyError:
        return d

    return None