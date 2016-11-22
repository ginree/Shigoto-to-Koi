label scene2_0_jp:
    scene bg station_day with dissolve

    "{rb}電車{/rb}{rt}でんしゃ{/rt}でマカティ市{rt}し{/rt}に行{rt}い{/rt}きました。"

    "この{rb}場所{/rb}{rt}ばしょ{/rt}はとても混{rt}こ{/rt}んでいて忙{rt}いそが{/rt}しいよ。この{rb}場所{/rb}{rt}ばしょ{/rt}はビルが多{rt}おお{/rt}いけど、左{rt}ひだり{/rt}に大{rt}おお{/rt}きいビルが見{rt}み{/rt}えた。"

    mc "すごい！{rb}採用{/rb}{rt}さいよう{/rt}はしているのかなー。{rb}本当{/rb}{rt}ほんとう{/rt}にあそこで働{rt}はたら{/rt}きたい！"
    mc "庭{rt}にわ{/rt}がとてもいい。床{rt}ゆか{/rt}もきれいだよ！"

    "そして、Busy-Busy {rb}会社{/rb}{rt}かいしゃ{/rt}に行{rt}い{/rt}きました."

    scene bg hall_day with dissolve

    "{rb}会場{/rb}{rt}かいじょう{/rt}は{rb}全部{/rb}{rt}ぜんぶ{/rt}白{rt}しろ{/rt}い。"

    "{rb}応接係{/rb}{rt}おうせつかかり{/rt}は「インタビューは21階{rt}かい{/rt}です」って言{rt}い{/rt}った。エレベーターに乗{rt}の{/rt}った。"

    "{rb}受験者{/rb}{rt}じゅけんしゃ{/rt}が多{rt}おお{/rt}いよ。{rb}絶対{/rb}{rt}ぜったい{/rt}{rb}有名{rt}ゆうめい{/rt}な{rb}会社{/rb}{rt}かいしゃ{/rt}だなー。"

    "{rb}根気{/rb}{rt}こんき{/rt}よくに{rb}職員{/rb}{rt}しょくいん{/rt}が{rb}名前{/rb}{rt}なまえ{/rt}を呼{rt}よ{/rt}ぶのを待{rt}ま{/rt}っていました。"

    staff "%(mc_surname)sさん, 付{rt}つ{/rt}いて来{rt}き{/rt}てください。"

    scene bg office_day with dissolve

    show ryuu suit serious
    "{rb}面接官{/rb}{rt}めんせつかん{/rt}が{rb}勤勉{/rb}{rt}きんべん{/rt}そうな男{rt}おとこ{/rt}だ。"

    "忙{rt}いそが{/rt}しいだろうが疲{rt}つか{/rt}れを見{rt}み{/rt}せなかったよ。"

    ryuu "おはよう、{rb}名前{/rb}{rt}なまえ{/rt}は{rb}重夫{/rb}{rt}しげお{/rt}竜{rt}りゅう{/rt}です。"
    $ ryuu_name = "竜{rt}りゅう{/rt}"
    ryuu "インタビューを始{rt}はじ{/rt}めます。"

    scene black with fade

    jump scene2_1_jp

    return


label scene2_1_jp:

    scene bg office_day with fade

    $ ryuu_points += 2

    show ryuu suit happy
    ryuu "{rb}会長{/rb}{rt}かいちょう{/rt}はあなたに{rb}好印象{/rb}{rt}こういんしょう{/rt}を持{rt}も{/rt}っています。"
    ryuu "{rb}会長{/rb}{rt}かいちょう{/rt}はあなたがこの{rb}会社{/rb}{rt}かいしゃ{/rt}で{rb}頑張{/rb}{rt}がんば{/rt}ると思{rt}おも{/rt}っています。"

    mc "このような{rb}機会{/rb}{rt}きかい{/rt}をありがとうございました。"
    mc "よろしくお願{rt}ねが{/rt}いして、{rb}重夫{/rb}{rt}しげお{/rt}さん。{rb}重夫{/rb}{rt}しげお{/rt}さんと{rb}一緒{/rb}{rt}いっしょ{/rt}に働{rt}はたら{/rt}くことができることがうれしいです。"

    ryuu "今{rt}いま{/rt}から、同{rt}おな{/rt}じ部{rt}ぶ{/rt}で働{rt}はたら{/rt}きます。"
    ryuu "{rb}一緒{/rb}{rt}いっしょ{/rt}にいい働{rt}はたら{/rt}きを願{rt}ねが{/rt}っています。"

    scene sky_night with fade

    "{rb}同僚{/rb}{rt}どうりょう{/rt}とすぐに{rb}友達{/rb}{rt}ともだち{/rt}になった。"

    "{rb}最初{/rb}{rt}さいしょ{/rt}の{rb}三ヶ月{/rb}{rt}さんかげつ{/rt}は{rb}一緒{/rb}{rt}いっしょ{/rt}に食{rt}た{/rt}べたり、飲{rt}の{/rt}んだり、{rb}時々{/rb}{rt}ときどき{/rt}パーティーに行{rt}い{/rt}った。"

    "Busy-busy　{rb}会社{/rb}{rt}かいしゃ{/rt}に働{rt}はたら{/rt}くのがいい{rb}選択{/rb}{rt}せんたく{/rt}だ。"

    scene bg cubicle_day with fade

    "ある日{rt}ひ{/rt}、{rb}重夫{/rb}{rt}しげお{/rt}さんが来{rt}き{/rt}た。"

    show ryuu suit happy
    ryuu "おはよう、%(mc_surname)sさん."

    mc "おはよう、{rb}重夫{/rb}{rt}しげお{/rt}さん！"

    ryuu "{rb}金曜日{/rb}{rt}きんようび{/rt}の夜{rt}よる{/rt}はお{rb}誕生日{/rb}{rt}たんじょうび{/rt}祝{rt}いわ{/rt}いがあります。"
    ryuu "いつもは{rb}大学{/rb}{rt}だいがく{/rt}の{rb}友達{/rb}{rt}ともだち{/rt}を誘{rt}さそ{/rt}っているんだけど、{rb}全員{/rb}{rt}ぜんいん{/rt}忙{rt}いさが{/rt}しいんだ。"
    ryuu "来{rt}こ{/rt}られるか？"

    # Selection 2.1
    menu:
        "はい、もちろん！{rb}形式的{/rb}{rt}けいしきてき{/rt}な祝{rt}いわ{/rt}いですか？":
            # result 2.1.1
            $ ryuu_points += 2

            $ decision_party = True

            "このような良{rt}よ{/rt}い{rb}理由{/rb}{rt}りゆう{/rt}なら、断{rt}ことわ{/rt}られない。"

            show ryuu suit grin
            ryuu "来{rt}き{/rt}てくれて、嬉{rt}うれ{/rt}しいよ。"
            ryuu "それは弟{rt}おとうと{/rt}の{rb}七歳{/rb}{rt}ななさい{/rt}のお{rb}誕生日{/rb}{rt}たんじょうび{/rt}です。"
            ryuu "母{rt}はは{/rt}は遠{rt}とお{/rt}い所{rt}ところ{/rt}に住{rt}す{/rt}んでいるから、母{rt}はは{/rt}も来{rt}こ{/rt}られない。弟{rt}おとうと{/rt}と{rb}二人{/rb}{rt}ふたり{/rt}で住{rt}す{/rt}んでいるから、{rb}会社{/rb}{rt}かいしゃ{/rt}の{rb}友達{/rb}{rt}ともだち{/rt}が来{rt}く{/rt}ることがいいと思{rt}おも{/rt}いました。"
            ryuu "実{rt}じつ{/rt}はあまり{rb}形式的{/rb}{rt}けいしきてき{/rt}じゃないよ。好{rt}す{/rt}きな服{rt}ふく{/rt}を着{rt}き{/rt}て来{rt}き{/rt}ていいよ。"

            scene black with fade

            jump scene2_2_jp

        "あのさ、ええと{rb}用事{/rb}{rt}ようじ{/rt}があると思{rt}おも{/rt}いますが。":
            # result 2.1.2

            $ decision_party = False

            "{rb}金曜日{/rb}{rt}きんようび{/rt}の夜{rt}よる{/rt}？「Ang Probinsyano」の{rb}最後{/rb}{rt}さいご{/rt}の{rb}挿話{/rb}{rt}そうわ{/rt}が{rb}発表{/rb}{rt}はっぴょう{/rt}するよ。"

            show ryuu suit sad
            ryuu "そうですか。じゃあ、ほかの人{rt}ひと{/rt}に聞{rt}き{/rt}いてみるね。"

            scene black with fade

            jump scene3_0_jp

    return


