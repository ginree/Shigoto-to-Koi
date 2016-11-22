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
    $ ryuu_name = "竜"
    ryuu "インタビューを始{rt}はじ{/rt}めます。"

    scene black with fade

    jump scene2_1_jp

    return


label scene2_1_jp:

    scene bg office_day with fade

    $ ryuu_points += 2

    show ryuu suit happy
    ryuu "会長はあなたに好印象を持っています。"
    ryuu "会長はあなたがこの会社で頑張ると思っています。"

    mc "このような機会をありがとうございました。"
    mc "よろしくお願いして、重夫さん。重夫さんと一緒に働くことができることがうれしいです。"

    ryuu "今から、同じ部で働きます。"
    ryuu "一緒にいい働きを願（ねが）っています。"

    scene sky_night with fade

    "同僚とすぐに友達になった。"

    "最初の三ヶ月は一緒に食べたり、飲んだり、時々パーティーに行った。"

    "Busy-busy　会社に働くのがいい選択だ。"

    scene bg cubicle_day with fade

    "ある日、竜さんが来た。"

    show ryuu suit happy
    ryuu "おはよう、%(mc_surname)sさん."

    mc "おはよう、重夫さん！"

    ryuu "金曜日の夜は誕生祝（いわ）いがあります。"
    ryuu "いつもは大学の友達を誘っているんだけど、全員忙しいんだ。"
    ryuu "来られるか？"

    # Selection 2.1
    menu:
        "はい、もちろん！形式的（けいしきてき）な祝いですか？":
            # result 2.1.1
            $ ryuu_points += 2

            $ decision_party = True

            "このような良い理由なら、断（ことわ）られない。"

            show ryuu suit grin
            ryuu "来てくれて、嬉しいよ。"
            ryuu "それは弟（おとうと）の七歳のお誕生日です。"
            ryuu "母は遠（とお）い所に住んでいるから、母も来られない。弟と一人で住んでいるから、会社の友達が来ることがいいと思いました。"
            ryuu "実はあまり形式的（けいしきてき）じゃないよ。好きな服 （ふく）を着て来ていいよ。"

            scene black with fade

            jump scene2_2_jp

        "あのさ、ええと用事があると思いますが。":
            # result 2.1.2

            $ decision_party = False

            "金曜日の夜？「Ang Probinsyano」の最後（さいご）の挿話（そうわ）が発表するよ。"

            show ryuu suit sad
            ryuu "そうですか。じゃあ、ほかの人に聞いてみるね。"

            scene black with fade

            jump scene3_0_jp

    return


label scene2_2_jp:

    scene bg frontdoor_night with fade
    show tora openmouth at mid_left
    show ryuu casual happy at mid_right

    ryuu "こんばんは、%(mc_surname)sさん。"
    mc "こんばんは、重雄さん！"
    ryuu "ここなら、竜と読んでもいいよ。"
    ryuu "これが弟です。虎です。"

    tora "来てくれたんだ！ありがとう!遊（あそ）ぼうよ。"
    tora "あなたとCOD2で遊びたいよ。"

    mc "もちろん！!"

    scene black with fade

    scene bg frontdoor_night with fade

    "色々なパーティーのゲームの後、帰らなきゃ。"

    show ryuu casual happy at mid_right
    show tora smile at mid_left

    ryuu "来てくれてありがとう。"
    mc "さそってくれてありがとう。本当に楽しかったよ！"
    tora "ねえ、%(mc_sib)sと呼んでもいい？"

    # Selection 2.2
    menu:
        "もちろん！":
            # result 2.2.1

            $ ryuu_points += 3
            $ decision_tora = True

            show tora grin at mid_left
            tora "やったー!!"
            tora "僕とお兄ちゃんは楽しかった、ありがとう！"
            tora "ねえ、お兄ちゃん、%(mc_sib)sとデートしたら、%(mc_sib)sが時々来られる？"
            show ryuu casual blush at mid_right
            ryuu "虎!"
            tora "冗談だよ！"
            tora "好きだから来れるって、もっと遊ぼう。"

        "ええと、やだよ。":
            # result 2.2.2

            $ ryuu_points -=2
            $ decision_tora = False

            show ryuu casual worried at mid_right
            show tora sad at mid_left
            tora "あ、聞いてすみません。"
            tora "あのお、話したくないよ。"


    scene black with fade
    jump scene3_0_jp

    return


