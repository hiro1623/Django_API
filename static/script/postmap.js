navigator.geolocation.getCurrentPosition(function succes_func(position) {
  //取得したデータを整理
  var data = position.coords;
  //lat:緯度　lng:経度
  var lat = data.latitude;
  var lng = data.longitude;
  var mpoint = [lat, lng];
  var osm = L.tileLayer('https://tile.openstreetmap.jp/{z}/{x}/{y}.png', { attribution: "<a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> " });
  //var osm = L.tileLayer('/static/osm/{z}/{x}/{y}.png');

  var map = L.map('minimap', {
    layers: [osm],
    center: [lat, lng],
    maxZoom: 15,
    minZoom: 15,
    zoom: 15,
    zoomControl: false
  });

  //クリックイベント
  map.on('click', function(e) {
    //クリック位置経緯度取得
    lat = e.latlng.lat;
    lng = e.latlng.lng;
    //経緯度表示
    //alert("lat: " + lat + ", lng: " + lng);
  });
});