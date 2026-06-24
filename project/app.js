const map = new naver.maps.Map("map", {
  center: new naver.maps.LatLng(37.5665, 126.9780), // 서울시청
  zoom: 15
});

const marker = new naver.maps.Marker({
  position: new naver.maps.LatLng(37.5665, 126.9780),
  map: map
});