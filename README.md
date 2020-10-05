# 寫一隻股狗網爬蟲
    一起照影片學習寫一隻股狗網的爬蟲吧！
    影片連結：https://www.youtube.com/watch?v=g49HtnX3SOo&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=9
    此代碼純學習，勿商用，勿造成他人困擾

## 發現原來GStype是每個統計圖的區塊
    透過影片中，我們要抓取股狗網的網頁資料，透過GStype裡面共有十個連結，都能把資料打印出來，這每個連結再個別去爬原始碼，就能把所有資料給抓出來了！
    https://www.stockdog.com.tw/stockdog/guest_show.php?sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e473
    https://www.stockdog.com.tw/stockdog/guest_show.php?click_btn3=1&click_btn6=1&click_btn7=1&sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e471
    https://www.stockdog.com.tw/stockdog/guest_show.php?date2=2020-09-30&sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e474
    https://www.stockdog.com.tw/stockdog/guest_show.php?sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e475&sdate=2012-06-11&edate=2020-10-05
    https://www.stockdog.com.tw/stockdog/guest_show.php?sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e476
    https://www.stockdog.com.tw/stockdog/guest_show.php?sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e477
    https://www.stockdog.com.tw/stockdog/guest_show.php?date=2020-10-05&sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e478
    https://www.stockdog.com.tw/stockdog/guest_show.php?sid=4956&GStype=114bf794d5b36fb798b7ee1293a4e6e479&day=120
    https://www.stockdog.com.tw/stockdog/guest_show.php?date=2020-10-05&sid=4956&Ym=202010&GStype=214bf794d5b36fb798b7ee1293a4e6e470
    https://www.stockdog.com.tw/stockdog/guest_show.php?date=2020-10-05&sid=4956&Ym=202010&GStype=214bf794d5b36fb798b7ee1293a4e6e472
    https://www.stockdog.com.tw/stockdog/guest_show.php?date=2020-10-05&sid=4956&Ym=202010&GStype=214bf794d5b36fb798b7ee1293a4e6e474

## 正規表達式練習！
    直接進行線上練習題,從實作中來學習完整的正規表達式
    線上考題:https://regexone.com/

## 正規表達式筆記
    *   表示0或任意字元或沒有
    +   表示1+以上個字元
    ?   表示一個字元或沒有
    
    \d  0-9任一數字
    \D  非數字任一字元
    \s  空白字元
    \S  非空白字元
    \t  對應Tab字元
    \w  對應任何文數字元包括"_"，對等於 [a-zA-Z0-9_]
    \W  對應任何非數字元，對等於[^a-zA-Z0-9_]

    ^   代表開頭
    $   代表結尾
    ()  能區分開群組，例如：檔名跟檔案類型 參考:https://regexone.com/lesson/capturing_groups?

## 已經抓出連結但爬不出東西?
    如同大家看到的，我們已經把GStype的整個連結都給打印出來了，但如果我們用單純的requests去爬資料，卻無法抓到任何東西
    今天如果你用無痕模式去直接打開連結，會直接重新跳轉到股狗網首頁，代表這些頁面不能直接做訪問，可能有做防爬蟲或保護的一些措施
    在影片中的教學，使用了request.session()的方式，來重新爬蟲這些連結，就是代表說，我們是登入過股狗網接著才查到這些資料
    如果你用一般瀏覽器再股狗網查詢後，再去貼上特殊連結，會發現可以直接看到圖表！
    