label scene2_2_jp:

    scene bg frontdoor_night with fade

    stop music fadeout 1.0
    play music "music/tora.mp3" loop

    show tora openmouth at mid_left
    show ryuu casual happy at mid_right

    ryuu "こんばんは、%(mc_surname)sさん。"
    mc "こんばんは、{rb}重夫{/rb}{rt}しげお{/rt}さん！"
    ryuu "ここなら、竜{rt}りゅう{/rt}と呼{rt}よ{/rt}んでもいいよ。"
    ryuu "これが弟{rt}おとうと{/rt}です。虎{rt}とら{/rt}です。"

    tora "来{rt}き{/rt}てくれたんだ！ありがとう!遊{rt}あそ{/rt}ぼうよ。"
    tora "あなたとCall of Duty 2で遊{rt}あそ{/rt}びたいよ。"

    mc "もちろん！!"

    scene black with fade

    scene bg frontdoor_night with fade

    "{rb}色々{/rb}{rt}いろいろ{/rt}なパーティーのゲームの後{rt}あと{/rt}、帰{rt}かえ{/rt}らなきゃ。"

    show ryuu casual happy at mid_right
    show tora smile at mid_left

    ryuu "来{rt}き{/rt}てくれてありがとう。"
    mc "誘{rt}さそ{/rt}ってくれてありがとう。{rb}本当{/rb}{rt}ほんとう{/rt}に楽{rt}たの{/rt}しかったよ！"
    tora "ねえ、%(mc_sib)sと呼{rt}よ{/rt}んでもいい？"

    # Selection 2.2
    menu:
        "もちろん！":
            # result 2.2.1

            $ ryuu_points += 3
            $ decision_tora = True

            show tora grin at mid_left
            tora "やったー!!"
            tora "僕{rt}ぼく{/rt}とおにいちゃんは楽{rt}たの{/rt}しかった、ありがとう！"
            tora "ねえ、おにいちゃん、%(mc_sib)sとデートしたら、%(mc_sib)sが{rb}時々{/rb}{rt}ときどき{/rt}来{rt}こ{/rt}られる？"
            show ryuu casual blush at mid_right
            ryuu "虎{rt}とら{/rt}!"
            tora "{rb}冗談{/rb}{rt}じょうだん{/rt}だよ！"
            tora "好{rt}す{/rt}きだから来{rt}こ{/rt}れるって、もっと遊{rt}あそ{/rt}ぼう。"

        "ええと、やだよ。":
            # result 2.2.2

            $ ryuu_points -=2
            $ decision_tora = False

            show ryuu casual worried at mid_right
            show tora sad at mid_left
            tora "あ、聞{rt}き{/rt}いてすみません。"
            tora "あのお、話{rt}はな{/rt}したくないよ。"


    scene black with fade
    jump scene3_0_jp

    return


label scene3_0_jp:
    scene bg cubicle_day with fade

    stop music fadeout 1.0
    play music "music/intro.mp3" loop

    "{rb}土曜日{/rb}{rt}どようび{/rt}。{rb}昨夜{/rb}{rt}さくや{/rt}は楽{rt}たの{/rt}しすぎたから、{rb}仕事{/rb}{rt}しごと{/rt}に{rb}集中{/rb}{rt}しゅうちゅう{/rt}ことが{rb}簡単{/rb}{rt}かんたん{/rt}だった。"
    "{rb}相変{/rb}{rt}あいか{/rt}わらず{rb}重夫{/rb}{rt}しげお{/rt}さんも{rb}頑張{/rb}{rt}がんば{/rt}っていると思{rt}おも{/rt}う。"

    scene bg cubicle_noon with dissolve

    "昼{rt}ひる{/rt}ご飯{rt}はん{/rt}の後{rt}あと{/rt}、私{rt}わたし{/rt}のところに来{rt}き{/rt}た。"

    if decision_party:

        if decision_tora:
            show ryuu suit grin
            ryuu "{rb}昨晩{/rb}{rt}さくばん{/rt}はありがとう。虎{rt}とら{/rt}は{rb}非常{/rb}{rt}ひじょう{/rt}に嬉{rt}うれ{/rt}しかったよ。"
            show ryuu suit grinblush
            ryuu "虎{rt}とら{/rt}が変{rt}へん{/rt}なことを言{rt}い{/rt}ってごめん。"

            mc "{rb}大丈夫{/rb}{rt}だいじょうぶ{/rt}よ。虎{rt}とら{/rt}くんは優{rt}やさ{/rt}しそうね。"
            mc "{rb}友達{/rb}{rt}ともだち{/rt}になったように遊{rt}あそ{/rt}んだよ。"

            show ryuu suit grin
            ryuu "そうだね。"
            show ryuu suit sad
            ryuu "虎{rt}とら{/rt}は僕{rt}ぼく{/rt}だけと住{rt}す{/rt}んでいることが寂{rt}さび{/rt}しいのかもしれない。"

        else:
            show ryuu suit happy
            ryuu "弟{rt}おとうと{/rt}のお{rb}誕生日{/rb}{rt}たんじょうび{/rt}に来{rt}き{/rt}てくれて、ありがとう。"
            show ryuu suit sad
            ryuu "でも、弟{rt}おとうと{/rt}は「%(mc_sib)s」に言{rt}い{/rt}わせるのは良{rt}よ{/rt}いと思{rt}おも{/rt}うよ。"
            show ryuu suit happy
            ryuu "悲{rt}かな{/rt}しまないで、あの弟{rt}おとうと{/rt}の{rb}態度{/rb}{rt}たいど{/rt}が珍{rt}めずら{/rt}しいだけ。"

        show ryuu suit happy
        ryuu "まあ、{rb}今日{/rb}{rt}きょう{/rt}の{rb}用事{/rb}{rt}ようじ{/rt}が終{rt}お{/rt}わってしまったから、暇{rt}ひま{/rt}そうだ。"
        ryuu "後{rt}あと{/rt}では何{rt}なん{/rt}にもすることがない。後{rt}あと{/rt}でどこかに行{rt}い{/rt}きませんか？"

    else:
        show ryuu suit happy
        ryuu "{rb}今日{/rb}{rt}きょう{/rt}の{rb}用事{/rb}{rt}ようじ{/rt}が終{rt}お{/rt}わってしまったから、暇{rt}ひま{/rt}そうだ。"
        ryuu "後{rt}あと{/rt}では何{rt}なん{/rt}にもすることがない。後{rt}あと{/rt}でどこかに行{rt}い{/rt}きませんか？"

    # Selection 3.0
    menu:
        "もちろん！":
            # result 3.0.1

            $ ryuu_points += 2

            show ryuu suit happy
            ryuu "いいよ!"

            if decision_party:
                show ryuu suit grin
                ryuu "あのね、弟{rt}おとうと{/rt}の祝{rt}いわ{/rt}いに来{rt}き{/rt}てくれたので、ごちそうしなくちゃ。"
                ryuu "{rb}本当{/rb}{rt}ほんとう{/rt}に、あなたは優{rt}やさ{/rt}しい。"
            else:
                ryuu "{rb}本当{/rb}{rt}ほんとう{/rt}に、あなたは優{rt}やさ{/rt}しい。"

            mc "おい、{rb}重夫{/rb}{rt}しげお{/rt}さんがご{rb}馳走{/rb}{rt}さそう{/rt}してよ！"
            mc "食{rt}た{/rt}べ物{rt}もの{/rt}のでお礼{rt}れい{/rt}をしなきゃいけないよ。"

            show ryuu suit happyblush
            ryuu "{rb}本当{/rb}{rt}ほんとう{/rt}に、あなたのそんな顔{rt}かお{/rt}はかわいいな。"

            "何{rt}なに{/rt}行{rt}い{/rt}った…？"

            jump scene3_1_jp

        "寝{rt}ね{/rt}たほうがいいと思{rt}おも{/rt}いますね。外{rt}ほか{/rt}に私{rt}わたし{/rt}も{rb}用事{/rb}{rt}ようじ{/rt}がまだたくさんし。":
            # result 3.0.2

            "{rb}週末{/rb}{rt}しゅうまつ{/rt}、{rb}仕事{/rb}{rt}しごと{/rt}の{rb}心配{/rb}{rt}しんぱい{/rt}したくないよ。"
            "{rb}出世{/rb}{rt}しゅっせ{/rt}したいなら、{rb}頑張{/rb}{rt}がんば{/rt}らないと。"

            mc "実{rt}じつ{/rt}は{rb}残業{/rb}{rt}ざんぎょう{/rt}するつもりだ。"

            show ryuu suit surprised
            ryuu "{rb}今日{/rb}{rt}きょう{/rt}は{rb}用事{/rb}{rt}ようじ{/rt}をしなくてもいいそうだけど、来{rt}き{/rt}たくないって{rb}本当{/rb}{rt}ほんとう{/rt}ですか？"

            mc "はい。ごめん。"

            show ryuu suit sad
            ryuu "{rb}残念{/rb}{rt}ざんねん{/rt}だなー。"
            show ryuu suit happy
            ryuu "じゃあ、また{rb}明日{/rb}{rt}あした{/rt}！"

            jump scene4_0_jp

    return