label scene3_0_jp:
    scene bg cubicle_day with fade

    "土曜日。昨夜（さくや）は楽しすぎたから、仕事に集中（しゅうちゅう）ことが簡単だった。"
    "相変わらず（あいかわらず）竜さんも頑張っていると思う。"

    scene bg cubicle_noon with dissolve

    "昼ご飯の後、私のところに来た。"

    if decision_party:

        if decision_tora:
            show ryuu suit grin
            ryuu "昨晩はありがとう。虎くんは非常に嬉（うれ）しかったよ。"
            show ryuu suit grinblush
            ryuu "虎が変なことを言ってごめん。"

            mc "大丈夫よ。虎くんは優しそうね。"
            mc "友達になったように遊んだよ。"

            show ryuu suit grin
            ryuu "そうだね。"
            show ryuu suit sad
            ryuu "虎は僕だけと住んでいることが寂しいのかもしれない。"

        else:
            show ryuu suit happy
            ryuu "弟のお誕生日に来てくれて、ありがとう。"
            show ryuu suit sad
            ryuu "でも、弟は「%(mc_sib)s」に言わせるのは良いと思うよ。"
            show ryuu suit happy
            ryuu "悲しまないで、あの弟の態度（たいど）が珍（めずら）しいだけ。"

        show ryuu suit happy
        ryuu "まあ、今日の用事（ようじ）が終（お）わってしまったから、暇（ひま）そうだ。"
        ryuu "後では何にもつることがない。後でどこかに行きませんか？"

    else:
        show ryuu suit happy
        ryuu "今日の用事（ようじ）が終（お）わってしまったから、暇（ひま）そうだ。"
        ryuu "後では何にもつることがない。後でどこかに行きませんか？"

    # Selection 3.0
    menu:
        "もちろん！":
            # result 3.0.1

            $ ryuu_points += 2

            show ryuu suit happy
            ryuu "いいよ!"

            if decision_party:
                show ryuu suit grin
                ryuu "あのね、弟の祝いに来てくれたので、ごちそうしなくちゃ。"
                ryuu "本当に、あなたは優しい。"
            else:
                ryuu "本当に、あなたは優しい。"

            mc "おい、竜さんがご馳走してよ！"
            mc "食べ物のでお礼をしなきゃいけないよ。"

            show ryuu suit happyblush
            ryuu "本当に、あなたのそんな顔はかわいいな。"

            "何行った…？"

            jump scene3_1_jp

        "寝（ね）たほうがいいと思いますね。外（ほか）に私も用事がまだたくさんし。":
            # result 3.0.2

            "週末、仕事の心配したくないよ。"
            "出世（しゅっせ）したいなら、頑張らないと。"

            mc "実は残業(ざんぎょう)するつもりだ。"

            show ryuu suit surprised
            ryuu "今日は用事をしなくてもいいそうだけど、来たくないって本当ですか？"

            mc "はい。ごめん。"

            show ryuu suit sad
            ryuu "残念（ざんねん）だなあ。"
            show ryuu suit happy
            ryuu "じゃあ、また明日！"

            jump scene4_0_jp

    return


