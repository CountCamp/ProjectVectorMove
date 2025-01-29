from manim import *


class Vector(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"color": WHITE}
        ).add_coordinates()

        # Add labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Define vectors
        vector_a = [3, 2]
        vector_b = [1, -1]

        # Create vector arrows
        arrow_a = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*vector_a), color=BLUE, buff=0
        )
        arrow_b = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*vector_b), color=GREEN, buff=0
        )

        # Create labels for the vectors
        label_a = MathTex(
            "\\vec{a} = \\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}"
        ).next_to(arrow_a.get_end(), UP)
        label_b = MathTex(
            "\\vec{b} = \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix}"
        ).next_to(arrow_b.get_end(), DOWN)

        # Add animations for axes, vectors, and labels
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(GrowArrow(arrow_a), Write(label_a))
        self.play(GrowArrow(arrow_b), Write(label_b))

        # Compute resultant vector
        resultant_vector = [vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]]
        arrow_resultant = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*resultant_vector), color=YELLOW, buff=0
        )
        label_resultant = MathTex(
            "\\vec{a} + \\vec{b} = \\begin{bmatrix} 4 \\\\ 1 \\end{bmatrix}"
        ).next_to(arrow_resultant.get_end(), RIGHT)

        # Animate the resultant vector
        self.play(GrowArrow(arrow_resultant), Write(label_resultant))

        # Hold the final scene for a moment
        self.wait(2)


class VectorVisualization1(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[0, 5, 1],  # Adjusted to only show the first quadrant
            y_range=[0, 5, 1],
            axis_config={"color": WHITE},
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
        ).add_coordinates()

        # Add a grid (rooster)
        grid = NumberPlane(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            },
        )

        # Define vectors
        vector_a = [3, 2]
        vector_b = [1, 1]

        # Create vector arrows
        arrow_a = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*vector_a), color=BLUE, buff=0
        )
        arrow_b = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*vector_b), color=GREEN, buff=0
        )

        # Create labels for the vectors
        label_a = MathTex(
            "\\vec{a} = \\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}"
        ).next_to(arrow_a.get_end(), UP)
        label_b = MathTex(
            "\\vec{b} = \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}"
        ).next_to(arrow_b.get_end(), RIGHT)

        # Compute resultant vector
        resultant_vector = [vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]]
        arrow_resultant = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*resultant_vector), color=YELLOW, buff=0
        )
        label_resultant = MathTex(
            "\\vec{a} + \\vec{b} = \\begin{bmatrix} 4 \\\\ 3 \\end{bmatrix}"
        ).next_to(arrow_resultant.get_end(), RIGHT)

        # Draw parallelogram
        parallelogram = Polygon(
            axes.c2p(0, 0),
            axes.c2p(*vector_a),
            axes.c2p(*resultant_vector),
            axes.c2p(*vector_b),
            color=ORANGE,
            fill_opacity=0.3,
        )

        # Add animations
        self.play(Create(grid), Create(axes))
        self.play(GrowArrow(arrow_a), Write(label_a))
        self.play(GrowArrow(arrow_b), Write(label_b))
        self.play(FadeIn(parallelogram))
        self.play(GrowArrow(arrow_resultant), Write(label_resultant))

        # Hold the final scene
        self.wait(3)


class VectorVisualization2(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[0, 5, 1],  # Adjusted to only show the first quadrant
            y_range=[0, 5, 1],
            axis_config={"color": WHITE},
        ).add_coordinates()

        # Add a grid (rooster)
        grid = NumberPlane(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            },
        )

        # Define vectors
        vector_a = [3, 2]
        vector_b = [1, 1]

        # Create vector arrows
        arrow_a = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*vector_a), color=BLUE, buff=0
        )
        arrow_b = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*vector_b), color=GREEN, buff=0
        )

        # Create labels for the vectors
        label_a = MathTex(
            "\\vec{a} = \\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}"
        ).next_to(arrow_a.get_end(), UP)
        label_b = MathTex(
            "\\vec{b} = \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}"
        ).next_to(arrow_b.get_end(), RIGHT)

        # Compute resultant vector
        resultant_vector = [vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]]
        arrow_resultant = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(*resultant_vector), color=YELLOW, buff=0
        )
        label_resultant = MathTex(
            "\\vec{a} + \\vec{b} = \\begin{bmatrix} 4 \\\\ 3 \\end{bmatrix}"
        ).next_to(arrow_resultant.get_end(), RIGHT)

        # Draw parallelogram
        parallelogram = Polygon(
            axes.c2p(0, 0),
            axes.c2p(*vector_a),
            axes.c2p(*resultant_vector),
            axes.c2p(*vector_b),
            color=ORANGE,
            fill_opacity=0.3,
        )

        # Add animations
        self.play(Create(grid), Create(axes))
        self.play(GrowArrow(arrow_a), Write(label_a))
        self.play(GrowArrow(arrow_b), Write(label_b))
        self.play(FadeIn(parallelogram))
        self.play(GrowArrow(arrow_resultant), Write(label_resultant))

        # Hold the final scene
        self.wait(3)


class VectorRepresentation(Scene):
    def construct(self):
        # Define points A and B
        point_A = np.array([2, 3, 0])  # A(2, 3)
        point_B = np.array([-4, 2, 0])  # B(-4, 2)

        # Define vectors
        vector_AB = point_B - point_A

        # Create the grid
        grid = NumberPlane()
        self.add(grid)

        # Plot points A and B
        A_dot = Dot(point_A, color=RED)
        B_dot = Dot(point_B, color=BLUE)
        A_label = MathTex("A(2, 3)").next_to(A_dot, UP + RIGHT)
        B_label = MathTex("B(-4, 2)").next_to(B_dot, DOWN + LEFT)

        # Add points and labels
        self.play(FadeIn(A_dot, B_dot), Write(A_label), Write(B_label))

        # Draw vector AB
        vector_AB_arrow = Arrow(point_A, point_B, buff=0, color=GREEN)
        vector_AB_label = MathTex("\\vec{AB}").next_to(vector_AB_arrow, UP, buff=0.2)
        self.play(GrowArrow(vector_AB_arrow), Write(vector_AB_label))

        # Show the parametric line equation
        equation = MathTex(
            "\\vec{r} = ",
            "\\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix} ",
            "+ t ",
            "\\begin{bmatrix} -6 \\\\ -1 \\end{bmatrix} ",
            ", t \\in \\mathbb{R}",
        ).to_edge(UP)
        self.play(Write(equation))

        # Add the direction vector (-6, -1)
        direction_vector_arrow = Arrow(
            start=ORIGIN, end=vector_AB, buff=0, color=YELLOW
        )
        direction_vector_label = MathTex(
            "\\vec{d} = ", "\\begin{bmatrix} -6 \\\\ -1 \\end{bmatrix}"
        ).next_to(direction_vector_arrow, DOWN, buff=0.5)
        self.play(GrowArrow(direction_vector_arrow), Write(direction_vector_label))

        # Add explanation for the parametric form
        explanation = MathTex(
            "\\text{Lijn: }", "\\vec{r} = \\vec{A} + t\\vec{d}"
        ).next_to(equation, DOWN, buff=0.5)
        self.play(Write(explanation))

        # Pause for visualization
        self.wait(3)


# create venv
# python3 -m venv venv
# activate venv
# source venv/bin/activate
# install manim and pandas
# pip install manim
# pip install pandas
# manim -qm WB_Vector_H09_34.py VectorVisualization