label scene3_1_jp:
    scene bg cubicle_night with dissolve

    "{rb}用事{/rb}{rt}ようじ{/rt}を早{rt}はや{/rt}ければ終{rt}お{/rt}わってしまったから、早{rt}はや{/rt}く出{rt}で{/rt}かけた。"

    scene bg restaurant_night with dissolve

    stop music fadeout 1.0
    play music "music/restaurant.mp3" loop

    "彼{rt}かれ{/rt}は{rb}有名{/rb}{rt}ゆうめい{/rt}なレストランに連{rt}つ{/rt}れて行った。"
    "このレストランに{rb}一回{/rb}{rt}いっかい{/rt}行{rt}い{/rt}った。"
    "{rb}毎日{/rb}{rt}まいにち{/rt}は{rb}電車{/rb}{rt}でんしゃ{/rt}の中{rt}なか{/rt}で見{rt}み{/rt}えたんだけど、そのレストランに行{rt}い{/rt}くことのイメージがまだ思{rt}おも{/rt}えない。"

    scene bg restaurant_indoor with dissolve

    "メニューが{rb}非常{/rb}{rt}ひじょう{/rt}に高{rt}たか{/rt}い。"
    "{rb}五日{/rb}{rt}いつか{/rt}ぐらい食{rt}た{/rt}べらなきゃいけなかった。"
    "例{rt}たと{/rt}えば、二{rt}ふた{/rt}つ小{rt}ちい{/rt}さい魚{rt}さかな{/rt}が{rb}五百{/rb}{rt}ごひゃく{/rt}ペソぐらい。"
    "その{rb}料理{/rb}{rt}りょうり{/rt}は{rb}一番{/rb}{rt}いちばん{/rt}高{rt}たか{/rt}い{rb}料理{/rb}{rt}りょうり{/rt}と思{rt}おも{/rt}った。ところが、{rb}一番{/rb}{rt}いちばん{/rt}安{rt}やす{/rt}かった{rb}料理{/rb}{rt}りょうり{/rt}だよ！"
    "でも、{rb}空気{/rb}{rt}くうき{/rt}が良{rt}よ{/rt}かった。レストランの{rb}空気{/rb}{rt}くうき{/rt}が天{rt}てん{/rt}の{rb}空気{/rb}{rt}くうき{/rt}みたかった。"
    "いかを食{rt}た{/rt}べてみた。生{rt}う{/rt}まれた時{rt}とき{/rt}から、{rb}非常{/rb}{rt}ひじょう{/rt}に{rb}美味{/rb}{rt}おい{/rt}しいいかを食{rt}た{/rt}べられました！"
    "味{rt}あじ{/rt}が流{rt}なが{/rt}れすぎた。"
    "飲{rt}の{/rt}み物{rt}もの{/rt}も{rb}高品質{/rb}{rt}こうひんしつ{/rt}だ。"
    "フランスのシャンペンを飲{rt}の{/rt}んで、お酒{rt}さけ{/rt}を飲{rt}の{/rt}んだ。"
    "食{rt}た{/rt}べるの後{rt}あと{/rt}は、{rb}重夫{/rb}{rt}しげお{/rt}さん{rb}全部{/rb}{rt}ぜんぶ{/rt}払{rt}はら{/rt}った。{rb}重夫{/rb}{rt}しげお{/rt}さんを聞{rt}き{/rt}いた、「{rb}大丈夫{/rb}{rt}だいじょうぶ{/rt}」ってた。"
    "彼{rt}かれ{/rt}にお返{rt}かえ{/rt}しするつもりと思{rt}おも{/rt}っている。"
    "でも、{rb}重夫{/rb}{rt}しげお{/rt}さん…いいえ、竜{rt}りゅう{/rt}さん…私{rt}わたし{/rt}が好{rt}す{/rt}き？"

    scene sky_night with fade

    stop music fadeout 1.0
    play music "music/sad.mp3" loop

    "レストランで食{rt}た{/rt}べる時{rt}とき{/rt}は竜{rt}りゅう{/rt}さんが私{rt}わたし{/rt}に{rb}時々{/rb}{rt}ときどき{/rt}見{rt}み{/rt}てることを見{rt}み{/rt}たと思{rt}おも{/rt}い出{rt}だ{/rt}した。"
    "彼{rt}かれ{/rt}の目{rt}め{/rt}を見{rt}み{/rt}たら、{rb}笑顔{/rb}{rt}えがお{/rt}をみせる。"
    "{rb}会社{/rb}{rt}かいしゃ{/rt}で、{rb}食堂{/rb}{rt}しょくどう{/rt}に{rb}一緒{/rb}{rt}いっしょ{/rt}に行{rt}い{/rt}ったら、{rb}時々{/rb}{rt}ときどき{/rt}彼{rt}かれ{/rt}の手{rt}て{/rt}を触{rt}さわ{/rt}りたい。"
    "触{rt}さわ{/rt}りたんだけど、手{rt}て{/rt}をたまたま触{rt}さわ{/rt}らせったら、{rb}緊張{/rb}{rt}きんちょう{/rt}して、手{rt}て{/rt}を引{rt}ひ{/rt}いた。"
    "私{rt}わたし{/rt}のバカ！"

    scene sky_noon with dissolve
    "いつもそのことだ。"
    "竜{rt}りゅう{/rt}さんが怒{rt}おこ{/rt}った{rb}時間{/rb}じかん{rt}{/rt}がなかった。彼{rt}かれ{/rt}が{rb}非常{/rb}{rt}ひじょう{/rt}に優{rt}やさ{/rt}しいだけ！"
    "{rb}本当{/rb}{rt}ほんとう{/rt}に、私{rt}わたし{/rt}が{rb}勿体{/rb}{rt}もったい{/rt}無{rt}な{/rt}いかもしれない。"
    "{rb}三ヶ月{/rb}{rt}さんかげつ{/rt}{rb}一緒{/rb}{rt}いっしょ{/rt}に{rb}友達{/rb}{rt}ともだち{/rt}と付{rt}つ{/rt}き合{rt}あ{/rt}うなのに、彼{rt}かれ{/rt}をまだ知{rt}し{/rt}ってると思{rt}おも{/rt}うんだ。"
    "始{rt}はじ{/rt}まりに彼{rt}かれ{/rt}が{rb}建前{/rb}{rt}たてまえ{/rt}を使{rt}つか{/rt}ってくれたかもしれない。"

    # Selection 3.1
    menu:
        "{rb}本音{/rb}{rt}ほんね{/rt}と思{rt}おも{/rt}うんだ。何{rt}なに{/rt}も{rb}心配{/rb}{rt}しんぱい{/rt}しないと思{rt}おも{/rt}うんだ。":
            $ ryuu_points += 1
            jump scene4_0_jp

        "{rb}建前{/rb}{rt}たてまえ{/rt}と思{rt}おも{/rt}うんだから、ちょっと信{rt}しん{/rt}じない。":
            $ ryuu_points -= 1
            jump scene3_2_jp

    return