label scene3_1_jp:
    scene bg cubicle_night with dissolve

    "用事を早ければ終わってしまったから、早く出かけた。"

    scene bg restaurant_night with dissolve
    "彼は有名なレストランに連れて行った。"
    "このレストランに一回行った。"
    "毎日は電車の中で見えたんだけど、そのレストランに行くことのイメージがまだ思えない。"

    scene bg restaurant_indoor with dissolve

    "メニューが非常に高い。"
    "五日ぐらい食べらなきゃいけなかった。"
    "例えば、二つ小さい魚が五百ペソぐらい。"
    "その料理は一番高い料理と思った。ところが、一番安かった料理だよ！"
    "でも、空気（くうき）が良かった。レストランの空気が天の空気みたかった。"
    "いかを食べてみた。生まれた時から、非常に美味しいいかを食べられました！"
    "味が流（なが）れすぎた。"
    "飲み物も高品質（こうひんしつ）だ。"
    "フランスのシャンペンを飲んで、お酒を飲んだ。"
    "食べるの後は、竜さん全部払った。竜さんを聞いた、「大丈夫」ってた。"
    "彼にお返（かえ）しするつもりと思っている。"
    "でも、竜さん。。。いいえ、竜くん。。。私を好き？"

    scene sky_night with fade
    "レストランで食べる時は竜さんが私に時々見てることを見たと思い出した。"
    "彼の目を見たら、笑顔（えがお）をみせる。"
    "会社で、食堂に一緒に行ったら、時々彼の手を触（さわ）りたい。"
    "触りたんだけど、手をたまたま触らせったら、緊張して、手を引いた。"
    "私のバカ！"

    scene sky_noon with dissolve
    "いつもそのことだ。"
    "竜さんが怒（おこ）った時間がなかった。彼が非常に優しいだけ！"
    "本当に、私が勿体無いかもしれない。"
    "三月一緒に友達と付き合うなのに、彼をまだ知ってると思うんだ。"
    "始まりに彼が建前を使ってくれたかもしれない。"

    # Selection 3.1
    menu:
        "本音（ほんね）と思うんだ。何も心配しないと思うんだ。":
            $ ryuu_points += 1
            jump scene4_0_jp

        "建前と思うんだから、ちょっと信じない。":
            $ ryuu_points -= 1
            jump scene3_2_jp

    return


