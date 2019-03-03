let currentWeight;
let currentColor;
let currentDashArray;
let currentFillOpacity;
let currentClickedCountry;

function resetHighlight(e) {
    // geojson.resetStyle(e.target);
    var layer = e.target;

    layer.setStyle({
        weight: currentWeight,
        color: currentColor,
        dashArray: currentDashArray,
        fillOpacity: currentFillOpacity
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function colorOthers(e) {
    // if (currentClickedCountry !== e.sourceTarget.feature.properties.name) {
    //     currentClickedCountry = e.sourceTarget.feature.properties.name;
    // map.fitBounds(e.target.getBounds());
    // geojson.resetStyle(e.target);

    removeMarkers();
    geojson = L.geoJson(countryData, {
        style: defaultStyle,
        onEachFeature: onEachFeature
    }).addTo(map);
    let clicked3Code = e.sourceTarget.feature.id;
    switch (clicked3Code) {
        case "ARG":
            L.geoJson(ARG, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "BRA":
            L.geoJson(BRA, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "CAN":
            L.geoJson(CAN, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "CHN":
            L.geoJson(CHN, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "CUB":
            L.geoJson(CUB, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "DEU":
            L.geoJson(DEU, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "HKG":
            L.geoJson(HKG, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "IND":
            L.geoJson(IND, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "MEX":
            L.geoJson(MEX, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "RUS":
            L.geoJson(RUS, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
        case "USA":
            L.geoJson(USA, {style: colorOthersStyle, onEachFeature: onEachFeature}).addTo(map);
            break;
    }
    // if (clicked3Code === "ARG") {
    //     console.log(clicked3Code);
    //
    // }

    // }
}

var removeMarkers = function () {
    map.eachLayer(function (layer) {

        if (layer.myTag && layer.myTag === "defaultLayer") {
            map.removeLayer(layer)
        }

    });

};

function onEachFeature(feature, layer) {
    layer.myTag = "defaultLayer";
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: colorOthers,
    });
}


function highlightFeature(e) {
    currentWeight = e.target.options.weight;
    currentColor = e.target.options.color;
    currentDashArray = e.target.options.dashArray;
    currentFillOpacity = e.target.options.fillOpacity;
    var layer = e.target;

    layer.setStyle({
        weight: 4,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.4
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}


function getColor(d) {
    if (d === 769420.0) {
        return '#A9A9A9';
    } else if (d === -769420.0) {
        return '#FFFFFF';
    } else if (d >= 30.0) {
        return '#9DF781';
    } else if (30.0 > d && d >= 10.0) {
        return '#CBFFC0';
    } else if (10.0 > d && d >= -10.0) {
        return '#FEE46E';
    } else if (-10.0 > d && d >= -30.0) {
        return '#E96245';
    } else if (-30.0 > d) {
        return '#7c1d00';
    } else {
        return '#FFFFFF';
    }
}

//getColor(feature.properties.score)

function defaultStyle(feature) {
    return {
        fillColor: 'white',
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.2
    };
}


function colorOthersStyle(feature) {
    return {
        fillColor: getColor(feature.properties.score),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.2
    };
}