label scene3_2_jp:
    scene sky_day with dissolve
    "{rb}先週{/rb}{rt}せんしゅう{/rt}、彼{rt}かれ{/rt}の{rb}内心{/rb}{rt}ないしん{/rt}についてことを思{rt}おも{/rt}った。"
    "竜{rt}りゅう{/rt}さんが私{rt}わたし{/rt}にあまり正{rt}ただ{/rt}さないことに山{rt}やま{/rt}をかけるなら良くと思{rt}おも{/rt}った。"
    "でも、全{rt}す{/rt}てが頭{rt}あたま{/rt}の中{rt}なか{/rt}だけだ。{rb}出来{/rb}{rt}でき{/rt}れば{rb}終息{/rb}{rt}しゅうそく{/rt}したい。"
    "…それをした。"

    scene cubicle_noon with fade

    stop music fadeout 1.0
    play music "music/intro.mp3" loop

    show ryuu suit sad
    mc "竜{rt}りゅう{/rt}さん、聞{rt}き{/rt}いてもいい？"
    "竜{rt}りゅう{/rt}さんが悲{rt}かな{/rt}しそう。珍{rt}めずら{/rt}しい。"
    "虎{rt}とら{/rt}くんは{rb}最近{/rb}{rt}さいきん{/rt}竜{rt}りゅう{/rt}さんがあまり{rb}元気{/rb}{rt}げんき{/rt}じゃないと言{rt}い{/rt}ってたと思{rt}おも{/rt}う。"

    show ryuu suit surprised
    ryuu "あっ, %(mc_gname)sさん."
    ryuu "いいよ。何{rt}なに{/rt}？"

    # Selection 4.1
    menu:
        "始{rt}はじ{/rt}まりから、竜{rt}りゅう{/rt}さんは優{rt}やさ{/rt}しくているんですが、あのさ、竜{rt}りゅう{/rt}さんが{rb}本当{/rb}{rt}ほんとう{/rt}に優{rt}やさ{/rt}しいかなー。":
            $ ryuu_points -= 2
            # result 4.1.1

            ryuu "えっ？どんな言{rt}い{/rt}うか？"
            mc "あなた…優{rt}やさ{/rt}しすぎると思{rt}おも{/rt}っているし。"
            mc "そのことは{rb}建前{/rb}{rt}たてまえ{/rt}かもしれないと思{rt}おも{/rt}っているし。"

            show ryuu suit mad
            ryuu "はっ？あなたが僕{rt}ぼく{/rt}の{rb}態度{/rb}{rt}たいど{/rt}を疑{rt}うたが{/rt}っているの？"
            ryuu "なんて頭{rt}あたま{/rt}に入{rt}い{/rt}れたんだ？"

            "怒{rt}おこ{/rt}った… つづく?"

            # Selection 4.2
            menu:
                "やっぱり、{rb}敬遠{/rb}{rt}けいえん{/rt}する人{rt}ひと{/rt}があなただ。{rb}余人{/rb}{rt}よじん{/rt}の{rb}気配{/rb}{rt}きくば{/rt}りをもらえるように、{rb}敬遠{/rb}{rt}けいえん{/rt}している。":

                    $ ryuu_points -= 3

                    ryuu "今{rt}いま{/rt}まで、僕{rt}ぼく{/rt}についてあなたの思{rt}おも{/rt}いことが知{rt}し{/rt}らなかった。"
                    ryuu "かわいそう。"
                    ryuu "働{rt}はたら{/rt}き者{rt}もの{/rt}だけど、この{rb}会社{/rb}{rt}かいしゃ{/rt}では、この{rb}会社員{/rb}{rt}かいしゃいん{/rt}に{rb}態度{/rb}{rt}たいど{/rt}も尊{rt}とうと{/rt}んでいるんだ。"
                    ryuu "{rb}自業自得{/rb}{rt}じごうじとく{/rt}だ。{rb}社長室{/rb}{rt}しゃちょうしつ{/rt}に行って、その{rb}態度{/rb}{rt}たいど{/rt}については話{rt}はな{/rt}します。"
                    ryuu "{rb}失礼{/rb}{rt}しつれい{/rt}します。"

                    mc "もういいよ。どの道{rt}みち{/rt}、辞{rt}や{/rt}めるつもりだ。"
                    ryuu "そのことは全{rt}すべ{/rt}て優{rt}やさ{/rt}しくなりました。"
                    ryuu "%(mc_surname)sさん、{rb}会社{/rb}{rt}かいしゃ{/rt}で、{rb}連携{/rb}{rt}れんけい{/rt}にありがとう。"

                    jump bad_jp

                "疑{rt}うたが{/rt}わないよ。この方{rt}ほう{/rt}に慣{rt}な{/rt}れっこじゃないし。それを話{rt}はな{/rt}してごめん。":
                    # result 4.2.2

                    $ ryuu_points += 3

                    show ryuu suit serious
                    ryuu "{rb}大丈夫{/rb}{rt}だいじょうぶ{/rt}だよ。"
                    ryuu "実{rt}じつ{/rt}は、あなたが正{rt}まさ{/rt}しくなってくれて、ありがとう。"
                    show ryuu suit sad
                    ryuu "そのことを言{rt}い{/rt}ってる{rb}一番{/rb}{rt}いちばん{/rt}人{rt}ひと{/rt}があなただ。"

                    if ryuu_points >= 12:
                        ryuu "お先{rt}さき{/rt}に忘{rt}わす{/rt}れましょう。"
                        show ryuu suit happy
                        ryuu "ああ、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}について話{rt}はな{/rt}していた。"
                        ryuu "実{rt}じつ{/rt}は{rb}寿司{/rb}{rt}すし{/rt}がほしいよ。"
                        show ryuu suit grin
                        ryuu "食{rt}た{/rt}べて行{rt}い{/rt}こうよ。"
                        mc "いいね！竜{rt}りゅう{/rt}さんに奢{rt}おご{/rt}ってあげる。"
                        show ryuu suit surprised
                        ryuu "それは{rb}大丈夫{/rb}{rt}だいじょうぶ{/rt}？"
                        mc "じゃあ、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}があなたをご{rb}馳走{/rb}{rt}さそう{/rt}してもいい？"
                        mc "いつもいつも竜{rt}りゅう{/rt}さんが払{rt}はら{/rt}ったんだけど。では、私{rt}わたし{/rt}、お返{rt}かえ{/rt}しをしなきゃと思{rt}おも{/rt}う。"
                        jump scene4_0_1_jp

                    else:
                        ryuu "実{rt}じつ{/rt}は…　私{rt}わたし{/rt}も正{rt}まさ{/rt}しくなりたい。"
                        show ryuu suit serious
                        ryuu "あなたと話{rt}はな{/rt}してもいい？"
                        jump scene4_0_2_jp

        "{rb}先週{/rb}{rt}せんしゅう{/rt}{rb}木曜日{/rb}{rt}もくようび{/rt}虎{rt}とら{/rt}くんに寄{rt}よ{/rt}ってあげた。虎{rt}とら{/rt}くんは「{rb}最近{/rb}{rt}さいきん{/rt}竜{rt}りゅう{/rt}さんが気{rt}き{/rt}があまり良くない」ってた。":
            # result 4.1.2

            $ ryuu_points += 3

            show ryuu suit serious
            ryuu "弟{rt}おとうと{/rt}とを寄{rt}よ{/rt}ってくれてありがとう。"
            show ryuu suit sad
            ryuu "はい、{rb}最近{/rb}{rt}さいきん{/rt}はちょっと気{rt}き{/rt}が悪{rt}わる{/rt}いだ。"
            ryuu "{rb}仕事{/rb}{rt}しごと{/rt}が{rb}非常{/rb}{rt}ひじょう{/rt}に忙{rt}いそが{/rt}しいし。締{rt}し{/rt}め切{rt}き{/rt}りが{rb}次々{/rb}{rt}つぎつぎ{/rt}にあったし。"
            ryuu "{rb}会長{/rb}{rt}かいちょう{/rt}が頼{rt}たの{/rt}んだ{rb}発表{/rb}{rt}はっぴょう{/rt}を{rb}準備{/rb}{rt}じゅんび{/rt}している。あの{rb}発表{/rb}{rt}はっぴょう{/rt}の締{rt}し{/rt}め切{rt}き{/rt}りも{rb}明日{/rb}{rt}あした{/rt}。"

            mc "{rb}大変{/rb}{rt}たいへん{/rt}ですね。"
            mc "じゃあ、{rb}発表{/rb}{rt}はっぴょう{/rt}はもう終{rt}お{/rt}わったから、あなたに助{rt}たす{/rt}ける"
            show ryuu suit surprised
            mc "それに、暇{rt}ひま{/rt}じゃないから、{rb}今度{/rb}{rt}こんど{/rt}は昼{rt}ひる{/rt}ご飯{rt}はん{/rt}にご{rb}馳走{/rb}{rt}さそう{/rt}だ。"
            mc "いい？"

            if ryuu_points >=5:
                show ryuu suit surprised
                ryuu "それは{rb}大丈夫{/rb}{rt}だいじょうぶ{/rt}？"
                mc "じゃあ、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}があなたをご{rb}馳走{/rb}{rt}さそう{/rt}してもいい？"
                mc "いつもいつも竜{rt}りゅう{/rt}さんが払{rt}はら{/rt}ったんだけど。では、私{rt}わたし{/rt}、お返{rt}かえ{/rt}しをしなきゃと思{rt}おも{/rt}う。"
                jump scene4_0_1_jp
            else:
                show ryuu suit serious
                ryuu "実{rt}じつ{/rt}は、%(mc_gname)sさんと話{rt}はな{/rt}したい。"
                jump scene4_0_2_jp