label scene3_2_jp:
    scene sky_day with dissolve
    "先週、彼の内心（ないしん）についてことを思った。"
    "竜さんが私にあまり正（ただ）さないことに山をかけるなら良くと思った。"
    "でも、全てが頭（あたま）の中だけだ。このことが友情（ゆうじょう）を壊（こわ）してるから、出来（でき）れば終息（しゅうそく）したい。"
    "…それをした。"

    scene cubicle_noon with fade

    show ryuu suit sad
    mc "竜さん、聞いてもいい？"
    "竜さんが悲しそう。珍（めずら）しい。"
    "虎くんは最近竜さんがあまり元気じゃないと言ってたと思う。"

    show ryuu suit surprised
    ryuu "あっ, %(mc_gname)sさん."
    ryuu "いいよ。何？"

    # Selection 4.1
    menu:
        "始まりから、竜さんは優しくているんですが、あのさ、竜さんが本当に優しいかなあ。":
            $ ryuu_points -= 2
            # result 4.1.1

            ryuu "えっ？どんな言うか？"
            mc "あなた…優しすぎると思っているし。"
            mc "そのことは建前かもしれないと思っているし。"

            show ryuu suit mad
            ryuu "はっ？あなたが僕の態度（たいど）を疑（うたが）っているの？"
            ryuu "なんて頭に入れたんだ？"

            "起こった… つづく?"

            # Selection 4.2
            menu:
                "やっぱり、敬遠（けいえん）する人があなただ。余人（よじん）の気配り（きくばり）をもらえるように、敬遠している。":

                    $ ryuu_points -= 3

                    ryuu "今まで、僕についてあなたの思いことが知らなかった。"
                    ryuu "かわいそう。"
                    ryuu "働き者だけど、この会社では、この会社員に態度も尊んでいるんだ。"
                    ryuu "自業自得（じごうじとく）だ。社長室（しゃちょうしつ）に行って、その態度については話します。"
                    ryuu "失礼します。"

                    mc "もういいよ。どの道（みち）、辞（や）めるつもりだ。"
                    ryuu "そのことは全て優しくなりました。"
                    ryuu "%(mc_surname)sさん、会社で、連携（れんけい）にありがとう。"

                    jump bad_jp

                "疑わないよ。この方に慣（な）れっこじゃないし。それを話してごめん。":
                    # result 4.2.2

                    $ ryuu_points += 3

                    show ryuu suit serious
                    ryuu "大丈夫だよ。"
                    ryuu "実は、あなたが正しくなってくれて、ありがとう。"
                    show ryuu suit sad
                    ryuu "そのことを言ってる一番人があなただ。"

                    if ryuu_points >= 12:
                        ryuu "お先（さき）に忘れましょう。"
                        show ryuu suit happy
                        ryuu "ああ、昼ご飯について話していた。"
                        ryuu "実は寿司がほしいよ。"
                        show ryuu suit grin
                        ryuu "食べて行こうよ。"
                        mc "いいね！竜さんに奢ってあげる。"
                        show ryuu suit surprised
                        ryuu "それは大丈夫？"
                        mc "じゃあ、昼ご飯があなたをご馳走してもいい？"
                        mc "いつもいつも竜さんが払ったんだけど。では、私、お返（かえ）しをしなきゃと思う。"
                        jump scene4_0_1_jp

                    else:
                        ryuu "実は…　私も正しくなりたい。"
                        show ryuu suit serious
                        ryuu "あなたと話してもいい？"
                        jump scene4_0_2_jp

        "先週木曜日虎（とら）くんに寄（よ）ってあげた。虎くんは「最近竜さんが気があまり良くない」ってた。":
            # result 4.1.2

            $ ryuu_points += 3

            show ryuu suit serious
            ryuu "弟とを寄(よ)ってくれてありがとう。"
            show ryuu suit sad
            ryuu "はい、最近はちょっと気が悪いだ。"
            ryuu "仕事が非常に忙しいし。締め切り（しめきり）が次々にあったし。"
            ryuu "会長が頼（たの）んだ発表（はっぴょう）を準備（じゅんび）している。あの発表の締め切りも明日。"

            mc "大変ですね。"
            mc "じゃあ、発表はもう終わったから、あなたに助（たす）ける"
            show ryuu suit surprised
            mc "それに、暇（ひま）じゃないから、今度は昼ご飯にご馳走だ。"
            mc "いい？"

            if ryuu_points >=5:
                show ryuu suit surprised
                ryuu "それは大丈夫？"
                mc "じゃあ、昼ご飯があなたをご馳走してもいい？"
                mc "いつもいつも竜さんが払ったんだけど。では、私、お返（かえ）しをしなきゃと思う。"
                jump scene4_0_1_jp
            else:
                show ryuu suit serious
                ryuu "実は、%(mc_gname)sさんと話したい。"
                jump scene4_0_2_jp

