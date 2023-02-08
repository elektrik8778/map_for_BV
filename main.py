# import folium
#
# m = folium.Map(location=[50.260924, 127.557525], zoom_start=13)
# m.save("map1.html")

from flask import Flask, render_template_string

import folium
from folium.plugins import MousePosition
from folium.plugins import Draw
from class1 import LatLngPopup

app = Flask(__name__)


@app.route("/")
def fullscreen():
    """Simple example of a fullscreen map."""
    m = folium.Map(
        location=[50.5740, 127.6601],
        zoom_start=18,
    )

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        name='Esri.WorldImagery',
        show=True,
        attr='Esri.WorldImagery').add_to(m)
    folium.TileLayer('openstreetmap',
                     show=False,
                     ).add_to(m)
    # folium.TileLayer('stamenterrain', attr="stamenterrain").add_to(m)
    # folium.TileLayer('stamenwatercolor', attr="stamenwatercolor").add_to(m)



    formatter = "function(num) {return L.Util.formatNum(num, 5);};"

    draw = Draw(
        draw_options={
            'export': True,
            'polyline': True,
            'rectangle': True,
            'polygon': True,
            'circle': False,
            'marker': True,
            'circlemarker': True},
        edit_options={'edit': True})


    mouse_position = MousePosition(
        position='topright',
        separator=' Long: ',
        empty_string='NaN',
        lng_first=False,
        num_digits=20,
        prefix='Lat:',
        lat_formatter=formatter,
        lng_formatter=formatter,
    )

    m.add_child(mouse_position)
    m.add_child(draw)
    # m.add_child(LatLngPopup())
    folium.LayerControl().add_to(m)

    # inject html into the map html
    m.get_root().html.add_child(folium.Element("""
    <div style="position: fixed; 
         top: 50px; left: 70px; width: 150px; height: 70px; 
         background-color:orange; border:2px solid grey;z-index: 900;">
        <h5>Hello World!!!</h5>
        <button>Test Button</button>
    </div>
    """))


    return m.get_root().render()


@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map(
        location=[50.260924, 127.557525],
        zoom_start=13,
    )

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


@app.route("/components")
def components():
    """Extract map components and put those on a page."""
    m = folium.Map(
        location=[50.260924, 127.557525],
        zoom_start=13,
        width=800,
        height=600
    )

    m.get_root().render()
    header = m.get_root().header.render()
    body_html = m.get_root().html.render()
    script = m.get_root().script.render()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head>
                    {{ header|safe }}
                </head>
                <body>
                    <h1>Using components</h1>
                    {{ body_html|safe }}
                    <script>
                        {{ script|safe }}
                    </script>
                </body>
            </html>
        """,
        header=header,
        body_html=body_html,
        script=script,
    )


if __name__ == "__main__":
    app.run(debug=True)