label scene4_0_jp:
    scene sky_day with dissolve

    stop music fadeout 1.0
    play music "music/sad.mp3" loop

    "彼{rt}かれ{/rt}に{rb}初回{/rb}{rt}しょかい{/rt}会{rt}あ{/rt}うことは１年{rt}ねん{/rt}ぐらい。"
    "{rb}無数{/rb}{rt}むすう{/rt}のパーティーと飲{rt}の{/rt}み会{rt}かい{/rt}が{rb}一緒{/rb}{rt}いっしょ{/rt}に行{rt}い{/rt}った。でも、{rb}二人{/rb}{rt}ふたり{/rt}はまだ{rb}友達{/rb}{rt}ともだち{/rt}です。"
    "それでも、たびにそのパーティーと飲{rt}の{/rt}み会{rt}かい{/rt}に行{rt}い{/rt}ったら、あなたに見{rt}み{/rt}ると彼{rt}かれ{/rt}が{rb}感情{/rb}{rt}かんじょう{/rt}を見{rt}み{/rt}せられなそう。"
    "私も{rb}感情{/rb}{rt}かんじょう{/rt}を見{rt}み{/rt}せられない。"

    scene bg cubicle_day with fade

    stop music fadeout 1.0
    play music "music/intro.mp3" loop

    "今{rt}いま{/rt}竜{rt}りゅう{/rt}さんが悲{rt}かな{/rt}しそう。珍{rt}めずら{/rt}しいなあ。"
    "{rb}普段{/rb}{rt}ふだん{/rt}の{rb}時間{/rb}{rt}じだん{/rt}はここに来{rt}き{/rt}ない。"
    "{rb}仕事{/rb}{rt}{/rt}に忙{rt}いそが{/rt}しいから、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}を食{rt}た{/rt}べないことに決{rt}た{/rt}めるかもしれないなあ。"
    "{rb}先週{/rb}{rt}せんしゅう{/rt}{rb}木曜日{/rb}{rt}もくようび{/rt}虎{rt}とら{/rt}くんに寄{rt}よ{/rt}った時{rt}とき{/rt}、「{rb}最近{/rb}{rt}さいきん{/rt}竜{rt}りゅう{/rt}ちゃんが気{rt}き{/rt}が悪{rt}わる{/rt}い」ってた。"
    "でも、なぜまだ働{rt}はたら{/rt}いているんだよ？"
    "私{rt}わたし{/rt}が構{rt}かま{/rt}っていると言{rt}い{/rt}わなきゃかもしれない。"
    "彼{rt}かれ{/rt}が昼{rt}ひる{/rt}ご飯{rt}はん{/rt}に誘{rt}さそ{/rt}うことが{rb}完璧{/rb}{rt}かんぺき{/rt}と思{rt}さそ{/rt}う。今{rt}いま{/rt}はまだ{rb}昼食時{/rb}{rt}ちゅうしょくじ{/rt}から、あまり変{rt}へん{/rt}じゃなかったと思{rt}おも{/rt}う。"
    "何{rt}なに{/rt}しってる？"

    # Selection 4.0
    menu:
        "昼{rt}ひる{/rt}ごはんに誘{rt}さそ{/rt}う":
            # result 4.0.1

            $ ryuu_points += 3

            scene bg cubicle_noon with dissolve
            show ryuu suit serious
            mc "ねぇ、何{rt}なに{/rt}か食{rt}た{/rt}べに行く？"

            show ryuu suit surprised
            ryuu "あっ! %(mc_gname)sさん..."

            if ryuu_points >= 12:
                ryuu "僕{rt}ぼく{/rt}はいつも昼{rt}ひる{/rt}ご飯{rt}はん{/rt}に誘{rt}さそ{/rt}っている。"
                ryuu "言{rt}い{/rt}ったらいいだけど、僕{rt}ぼく{/rt}に誘{rt}さそ{/rt}うことがちょっと変{rt}へん{/rt}そう。"
                mc "ぜんぜん変{rt}へん{/rt}じゃないよ。"
                mc "ええと、ああ、{rb}今度{/rb}{rt}こんど{/rt}は私{rt}わたし{/rt}{rb}何々{/rb}{rt}なになに{/rt}をしてあげたいし。"
                mc "じゃあ、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}があなたをご{rb}馳走{/rb}{rt}さそう{/rt}してもいい？"
                mc "いつもいつも竜{rt}りゅう{/rt}さんが払{rt}はら{/rt}ったんだけど。では、私{rt}わたし{/rt}、お返{rt}かえ{/rt}しをしなきゃと思{rt}おも{/rt}う。"
                jump scene4_0_1_jp

            else:
                show ryuu suit sad
                ryuu "今{rt}いま{/rt}はちょっと…"
                "竜{rt}りゅう{/rt}さんは忙しそう。"
                show ryuu suit serious
                ryuu "実{rt}じつ{/rt}は、%(mc_gname)sさんと話{rt}さなしたい{/rt}したい。"
                jump scene4_0_2_jp

        "彼{rt}かれ{/rt}を言{rt}い{/rt}うことを待{rt}ま{/rt}って":

            $ ryuu_points += 1

            scene bg cubicle_noon with dissolve
            if ryuu_points >= 12:
                show ryuu suit happy
                ryuu "昼{rt}ひる{/rt}ごはんを食{rt}たべ{/rt}べに行{rt}い{/rt}きたい？"
                mc "あっ、竜{rt}りゅう{/rt}さん！いいね。行{rt}い{/rt}こう！竜{rt}りゅう{/rt}さんに奢{rt}おご{/rt}ってあげよう。"
                show ryuu suit surprised
                ryuu "それは{rb}大丈夫{/rb}{rt}だいじょうぶ{/rt}？"
                mc "じゃあ、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}があなたをご{rb}馳走{/rb}{rt}ちそう{/rt}してもいい？"
                mc "いつもいつも竜{rt}りゅう{/rt}さんが払{rt}はら{/rt}ったんだけど。では、私{rt}わたし{/rt}、お返{rt}かえ{/rt}しをしなきゃと思{rt}おも{/rt}う。"
                jump scene4_0_1_jp

            else:
                show ryuu suit serious
                ryuu "%(mc_gname)sさんと話{rt}はな{/rt}したい。"
                jump scene4_0_2_jp

    return


label scene4_0_1_jp:

    show ryuu suit surprised
    ryuu "そうか。いいね。"
    show ryuu suit grin
    ryuu "ほかにこの間{rt}あいだ{/rt}の買{rt}か{/rt}い物{rt}もの{/rt}が高{rt}たか{/rt}すぎたそう。"
    ryuu "レストランの食{rt}た{/rt}べ物{rt}もの{/rt}も高{rt}たか{/rt}すぎた。"
    ryuu "{rb}今度{/rb}{rt}こんど{/rt}{rb}財布{/rb}{rt}さいふ{/rt}を使{rt}つか{/rt}わなきゃね。"

    mc "違{rt}ちが{/rt}うよ。"
    mc "ええと、あ、構{rt}かま{/rt}うだけ。"

    show ryuu suit surprisedblush
    ryuu "あなた…今{rt}いま{/rt}、何{rt}なに{/rt}を言{rt}い{/rt}ってる？構{rt}かま{/rt}うか？"

    "やばい!!"

    mc "何{rt}なん{/rt}でもない！"
    mc "早{rt}はや{/rt}く行{rt}い{/rt}こうよ。お腹{rt}はら{/rt}が空{rt}す{/rt}いてるよ。"
    mc "{rb}寿司{/rb}{rt}すし{/rt}を食{rt}た{/rt}べようよ。"

    show ryuu suit grinblush
    ryuu "いいよ。"

    jump scene4_1_jp
    return


