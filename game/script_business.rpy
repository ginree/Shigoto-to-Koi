label scene1_business_en:
    "Business"
    return

label scene1_business_jp:
    scene bg station_day with fade

    "電車でマカチ市にいきました。"

    "この場所は非常(ひじょう)に込んで忙(いそが)しいよ。このところでビルが多い。"

    "歩きながら、左(ひだり)に大きいビルを見た。"

    mc "すげえ！このビルではたらきたい！ぜったいにはたらきたい！"

    "Busy-Busy会社に行きました。"

    scene bg hall_day with fade

    "エレベーターのボタンを押した。"

    "２１階に行って求職係と会いました。"

    scene bg office_day with fade

    "あなたの名前を聞く前は待ちました。求職係は部屋に連れていった。"

    jump scene2_business_jp

    return

label scene2_business_jp:

    scene black
    show text "初見" with Pause(1.0)

    scene bg office_day with fade

    "インタビューは結構でした。会長はあなたは仕事に本当に頑張ると思います。"

    "求職係は名前が竜さんと言った。竜さんさんは同じ部で働きます。竜さんも会長も会社に迎えをもらいました。"

    "頑張っているので、始まりから、新しい友達が作った。一緒(いっしょ)に食(た)べて、飲(の)んで時々パチイーに行きました。"

    "あの三月は早く過ぎた。"

    scene bg cubicle_day with fade

    "ある日、竜さんさん何か聞いた。"

    show ryuu suit happy

    ryuu "金曜日の夜は誕生祝いがあります。"

    show ryuu suit sad

    ryuu "でも、全部友達が用事があるんです。"

    show ryuu suit happy

    ryuu "来られるか？"

    menu:

        "はい、もちろん！形式的な祝いですか？":

            show ryuu suit grin
            ryuu "賛成した嬉しいです。"
            ryuu "この祝いは弟の七歳の誕生日です。"
            ryuu "母は遠いところに住んでいるから、来られない。"
            ryuu "今、弟と家に住んでいるますから、友達が来られたもいいと思いました。"
            ryuu "形式的じゃないですよ。好きな服を着れるよ。"

            jump scene2_party_business_jp

        "あのさ、ええと用事があると思いますね。。。来週がいい？":

            show ryuu suit sad
            ryuu "はい、余人を聞いてもいいですが…"
            jump scene3_business_jp

    return

label scene2_party_business_jp:

    scene bg frontdoor_night with fade
    show otouto openmouth

    otouto "来たから嬉しい！"
    otouto "親切のおかげでありがとうございました。"
    otouto "お姉ちゃんは言ってもいい？"

    menu:

        "もちろん！":
            show otouto grin
            otouto "やった！"
            otouto "お姉さん、私とお兄ちゃんは嬉しいになるので、ありがとう！"
            otouto "お姉ちゃんとお兄さんはちょうどいいと思いますよ。"
            show ryuu casual blush at right
            ryuu "ちょ…ちょっと…"

        "ええと、お姉ちゃんはちょっと。。。":
            show otouto sad
            otouto "そうか。。。はい。でも。。。話したくないよ。"

    scene black
    show text "to be continued"
    return

label scene3_business_jp:

    "selection 3.3"

    return
