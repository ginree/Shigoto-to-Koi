label scene2_0_en:
    scene bg station_day with fade

    "I rode a train to Ayala Station in Makati."

    "This place is so crowded and busy! There are so many buildings in the area, but I saw this large building on my left."

    mc "Wow! I wonder if they’re hiring? I really want to work there!"
    mc "They have a really nice garden. They also have clean floors!"

    "And so, I entered Busy-Busy corporation."

    scene bg hall_day with fade

    "The hall was pure white."

    "The receptionist said that the interviews were in the 21st floor. I got in the elevator."

    "There were so many interviewees! They must be a really famous company."

    "I waited patiently for the staff to call my name."

    staff "%(mc_title)s %(mc_surname)s, please follow me."

    scene bg office_day with fade

    show ryuu suit serious
    "The interviewer was a diligent-looking man."

    "Even though he was so busy, he didn’t look tired!"

    ryuu "Hello, my name is Shigeo Ryuu."
    $ ryuu_name = "Ryuu"
    ryuu "Let’s begin the interview."

    jump scene2_1_en

    return

label scene2_0_jp:
    scene bg station_day with fade

    "{rb}電車{/rb}{rt}でんしゃ{/rt}でマカティ市{rt}し{/rt}に行{rt}い{/rt}きました。"

    "この{rb}場所{/rb}{rt}ばしょ{/rt}はとても混{rt}こ{/rt}んでいて忙{rt}いそが{/rt}しいよ。この{rb}場所{/rb}{rt}ばしょ{/rt}はビルが多{rt}おお{/rt}いけど、左{rt}ひだり{/rt}に大{rt}おお{/rt}きいビルが見{rt}み{/rt}えた。"

    mc "すごい！{rb}採用{/rb}{rt}さいよう{/rt}はしているのかなー。{rb}本当{/rb}{rt}ほんとう{/rt}にあそこで働{rt}はたら{/rt}きたい！"
    mc "庭{rt}にわ{/rt}がとてもいい。床{rt}ゆか{/rt}もきれいだよ！"

    "そして、Busy-Busy {rb}会社{/rb}{rt}かいしゃ{/rt}に行{rt}い{/rt}きました."

    scene bg hall_day with fade

    "{rb}会場{/rb}{rt}かいじょう{/rt}は{rb}全部{/rb}{rt}ぜんぶ{/rt}白{rt}しろ{/rt}い。"

    "{rb}応接係{/rb}{rt}おうせつかかり{/rt}は「インタビューは21階{rt}かい{/rt}です」って言{rt}い{/rt}った。エレベーターに乗{rt}の{/rt}った。"

    "{rb}受験者{/rb}{rt}じゅけんしゃ{/rt}が多{rt}おお{/rt}いよ。{rb}絶対{/rb}{rt}ぜったい{/rt}{rb}有名{rt}ゆうめい{/rt}な{rb}会社{/rb}{rt}かいしゃ{/rt}だなー。"

    "{rb}根気{/rb}{rt}こんき{/rt}よくに{rb}職員{/rb}{rt}しょくいん{/rt}が{rb}名前{/rb}{rt}なまえ{/rt}を呼{rt}よ{/rt}ぶのを待{rt}ま{/rt}っていました。"

    staff "%(mc_surname)sさん, 付{rt}つ{/rt}いて来{rt}き{/rt}てください。"

    scene bg office_day with fade

    show ryuu suit serious
    "{rb}面接官{/rb}{rt}めんせつかん{/rt}が{rb}勤勉{/rb}{rt}きんべん{/rt}そうな男{rt}おとこ{/rt}だ。"

    "忙{rt}いそが{/rt}しいだろうが疲{rt}つか{/rt}れを見{rt}み{/rt}せなかったよ。"

    ryuu "おはよう、{rb}名前{/rb}{rt}なまえ{/rt}は{rb}重夫{/rb}{rt}しげお{/rt}竜{rt}りゅう{/rt}です。"
    $ ryuu_name = "竜"
    ryuu "インタビューを始{rt}はじ{/rt}めます。"

    scene black with fade

    jump scene2_1_jp

    return


