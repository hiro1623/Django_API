function main() {
    navigator.geolocation.getCurrentPosition(function succes_func(position) {

            //取得したデータを整理
            var data = position.coords;
            //lat:緯度　lng:経度
            var lat = data.latitude;
            var lng = data.longitude;
            var mpoint = [lat, lng];
            // 地図表示
            var osm = L.tileLayer('https://tile.openstreetmap.jp/{z}/{x}/{y}.png', { attribution: "<a href='https://osm.org/copyright' target='_blank'>OpenStreetMap</a> " });
            //var osm = L.tileLayer('/static/osm/{z}/{x}/{y}.png');

            var map = L.map('mapcontainer', {
                layers: [osm],
                center: [lat, lng],
                maxZoom: 15,
                minZoom: 15,
                zoom: 15,
                zoomControl: false
            });


            // マーカー表示
            var pulsingIcon = L.icon.pulse({
                fillColor: 'rgba(248, 181, 0, 1.0)',
                iconSize: [25, 25],
                color: 'rgba(248, 181, 0, 1.0)',
                border: '3px'
            });
            var circle = L.circle(mpoint, {
                className: "clCircle",
                radius: 500,
                weight: 6,
                color: "rgba(248, 181, 0, 1.0)",
                fillColor: "white",
                fillOpacity: 0.5
            }).addTo(map);


            L.marker(mpoint, { icon: pulsingIcon }).addTo(map);

            //L.simpleMapScreenshoter().addTo(map)
// [TEST-01] 投稿表示機能 [日時, userID, 属性, 緯度, 経度, 投稿内容]
for (var i = 0; i < 100; i++) {
    if(posted_data[i].post_flag == "True"){
        if (0.50 >= distance(lat, lng, posted_data[i].lat, posted_data[i].lng)) {
            console.log(posted_data[i].purpose)
            if(posted_data[i].purpose == "SOS"){
                console.log(posted_data[i].pic)
                L.marker([posted_data[i].lat,posted_data[i].lng], {icon: L.icon({ 
                    iconUrl: '/static/images/pin/pin_red.png',
                    shadowUrl: '/static/images/pin/pin_shadow.png',
                    iconSize: [55,55], shadowSize:[100,50],
                    iconAnchor: [27,55], shadowAnchor: [35,30], popupAnchor: [0,-35]
                }) }).bindPopup('<div class="title"><B>' + posted_data[i].purpose +'</B></div><div class="message">' + posted_data[i].message + '</div><div class="picture"><img src=' + posted_data[i].pic + '><div class="date">' + posted_data[i].post_time + '</div>').addTo(map);
            }else if(posted_data[i].purpose == '災害情報'){
                console.log("災害")
                L.marker([posted_data[i].lat,posted_data[i].lng], { icon: L.icon({
                    iconUrl: '/static/images/pin/pin_blue.png',
                    shadowUrl: '/static/images/pin/pin_shadow.png',
                    iconSize: [55,55], shadowSize:[100,50],
                    iconAnchor: [27,55], shadowAnchor: [35,30], popupAnchor: [0,-35]
                }) }).bindPopup('<div class="title"><B>' + posted_data[i].purpose +'</B></div><div class="message">' + posted_data[i].message + '</div><div class="picture"><img src=' + posted_data[i].pic + '><div class="date">' + posted_data[i].post_time + '</div>').addTo(map);
            }else if(posted_data[i].purpose == '落し物'){
                console.log("落とし物2")
                L.marker([posted_data[i].lat,posted_data[i].lng], { icon: L.icon({
                    iconUrl: '/static/images/pin/pin_green.png',
                    shadowUrl: '/static/images/pin/pin_shadow.png',
                    iconSize: [55,55], shadowSize:[100,50],
                    iconAnchor: [27,55], shadowAnchor: [35,30], popupAnchor: [0,-35]
                }) }).bindPopup('<div class="title"><B>' + posted_data[i].purpose +'</B></div><div class="message">' + posted_data[i].message + '</div><div class="picture"><img src=' + posted_data[i].pic + '><div class="date">' + posted_data[i].post_time + '</div>').addTo(map);
            }else if(posted_data[i].purpose == '人探し'){
                console.log("人探し")
                L.marker([posted_data[i].lat,posted_data[i].lng], { icon: L.icon({
                    iconUrl: '/static/images/pin/pin_yellow.png',
                    shadowUrl: '/static/images/pin/pin_shadow.png',
                    iconSize: [55,55], shadowSize:[55,55],
                    iconAnchor: [27,55], shadowAnchor: [35,30], popupAnchor: [0,-35]
                }) }).bindPopup('<div class="title"><B>' + posted_data[i].purpose +'</B></div><div class="message">' + posted_data[i].message + '</div><div class="picture"><img src=' + posted_data[i].pic + '><div class="date">' + posted_data[i].post_time + '</div>').addTo(map);
            }else if(posted_data[i].purpose == 'その他'){
                console.log("その他")
                L.marker([posted_data[i].lat,posted_data[i].lng], { icon: L.icon({
                    iconUrl: '/static/images/pin/pin_pink.png',
                    shadowUrl: '/static/images/pin/pin_shadow.png',
                    iconSize: [55,55], shadowSize:[100,50],
                    iconAnchor: [27,55], shadowAnchor: [35,30], popupAnchor: [0,-35]
                }) }).bindPopup('<div class="title"><B>' + posted_data[i].purpose +'</B></div><div class="message">' + posted_data[i].message + '</div><div class="picture"><img src=' + posted_data[i].pic + '><div class="date">' + posted_data[i].post_time + '</div>').addTo(map);            }
        } else {
            console.log("else")
            L.marker([posted_data[i].lat,posted_data[i].lng], { icon: L.icon({
                iconUrl: '/static/images/pin/pin_gray.png',
                shadowUrl: '/static/images/pin/pin_shadow.png',
                iconSize: [55,55], shadowSize:[100,50],
                iconAnchor: [27,55], shadowAnchor: [35,30]
            }) }).addTo(map);
        }
    }
}


            // 内部関数
            // 関数： 2点間の距離を算出
            function distance(lat1, lng1, lat2, lng2) {
                lat1 *= Math.PI / 180;
                lng1 *= Math.PI / 180;
                lat2 *= Math.PI / 180;
                lng2 *= Math.PI / 180;
                return 6371 * Math.acos(Math.cos(lat1) * Math.cos(lat2) * Math.cos(lng2 - lng1) + Math.sin(lat1) * Math.sin(lat2));
            }
            // error messege
        },
        function(error) {
            switch (error.code) {
                case 1: //PERMISSION_DENIED
                    alert("位置情報の利用が許可されていません");
                    break;
                case 2: //POSITION_UNAVAILABLE
                    alert("現在位置が取得できませんでした");
                    break;
                case 3: //TIMEOUT
                    alert("タイムアウトになりました");
                    break;
                default:
                    alert("その他のエラー(エラーコード:" + error.code + ")");
                    break;
            }
        });

}