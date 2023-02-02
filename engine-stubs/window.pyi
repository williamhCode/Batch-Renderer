from engine.render import Renderer
from engine.surface import Surface
from engine.event import Event
from ._common import Vec2

class Window:

    def __init__(self, size: Vec2, window_name: str, vsync: bool = False, high_dpi: bool = True) -> None: ...

    def get_size(self) -> tuple[int, int]: ...

    def create_renderer(self) -> Renderer: ...

    def create_surface(self, size: Vec2, resize_nearest: bool = False, high_dpi: bool | None = None) -> Surface: ...

    def set_title(self, title: str) -> None: ...

    def get_title(self) -> str: ...

    def close(self) -> None: ...

    def should_close(self) -> bool: ...

    def get_events(self) -> list[Event]: ...

    def get_key(self, key: int) -> int: ...

    def get_mouse_button(self, button: int) -> int: ...

    def update(self) -> None: ...

    def quit(self) -> None: ...