label scene2_1_en:

    scene bg office_day with fade

    $ ryuu_points += 2

    show ryuu suit happy
    ryuu "The president was very impressed with you."
    ryuu "He thinks that you will do your best in this company."

    mc "Thank you for this opportunity."
    mc "Please treat me well, Mr. Shigeo. I would also be happy working with you."

    ryuu "From now on, we’ll be in the same department."
    ryuu "I hope we will work well together."

    scene black with fade

    "I quickly made friends with the other employees of the company."

    "Over the next three months, we ate together, drank together, and sometimes went to parties together!"

    "Working in Busy-busy corporation was a good decision."

    scene bg cubicle_day with fade

    "One day, Mr. Shigeo approached me."

    show ryuu suit happy
    ryuu "Good morning, %(mc_title)s %(mc_surname)s."

    mc "Good morning, Mr. Shigeo!"

    ryuu "I’m having a birthday celebration this Friday night."
    ryuu "I usually invite my friends from university, but they’re all busy."
    ryuu "Would you be able to come?"

    # Selection 2.1
    menu:
        "Yes, of course! Is it a formal party?":
            # result 2.1.1
            $ ryuu_points += 2

            "If it’s for such a nice reason, I can’t say no..."

            show ryuu suit grin
            ryuu "I’m so glad you agreed!"
            ryuu "It’s my brother’s 7th birthday."
            ryuu "My mom lives far away, so she can’t come, either. I’m the only one living with my brother, so I thought it would be better if my officemates could come."
            ryuu "It’s nothing formal, actually. You can wear anything you like."

            scene black with fade

            jump scene2_2_en

        "I think I have something to do...":
            # result 2.1.2

            "Friday night? That’s when the last episode of Ang Probinsyano airs!"

            show ryuu suit sad
            ryuu "Is that so? Alright, I’ll ask the others..."

            scene black with fade

            jump scene3_0_en

    return

label scene2_1_jp:

    scene bg office_day with fade

    show ryuu suit happy
    ryuu "会長はあなたに好印象を持っています。"
    ryuu "会長はあなたがこの会社で頑張ると思っています。"

    mc "このような機会をありがとうございました。"
    mc "よろしくお願いして、重夫さん。重夫さんと一緒に働くことができることがうれしいです。"

    ryuu "今から、同じ部で働きます。"
    ryuu "一緒にいい働きを願（ねが）っています。"

    scene black with fade

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

            "金曜日の夜？「Ang Probinsyano」の最後（さいご）の挿話（そうわ）が発表するよ。"

            show ryuu suit sad
            ryuu "そうですか。じゃあ、ほかの人に聞いてみるね。"

            scene black with fade

            jump scene3_0_jp

    return

label scene2_2_en:

    scene bg frontdoor_night with fade
    show tora openmouth at mid_left
    show ryuu casual happy at mid_right

    ryuu "This is my little brother, Tora."

    tora "You came! Thank you so much! Let’s play!"
    tora "I want to play Call of Duty 2 with you!"

    mc "Sure!"

    scene black with fade

    scene bg frontdoor_night with fade

    "After playing all sorts of party games with Ryuu and Tora, it was time to go home."

    show ryuu casual happy at mid_right
    show tora smile at mid_left

    ryuu "Thank you again for coming."
    tora "Hey, can I call you big %(mc_sib)s?"

    # Selection 2.2
    menu:
        "Of course!":
            # result 2.2.1

            $ ryuu_points += 3
            $ decision_tora = True

            show tora grin at mid_left
            tora "Yaaay!!"
            tora "Big %(mc_sib)s, thank you for making me and my brother happy!"
            tora "Hey, big brother, if you date %(mc_pronoun2)s, will %(mc_pronoun1)s come over more?"
            show ryuu casual blush at mid_right
            ryuu "Tora!"
            tora "Just kidding!"
            tora "You can come as you like, and we’ll play some more!"

        "Hmmm... no.":
            # result 2.2.2

            $ ryuu_points -=2
            $ decision_tora = False

            show ryuu casual worried at mid_right
            show tora sad at mid_left
            tora "Oh... okay. Sorry I asked."
            tora "I don’t want to talk to you anymore..."


    scene black with fade
    jump scene3_0_en

    return


label scene2_2_jp:

    "selection 3.3"

    return



label scene3_0_en:
    "hello"
    return


label scene3_0_jp:
    "hi"
    return
