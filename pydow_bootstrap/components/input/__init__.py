from pydow import Component
from blinker import signal


class BootstrapInput(Component):

    def __init__(self: object, *args, **kwargs) -> None:
        super(BootstrapInput, self).__init__(template_location=__file__, *args, **kwargs)

        # Specify signals
        self.signal_on_click = signal(f"ON_CLICK_{self.identifier}")
        self.signal_on_change = signal(f"ON_CHANGE_{self.identifier}")

        self.bindings = {
            "value": ""
        }

        # Create the onClick behaviour
        if hasattr(self, "onClick"):
            on_click_method = self.onClick
            if on_click_method is not None:
                self.signal_on_click.connect(on_click_method, weak=False)

        # Store the content of the field
        self.signal_on_change.connect(self.onChange, weak=False)

    def onChange(self: object, event: dict):
        session_id = event.get("session_id")
        self.store.setState(f"INPUT_{self.identifier}_{session_id}", event.get("value", ""))

    def setValue(self: object, new_value: str, session_id: str):
        self.store.setState(f"INPUT_{self.identifier}_{session_id}", new_value)

    def getValue(self: object, session_id: str, default=""):
        return self.store.getState(f"INPUT_{self.identifier}_{session_id}", default)

    def update(self: object, session_id: str, *args, **kwargs) -> None:
        self.bindings["value"] = self.store.getState(f"INPUT_{self.identifier}_{session_id}", "")
