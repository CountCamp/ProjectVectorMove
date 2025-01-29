from manim import *
import numpy as np


class vectorAdd(MovingCameraScene):
    def construct(self):
        # Create a number plane, extend grid for zooming
        plane = NumberPlane(
            x_range=(-20, 20, 1),
            y_range=(-20, 20, 1),
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.8,
            },
        )
        # Add the plane to the scene
        self.play(Create(plane))

        # Define points A and B as numpy arrays
        A = np.array([-1, 2, 0])
        B = np.array([2, 3, 0])

        # Define dots for points A and B
        dot_A = Dot(A, color=BLUE, radius=0.08)
        dot_B = Dot(B, color=RED, radius=0.08)
        label_A = MathTex("A").next_to(dot_A, LEFT)
        label_B = MathTex("B").next_to(dot_B, RIGHT)

        # Add dots and labels to the scene one by one
        self.play(FadeIn(dot_A))
        self.wait(1)
        self.play(FadeIn(dot_B))
        self.wait(1)
        self.play(Write(label_A))
        self.wait(1)
        self.play(Write(label_B))
        self.wait(1)

        # Create vectors A and B
        vector_A = Arrow(ORIGIN, A, buff=0, color=BLUE, stroke_width=3)
        vector_B = Arrow(ORIGIN, B, buff=0, color=RED, stroke_width=3)
        label_vector_A = MathTex(r"\vec{a}").move_to(plane.c2p(-1, 1.1))
        label_vector_B = MathTex(r"\vec{b}").move_to(plane.c2p(1.5, 1.3))

        # Add vectors and labels to the scene one by one
        self.play(Create(vector_A))
        self.wait(1)
        self.play(Write(label_vector_A))
        self.wait(1)
        self.play(Create(vector_B))
        self.wait(1)
        self.play(Write(label_vector_B))
        self.wait(1)

        # Higher values than 14 will zoom out, lower values will zoom in
        # Moving camera to the left and up
        self.play(
            self.camera.frame.animate.move_to(ORIGIN)
            .set(width=18)
            .shift(LEFT * 5 + UP * 1.5),
            run_time=5,
        )
        self.wait(2)

        # Vector notations
        vector_notation = MathTex(
            r"\vec{a} = \begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} \quad \text{and} \quad \vec{b} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}"
        )
        # Move the vector_notation to the top left corner
        vector_notation.move_to(plane.c2p(-7.5, 5, 0))
        # Scaledown the vector_notation
        vector_notation.scale(1)
        self.play(Write(vector_notation))
        self.wait(1)

        # Create a sum vector using the vector addition formula
        vector_sum_formula = MathTex(
            r"\vec{a} + \vec{b} = \begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} + \begin{bmatrix} 2 \\ 3 \end{bmatrix}"
        )
        vector_sum_formula.move_to(plane.c2p(-7.5, 3, 0))
        self.play(Write(vector_sum_formula))
        self.wait(1)

        # add vector b to a: Move vector b with it's tail to the head of vector a
        self.play(vector_B.animate.shift(A))
        # vector_b_label should fade out.
        self.play(FadeOut(label_vector_B))
        self.wait(1)
        # We need to create a new label for the new vector b
        label_vector_B_new = MathTex(r"\vec{b}").move_to(plane.c2p(-0.5, 4))
        # Add the new label to the scene
        self.play(Write(label_vector_B_new))
        self.wait(1)

        # Draw point C at the end of the sum vector
        C = np.add(A, B)
        dot_C = Dot(C, color=GREEN, radius=0.05)
        label_C = MathTex("C").next_to(dot_C, UP)
        self.play(FadeIn(dot_C))
        self.wait(1)
        self.play(Write(label_C))
        self.wait(1)

        # Draw thin dashed line from origin to point B.
        dashed_line_OB = DashedLine(ORIGIN, B, color=RED, stroke_width=2)
        self.play(Create(dashed_line_OB))
        self.wait(1)

        # Draw thin dashed line from B to point C.
        dashed_line_BC = DashedLine(B, C, color=GREEN, stroke_width=2)
        self.play(Create(dashed_line_BC))
        self.wait(1)

        # Create a sum vector using the vector addition formula
        vector_sum = MathTex(
            r"\vec{c} = \vec{a} + \vec{b} =",
            r"\begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} + \begin{bmatrix} 2 \\ 3 \end{bmatrix} =",
            r"\begin{bmatrix} \text{-}1 + 2 \\ 2 + 3 \end{bmatrix} =",
            r"\begin{bmatrix} 1 \\ 5 \end{bmatrix}",
        )
        vector_sum.move_to(plane.c2p(-7.5, 1, 0)).scale(1.0)
        self.play(Write(vector_sum))
        self.wait(1)

        # Create a vector C
        vector_C = Arrow(ORIGIN, C, buff=0, color=GREEN, stroke_width=3)
        label_vector_C = MathTex(r"\vec{c}").move_to(
            plane.c2p(1, 2.4)
        )  # Adjust the position as needed
        self.play(GrowArrow(vector_C))
        self.wait(1)
        self.play(Write(label_vector_C))
        self.wait(1)

        # Vector notations
        vector_notation_c = MathTex(r"\vec{c} = \begin{bmatrix} \ 1 \\ 5 \end{bmatrix}")
        # Move the vector_notation to the top left corner
        vector_notation_c.move_to(plane.c2p(-7.5, -1, 0))
        # Scaledown the vector_notation_c
        vector_notation_c.scale(1)
        self.play(Write(vector_notation_c))
        self.wait(1)


