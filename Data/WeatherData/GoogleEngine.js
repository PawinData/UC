// Define a FeatureCollection: regions of the American West.
// Define a FeatureCollection: regions of the American West.
var regions = ee.FeatureCollection([
  ee.Feature(    // San Francisco.
    ee.Geometry.Point(-123.032229, 37.727239), {label: 'San Francisco'}),
  ee.Feature(  // Tahoe National Forest.
    ee.Geometry.Point(-122.325995, 38.507351), {label: 'Napa'}),
  ee.Feature(  // Black Rock Desert.
    ee.Geometry.Point(-121.690622, 37.220777), {label: 'Santa Clara'}),
  ee.Feature(    // San Francisco.
    ee.Geometry.Point(-122.945194, 38.532574), {label: 'Sonoma'}),
  ee.Feature(  // Tahoe National Forest.
    ee.Geometry.Point(-121.913304, 37.648081), {label: 'Alameda'}),
  ee.Feature(  // Black Rock Desert.
    ee.Geometry.Point(-122.371542, 37.414664), {label: 'San Mateo'}),
  ee.Feature(    // San Francisco.
    ee.Geometry.Point(-121.939594, 38.267226), {label: 'Solano'}),
  ee.Feature(  // Tahoe National Forest.
    ee.Geometry.Point(-121.951543, 37.919479), {label: 'Contra Costa'}),
  ee.Feature(  // Black Rock Desert.
    ee.Geometry.Point(-122.745974, 38.051817), {label: 'Marin'})    
]);

var select = 'tmax'
var date1 = '2020-01-01'
var date2 = '2020-05-05'
var dataset = 'NASA/ORNL/DAYMET_V3'

// Load Landsat 8 brightness temperature data for 1 year.
var temps2013 = ee.ImageCollection(dataset)
    .filterDate(date1, date2)
    .select(select);

print(temps2013)

// Create a time series chart.
var tempTimeSeries = ui.Chart.image.seriesByRegion(
    temps2013, regions, ee.Reducer.mean(), select, 200, 'system:time_start', 'label')
        .setChartType('ScatterChart')
        .setOptions({
          title: 'Temperature over time in regions of the American West',
          vAxis: {title: 'Temperature (Kelvin)'},
          lineWidth: 1,
          pointSize: 4,
          series: {
            0: {color: 'FF0000'}, // urban
            1: {color: '00FF00'}, // forest
            2: {color: '0000FF'}  // desert
}});

// Display.
print(tempTimeSeries);