label scene4_0_jp:
    scene sky_day with dissolve
    "彼に初回(しょかい)会うことは１年ぐらい。"
    "無数（むすう）のパーチーと飲み会が一緒にに行った。でも、二人はまだ友達です。"
    "それでも、たびにそのパーチーと飲み会に行ったら、あなたに見ると彼が感情（かんじょう）を見せられなそう。"
    "私も感情を見せられない。"

    scene bg cubicle_day with fade

    "今竜さんが悲（かな）しそう。珍（めずら）しいなあ。"
    "普段（ふだん）の時間はここに来ない。"
    "仕事に忙しいから、昼ご飯を食べないことに決（た）めるかもしれないなあ。"
    "先週木曜日虎（とら）くんに寄（よ）った時、「最近竜ちゃんが気が悪い」ってた。"
    "でも、なぜまだ働いているんだよ？"
    "私が構（かま）っていると言わなきゃかもしれない。"
    "彼が昼ご飯に誘うことが完璧（かんぺき）と思う。今、はまだ昼食時（ちゅうしょくじ）から、あまり変じゃなかったと思う。"
    "何しってる？"

    # Selection 4.0
    menu:
        "昼ごはんに誘う":
            # result 4.0.1

            $ ryuu_points += 3

            scene bg cubicle_noon with dissolve
            show ryuu suit serious
            mc "ねぇ、何か食べに行く？"

            show ryuu suit surprised
            ryuu "あっ! %(mc_gname)sさん..."

            if ryuu_points >= 12:
                ryuu "僕はいつも昼ご飯に誘っている。"
                ryuu "言ったらいいだけど、僕に誘うことがちょっと変そう。"
                mc "ぜんぜん変じゃないよ。"
                mc "ええと、ああ、今度は私何々をしてあげたいし。"
                mc "じゃあ、昼ご飯があなたをご馳走してもいい？"
                mc "いつもいつも竜さんが払ったんだけど。では、私、お返（かえ）しをしなきゃと思う。"
                jump scene4_0_1_jp

            else:
                show ryuu suit sad
                ryuu "今はちょっと…"
                "竜さんは忙しそう。"
                show ryuu suit serious
                ryuu "実は、%(mc_gname)sさんと話したい。"
                jump scene4_0_2_jp

        "彼を言うことを待って":

            $ ryuu_points += 1

            scene bg cubicle_noon with dissolve
            if ryuu_points >= 12:
                show ryuu suit happy
                ryuu "昼ごはんを食べに行きたい？"
                mc "あっ、竜さん！いいね。行こう！竜さんに奢ってあげよう。"
                show ryuu suit surprised
                ryuu "それは大丈夫？"
                mc "じゃあ、昼ご飯があなたをご馳走してもいい？"
                mc "いつもいつも竜さんが払ったんだけど。では、私、お返（かえ）しをしなきゃと思う。"
                jump scene4_0_1_jp

            else:
                show ryuu suit serious
                ryuu "%(mc_gname)sさんと話したい。"
                jump scene4_0_2_jp

    return


label scene4_0_1_jp:

    show ryuu suit surprised
    ryuu "そうか。いいね。"
    show ryuu suit grin
    ryuu "ほかにこの間（あいだ）の買い物が高すぎたそう。"
    ryuu "レストランの食べ物も高すぎた。"
    ryuu "今度財布を使わなきゃね。"

    mc "違うよ。"
    mc "ええと、あ、構うだけ。"

    show ryuu suit surprisedblush
    ryuu "あなた…今、何を言ってる？構うか？"

    "やばい!!"

    mc "何でもない！"
    mc "早く行こうよ。お腹が空いてるよ。"
    mc "寿司（すし）を食べようよ。"

    show ryuu suit grinblush
    ryuu "いいよ。"

    jump scene4_1_jp
    return