label scene4_0_2_jp:
    mc "私{rt}わたし{/rt}？どうしたの？"
    ryuu "言{rt}い{/rt}わなきゃいけないだけど、あなただけがこの{rb}会話{/rb}{rt}かいわ{/rt}を聞{rt}あ{/rt}かなくちゃ。"

    scene bg roadside_noon with dissolve

    stop music fadeout 1.0
    play music "music/sad.mp3" loop

    "{rb}一緒{/rb}{rt}いっしょに{/rt}に{rb}散歩{/rb}した。あまり込{rt}こ{/rt}んでいない。"

    "竜{rt}りゅう{/rt}さんは急{rt}きゅう{/rt}に話{rt}はなした{/rt}した。"

    show ryuu suit sad
    ryuu "それは早{rt}はや{/rt}く話{rt}はな{/rt}さなきゃ。"
    mc "え？なんで？どういうの？まだわからないよ。"
    show ryuu suit serious
    ryuu "乱{rt}みだ{/rt}れたくないけど、その{rb}事体{/rb}{rt}じだい{/rt}がつづけるなら、もうできないかも知{rt}し{/rt}れないよ。"
    mc "何{rt}なに{/rt}…？"
    ryuu "僕{rt}ぼく{/rt}たちの{rb}関係{/rb}{rt}かんけい{/rt}… {rb}全部{/rb}{rt}ぜんぶ{/rt}早すぎるんだ。"

    show ryuu suit sad
    ryuu "僕{rt}ぼく{/rt}の{rb}仕草{/rb}{rt}しぐさ{/rt}、ごめん。"
    ryuu "でも、{rb}仕事{/rb}{rt}しごと{/rt}に{rb}集中{/rb}{rt}しゅうちゅう{/rt}したい。"

    show ryuu suit worried
    ryuu "それなのに、あなたに僕{rt}ぼく{/rt}の感{rt}かん{/rt}じをまだ消さない。{rb}同僚{/rb}{rt}どうりょう{/rt}...{rb}会社{/rb}{rt}かいしゃ{/rt}で働{rt}はたら{/rt}いなきゃだけ。"
    ryuu "{rb}会長{/rb}{rt}かいちょう{/rt}がぼくたちを見{rt}み{/rt}えるどう？そして、僕{rt}ぼく{/rt}たちが{rb}友達{/rb}{rt}ともだち{/rt}だけことを思{rt}おも{/rt}わなければいけない。"

    show ryuu suit sad
    ryuu "それなのに、あなたに僕{rt}ぼく{/rt}の感{rt}かん{/rt}じをまだ消{rt}け{/rt}さない。"
    ryuu "聞{rt}き{/rt}かされてごめん。"
    ryuu "まだできない物{rt}もの{/rt}について{rb}全部{/rb}{rt}ぜんぶ{/rt}がみだれます。"
    ryuu "僕{rt}ぼく{/rt}が変{rt}へん{/rt}のように見{rt}み{/rt}ないでくれ。"

    mc "ごめんなさい。実{rt}じつ{/rt}は私{rt}わたし{/rt}も同{rt}かんじ{/rt}じ。"
    show ryuu suit surprised
    mc "私{rt}わたし{/rt}も{rb}実感{/rb}{rt}じゅかん{/rt}をまだ表{rt}あらわ{/rt}せなかった。"
    mc "あなたは言{rt}い{/rt}えたと思{rt}おも{/rt}ったから、あなたに待{rt}も{/rt}っている。"
    mc "あなたの感{rt}かん{/rt}じることがわかった。ぜんぜん変{rt}へん{/rt}じゃないよ。{rb}二人{/rb}は同{rt}おな{/rt}じだけ。"
    mc "{rb}友達{/rb}{rt}ともだち{/rt}…だね？じゃあ、その{rb}選択{/rb}{rt}せんたく{/rt}を選{rt}えら{/rt}んだったら、いいよ。"

    mc "{rb}友達{/rb}{rt}だち{/rt}だけが良{rt}よ{/rt}くなると思{rt}おも{/rt}う。泣{rt}な{/rt}かないでください。"

    show ryuu suit happy
    ryuu "聞{rt}き{/rt}いてくれてありがとう。"
    ryuu "そのことを言{rt}い{/rt}ったまだ信{rt}しん{/rt}じられない。"
    ryuu "言{rt}い{/rt}ったことが考{rt}かんが{/rt}えなかったでしょうか。"
    show ryuu suit sad
    ryuu "頭{rt}あたま{/rt}を失{rt}うしな{/rt}うと思{rt}おも{/rt}う。"

    mc "{rb}大丈夫{/rb}{rt}{/rt}よ。同{rt}かん{/rt}じ感{rt}かん{/rt}じているよ。"
    mc "私{rt}わたし{/rt}に正{rt}ただ{/rt}しいになってくれてありがとう。"
    mc "多{rt}おお{/rt}い物{rt}もの{/rt}がまだしなきゃいけなかったけど、そのことはまだ入られない。"
    mc "竜{rt}りゅう{/rt}さんは竜{rt}りゅう{/rt}くんだ。その{rb}事体{/rb}{rt}じたい{/rt}で、あなたたちがその話{rt}はな{/rt}せない物{rt}もの{/rt}が{rb}出来{/rb}{rt}しゅったい{/rt}ます。"
    mc "{rb}自明{/rb}{rt}じめい{/rt}物{rt}もの{/rt}についてだけを話{rt}はな{/rt}したら、竜{rt}りゅう{/rt}さんと私{rt}わたし{/rt}について習{rt}なら{/rt}えなかった。"
    mc "実{rt}じつ{/rt}は、これは{rb}失敗{/rb}{rt}しっぱい{/rt}じゃないよ。この{rb}会話{/rb}{rt}かいわ{/rt}が{rb}友達{/rb}{rt}ともだち{/rt}にもっと近{rt}ちか{/rt}づくことにチャンスだ。"
    mc "その方{rt}ほう{/rt}がいいだね？"

    show ryuu suit grin
    ryuu "もういいよ。ありがとう。どもありがとう。"

    jump neutral_jp
    return


label scene4_1_jp:
    scene sushi with dissolve

    show ryuu suit happy
    ryuu "おにぎりとカリフォルニア巻{rt}まき{/rt}お願{rt}ねがい{/rt}いします。"
    mc "はい、{rb}荒巻{/rb}{rt}あらまき{/rt}お願いします。"

    scene sushi with fade

    show ryuu suit happy
    ryuu "お先{rt}さき{/rt}には、昼{rt}ひる{/rt}ご飯{rt}はん{/rt}に誘{rt}さそ{/rt}うの前{rt}まえ{/rt}には、なにを言{rt}い{/rt}ってる？"

    "しまった、それにまかり通{rt}とお{/rt}ったとおもった。"

    mc "別{rt}べつ{/rt}に。"
    mc "昼{rt}ひる{/rt}ご飯{rt}はん{/rt}に誘{rt}さそ{/rt}かっただけ。"

    show ryuu suit grin
    ryuu "僕{rt}ぼく{/rt}に構{rt}かま{/rt}ったっけ？"

    "えっ！やれやれ。うそをつくことに{rb}無駄{/rb}{rt}むだ{/rt}だ。"

    mc "はい。構{rt}かま{/rt}うよ。"
    mc "それが{rb}友達{/rb}{rt}ともだち{/rt}が気{rt}き{/rt}が悪{rt}わる{/rt}かったら、{rb}自然{/rb}{rt}じぜん{/rt}な{rb}人間{/rb}{rt}にんげん{/rt}を感{rt}かん{/rt}じてでしょう？"

    show ryuu suit happy
    ryuu "ええ。それは本{rt}ほん{/rt}から読{rt}よ{/rt}んだし。"
    show ryuu suit happyblush
    ryuu "あの本{rt}ほん{/rt}が「人{rt}ひと{/rt}が構{rt}かま{/rt}ったら、あの人{rt}ひと{/rt}が上{rt}うえ{/rt}のチャンスが…」ってた…まあ、言{rt}い{/rt}いたくないよ。でも、もう知{rt}し{/rt}ってるでしょう？"

    # Selection 4.3.
    menu:
        "まだ知{rt}し{/rt}らないよ。何{rt}なん{/rt}て言{rt}い{/rt}ってる？上{rt}うえ{/rt}のチャンスが…":
            # result 4.3.1

            $ ryuu_points += 2

            show ryuu suit shyhappy
            ryuu "あの人{rt}ひと{/rt}があなたが好{rt}す{/rt}き、とか。"
            ryuu "でも、何{rt}なに{/rt}か思{rt}おも{/rt}ってる…"
            mc "何{rt}なに{/rt}？"

            show ryuu suit worriedblush
            ryuu "何{rt}なに{/rt}かならどうと思{rt}おも{/rt}ってる。"
            mc "何{rt}なに{/rt}かなら何{rt}なん{/rt}で？"
            show ryuu suit shyhappy
            ryuu "その本{rt}ほん{/rt}が{rb}真実{/rb}{rt}しんじつ{/rt}ならどう？"
            mc "あっ、ええと、帰{rt}し{/rt}らなきゃね。遅{rt}おそ{/rt}くてはいけないよ。"
            show ryuu suit grinblush
            ryuu "じゃあ、行{rt}い{/rt}こう。"

        "読{rt}よ{/rt}んでしまって良{rt}よ{/rt}かったよ。":
            # result 4.3.2
            show ryuu suit grin
            ryuu "じゃあ、行{rt}い{/rt}こう。"

    jump scene4_1_1_jp

    return

label scene4_1_1_jp:
    scene station_noon with dissolve

    "{rb}会社{/rb}{rt}かいしゃ{/rt}に行{rt}い{/rt}った時{rt}とき{/rt}、{rb}同僚{/rb}{rt}どうりょう{/rt}が帰{rt}かえ{/rt}っている見{rt}み{/rt}えました。"
    "{rb}会社{/rb}{rt}かいしゃ{/rt}が{rb}整備{/rb}{rt}せいび{/rt}しているんだ。{rb}明日{/rb}{rt}あした{/rt}まで{rb}整備{/rb}{rt}せいび{/rt}を続{rt}つづ{/rt}けるよ。"
    "竜{rt}りゅう{/rt}くんがだれかに{rb}電話{/rb}{rt}でんわ{/rt}をしています。"

    show ryuu suit surprised
    ryuu "はい、はい、わかりました。ありがとうございました。"
    mc "{rb}会長{/rb}{rt}かいちょう{/rt}ですか？"
    show ryuu suit serious
    ryuu "はい。{rb}全部{/rb}{rt}ぜんぶ{/rt}の{rb}用事{/rb}{rt}ようじ{/rt}が{rb}来週{/rb}{rt}らいしゅう{/rt}に延{rt}の{/rt}びた。"
    ryuu "まあ、ファイルについて、メールにセーブデータがあるので、家{rt}いえ{/rt}でできる。"
    show ryuu suit happy
    ryuu "それから、{rb}発表{/rb}{rt}はっぴょう{/rt}に{rb}手伝{/rb}{rt}てつだ{/rt}わなくていいよ。"

    "へー休{rt}やす{/rt}みの日{rt}ひ{/rt}だな。何{rt}なに{/rt}をしてる？"

    # Selection 4.4.
    menu:
        "どこかに行{rt}い{/rt}きたい？":
            $ ryuu_points += 2
            show ryuu suit grin
            ryuu "いいね。行{rt}{/rt}こう！"

            jump scene4_2_jp

        "早{rt}はや{/rt}く帰{rt}かえ{/rt}ったほうがいいと思{rt}おも{/rt}う。":
            mc "いいね。"
            mc "じゃあ、帰{rt}かえ{/rt}る。またね！"
            show ryuu suit grin
            ryuu "ありがとう。"
            jump neutral_bridge_jp

    return

