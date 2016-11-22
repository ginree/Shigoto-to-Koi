## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define ryuu_points = 0
define decision_tora = False
define decision_party = False

define ryuu = DynamicCharacter("ryuu_name")
define felicia = DynamicCharacter("felicia_name")
define mc = DynamicCharacter("mc_gname")
define staff = DynamicCharacter("staff_name")
define tora = DynamicCharacter("tora_name")
define coworkers = DynamicCharacter("coworker_name")
define hanako = DynamicCharacter("hanako_name")


# Positions

transform mid_left:
    xalign .3 yalign 1.0
transform mid_right:
    xalign .7 yalign 1.0

## The game starts here.

init:
    image bg room_day = "images/room_day.jpg"
    image bg school_noon = "images/school_noon.jpg"
    image bg station_day = "images/station_day.jpg"
    image bg station_noon = "images/station_noon.jpg"
    image bg office_day = "images/office_day.jpg"
    image bg hall_day = "images/hall_day.jpg"
    image bg cubicle_day = "images/cubicle_day.jpg"
    image bg cubicle_noon = "images/cubicle_noon.jpg"
    image bg cubicle_night = "images/cubicle_night.jpg"
    image bg cubicle_off = "images/cubicle_off.jpg"
    image bg frontdoor_night = "images/frontdoor_night.jpg"
    image bg restaurant_night = "images/restaurant_night.jpg"
    image bg restaurant_indoor = "images/restaurant_indoor.jpg"
    image bg sky_day = "images/sky_day.jpg"
    image bg sky_noon = "images/sky_noon.png"
    image bg sky_night = "images/sky_night.png"
    image bg field_noon = "images/field_noon.png"
    image bg sushi = "images/sushi.png"
    image bg toy_shop = "images/toy_shop.jpg"
    image bg game_center = "images/game_center.jpg"
    image bg roadside_noon = "images/roadside_noon.jpg"
    image bg park_night = "images/park_night.jpg"
    image bg park_dusk = "images/park_dusk.jpg"
    image bg bar_night = "images/bar_night.jpg"


    image ryuu suit happy = "characters/ryuu_suit_smile.png"
    image ryuu suit happyblush = "characters/ryuu_suit_happyblush.png"
    image ryuu suit grin = "characters/ryuu_suit_grin.png"
    image ryuu suit grinblush = "characters/ryuu_suit_grinblush.png"
    image ryuu suit sad = "characters/ryuu_suit_sad.png"
    image ryuu suit mad = "characters/ryuu_suit_mad.png"
    image ryuu suit worried = "characters/ryuu_suit_worried.png"
    image ryuu suit worriedblush = "characters/ryuu_suit_worriedblush.png"
    image ryuu suit serious = "characters/ryuu_suit_serious.png"
    image ryuu suit surprised = "characters/ryuu_suit_surprised.png"
    image ryuu suit surprisedblush = "characters/ryuu_suit_surprisedblush.png"
    image ryuu suit shyhappy = "characters/ryuu_suit_shyhappy.png"
    image ryuu suit shygrin = "characters/ryuu_suit_shygrin.png"

    image ryuu casual happy = "characters/ryuu_casual_happy.png"
    image ryuu casual grin = "characters/ryuu_casual_grin.png"
    image ryuu casual sad = "characters/ryuu_casual_sad.png"
    image ryuu casual blush = "characters/ryuu_casual_blush.png"
    image ryuu casual worried = "characters/ryuu_casual_worried.png"

    image tora grin = "characters/otouto_grin.png"
    image tora openmouth = "characters/otouto_open.png"
    image tora smile = "characters/otouto_smile.png"
    image tora sad = "characters/otouto_sad.png"

    image hanako smile = "characters/hanako_smile.png"
    image hanako grin = "characters/hanako_grin.png"

init -3 python:
    if persistent.lang is None:
        persistent.lang = "english"

    lang = persistent.lang

init python:
    style.default.line_leading = 15

    style.ruby_style = Style(style.default)
    style.ruby_style.size = 15
    style.ruby_style.yoffset = -27

    style.default.ruby_style = style.ruby_style

label start:
    jump settings_chooser

