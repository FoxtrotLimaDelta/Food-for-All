# BCS_Project3

## Bus Stop Data Portion

API for ARCOGIS for Valley Metro has a 50token a month limit. Utilizing KML files
To read in KML files, ... utilizing direct geojson links (directly in file ..._create_artifact)

```
$ pip install geopandas and fiona (if necessary)
```

Utilize geopandas to read in your geojson file/url/api.
So as to not continue to make requests to host server (unless needing live data), 
utilize geopandas write function to write ```to_file("filename.geojson", Driver='geoJSON') ```

~after writing geopandas, environment stopped liking geopandas.

Switching to read the geoJSON file back in with dependency geojson

index.html, container for JS script. from index.html location, terminal code: `$ python -m http.server`



