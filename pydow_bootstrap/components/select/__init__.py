from pydow.components import Select


class BootstrapSelect(Select):
    def __init__(self, *args, **kwargs):
        super(BootstrapSelect, self).__init__(template_location=__file__, *args, **kwargs)
