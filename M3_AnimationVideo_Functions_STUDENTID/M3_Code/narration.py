"""
Narration script for M3 Animation Video: Single-Variable Functions & Graphs
All beats are preserved exactly as written in the approved script.
Grouped by scene and organized into bite-sized beats for audio/visual synchronisation.
"""

NARRATION = {
    "scene1": [
        # Beat 0: 0:00 - 0:08 (4s title, then coaster begins)
        "Picture a roller coaster. At every point along the ground, the track has exactly one height.",
        # Beat 1: 0:08 - 0:16
        "Slide forward, and the height changes: up, down, and up again.",
        # Beat 2: 0:16 - 0:23
        "Here is the question: could a single formula describe that entire ride?",
        # Beat 3: 0:23 - 0:29
        "It can. That formula is called a function, and its graph is the picture of the ride.",
        # Beat 4: 0:29 - 0:35
        "I'm Abhinav, and in the next five minutes you'll learn to read a function's graph like a map."
    ],

    "scene2": [
        # Beat 0: 0:35 - 0:45
        "A function f from a set X to a set Y is a rule that assigns to each input x in X exactly one output, written f of x, in Y.",
        # Beat 1: 0:45 - 0:52
        "We write f from the real numbers to the real numbers.",
        # Beat 2: 0:52 - 1:00
        "The set of allowed inputs is the domain. The set of outputs the rule actually produces is the range.",
        # Beat 3: 1:00 - 1:06
        "Our example is f of x equals x cubed minus three x.",
        # Beat 4: 1:06 - 1:15
        "By the end, you'll be able to read from its graph where it crosses the axes, its symmetry, its turning points, how it behaves far out to either side, and its domain and range."
    ],

    "scene3": [
        # Beat 0: 1:15 - 1:22
        "Think of f as a machine. Feed in 2.",
        # Beat 1: 1:22 - 1:36
        "Cube it: eight. Subtract three times two, which is six. Out comes 2. So the pair two, two is a point on the graph.",
        # Beat 2: 1:36 - 1:52
        "Let's try more inputs: minus 2 gives minus 2, minus 1 gives 2, 0 gives 0, 1 gives minus 2.",
        # Beat 3: 1:52 - 2:00
        "Each pair becomes a point, x across and f of x up.",
        # Beat 4: 2:00 - 2:15
        "Now let x slide continuously. The dot's height is f of x, and the curve it traces is our roller coaster.",
        # Beat 5: 2:15 - 2:30
        "Notice that a vertical line always cuts the curve exactly once. One input, one output. That is the vertical line test."
    ],

    "scene4": [
        # Beat 0: 2:30 - 2:42
        "Step one, the domain. The formula only cubes, multiplies and subtracts. Nothing can break, so every real number is allowed.",
        # Beat 1: 2:42 - 2:54
        "Step two, the intercepts. At x equals 0, f of 0 is 0, so the graph crosses the y-axis at the origin.",
        # Beat 2: 2:54 - 3:06
        "To cross the x-axis, set x cubed minus 3x equal to 0. Factor out x: x times x squared minus 3 equals 0.",
        # Beat 3: 3:06 - 3:18
        "So x is 0, or x squared is 3, giving x equal to plus or minus root 3, about 1.73.",
        # Beat 4: 3:18 - 3:28
        "Check: f of root 3 is 3 root 3 minus 3 root 3, which is 0.",
        # Beat 5: 3:28 - 3:40
        "Step three, symmetry. Replace x with minus x: minus x cubed plus 3x. That's exactly minus f of x.",
        # Beat 6: 3:40 - 3:52
        "This is an odd function, so rotating the graph 180 degrees about the origin leaves it unchanged. Check with numbers: f of 2 is 2, and f of minus 2 is minus 2.",
        # Beat 7: 3:52 - 4:04
        "Step four, turning points. Look at the table: f of minus 2 is minus 2, f of minus 1 is 2, then f of 0 is 0, f of 1 is minus 2, f of 2 is 2.",
        # Beat 8: 4:04 - 4:14
        "The curve climbs to a peak at minus 1, 2, falls to a valley at 1, minus 2, and climbs again.",
        # Beat 9: 4:14 - 4:22
        "Calculus will later explain exactly why these happen at x equals plus or minus 1.",
        # Beat 10: 4:22 - 4:32
        "Step five, end behaviour. When x is huge, x cubed overwhelms 3x.",
        # Beat 11: 4:32 - 4:42
        "So as x grows large and positive, f grows large and positive. As x grows large and negative, f grows large and negative."
    ],

    "scene5": [
        # Beat 0: 4:00 - 4:08
        "Now let's connect the algebra back to the picture.",
        # Beat 1: 4:08 - 4:18
        "Because the curve is unbroken and runs from far below to far above, every height is reached, so the range is all real numbers.",
        # Beat 2: 4:18 - 4:30
        "Sweep a horizontal line upward: at height 1 it cuts the graph three times. Three different inputs give the same output, so this function is not one-to-one.",
        # Beat 3: 4:30 - 4:40
        "And for our roller coaster: a hill with peak height 2, a valley of depth minus 2, and then the track climbs forever."
    ],

    "scene6": [
        # Beat 0: 4:40 - 4:45
        "Three takeaways.",
        # Beat 1: 4:45 - 4:54
        "One: a function gives each input exactly one output, and its domain and range say what goes in and what comes out.",
        # Beat 2: 4:54 - 5:02
        "Two: the graph is every point x, f of x, and the vertical line test checks it.",
        # Beat 3: 5:02 - 5:10
        "Three: you can read a graph's features, which are intercepts, symmetry, turning points and end behaviour, and confirm each one by substitution. Thanks for watching."
    ]
}
