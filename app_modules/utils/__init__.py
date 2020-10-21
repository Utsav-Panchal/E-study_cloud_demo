def app_urlname(value, arg, user=None):
    """Given model opts (model._meta) and a url name, return a named pattern.
    URLs should be named as: customadmin:app_label:model_name-list"""

    pattern = "%s:%s-%s" % (value.app_label, value.model_name, arg)
    return pattern