label scene4_0_2_jp:
    mc "私？どうしたの？"
    ryuu "言わなきゃいけないだけど、あなただけがこの会話を聞かなくちゃ。"

    scene bg roadside_noon with dissolve

    "一緒に散歩した。あまり込んでいない。"
    "竜さんは急に話した。"

    show ryuu suit sad
    ryuu "それは早く話さなきゃ。"
    mc "え？なんで？どういうの？まだわからないよ。"
    show ryuu suit serious
    ryuu "乱れたくないけど、その事体がつづけるなら、もうできないかも知れないよ。"
    mc "何…？"
    ryuu "僕たちの関係… 全部早すぎるんだ。"

    show ryuu suit sad
    ryuu "僕の仕草、ごめん。"
    ryuu "でも、仕事に集中したい。"

    show ryuu suit worried
    ryuu "それなのに、あなたに僕の感じをまだ消さない。同僚...会社で働いなきゃだけ。"
    ryuu "会長がぼくたちを見えるどう？そして、僕たちが友達だけことを思わなければいけない。"

    show ryuu suit sad
    ryuu "それなのに、あなたに僕の感じをまだ消さない。"
    ryuu "聞かされてごめん。"
    ryuu "まだできない物について全部がみだれます。"
    ryuu "僕が変のように見ないでくれ。"

    mc "ごめんなさい。実は私も同じ。"
    show ryuu suit surprised
    mc "私も実感をまだ表せなかった。"
    mc "あなたは言えたと思ったから、あなたに待っている。"
    mc "あなたの感じることがわかった。ぜんぜん変じゃないよ。二人は同じだけ。"
    mc "友達…だね？じゃあ、その選択を選んだったら、いいよ。"
    mc "友達だけが良くなると思う。泣かないでください。"

    show ryuu suit happy
    ryuu "聞いてくれてありがとう。"
    ryuu "そのことを言ったまだ信じられない。"
    ryuu "言ったことが考えなかったでしょうか。"
    show ryuu suit sad
    ryuu "頭（あたま）を失（うしな）うと思う。"

    mc "大丈夫よ。同じ感じているよ。"
    mc "私に正しいになってくれてありがとう。"
    mc "多い物がまだしなきゃいけなかったけど、そのことはまだ入られない。"
    mc "竜さんは竜くんだ。その事体で、あなたたちがその話せない物が出来ます。"
    mc "自明（じめい）物についてだけを話したら、竜さんと私について習えなかった。"
    mc "実は、これは失敗（しっぱい）じゃないよ。この会話が友達にもっと近（ちか）づくことにチャンスだ。"
    mc "その方がいいだね？"

    show ryuu suit grin
    ryuu "もういいよ。ありがとう。どもありがとう。"

    jump neutral_jp
    return


label scene4_1_jp:
    scene sushi with dissolve

    show ryuu suit happy
    ryuu "おにぎりとカリフォルニア巻お願（おねが）いします。"
    mc "はい、荒巻（あらまき）お願いします。"

    scene sushi with fade

    show ryuu suit happy
    ryuu "お先には、昼ご飯に誘うの前には、なにを言ってる？"

    "しまった、それにまかり通（とお）ったと思った。"

    mc "別に。"
    mc "昼ご飯に誘いたかっただけ。"

    show ryuu suit grin
    ryuu "僕に構ったっけ？"

    "えっ！やれやれ。うそをつくことに無駄（むだ）だ。"

    mc "はい。構るよ。"
    mc "それが友達が気が悪かったら、自然（しぜん）な人間（にんげん）を感じてでしょう？"

    show ryuu suit happy
    ryuu "ええ。それは本から読んだし。"
    show ryuu suit happyblush
    ryuu "あの本が「人が構ったら、あの人が上のチャンスが…」ってた…まあ、言いたくないよ。でも、もう知ってるでしょう？"

    # Selection 4.3.
    menu:
        "まだ知らないよ。何て言ってる？上のチャンスが…":
            # result 4.3.1

            $ ryuu_points += 2

            show ryuu suit shyhappy
            ryuu "あの人があなたが好き、とか。"
            ryuu "でも、何か思ってる…"
            mc "何？"

            show ryuu suit worriedblush
            ryuu "何にかならどうと思ってる。"
            mc "何かなら何で？"
            show ryuu suit shyhappy
            ryuu "その本が真実ならどう？"
            mc "あっ、ええと、帰らなきゃね。遅（おそ）くてはいけないよ。"
            show ryuu suit grinblush
            ryuu "じゃあ、行こう。"

        "読んでしまって良かったよ。":
            # result 4.3.2
            show ryuu suit grin
            ryuu "じゃあ、行こう。"

    jump scene4_1_1_jp

    return

label scene4_1_1_jp:
    scene station_noon with dissolve

    "会社に行った時、同僚が帰ている見えました。"
    "会社が整備（せいび）しているんだ。明日まで整備を続（つづ）けるよ。"
    "竜くんがだれかに電話をしています。"

    show ryuu suit surprised
    ryuu "はい、はい、わかりました。ありがとうございました。"
    mc "会長ですか？"
    show ryuu suit serious
    ryuu "はい。全部の用事が来週に延（の）びた。"
    ryuu "まあ、ファイルについて、メールにセーブデータがあるので、家でできる。"
    show ryuu suit happy
    ryuu "それから、発表に手伝わなくていいよ。"

    "へー休みの日だな。何をしてる？"

    # Selection 4.4.
    menu:
        "どこかに行きたい？":
            $ ryuu_points += 2
            show ryuu suit grin
            ryuu "いいね。行こう！"

            jump scene4_2_jp

        "早く帰ったほうがいいと思う。":
            mc "いいね。"
            mc "じゃあ、帰る。またね！"
            show ryuu suit grin
            ryuu "ありがとう。"

    return

