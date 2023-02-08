from branca.element import Element, Figure, Html, MacroElement
from jinja2 import Template


class LatLngPopup(MacroElement):
    """
    When one clicks on a Map that contains a LatLngPopup,
    a popup is shown that displays the latitude and longitude of the pointer.

    """
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                data = e.latlng.lat.toFixed(4) + "," + e.latlng.lng.toFixed(4);
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent( "Latitude: " + e.latlng.lat.toFixed(4) + 
                                     "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn({{this._parent.get_name()}})
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
                
                function myFunction() {
                      /* Get the text field */
                      var copyText = document.getElementById("myInput");
                
                      /* Select the text field */
                      copyText.select();
                      copyText.setSelectionRange(0, 99999); /* For mobile devices */
                
                      /* Copy the text inside the text field */
                      document.execCommand("copy");
                    }
            {% endmacro %}
            """)

    # _template = Template(u"""
    #             {% macro script(this, kwargs) %}
    #                 var {{this.get_name()}} = L.popup();
    #                 function latLngPop(e) {
    #                     {{this.get_name()}}
    #                         .setLatLng(e.latlng)
    #                         .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
    #                                     "<br>Longitude: " + e.latlng.lng.toFixed(4))
    #                         .openOn({{this._parent.get_name()}});
    #                     parent.document.getElementById("id_lng").value = e.latlng.lng.toFixed(4); # add this
    #                     parent.document.getElementById("id_lat").value = e.latlng.lat.toFixed(4); # add this
    #                     }
    #                 {{this._parent.get_name()}}.on('click', latLngPop);
    #             {% endmacro %}
    #             """)  # noqa


    def __init__(self):
        super(LatLngPopup, self).__init__()
        self._name = 'LatLngPopup'