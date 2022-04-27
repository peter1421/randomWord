{
  /* <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script> */
}

function checkJS() {
  alert("引入成功!");
}
function deleteAllCookies() {
  var cookies = document.cookie.split(";");
  for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i];
    var eqPos = cookie.indexOf("=");
    var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
  }
  console.log("cookies 清除完成");
}

function getRandom(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomWord() {
  let sentence = "";
  for (const key in response) {
    if (key == "place") {
      sentence += "在";
    }
    if (key == "addTimes") {
      continue;
    }
    // console.log(key, response[key]);
    // console.log(response[key].length)
    R = getRandom(0, response[key].length - 1);
    // console.log("getRandom:"+R)
    // console.log(response[key][R])
    // console.log(response[key][R][1])
    sentence += response[key][R][1];
  }
  console.log(sentence);
  var s = document.getElementById("sentence");
  s.innerHTML = sentence;

  window.getSelection().selectAllChildren(s);
  document.execCommand("Copy");
}
function copyWindow() {
  var toastTrigger = document.getElementById("liveToastBtn");
  var toastLiveExample = document.getElementById("liveToast");
  if (toastTrigger) {
    toastTrigger.addEventListener("click", function () {
      var toast = new bootstrap.Toast(toastLiveExample);
      toast.show();
    });
  }
}
function disabledSubmitButton02(submitButtonName, submitButtonText) {
  $("#" + submitButtonName).attr({
    disabled: "disabled",
  }); //控制按钮为禁用
  var second = 3;
  var intervalObj = setInterval(function () {
    $("#" + submitButtonName).text(submitButtonText + "(" + second + ")");
    if (second == 0) {
      $("#" + submitButtonName).text(submitButtonText);
      $("#" + submitButtonName).removeAttr("disabled"); //将按钮可用
      /* 清除已设置的setInterval对象 */
      clearInterval(intervalObj);
    }
    second--;
  }, 1000);
}
function addDataList(wordType) {
  try {
    id = "#" + wordType + "List";
    $(id).empty();
    let html = "";
    for (var i = 0; i < response[wordType].length; i++) {
      // console.log(response[wordType][i][1])
      html +=
        '<li><a class="dropdown-item" href="#" value=""' +
        response[wordType][i][1] +
        '">' +
        (i + 1) +
        ". " +
        response[wordType][i][1] +
        "</a></li>";
    }
    $(id).append(html);
  } catch {
    alert("發生錯誤!，請稍後再試");
  }
}

async function getIpClient() {
  try {
    const responseClient = await axios.get("https://api.ipify.org?format=json");
    console.log(responseClient);
  } catch (error) {
    console.error(error);
  }
}
function story() {
  str =
    "今天，動物們要舉行一次有趣的跑步比賽，他們請來了老牛作裁判，比賽前，老牛宣佈比賽規則：動物們必須戴上由自己喜歡的食物做成的項鍊參加比賽，誰能夠戴着項鍊跑到終點就能取得勝利。小猴、公雞、小狗和小貓都戴上了各自喜歡的食物項鍊精神抖擻地站在起跑線上，信心百倍地準備比賽。隨着老牛的一聲令響，動物們撒開腿向前跑去，沒跑多遠，小猴盯着桃子項鍊抓耳撓腮，差點兒摔了一跤；公雞將項鍊上的玉米數了一遍又一遍，越數心越癢；肉骨頭項鍊被小狗的口水弄得濕漉漉的了；香香的魚乾引得小貓不停地叫喚。這可怎麼辦呢？小猴看了看旁邊的公雞，想出了一個好辦法，他急忙叫住公雞，提出交換項鍊後繼續跑；小狗實在忍不住了，就停下來吃起了肉骨頭項鍊了，小貓看見了他們。心裏想：“我不能象他們那樣饞嘴，我一定要堅持到底，取得勝利。”小狗吃完了肉骨頭項鍊，很快就第一個衝到了終點；隨後小猴、小貓、公雞都先後到達終點，小狗認為他是冠軍，可是其他動物都不同意，最後老牛裁判説：“今天我們進行的可不是普通的賽跑，而是毅力賽跑，只有戴着自己的項鍊跑到終點的才能獲得冠軍，請大家檢查一下項鍊。”小狗難為情地低下了頭；小猴也紅着臉説：“我的項鍊不是我自己的...”老牛裁判接着説：“小貓在比賽中碰到困難後能夠堅持到底，小貓獲得了這次比賽的冠軍！”";
}