label scene4_2_jp:

    scene bg toy_shop with dissolve

    "先日は割引券（わりびきけん）を得（え）たから、おもちゃ屋に行った。"
    "竜くんが青い縫（ぬ）いぐるみを買ってくれた。"
    "竜くんが「ぼくの趣味（しゅみ）が縫いぐるみを作ること」ってた。"

    show ryuu suit happy
    ryuu "母が縫いぐるみを編むことを教えてくれました。"
    ryuu "始まりはしたくないけど、早く趣味になった。"
    ryuu "毎日、二三個ぐらいを作れました。元気なら、十個（こ）を作れました。それから、時々、食べることを忘れちゃった。"
    mc "私も母に何かを習ってもらった。"
    mc "料理するのがまだ始まりました時、母は「完ぺき卵（たまご）」を作ることを教えてくれた。"
    mc "そして、母が私に家族のためにアドボを作らせた。"

    show ryuu suit grin
    ryuu "ハハハ！お前のお母さんが面白そうなあ。"
    ryuu "お母さんが将来（しょうらい）会いたいよ。"

    scene bg sky_noon with dissolve

    "午後が早く過（す）ぎた。空が黒（くろ）くなる。"
    "でも、土曜日から、明日仕事に行くことに心配することない。"

    scene bg game_center with dissolve
    "ゲームセンターに行って、テディベアを勝った！"
    "おもちゃ屋の社長友達、フェリシャさんが会った。"
    "フェリシャさんが「同じおもちゃ屋で働いている幼（おさな）なじみが会った」ってたから、最近フェリシャさんは嬉しい見たい。"

    scene bg park_night with dissolve

    "もう夜？"
    show ryuu suit grin
    ryuu "はー、楽しかったよ。"
    ryuu "ここで休息（きゅうそく）して。"
    mc "うん、私も疲れた。"

    "ちょっと休む…"

    scene black with fade

    jump good_jp
    return


label good_jp:

    scene bg park_dusk with fade

    "へー？寝たの？何時？"
    "ああ、午後１１：４５。暖（あたた）かいと感じました。時間が気づけなかった。"

    "何これ？竜くんのジャケットか？"

    show ryuu suit surprisedblush
    "竜くんに突如見て、私に見ていることを見た。"
    "現行犯（げんこうはん）のように、驚（おどろ）きたそう。"
    show ryuu suit happyblush
    "赤面（せきめん）する見たいことを終わって、元気になりました。笑顔を見せた。"
    "緊張（きんちょう）の代わりに暖かくて楽と感じました。"
    "この感じが以前（いぜん）とは違う。"
    "今二人だけから、この感じがもう強くなった。純（じゅん）になった。"
    "楽以外何も感じると手を取った。"
    "迫っていると、ジャケットの懐（ふところ）が重（おも）そうことを気づけた。"
    "懐の中で外の手を抜（ぬ）け出した。これ、本？"

    show ryuu suit grinblush
    ryuu "あのさ、その本をまだ考えているよ。"
    mc "これ？"

    "その本は恋仲（こいなか）の本。"
    "その本では、デートについて方法（ほうほう）と人が誰かが好きの気配がある。"
    "多いページでは手書き（てがき）なノートがある。誰かを勉強してしまったそう。"
    "後ろ（うしろ）のページに繰（く）った。もう手書きなノートがある。その言葉…"
    "もう一度見た。"
    "彼が手を触ると、見た。"

    mc "はい、そうだ。"

    scene black with fade
    return


