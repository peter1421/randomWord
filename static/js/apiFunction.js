function makeRequest(url) {
    xhr = new XMLHttpRequest();
    xhr.onload = function () {
        response = JSON.parse(this.response);
        console.log(response);
        $('#getRandomWord').text('已取得資料').removeAttr('disabled');
    };
    xhr.open('GET', url, true);
    xhr.send();
}