label scene4_2_jp:

    scene bg toy_shop with dissolve

    stop music fadeout 1.0
    play music "music/tora.mp3" loop

    "{rb}先日{/rb}{rt}せんじつ{/rt}は{rb}割引券{/rb}{rt}わりびきけん{/rt}を得{rt}え{/rt}たから、おもちゃ屋{rt}ひる{/rt}に行{rt}い{/rt}った。"
    "竜{rt}りゅう{/rt}くんが青{rt}あお{/rt}い縫{rt}ぬ{/rt}いぐるみを買{rt}か{/rt}ってくれた。"
    "竜{rt}りゅう{/rt}くんが「ぼくの{rb}趣味{/rb}{rt}しゅみ{/rt}が縫{rt}ぬ{/rt}いぐるみを作{rt}作って{/rt}ること」ってた。"

    show ryuu suit happy
    ryuu "母{rt}はは{/rt}が縫{rt}ぬ{/rt}いぐるみを編{rt}あ{/rt}むことを教{rt}おし{/rt}えてくれました。"
    ryuu "始{rt}はじ{/rt}まりはしたくないけど、早{rt}はや{/rt}。"

    ryuu "{rb}毎日{/rb}{rt}まいにち{/rt}、{rb}二三個{/rb}{rt}にさんそ。{/rt}ぐらいを作{rt}つく{/rt}れました。{rb}元気{/rb}{rt}げんき{/rt}なら、{rb}十個{/rb}{rt}じゅうこ{/rt}を作{rt}つく{/rt}れました。それから、{rb}時々{/rb}{rt}ときどき{/rt}、食{rt}た{/rt}べることを忘{rt}わす{/rt}れちゃった。"
    mc "私も母{rt}はは{/rt}に何{rt}なに{/rt}かを習{rt}なら{/rt}ってもらった。"
    mc "{rb}料理{/rb}{rt}りょうり{/rt}するのがまだ始{rt}{/rt}まりました時{rt}とき{/rt}、母{rt}はは{/rt}は「完{rt}かん{/rt}ぺき卵{rt}たまご{/rt}」を作{rt}つく{/rt}ることを教{rt}おし{/rt}えてくれた。"
    mc "そして、母{rt}はは{/rt}が私{rt}わたし{/rt}に{rb}家族{/rb}{rt}かぞく{/rt}のためにアドボを作{rt}つく{/rt}らせた。"

    show ryuu suit grin
    ryuu "ハハハ！あなたのお母{rt}かあ{/rt}さんが{rb}面白{/rb}{rt}おもしろい{/rt}そうなー。"
    ryuu "お母{rt}かあ{/rt}さんが{rb}将来{/rb}{rt}しょうらい{/rt}。会{rt}あ{/rt}いたいよ。"

    scene bg sky_noon with dissolve

    "{rb}午後{/rb}{rt}ごご{/rt}が早{rt}はや{/rt}く過{rt}す{/rt}ぎた。空{rt}そら{/rt}が黒{rt}くろ{/rt}くなる。"
    "でも、{rb}土曜日{/rb}{rt}どようび{/rt}だから、{rb}明日{/rb}{rt}あした{/rt}{rb}仕事{/rb}{rt}あした{/rt}に行{rt}い{/rt}くことに{rb}心配{/rb}{rt}しんぱい{/rt}することない。"

    scene bg game_center with dissolve
    "ゲームセンターに行{rt}い{/rt}って、テディベアを勝{rt}か{/rt}った！"
    "おもちゃ屋{rt}や{/rt}の{rb}社長{/rb}{rt}しゃちょう{/rt}{rb}友達{/rb}{rt}ともだち{/rt}、フェリシャさんが会{rt}あ{/rt}った。"
    "フェリシャさんが「同{rt}おな{/rt}じおもちゃ屋{rt}や{/rt}で働{rt}はたら{/rt}いている幼{rt}おさな{/rt}なじみが会{rt}あ{/rt}った」ってたから、{rb}最近{/rb}{rt}さいきん{/rt}フェリシャさんは嬉{rt}うれ{/rt}しい見{rt}み{/rt}たい。"

    scene bg park_night with dissolve

    "もう夜{rt}よる{/rt}？"
    show ryuu suit grin
    ryuu "はー、楽{rt}たの{/rt}しかったよ。"
    ryuu "ここで{rb}休息{/rb}{rt}きゅうそく{/rt}して。"
    mc "うん、私{rt}わたし{/rt}も疲{rt}つか{/rt}れた。"

    "ちょっと休{rt}やす{/rt}む…"

    scene black with fade

    jump good_jp
    return


label good_jp:

    scene bg park_dusk with fade

    stop music fadeout 1.0
    play music "music/good.mp3" loop

    "へー？寝{rt}ね{/rt}たの？{rb}何時{/rb}{rt}なんじ{/rt}？"
    "ああ、{rb}午後{/rb}{rt}ごご{/rt}１１：４５。暖{rt}あたた{/rt}かいと感{rt}かん{/rt}じました。{rb}時間{/rb}{rt}じかん{/rt}が気{rt}き{/rt}づけなかった。"

    "何{rt}なに{/rt}これ？竜{rt}りゅう{/rt}くんのジャケットか？"

    show ryuu suit surprisedblush
    "竜{rt}りゅう{/rt}くんに{rb}突如{/rb}{rt}とつじょ{/rt}見{rt}み{/rt}て、私{rt}わたし{/rt}に見{rt}み{/rt}ていることを見{rt}み{/rt}た。"
    "{rb}現行犯{/rb}{rt}げんこうはん{/rt}のように、驚{rt}おどろ{/rt}きたそう。"
    show ryuu suit happyblush
    "{rb}赤面{/rb}{rt}せきめん{/rt}する見{rt}み{/rt}たいことを終{rt}お{/rt}わって、{rb}元気{/rb}{rt}げんき{/rt}になりました。{rb}笑顔{/rb}{rt}えがお{/rt}を見{rt}み{/rt}せた。"
    "{rb}緊張{/rb}{rt}きんちょう{/rt}の代{rt}か{/rt}わりに暖{rt}あたた{/rt}かくて楽{rt}らく{/rt}と感{rt}かん{/rt}じました。"
    "この感{rt}かん{/rt}じが{rb}以前{/rb}{rt}いぜん{/rt}いぜん）とは違{rt}ちが{/rt}う。"
    "今{rt}いま{/rt}{rb}二人{/rb}{rt}ふたり{/rt}だけから、この感{rt}かん{/rt}じがもう強{rt}つよ{/rt}くなった。純{rt}{/rt}{rt}じゅん{/rt}になった。"
    "{rb}楽以外{/rb}{rt}らくいがい{/rt}何{rt}なに{/rt}も感{rt}かん{/rt}じると手{rt}て{/rt}を取{rt}と{/rt}った。"
    "迫{rt}せま{/rt}っていると、ジャケットの懐{rt}ふところ{/rt}が重{rt}おも{/rt}そうことを気{rt}き{/rt}づけた。"
    "懐{rt}ふところ{/rt}の中{rt}なか{/rt}で外{rt}ほか{/rt}の手{rt}て{/rt}を抜{rt}ぬ{/rt}け出{rt}だ{/rt}した。これ、本{rt}ほん{/rt}？"

    show ryuu suit grinblush
    ryuu "あのさ、その本{rt}ほん{/rt}をまだ考{rt}かんが{/rt}えているよ。"
    mc "これ？"

    "その本{rt}ほん{/rt}は{rb}恋仲{/rb}{rt}こいなか{/rt}の本{rt}ほん{/rt}。"
    "その本{rt}ほん{/rt}では、デートについて{rb}方法{/rb}{rt}ほうほう{/rt}と人{rt}ひと{/rt}が誰{rt}だれ{/rt}かが好{rt}す{/rt}きの{rb}気配{/rb}{rt}きはい{/rt}がある。"
    "多いページでは{rb}手書{/rb}{rt}てがき{/rt}なノートがある。誰{rt}だれ{/rt}かを{rb}勉強{/rb}{rt}べんきょう{/rt}してしまったそう。"
    "後{rt}うし{/rt}ろのページに繰{rt}く{/rt}った。もう{rb}手書{/rb}{rt}てがき{/rt}きなノートがある。その{rb}言葉{/rb}{rt}ことば{/rt}…"
    "もう{rb}一度{/rb}{rt}いちど{/rt}見{rt}み{/rt}た。"
    "彼{rt}かれ{/rt}が手{rt}て{/rt}を触{rt}さわ{/rt}ると、見{rt}み{/rt}た。"

    mc "はい、そうだ。"

    scene black with fade
    return


