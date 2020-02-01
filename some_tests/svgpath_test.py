from svgpathtools import *
from svgpathtools.paths2svg import *

closed_path = Path(Line(0,5), Line(5,5+5j), Line(5+5j, 0))

def paths2Drawing(paths=None, colors=None,
          filename=os_path.join(getcwd(), 'disvg_output.svg'),
          stroke_widths=None, nodes=None, node_colors=None, node_radii=None,
          openinbrowser=False, timestamp=False,
          margin_size=0.1, mindim=600, dimensions=None,
          viewbox=None, text=None, text_path=None, font_size=None,
          attributes=None, svg_attributes=None, svgwrite_debug=False, paths2Drawing=True):
    """Convenience function; identical to disvg() except that
    paths2Drawing=True by default.  See disvg() docstring for more info."""
    disvg(paths, colors=colors, filename=filename,
          stroke_widths=stroke_widths, nodes=nodes,
          node_colors=node_colors, node_radii=node_radii,
          openinbrowser=openinbrowser, timestamp=timestamp,
          margin_size=margin_size, mindim=mindim, dimensions=dimensions,
          viewbox=viewbox, text=text, text_path=text_path, font_size=font_size,
          attributes=attributes, svg_attributes=svg_attributes
          )

paths2Drawing(closed_path)