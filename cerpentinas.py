from manim import *
class Bullet(Square):
    CONFIG = {
        'fill_opacity': 1,
        'stroke_width': 0,
        'start_angle': PI,
        'length': DEFAULT_ARROW_TIP_LENGTH,
        'aspect': 1.5,
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_height(self.CONFIG['length'])
        self.stretch_to_fit_height(.8)
        # self.points[5:7]+=np.array([self.CONFIG['length'],0,0])
        self.scale(0.5)
    def get_angle(self):
        return angle_of_vector(self.get_vector())
    def get_vector(self):
        return self.point_from_proportion(.5) - self.get_start()
class TestBullet(Scene):
    CONFIG={
        'an':.1
    }
    def construct(self):
        bullet=Bullet()
        def update(bullet,dt):
            rot=0
            rot+=self.CONFIG['an']*dt
            bullet.rotate(self.CONFIG['an']+rot)
            bullet.shift(np.array([self.CONFIG['an']*10*dt,0,0]))
        bullet.add_updater(update)
        self.add(bullet)
        self.wait(2)