label neutral_bridge_jp:
    scene bg cubicle_noon with fade:

    "{rb}月曜日{/rb}{rt}げつようび{/rt}は、昼{rt}ひる{/rt}ごはんの前{rt}まえ{/rt}に、竜{rt}りゅう{/rt}くんが来{rt}き{/rt}た。"
    show ryuu suit serious
    ryuu "あなたと話{rt}はな{/rt}したい。"
    jump scene4_0_2_jp


label neutral_jp:
    scene bg bar_night with fade

    stop music fadeout 1.0
    play music "music/neutral.mp3" loop

    "{rb}人生{/rb}{rt}じんせい{/rt}の{rb}選択{/rb}{rt}せんたく{/rt}なら、{rb}時間{/rb}{rt}じかん{/rt}がかかなくて、{rb}状態{/rb}{rt}しょうたい{/rt}に考{rt}かんが{/rt}えなきゃいけないと。"

    "{rb}会社{/rb}{rt}かいしゃ{/rt}では、{rb}同席{/rb}{rt}どうせき{/rt}して楽{rt}たの{/rt}しい{rb}友達{/rb}{rt}ともだち{/rt}がいるよ。{rb}友達{/rb}{rt}ともだち{/rt}、特{rt}とく{/rt}に竜{rt}りゅう{/rt}くんが今{rt}いま{/rt}{rb}信頼{/rb}{rt}しんらい{/rt}している。"
    "{rb}幹事{/rb}{rt}かんじ{/rt}に挙{rt}あ{/rt}がったから、この夜{rt}よる{/rt}が祝{rt}いわっている{/rt}"
    "竜{rt}りゅう{/rt}くんは、{rb}六ヶ月{/rb}{rt}ろっかげつ{/rt}前{rt}まえ{/rt}は私{rt}わたし{/rt}に言{rt}い{/rt}ったが正{rt}ただ{/rt}しいと思{rt}おも{/rt}います。"
    "全{rt}まった{/rt}くあの{rb}選択{/rb}{rt}せんたく{/rt}を追{rt}お{/rt}い求{rt}もと{/rt}めることに{rb}時間{/rb}{rt}じかん{/rt}がかかなきゃ。"
    "私{rt}わたし{/rt}の{rb}選択{/rb}{rt}せんたく{/rt}について、今{rt}いま{/rt}、{rb}元気{/rb}{rt}げんき{/rt}になると思{rt}おも{/rt}う。でも、あの{rb}可能性{/rb}{rt}かのうせい{/rt}が{rb}時々{/rb}{rt}ときどき{/rt}まだ思{rt}おも{/rt}ってる。"
    "竜{rt}りゅう{/rt}くんがそのことを言{rt}い{/rt}わなかったどう？"
    "{rb}社則{/rb}{rt}しゃそく{/rt}ながら、彼{rt}かれ{/rt}が恐{rt}おそ{/rt}れたどう？"
    "それなのに、{rb}二人{/rb}{rt}ふたり{/rt}はまだ嬉{rt}うれ{/rt}しいだ。"

    coworkers "お～い！もう飲{rt}の{/rt}もうよ！"
    show ryuu suit grin
    ryuu "おい！{rb}会社{/rb}{rt}かいしゃ{/rt}にいないけど、まだ%(mc_gname)sが{rb}幹事{/rb}{rt}かんじ{/rt}よ。"
    ryuu "早{rt}はや{/rt}く、 %(mc_gname)s！"
    mc "来{rt}き{/rt}てる！"

    scene black with fade
    return


label bad_jp:
    scene bg cubicle_night with fade

    stop music fadeout 1.0
    play music "music/sad.mp3" loop

    "{rb}社長室{/rb}{rt}しゃちょうしつ{/rt}から出{rt}で{/rt}ながら、竜{rt}りゅう{/rt}さんにもらった{rb}辞表{/rb}{rt}じひょう{/rt}）を読{rt}よ{/rt}んでいる。"
    "{rb}諸条件{/rb}{rt}しょじょうけん{/rt}の{rb}列挙{/rb}{rt}れっきょ{/rt}が付{rt}い{/rt}きました。"
    "何{rt}なに{/rt}これ？「{rb}特定{/rb}{rt}とくてい{/rt}人{rt}ひと{/rt}と合{rt}あ{/rt}わなければいけない」って。"
    "この{rb}会社{/rb}{rt}かいしゃ{/rt}、変{rt}へん{/rt}なことがあるそう。"
    "{rb}社長室{/rb}{rt}しゃちょうしつ{/rt}のドアを開{rt}あ{/rt}けてみたけど、鍵{rt}かぎ{/rt}をかけている。"

    scene bg cubicle_off with dissolve

    stop music fadeout 1.0
    play music "music/bad.mp3" loop

    "{rb}電気{/rb}{rt}でんき{/rt}が{rb}突如{/rb}{rt}とつじょ{/rt}。閉{rt}し{/rt}まった。何{rt}なに{/rt}も見{rt}み{/rt}えない。"
    "全{rt}すべ{/rt}ては真{rt}ま{/rt}っ黒{rt}くろ{/rt}だ。"
    "あのキュービクルから{rb}電気{/rb}{rt}でんき{/rt}を見{rt}み{/rt}て、{rb}徐々{/rb}{rt}に来{rt}来{/rt}ます。"

    mc "{rb}今晩{/rb}{rt}こんばんは{/rt}は？このフォームでは、このキュービクルで合{rt}あ{/rt}わなければいけませんか？"
    mc "キュービクル４４ですか？私{rt}わたし{/rt}と会{rt}あ{/rt}う人{rt}ひと{/rt}ですか？"

    show hanako smile
    "その人{rt}ひと{/rt}が振{rt}ふ{/rt}り替{rt}か{/rt}えた。顔{rt}かお{/rt}が{rb}絶対{/rb}{rt}ぜつたい{/rt}にわかりません。"
    "その人{rt}ひと{/rt}が{rb}笑顔{/rb}{rt}えがお{/rt}を見{rt}み{/rt}せる。"

    hanako "ええ、その人{rt}ひと{/rt}が私{rt}わたし{/rt}だ。"
    mc "お{rb}名前{/rb}{rt}まえ{/rt}は教{rt}おし{/rt}えてくれませんか？"
    mc "{rb}我々{/rb}{rt}われわれ{/rt}は知{rt}し{/rt}られない{rb}場所{/rb}{rt}ばしょ{/rt}でいる{rb}気付{/rb}{rt}きづ{/rt}きました。"
    hanako "{rb}花子{/rb}{rt}はなこ{/rt}です。もっと何{rt}なん{/rt}でもない。"
    $ hanako_name = "{rb}花子{/rb}{rt}はなこ{/rt}"
    hanako "外{rt}ほか{/rt}の{rb}選択肢{/rb}{rt}せんたくし{/rt}があるのがまだ知{rt}し{/rt}ってるのに、この方{rt}ほう{/rt}を選{rt}えら{/rt}んだね。"
    mc "どんな言{rt}い{/rt}うか？"
    hanako "全{rt}すべ{/rt}てはゲームだけ。選{rt}えら{/rt}ぶのが{rb}出来損{/rb}{rt}できそこ{/rt}ない。"
    hanako "今{rt}いま{/rt}から、君{rt}きみ{/rt}は私{rt}わたし{/rt}とずっとここにいる。"
    mc "何{rt}なに{/rt}が{rb}残念{/rb}{rt}ざんねん{/rt}だ？"
    mc "まだ知{rt}し{/rt}られないでしまいました。"
    show hanako grin
    hanako "ああ、思{rt}おも{/rt}い出{rt}だ{/rt}さないか？僕{rt}ぼく{/rt}は１７番{rt}ばん{/rt}の聞{rt}あ{/rt}く{rb}練習{/rb}{rt}れんしゅう{/rt}の中{rt}なか{/rt}で。"
    mc "まさか！怖{rt}こわ{/rt}い{rb}練習{/rb}{rt}れんしゅう{/rt}を終{rt}お{/rt}わると思った。"

    "だめだ。どんあ罰{rt}ばち{/rt}を開{rt}あ{/rt}けてしまった？"

    hanako "そうじゃないよ。思{rt}おも{/rt}い出{rt}だ{/rt}したか？じゃあ、その{rb}選択肢{/rb}{rt}せんたくし{/rt}ので、君{rt}きみ{/rt}が目{rt}め{/rt}に合{rt}あ{/rt}わなきゃ。"
    hanako "じゃあ、せ～の。"
    hanako "好{rt}す{/rt} {w=1.0}き {w=1.0}だ {w=1.0}よ～"
    mc "辞{rt}や{/rt}めて… {w=1.0} 辞{rt}や{/rt}めて… {w=1.0}"
    mc "ヤメテェーーーー!!!!" with hpunch
    mc "ながい{rb}先生{/rb}{rt}せんせい{/rt}、助{rt}たす{/rt}けてーーーー！!!!!" with hpunch

    scene black with fade

    "そして、体{rt}からだ{/rt}が固{rt}かた{/rt}めてしまった。"
    return
