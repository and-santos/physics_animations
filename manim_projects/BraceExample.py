# Referência Brace()
# https://docs.manim.community/en/v0.4.0/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace

from manim import *

class BraceExample(Scene):
	def construct(self):
		circle = Circle()
		brace = Brace(circle, direction=RIGHT)  #  brace = colchete (tradução)
		self.play(ShowCreation(circle))  # Animação do círculo sendo criado. Por padrão, a animação dura exato 1 sec
		self.play(ShowCreation(brace))  # Animação do colchete sendo criado. Por padrão a animação dura exato 1 sec
		self.wait(2)  # pausa de dois segundos após a animação


"""
class BraceAnnotation(Scene):
	def construct(self):
		dot = Dot([-2, -1, 0])
		dot2 = Dot([2, 1, 0])
		line = Line(dot, dot2).set_color(ORANGE)
		b1 = Brace(line)
		#b1text = b1.get_text("Horizontal distance")
		#b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector())
		#b2text = b2.get_tex("x-x_1")
		self.add(line, dot, dot2, b1)

#ERROR: invalid data found when processing input
"""
class BraceAnnotation(Scene):
	def construct(self):
		dot = Dot([-2, -1, 0])
		dot2 = Dot([2, 1, 0])
		line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
		b1 = Brace(line)
		self.add(dot, dot2)
		self.play(ShowCreation(line))
		self.play(ShowCreation(b1),run_time=2)

