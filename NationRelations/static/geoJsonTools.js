function resetHighlight(e) {
    geojson.resetStyle(e.target);
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}


function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}


function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}


function getColor(d) {
    if (d >= 30.0) {
        return '#9DF781';
    } else if (30.0 > d && d >= 10.0) {
        return '#CBFFC0';
    } else if (10.0 > d && d >= -10.0) {
        return '#FEE46E';
    } else if (-10.0 > d && d >= -30.0) {
        return '#E96245';
    } else if (-30.0 > d) {
        return '#A62700';
    } else {
        return '#FFFFFF';
    }
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.score),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}