from manim import *

class Bullet(Triangle):
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 0,
        "length": DEFAULT_ARROW_TIP_LENGTH,
        "start_angle": PI,
        "aspect": 1.5,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stretch_to_fit_height(self.CONFIG['length'])
        self.stretch_to_fit_width(self.CONFIG['length'] * self.CONFIG['aspect'])
        self.points[5:7] += np.array([self.CONFIG['length'], 0, 0])
        self.scale(0.5)

    def get_angle(self):
        return angle_of_vector(self.get_vector())

    def get_vector(self):
        return self.point_from_proportion(0.5) - self.get_start()

class TestBullet(Scene):
    CONFIG2={
        'time':10
    }
    def construct(self):
        vqueue1 = VGroup()
        vqueue2 = VGroup()
        vqueue3 = VGroup()
        self.an = 0
        
        def update_bullet1(obj, dt):
            bullet1 = Bullet().scale(0.7).rotate(self.CONFIG2['time'] * 10 + self.an * 10)
            texto1=self.getting_tex(bullet1)
            bullet1.add(texto1)
            obj.add(bullet1)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(np.linalg.norm(k.get_center() - ORIGIN)) > 7:
                    obj.remove(k)
            self.an += 1 * DEGREES

        def update_bullet2(obj, dt):
            bullet2 = Bullet().scale(0.7).rotate(self.CONFIG2['time'] * 10 + self.an * 10)
            texto2=self.getting_tex(bullet2)
            bullet2.add(texto2)
            obj.add(bullet2)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(np.linalg.norm(k.get_center() - ORIGIN)) > 7:
                    obj.remove(k)
            self.an += 1 * DEGREES
        def update_bullet3(obj, dt):
            bullet = Bullet().scale(0.7).rotate(self.CONFIG2['time'] * 10 + self.an * 10)
            texto=self.getting_tex(bullet)
            bullet.add(texto)
            obj.add(bullet)
            for k in obj:
                k.shift(dt * .2 *np.array([
                    np.cos(k.get_angle())+3*np.cos(k.get_angle()),
                    np.sin(k.get_angle())+3*np.sin(k.get_angle()),
                    0
                ]))
        vqueue1.add_updater(update_bullet1)
        vqueue2.add_updater(update_bullet2)
        vqueue3.add_updater(update_bullet3)
        self.add(vqueue1,vqueue2,vqueue3)
        self.wait(5)
    def getting_tex(self,mob):
        texto=Tex('Farnaz').add_updater(lambda m: m.move_to(mob.get_center()+np.array([0,.1,0])))
        texto.scale(.3)
        return texto