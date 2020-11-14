// mapbox accessToken:apiKey
// tile layers variables of map(s)
var mapGrayScale = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 20,
  accessToken:apiKey
});

var mapSatellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}",{
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 20,
    accessToken: apiKey
});

// outdoors background.
var mapOutdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}",{
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 20,
    accessToken: apiKey
});

//map to created layer
var map =L.map("map", {
    center: [33.5,-112],
    zoom:10.75,
    layers: [mapOutdoors]
});

//mapGrayScale added into the created layer array
mapGrayScale.addTo(map);

//layer for bus stop data
var busStopData = new L.LayerGroup(),
lightRailData = new L.LayerGroup();

var mapOptions = {
    // Grayscale: mapGrayScale,
    Satellite: mapSatellite,
    Outdoors: mapOutdoors
},
overLays = {
    "Light Rail":lightRailData,
    'Bus Stop': busStopData
};

L.control.layers(mapOptions,overLays).addTo(map);

// d3 pull from arcgis, bus stops
d3.json("https://opendata.arcgis.com/datasets/ba0a1ffe10d444cd9a3e7c2060f6969f_0.geojson", function(data) {
    function styleFxn(feature) {
         return {
             opacity: 0.75,
             fillOpacity: 1,
             fillColor: 'blue',
             radius: 3,
             stroke:true, 
             weight: 1
         };
    }

    //geoJson to map layers
    L.geoJson(data, {
        pointToLayer: function(feature, latlng) {
            return L.circleMarker(latlng);
        },
        style: styleFxn,
        onEachFeature: function(feature, layer) {
            layer.bindPopup("Stop Location: " + feature.properties.Location + "<br> City: " + feature.properties.Juris);
        }
    }).addTo(busStopData);

    //make data visible by adding to map array
    busStopData.addTo(map);

    // light rail data entry
    d3.json("https://opendata.arcgis.com/datasets/00a92b98e7fc4ef5999d68f9cb86c36f_1.geojson", function(data2) {
    function styleFxn2(feature) {
         return {
             opacity: 0.75,
             fillOpacity: 1,
             fillColor: 'orange',
             radius: 6,
             stroke:true, 
             weight: 1
         };
    }
    //geoJson to map layers
    L.geoJson(data2, {
        pointToLayer: function(feature, latlng) {
            return L.circleMarker(latlng);
        },
        style: styleFxn2,
        onEachFeature: function(feature, layer) {
            layer.bindPopup("Light Rail Station: " + feature.properties.StationName + "<br> City: " + feature.properties.Jurisdiction);
        }
    }).addTo(lightRailData);

    //make data visible by adding to map array
    lightRailData.addTo(map);
    });
});