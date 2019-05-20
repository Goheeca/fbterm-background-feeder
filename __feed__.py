import cairo
import math
from PIL import Image

if __package__ == '':
    from util.drawing import Drawer, SubContext
else:
    from .util.drawing import Drawer, SubContext

FULL_ANGLE = 2 * math.pi


class DemoDrawer(Drawer):
    def _setup(self, ctx, w, h, _):
        self.i = 0
        self.time = 0
        self.COLORS = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
        ]

    def _draw(self, ctx, w, h, f, t):
        ctx.set_source_rgb(0, 0, 0)
        ctx.paint()
        color = self.COLORS[self.i]
        if f % 100 == 0:
            self.i = (self.i + 1) % len(self.COLORS)
        ctx.set_source_rgb(*color)
        omega = 1 * FULL_ANGLE
        amplitude = w/8 if w/8 < h/8 else h/8
        angle = omega * t % FULL_ANGLE
        position = w/2 + amplitude * math.cos(angle), h/2 + amplitude * math.sin(angle)
        ctx.arc(position[0], position[1], 200, 0, FULL_ANGLE)
        ctx.fill()
        #print(f'Color: {color}, Angle: {angle/FULL_ANGLE*360:06.2f}, Position: {position}')
        return 0.01

    def _last(self, ctx, w, h, f, t):
        ctx.set_source_rgb(0, 0, 0)
        ctx.paint()


__drawer__ = DemoDrawer