label neutral_bridge_jp:
    scene bg cubicle_noon with fade:

    "月曜日は、昼ごはんの前に、竜くんが来た。"
    show ryuu suit serious
    ryuu "あなたと話したい。"
    jump scene4_0_2_jp


label neutral_jp:
    scene bg bar_night with fade

    "人生（じんせい）の選択（せんたく）なら、時間がかかなくて、状態（じょうたい）に考えなきゃいけないと思う。"
    "会社では、同席（どうせき）して楽しい友達がいるよ。友達、特に竜くんが今信頼（しんらい）している。"
    "幹事（かんじ）に挙（あ）がったから、この夜が祝っている。"
    "竜くんは、六月前は私に言ったが正（ただ）しいと思います。"
    "全く（まったく）あの選択を追い求（おいもと）めることに時間がかかなきゃ。"
    "「桃栗三年柿八年」ってた。"
    "私の選択について、今、元気になると思う。でも、あの可能性（かのうせい）が時々まだ思ってる。"
    "竜くんがそのことを言わなかったどう？"
    "社則（しゃそく）ながら、彼が恐（おそ）れたどう？"
    "それなのに、二人はまだ嬉（うれ）しいだ。"

    coworkers "お～い！もう飲もうよ！"
    show ryuu suit grin
    ryuu "おい！会社にいないけど、まだ%(mc_gname)sが幹事よ。"
    ryuu "早く、 %(mc_gname)s！"
    mc "来てる！"

    scene black with fade
    return


label bad_jp:
    scene bg cubicle_night with fade

    "社長室から出ながら、竜さんにもらった辞表（じひょう）を読んでいる。"
    "諸条件（しょじょうけん）の列挙（れっきょ）が付きました。"
    "何これ？「特定（とくてい）人と合わなければいけない」って。"
    "この会社、変なことがあるそう。"
    "社長室のドアを開けてみたけど、鍵（かぎ）をかけている。"

    scene bg cubicle_off with dissolve

    "電気が突如（とつじょ）閉まった。何も見えない。"
    "全ては真っ黒（まっくろ）だ。"
    "あのキュービクルから電気を見て、徐（じょ）々に来ます。"

    mc "今晩は？このフォームでは、このキュービクルで合わなければいけませんか？"
    mc "キュービクル４４ですか？私と会う人ですか？"

    show hanako smile
    "その人が振り替えた（ふりかえた）。顔が絶対（ぜったい）にわかりません。"
    "その人が笑顔を見せる。"

    hanako "ええ、その人が私だ。"
    mc "お名前は教えてくれませんか？"
    mc "我（われ）々は知られない場所でいる気付（きづ）きました。"
    hanako "花子です。もっと何でもない。"
    $ hanako_name = "花子"
    hanako "外の選択肢（せんたくし）があるのがまだ知ってるのに、この方を選んだね。"
    mc "どんな言うか？"
    hanako "全てはゲームだけ。選ぶのが出来損（できそこ）ない。"
    hanako "今から、君は私とずっとここにいる。"
    mc "何が残念（ざんねん）だ？"
    mc "まだ知られないでしまいました。"
    show hanako grin
    hanako "ああ、思い出さないか？僕は１７番の聞く練習の中で。"
    mc "まさか！怖（こわ）い練習を終わると思った。"

    "だめだ。どんあ罰（ばち）を開けてしまった？"

    hanako "そうじゃないよ。思い出したか？じゃあ、その選択肢ので、君が目に合わなきゃ。"
    hanako "じゃあ、せ～の。"
    hanako "好 {w=1.0}き {w=1.0}だ {w=1.0}よ～"
    mc "辞めて… {w=1.0} 辞めて… {w=1.0}"
    mc "ヤメテェーーーー!!!!" with hpunch
    mc "ながい先生、助けてーーーー！!!!!" with hpunch

    scene black with fade

    "そして、体（からだ）が固（かた）めてしまった。"
    return
