## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define b = Character('Billy')
define s = Character('Steph')
define a = Character('Artemia')
define p = Character('Phil')

$ lang = 'english'


## The game starts here.

init python:
    style.default.line_leading = 17

    style.ruby_style = Style(style.default)
    style.ruby_style.size = 17
    style.ruby_style.yoffset = -25

    style.default.ruby_style = style.ruby_style

label start:
    jump langchooser
    return

label langchooser:

    "Do you want to view this in English or Japanese?"

    menu:

        "English":

            $ lang = 'english'

        "Japanese":

            $ lang = 'japanese'

    jump scene1_start

    return

label scene1_start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.


    if lang is 'english':

        scene black with dissolve
        show text "Looking for a Job" with Pause(1.5)
        scene black with dissolve

        # show graduation and city

        "It's 7AM, Monday. You woke up feeling well. You have a lot of interviews today, so you ate a good breakfast. You drank milk also. You brought your souvenir from Japan for good luck."

        "You just graduated college and so you are going to look for a job. It’s your first job, so you prefer working in Metro Manila. You want to have a good experience of many things, so any job will do."

        "You narrow down your options, and choose the four jobs that you like best."

        menu:
            "Which work do you like best?"

            "Work about negotiations and corporate meetings":

                jump scene1_business

            "Work about easy, cute things":

                jump scene1_plushies

            "Work about art and aesthetics":

                jump scene1_art

            "Work about research and technology":

                jump scene1_physics

    if lang is 'japanese':

        scene black with dissolve
        show text "仕事探し" with Pause(1.5)
        scene black with dissolve

        # show graduation and city

        "今日{rt}きょう{/rt}は午前{rt}ごぜん{/rt}７時です。起きて、元気。たくさんインタビューをしなきゃいけないので、いい朝ご飯を食べました。牛乳も飲んだ。幸に日本のお土産を待ちました。"

        "昨日は大学から卒業しましたので、仕事探しことをします。これは一番仕事だので、マニラで働いていた方がいいです。多くの中にいい経験をもらいたいので、何でも仕事がいい。"

        "選択肢を絞り込んで四つ一番好き仕事を選びます。"

        menu:
            "どの仕事がいちばん好きですか?"

            "negotiationやmeetingsについての仕事":

                jump scene1_business

            "やさしくてかわいい物についての仕事":

                jump scene1_plushies

            "artやaestheticsについての仕事":

                jump scene1_art

            "けんきゅうやtechnologyについての仕事":

                jump scene1_physics

    return

label scene1_business:

    "Business"

    return

label scene1_plushies:

    "Plushies"

    return

label scene1_art:

    "Art"

    return

label scene1_physics:

    "Physics"

    return
