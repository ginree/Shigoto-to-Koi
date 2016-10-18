## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define ryuu = Character('Ryuu')
define felicia = Character('Felicia')
define mc = Character('You')

define otouto = Character("Ryuu's Brother")

# $ lang = 'english'


## The game starts here.

init:
    image bg room_day = "images/room_day.jpg"
    image bg school_noon = "images/school_noon.jpg"
    image bg station_day = "images/station_day.jpg"
    image bg office_day = "images/office_day.jpg"
    image bg hall_day = "images/hall_day.jpg"
    image bg cubicle_day = "images/cubicle_day.jpg"
    image bg frontdoor_night = "images/frontdoor_night.jpg"

    image ryuu suit happy = "characters/ryuu_suit_smile.png"
    image ryuu suit grin = "characters/ryuu_suit_grin.png"
    image ryuu suit sad = "characters/ryuu_suit_sad.png"
    image ryuu casual blush = "characters/ryuu_casual_blush.png"
    image otouto grin = "characters/otouto_grin.png"
    image otouto openmouth = "characters/otouto_open.png"
    image otouto smile = "characters/otouto_smile.png"
    image otouto sad = "characters/otouto_sad.png"

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
    jump language_chooser

label language_chooser:

    scene black

    "Do you want to view this in English or Japanese?"

    menu:

        "English":

            $ persistent.lang = "english"
            jump scene1_start_en

        "Japanese":

            $ persistent.lang = "japanese"
            jump scene1_start_jp
    return

label scene1_start_en:
    scene black
    show text "Looking for a Job" with Pause(1.0)

    scene bg room_day with dissolve

    # show graduation and city
    "It's 7AM, Monday. You woke up feeling well. You have a lot of interviews today, so you ate a good breakfast. You drank milk also. You brought your souvenir from Japan for good luck."



    "You just graduated college and so you are going to look for a job. It’s your first job, so you prefer working in Metro Manila. You want to have a good experience of many things, so any job will do."
    "You narrow down your options, and choose the four jobs that you like best."

    menu:
        "Which work do you like best?"
        "Work about negotiations and corporate meetings":
            jump scene1_business_en
        "Work about easy, cute things":
            jump scene1_plushies_en
        "Work about art and aesthetics":
            jump scene1_art_en
        "Work about research and technology":
            jump scene1_physics_en
    return

label scene1_start_jp:
    scene black

    show text "仕事探し" with Pause(1.5)

    scene bg room_day with fade

    # show graduation and city
    "{rb}今日{/rb}{rt}きょう{/rt}は{rb}午前{/rb}{rt}ごぜん{/rt}７時{rt}じ{/rt}です。 起{rt}お{/rt}きて、{rb}元気{/rb}{rt}げんき{/rt}。"

    "たくさんインタビューをしなきゃいけないので、いい朝{rt}あさ{/rt}ご飯{rt}ごはん{/rt}を食{rt}た{/rt}べました。{rb}牛乳{/rb}{rt}ぎゅうにゅう{/rt}も飲{rt}の{/rt}んだ。"

    "幸{rt}さち{/rt}に{rb}日本{/rb}{rt}にほん{/rt}のお{rb}土産{/rb}{rt}みやげ{/rt}を待{rt}ま{/rt}ちました。"

    scene bg school_noon with fade

    "{rb}昨日{/rb}{rt}きのう{/rt}は{rb}大学{/rb}{rt}だいがく{/rt}から{rb}卒業{/rb}{rt}そつぎょう{/rt}しましたので、{rb}仕事探{/rb}{rt}しごとさが{/rt}しことをします。これは{rb}一番{/rb}{rt}いちばん{/rt}{rb}仕事{/rb}{rt}しごと{/rt}だので、マニラで働{rt}はたら{/rt}いていた方{rt}ほう{/rt}がいいです。"

    "多{rt}おお{/rt}くの中{rt}なか{/rt}にいい{rb}経験{/rb}{rt}けいけん{/rt}をもらいたいので、何{rt}なん{/rt}でも{rb}仕事{/rb}{rt}しごと{/rt}がいい。"

    "{rb}選択肢{/rb}{rt}せんたくし{/rt}を絞{rt}しぼ{/rt}り込{rt}こ{/rt}んで四{rt}よっ{/rt}つ{rb}一番{/rb}{rt}いちばん{/rt}好{rt}す{/rt}き{rb}仕事{/rb}{rt}しごと{/rt}を選{rt}えら{/rt}びます。"

    menu:
        "どの{rb}仕事{/rb}{rt}しごと{/rt}がいちばん好{rt}す{/rt}きですか?"
        "negotiationやmeetingsについての{rb}仕事{/rb}{rt}しごと{/rt}":
            jump scene1_business_jp
        "やさしくてかわいい物についての{rb}仕事{/rb}{rt}しごと{/rt}":
            jump scene1_plushies_jp

        #"artやaestheticsについての{rb}仕事{/rb}{rt}しごと{/rt}":
            #jump scene1_art_en
        #"けんきゅうやtechnologyについての{rb}仕事{/rb}{rt}しごと{/rt}":
            #jump scene1_physics_en
    return