label settings_chooser:

    scene black

    "Are you male or female?"
    menu:
        "Male":
            $ mc_gender = "male"
            $ mc_pronoun1 = "he"
            $ mc_pronoun2 = "him"
            $ mc_title = "Mr."
            $ mc_sib = "brother"
        "Female":
            $ mc_gender = "female"
            $ mc_pronoun1 = "she"
            $ mc_pronoun2 = "her"
            $ mc_title = "Ms."
            $ mc_sib = "sister"

    $ mc_gname = renpy.input("What is your given name?")
    $ mc_surname = renpy.input("What is your surname?")

    "Do you want to view this in English or Japanese?"

    menu:

        "English":

            $ persistent.lang = "english"

            $ ryuu_name = "Interviewer"
            $ felicia_name = "Felicia"
            $ staff_name = "Staff"
            $ tora_name = "Tora"
            $ coworker_name = "Co-workers"
            $ hanako_name = "Stranger"

            jump scene1_en

        "Japanese":

            $ persistent.lang = "japanese"

            $ ryuu_name = "面接官"
            $ felicia_name = "Felicia"
            $ staff_name = "職員"
            $ tora_name = "虎"
            $ coworker_name = "同僚"
            $ hanako_name = "知らない人"

            if mc_gender == "male":
                $ mc_sib = "おにいちゃん"
            else:
                $ mc_sib = "おねえちゃん"

            jump scene1_jp

label scene1_en:
    scene bg room_day with dissolve

    "Good morning! It’s 7AM, Monday. I feel good today!"

    "I have a lot of interviews today, so I’ll have a good breakfast. And I’ll drink milk, too!"

    "I’ll bring my souvenir from Japan for good luck."

    scene bg school_noon with fade

    "I just graduated college, so I’m going to look for a job."

    "It’s my first job, so I prefer to work in Metro Manila. I want to have experience in all sorts of jobs, so any job will do."

    "I’ve narrowed down my options to two jobs, but I prefer work about corporate management and corporate accounting."

    jump scene2_0_en


label scene1_jp:
    scene bg room_day with dissolve

    "おはよう！{rb}午前{/rb}{rt}ごぜん{/rt}７時{rt}じ{/rt}、{rb}月曜日{/rb}{rt}げつようび{/rt}。"

    "{rb}今日{/rb}{rt}きょう{/rt}、{rb}元気{/rb}{rt}げんき{/rt}だ！たくさんインタービューをしなきゃいけないから、いい朝{rt}あさ{/rt}ご飯{rt}はん{/rt}を食{rt}た{/rt}べる。{rb}牛乳{/rb}{rt}ぎゅうにゅう{/rt}も飲{rt}の{/rt}む！"

    "{rb}幸運{/rb}{rt}こううん{/rt}を祈{rt}いの{/rt}ってに{rb}日本{/rb}{rt}にほん{/rt}のお{rb}土産{/rb}{rt}みやげ{/rt}を持{rt}も{/rt}って行{rt}い{/rt}くよ。"

    scene bg school_noon with dissolve

    "{rb}最近{/rb}{rt}さいきん{/rt}、{rb}大学{/rb}{rt}だいがく{/rt}から{rb}卒業{/rb}{rt}そつぎょう{/rt}したから、{rb}仕事探{/rb}{rt}しごとさ{/rt}しをするつもり。"

    "{rb}最初{/rb}{rt}さいしょ{/rt}の{rb}仕事{/rb}{rt}しごと{/rt}だから、マニラで働{rt}はたら{/rt}きたい。たくさん{rb}経験{/rb}{rt}けいけん{/rt}を積{rt}つ{/rt}みたいから、{rb}仕事{/rb}{rt}しごと{/rt}は何{rt}なん{/rt}でもいい。"

    "{rb}選択肢{/rb}{rt}せんたくし{/rt}を二{rt}ふた{/rt}つに絞{rt}しぼ{/rt}り込{rt}こ{/rt}んで{rb}一番{/rb}{rt}いちばん{/rt}好{rt}す{/rt}きな{rb}仕事{/rb}{rt}しごと{/rt}を選{rt}えら{/rt}びます。{rb}一番{/rb}{rt}いちばん{/rt}好{rt}す{/rt}きな{rb}仕事{/rb}{rt}しごと{/rt}は{rb}企業{/rb}{rt}きぎょう{/rt}マネージメントと{rb}企業会計{/rb}{rt}きぎょうかいけい{/rt}について{rb}仕事{/rb}{rt}しごと{/rt}だ。"

    jump scene2_0_jp