class vectorSub(MovingCameraScene):
    def construct(self):
        # Create a number plane, extend grid for zooming
        plane = NumberPlane(
            x_range=(-20, 20, 1),
            y_range=(-20, 20, 1),
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.8,
            },
        )
        # Add the plane to the scene
        self.play(Create(plane))

        # Define points A and B as numpy arrays
        A = np.array([-1, 2, 0])
        B = np.array([2, 3, 0])
        # Negative of B
        B_neg = np.array([-2, -3, 0])

        # Define dots for points A and B
        dot_A = Dot(A, color=BLUE, radius=0.08)
        dot_B = Dot(B, color=RED, radius=0.08)
        label_A = MathTex("A").next_to(dot_A, LEFT)
        label_B = MathTex("B").next_to(dot_B, RIGHT)

        # Add dots and labels to the scene
        self.play(FadeIn(dot_A))
        self.wait(1)
        self.play(FadeIn(dot_B))
        self.wait(1)
        self.play(Write(label_A))
        self.wait(1)
        self.play(Write(label_B))
        self.wait(1)

        # Create vectors A and B
        vector_A = Arrow(ORIGIN, A, buff=0, color=BLUE, stroke_width=3)
        vector_B = Arrow(ORIGIN, B, buff=0, color=RED, stroke_width=3)
        label_vector_A = MathTex(r"\vec{a}").move_to(plane.c2p(-0.8, 0.8))
        label_vector_B = MathTex(r"\vec{b}").move_to(plane.c2p(1.5, 1.3))

        # Add vectors and labels to the scene
        self.play(Create(vector_A))
        self.wait(1)
        self.play(Write(label_vector_A))
        self.wait(1)
        self.play(Create(vector_B))
        self.wait(1)
        self.play(Write(label_vector_B))
        self.wait(1)

        # Adjust camera for better visibility Zoom and Move
        self.play(
            self.camera.frame.animate.move_to(ORIGIN)
            .set(width=18)
            .shift(LEFT * 6 + UP * 0.5),
            run_time=5,
        )
        self.wait(2)

        # Vector notations
        vector_notation = MathTex(
            r"\vec{a} = \begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} \quad \text{and} \quad \vec{b} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}"
        )
        vector_notation.move_to(plane.c2p(-9.5, 4.5, 0))
        vector_notation.scale(1)
        self.play(Write(vector_notation))
        self.wait(1)

        # Compute the subtraction: C = A - B
        C = np.subtract(A, B)

        # Display subtraction formula 1
        vector_sub_formula = MathTex(r"\vec{a} - \vec{b} =", r"\vec{a} + - \vec{b}")
        vector_sub_formula.move_to(plane.c2p(-9.5, 3.0, 0))
        self.play(Write(vector_sub_formula))
        self.wait(1)

        # Change vector B to negative
        vector_B_neg = Arrow(ORIGIN, B_neg, buff=0, color=RED, stroke_width=3)
        # Replace vector_B with vector_B_neg explicitly
        self.play(FadeOut(vector_B), Create(vector_B_neg))
        self.wait(1)
        # Change label for vector B to
        label_vector_B_neg = MathTex(r"\text{-}\vec{b}").move_to(plane.c2p(-1.5, -1.3))
        label_vector_B_neg.scale(1)
        self.play(FadeOut(label_vector_B), Write(label_vector_B_neg))
        self.wait(1)

        # Display subtraction formula 2
        vector_sub_formula2 = MathTex(
            r"\begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} - \begin{bmatrix} 2 \\ 3 \end{bmatrix}=",
            r"\begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} + - \begin{bmatrix} 2 \\ 3 \end{bmatrix}",
            r"= \begin{bmatrix} \text{-}1 \\ 2 \end{bmatrix} + \begin{bmatrix} \text{-}2 \\ \text{-}3 \end{bmatrix}=",
        )
        vector_sub_formula2.move_to(plane.c2p(-9.5, 1.5, 0))
        self.play(Write(vector_sub_formula2))
        self.wait(1)

        # Animate vector_B_neg subtraction by shifting vectorto head of vector A
        self.play(vector_B_neg.animate.shift(A))  # Shift B_Neg's to head of A
        self.play(FadeOut(label_vector_B_neg))  # Fade out old labe
        self.wait(1)
        # Write new label for vector_B_neg new position
        label_vector_B_neg_new = MathTex(r"\text{-}\vec{b}").move_to(
            plane.c2p(-2.1, 1.2)
        )
        self.play(Write(label_vector_B_neg_new))
        self.wait(1)

        # Create point C at the end of the subtraction vector
        dot_C = Dot(C, color=GREEN, radius=0.08)
        label_C = MathTex("C").next_to(dot_C, LEFT)
        self.play(Create(dot_C), Write(label_C))
        self.wait(1)

        # Create vector C
        vector_C = Arrow(ORIGIN, C, buff=0, color=GREEN, stroke_width=3)
        self.play(Create(vector_C))
        self.wait(1)

        # Write label for vector C
        label_vector_C = MathTex(r"\vec{c}").move_to(plane.c2p(-1.5, -1))
        self.play(Write(label_vector_C))
        self.wait(1)

        # Draw thin dashed line from origin to point -B.
        dashed_line_OB = DashedLine(ORIGIN, B_neg, color=GREEN_A, stroke_width=2)
        self.play(Create(dashed_line_OB))
        self.wait(1)
        # Draw thin dashed line from point -B to point C.
        dashed_line_B_NEG_C = DashedLine(B_neg, C, color=GREEN_A, stroke_width=2)
        self.play(Create(dashed_line_B_NEG_C))  # Draw dashed line from B to C
        self.wait(1)

        # Display subtraction formula 3
        vector_sub_formula3 = MathTex(
            r"\vec{c} =",
            r"\begin{bmatrix} \text{-}1 + \text{-}2 \\ 2 + \text{-}3 \end{bmatrix}=",
            r"\begin{bmatrix} \text{-}3 \\ \text{-}1 \end{bmatrix}",
        )
        vector_sub_formula3.move_to(plane.c2p(-9.5, -1.5, 0))
        self.play(Write(vector_sub_formula3))
        self.wait(1)


# For medium quality
# manim -qm VectorAddSub.py vectorAdd
# manim -qm VectorAddSub.py vectorSub
# For high quality
# manim -qh VectorAddSub.py vectorAdd
# manim -qh VectorAddSub.py vectorSub
