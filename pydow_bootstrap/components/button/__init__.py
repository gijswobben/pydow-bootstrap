from pydow import Component


class BootstrapButton(Component):

    def __init__(self, *args, **kwargs):
        super(BootstrapButton, self).__init__(template_location=__file__, *args, **kwargs)

        size = kwargs.get("size", "")
        if size == "small":
            size = "btn-sm"
        if size == "large":
            size = "btn-lg"

        self.bindings = {
            "content": self.content if hasattr(self, "content") else "",
            "mode": kwargs.get("mode", "primary"),
            "size": size
        }

        # Create the onClick behaviour
        if hasattr(self, "onClick"):
            on_click_method = self.onClick
            if on_click_method is not None:
                self.dispatcher.addEventListener(f"ON_CLICK_{self.identifier}", on_click_method)
