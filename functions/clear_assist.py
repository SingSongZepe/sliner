import typing

if typing.TYPE_CHECKING:
    from sline import SLINE

def clear_assist(self: 'SLINE'):
    for item in self.assist_graphics_item.all():
        self.gv_graphics.scene().removeItem(item)
        self.assist_graphics_item.cls()
