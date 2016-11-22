label scene2_0_en:
    scene bg station_day with dissolve

    "I rode a train to Ayala Station in Makati."

    "This place is so crowded and busy! There are so many buildings in the area, but I saw this large building on my left."

    mc "Wow! I wonder if they're hiring? I really want to work there!"
    mc "They have a really nice garden. They also have clean floors!"

    "And so, I entered Busy-Busy corporation."

    scene bg hall_day with dissolve

    "The hall was pure white."

    "The receptionist said that the interviews were in the 21st floor. I got in the elevator."

    "There were so many interviewees! They must be a really famous company."

    "I waited patiently for the staff to call my name."

    staff "%(mc_title)s %(mc_surname)s, please follow me."

    scene bg office_day with dissolve

    show ryuu suit serious
    "The interviewer was a diligent-looking man."

    "Even though he was so busy, he didn't look tired!"

    ryuu "Hello, my name is Ryuu Shigeo."
    $ ryuu_name = "Ryuu"
    ryuu "Let's begin the interview."

    scene black with fade

    jump scene2_1_en

    return


label scene2_1_en:

    scene bg office_day with fade

    $ ryuu_points += 2

    show ryuu suit happy
    ryuu "The president was very impressed with you."
    ryuu "He thinks that you will do your best in this company."

    mc "Thank you for this opportunity."
    mc "Please treat me well, Mr. Shigeo. I would also be happy working with you."

    ryuu "From now on, we'll be in the same department."
    ryuu "I hope we will work well together."

    scene sky_night with fade

    "I quickly made friends with the other employees of the company."

    "Over the next three months, we ate together, drank together, and sometimes went to parties together!"

    "Working in Busy-busy corporation was a good decision."

    scene bg cubicle_day with fade

    "One day, Mr. Shigeo approached me."

    show ryuu suit happy
    ryuu "Good morning, %(mc_title)s %(mc_surname)s."

    mc "Good morning, Mr. Shigeo!"

    ryuu "I'm having a birthday celebration this Friday night."
    ryuu "I usually invite my friends from university, but they're all busy."
    ryuu "Would you be able to come?"

    # Selection 2.1
    menu:
        "Yes, of course! Is it a formal party?":
            # result 2.1.1
            $ ryuu_points += 2

            $ decision_party = True

            "If it's for such a nice reason, I can't say no..."

            show ryuu suit grin
            ryuu "I'm so glad you agreed!"
            ryuu "It's my brother's 7th birthday."
            ryuu "My mom lives far away, so she can't come, either. I'm the only one living with my brother, so I thought it would be better if my officemates could come."
            ryuu "It's nothing formal, actually. You can wear anything you like."

            scene black with fade

            jump scene2_2_en

        "I think I have something to do...":
            # result 2.1.2

            $ decision_party = False

            "Friday night? That's when the last episode of Ang Probinsyano airs!"

            show ryuu suit sad
            ryuu "Is that so? Alright, I'll ask the others..."

            scene black with fade

            jump scene3_0_en

    return


label scene2_2_en:

    scene bg frontdoor_night with fade
    show tora openmouth at mid_left
    show ryuu casual happy at mid_right

    ryuu "Good evening, %(mc_title)s %(mc_surname)s."
    mc "Good evening, Mr. Shigeo!"
    ryuu "Please, while we're here, Ryuu is okay."
    ryuu "This is my little brother, Tora."

    tora "You came! Thank you so much! Let's play!"
    tora "I want to play Call of Duty 2 with you!"

    mc "Sure!"

    scene black with fade

    scene bg frontdoor_night with fade

    "After playing all sorts of party games with Ryuu and Tora, it was time to go home."

    show ryuu casual happy at mid_right
    show tora smile at mid_left

    ryuu "Thank you again for coming."
    mc "Thank you for inviting me. I had a lot of fun!"
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
            tora "You can come as you like, and we'll play some more!"

        "Hmmm... no.":
            # result 2.2.2

            $ ryuu_points -=2
            $ decision_tora = False

            show ryuu casual worried at mid_right
            show tora sad at mid_left
            tora "Oh... okay. Sorry I asked."
            tora "I don't want to talk to you anymore..."


    scene black with fade
    jump scene3_0_en

    return


label scene3_0_en:

    scene bg cubicle_day with fade

    "That Saturday, it was easy to focus on work since I had so much fun last night."
    "I think Mr. Shigeo was working hard as usual, too."

    scene bg cubicle_noon with dissolve

    "After lunch, he approached me."

    if decision_party:

        if decision_tora:
            show ryuu suit grin
            ryuu "Thanks again for last night. My brother was very happy."
            show ryuu suit grinblush
            ryuu "Sorry for what he said..."

            mc "It's alright! I like how he's so kind to me."
            mc "It was as if we were already friends when we played."

            show ryuu suit grin
            ryuu "Is that so?"
            show ryuu suit sad
            ryuu "He must be so lonely, living only with me."

        else:
            show ryuu suit happy
            ryuu "Thank you for coming to my brother's party."
            show ryuu suit sad
            ryuu "I think it would be better if you let him call you big %(mc_sib)s."
            show ryuu suit happy
            ryuu "Don't be sad, I just rarely see my brother sad like that."

        show ryuu suit happy
        ryuu "Anyway, it looks like I'm free today, since I already finished today's tasks."
        ryuu "I have nothing to do later... Say, would you like to go out after work?"

    else:
        show ryuu suit happy
        ryuu "It looks like I'm free today, since I already finished today's tasks."
        ryuu "I have nothing to do later... Say, would you like to go out after work?"

    # Selection 3.0
    menu:
        "Sure!":
            # result 3.0.1

            $ ryuu_points += 2

            show ryuu suit happy
            ryuu "Great!"

            if decision_party:
                show ryuu suit grin
                ryuu "I have to treat you since you came to my brother's party."
                ryuu "Really, you're so kind."
            else:
                ryuu "You're so kind."

            mc "Hey, you're the one who's treating me!"
            mc "I should thank you in advance for the food."

            show ryuu suit happyblush
            ryuu "You... you look so cute when your face is like that, haha."

            "What did he say...?"

            jump scene3_1_en

        "I think you need to rest. I also have many things to do.":
            # result 3.0.2

            "I don't want to worry about this work all weekend."
            "I have to work hard if I want a promotion!"

            mc "Actually, I plan to have overtime today."

            show ryuu suit surprised
            ryuu "I heard you didn't have to do much tasks today. Are you sure you don't wanna come?"

            mc "Yes, I'm sure. I'm sorry."

            show ryuu suit sad
            ryuu "That's too bad."
            show ryuu suit happy
            ryuu "Well then, see you tomorrow!"

            jump scene4_0_en

    return


label scene3_1_en:
    scene bg cubicle_night with dissolve

    "I finished work as quickly as possible, so we left early."

    scene bg restaurant_night with dissolve
    "He took us to a famous restaurant."
    "I've gone here once."
    "I see it everyday from the train, but I still couldn't imagine myself going here."

    scene bg restaurant_indoor with dissolve

    "Everything in the menu was extremely expensive."
    "If I wanted to buy one meal, I would have to skip meals for around five days."
    "For example, two small fishes was around Php500!"
    "I thought those dishes were the most expensive they had, but it turned out to be the cheapest!"
    "But the air is excellent! It is as if the air inside the restaurant is like that of heaven's."
    "I tried the squid. This is the most flavorful squid that I have ever tasted!"
    "The flavor was overflowing."
    "The drinks were high quality as well."
    "I tried French champagne, as well as Japanese sake."
    "After eating, Mr. Shigeo paid for everything. He told me it is alright."
    "I am thinking of a return favor, but..."
    "Mr. Shigeo... No, Ryuu... Does he like me?"

    scene sky_night with fade
    "I remembered when we were eating at the restaurant, I saw Ryuu sometimes looking at me."
    "When our eyes met, a smile appeared on his face."
    "Even in the office, when we would go to the cafeteria together, I wanted to touch his hand."
    "Even so, when they accidentally touched, I got nervous, and pulled it back."
    "I'm so stupid!"

    scene sky_noon with dissolve
    "It was always like this."
    "Ryuu has never gotten mad at me."
    "I don't know if I deserve all of this. He's just too nice!"
    "But even after over three months of going out together with his friends, I still haven't known him any better."
    "I wonder whether he's just being fake with me all this time?"

    # Selection 3.1
    menu:
        "I think he's being his own self all along. There's nothing to worry about.":
            $ ryuu_points += 1
            jump scene4_0_en

        "I think he's just being fake, so I won't believe it.":
            $ ryuu_points -= 1
            jump scene3_2_en

    return


label scene3_2_en:
    scene sky_day with dissolve
    "This past week, I have thought about what his real thoughts were."
    "I thought that it's not too bad when I speculate about Ryuu for being not so honest with me."
    "But these are just inside my head. I wanted to resolve this as soon as possible."
    "...And that's what I did."

    scene cubicle_noon with fade

    show ryuu suit sad
    mc "Ryuu, can I ask you something?"
    "Ryuu looks sad. This is rare."
    "I remembered that Tora mentioned that he hasn't been feeling well, lately..."

    show ryuu suit surprised
    ryuu "Ah, %(mc_gname)s."
    ryuu "Sure, what is it?"

    # Selection 4.1
    menu:
        "You have been nice ever since we met. I was wondering if you are really that nice as a person.":
            $ ryuu_points -= 2
            # result 4.1.1

            ryuu "What do you mean?"
            mc "I was thinking that... you're being too nice."
            mc "That you might just be faking."

            show ryuu suit mad
            ryuu "Huh? So are you doubting my attitude towards you?"
            ryuu "What's gotten into you?"

            "He got mad... Do I keep going?"

            # Selection 4.2
            menu:
                "I knew it, you're the kind of person that plays nice to people, so you can get other people's attention.":

                    $ ryuu_points -= 3

                    ryuu "I didn't know until now that that's what you thought about me."
                    ryuu "I pity you."
                    ryuu "You might be hard working, but this company also values attitude towards other office workers."
                    ryuu "Your... speculations lead to bad consequences, so I'm going to the president's office, and speak of your attitude."
                    ryuu "Excuse me."

                    mc "Fine, I was planning to resign anyway."
                    ryuu "That makes everything easier."
                    ryuu "Thank you for your coordination with us in this company, %(mc_title)s %(mc_surname)s."

                    jump bad_en

                "I'm not doubting you... it's just I'm not used to be treated this way. I'm sorry I brought this up.":
                    # result 4.2.2

                    $ ryuu_points += 3

                    show ryuu suit serious
                    ryuu "It's okay."
                    ryuu "Actually, I have to thank you for being honest with me."
                    show ryuu suit sad
                    ryuu "You're the first person who ever said those things to me."

                    if ryuu_points >= 12:
                        ryuu "Let's just forget about what happened earlier..."
                        show ryuu suit happy
                        ryuu "Why don't we go out for lunch?"
                        ryuu "I think I want sushi right now."
                        show ryuu suit grin
                        ryuu "Let's go!"
                        mc "Okay! My treat."
                        show ryuu suit surprised
                        ryuu "Are you sure?"
                        mc "I want to do something for you."
                        mc "Besides, it's always you who pays for my meal, so I thought I would return the favor."
                        jump scene4_0_1_en

                    else:
                        ryuu "Actually... I have to be honest, too."
                        show ryuu suit serious
                        ryuu "Can I speak with you?"
                        jump scene4_0_2_en

        "I visited your brother last Thursday. He told me that you don't feel so well lately.":
            # result 4.1.2

            $ ryuu_points += 3

            show ryuu suit serious
            ryuu "Thank you for visiting my brother."
            show ryuu suit sad
            ryuu "Yes, I am not feeling well lately."
            ryuu "It's just that work is so hectic right now. The deadlines are popping up one after another."
            ryuu "I'm also working on the presentation the president asked me to do. It's also due tomorrow..."

            mc "Okay, since I'm done with my presentations for today, I can help you in yours."
            show ryuu suit surprised
            mc "Also, since you're so busy, I'll get you lunch--my treat!"
            mc "Is that okay with you?"

            if ryuu_points >=5:
                show ryuu suit surprised
                ryuu "Are you sure?"
                mc "Yeah... I want to do something for you."
                mc "Besides, it's always you who pays for my meal, so I thought I would return the favor."
                jump scene4_0_1_en
            else:
                show ryuu suit serious
                ryuu "Actually, I want to talk to you."
                jump scene4_0_2_en


label scene4_0_en:
    scene sky_day with dissolve
    "It has been almost a year since I first met him."
    "I have gone to countless parties and hangouts. But we're still just friends."
    "But every time, it seemed that he couldn't express his true feelings."
    "I couldn't, either."

    scene bg cubicle_day with fade

    "Today, for some reason, he looked kind of sad, which was unusual."
    "He didn't approach me at the usual time."
    "Maybe he's busy with work and decided to skip lunch?"
    "When I visited Tora last Thursday, he told me that Ryuu wasn't feeling well recently."
    "But if that was the case, then why was he still working?"
    "Maybe I should tell him that I was concerned."
    "I think a lunch would be perfect. Besides, it's still lunch time so it wouldn't be so weird."
    "What should I do?"

    # Selection 4.0
    menu:
        "Invite him to lunch":
            # result 4.0.1

            $ ryuu_points += 3

            scene bg cubicle_noon with dissolve
            show ryuu suit serious
            mc "Hey, want to get something to eat?"

            show ryuu suit surprised
            ryuu "Oh! %(mc_gname)s..."

            if ryuu_points >= 12:
                ryuu "I always invite you to lunch, but I'm okay with you initiating."
                ryuu "It's kind of odd, though."
                mc "It's not weird at all."
                mc "Umm... oh, it's just because I want to do something for you."
                mc "Besides, it's always you who pays for my meal, so I thought I would return the favor."
                jump scene4_0_1_en

            else:
                show ryuu suit sad
                ryuu "Right now is a bit..."
                "He looks busy. I should go..."
                show ryuu suit serious
                ryuu "Actually, I want to talk to you."
                jump scene4_0_2_en

        "Wait for him to say it":

            $ ryuu_points += 1

            scene bg cubicle_noon with dissolve
            if ryuu_points >= 12:
                show ryuu suit happy
                ryuu "Want to go out for lunch?"
                mc "Oh, Ryuu! Sure, let's go. My treat!"
                show ryuu suit surprised
                ryuu "Are you sure?"
                mc "Yeah... I want to do something for you."
                mc "Besides, it's always you who pays for my meal, so I thought I would return the favor."
                jump scene4_0_1_en

            else:
                show ryuu suit serious
                ryuu "I want to talk to you."
                jump scene4_0_2_en

    return


label scene4_0_1_en:

    show ryuu suit surprised
    ryuu "Is that so? If you insist..."
    show ryuu suit grin
    ryuu "I guess that shopping from the other day was too expensive."
    ryuu "The restaurant food was also expensive."
    ryuu "I think I have to rest my wallet a bit, right?"

    mc "I didn't mean it that way."
    mc "It's just... um, I'm just concerned."

    show ryuu suit surprisedblush
    ryuu "You, what did you say just now? You're concerned?"

    "Oh no!!"

    mc "It's nothing!!"
    mc "Let's go! I'm so hungry."
    mc "Let's have sushi!"

    show ryuu suit grinblush
    ryuu "Okay."

    jump scene4_1_en

    return


label scene4_0_2_en:

    mc "Me? What's up?"
    ryuu "I need to tell you this, but let's go somewhere private."

    scene bg roadside_noon with dissolve

    "We went for a walk. There weren't many people around."
    "Ryuu suddenly spoke."

    show ryuu suit sad
    ryuu "Okay, I have to say this fast."
    mc "Huh? What? I don't understand."
    show ryuu suit serious
    ryuu "I don't want to disturb you, but... if this continues, I might not take it anymore."
    mc "What...?"
    ryuu "What we have between us... it's happening too fast."

    show ryuu suit sad
    ryuu "I'm sorry if I confused you with my actions."
    ryuu "But I want to focus on my work."

    show ryuu suit worried
    ryuu "Moreover, we're co-workers. Co-workers... should only be working inside the company."
    ryuu "What if the president sees us? I have to think that we are just friends."

    show ryuu suit sad
    ryuu "Even so, I cannot erase my feelings for you."
    ryuu "I'm really sorry for letting you hear this."
    ryuu "It's just that... I'm so confused about everything for which I am not ready yet."
    ryuu "Please don't look at this as if I am weird."

    mc "I'm so sorry. In fact, I'm the same."
    show ryuu suit surprised
    mc "I couldn't express my real feelings to you as well."
    mc "Since I thought you could say it, I waited for you."
    mc "I understand what you are feeling. You're not weird at all, we're just the same."
    mc "If it is your choice, then I respect it."
    mc "I think we could be better off as friends... Please don't cry."

    show ryuu suit happy
    ryuu "Thank you very much for listening to me."
    ryuu "I still can't believe I told you these things."
    ryuu "Maybe I didn't think through what I have said."
    show ryuu suit sad
    ryuu "I think I'm losing my head."

    mc "It's all right. We share the same sentiment."
    mc "Thank you for being honest with me."
    mc "I know that we still have many things left for us, and think this kind of things are just not yet meant to be."
    mc "You are you, Ryuu. This only shows that we can handle these unspoken things."
    mc "Had we spoke of trivial things, we wouldn't have learned about each other."
    mc "In fact, this is not even a mistake, but an opening for us to be closer as friends."
    mc "Don't you think it's better this way?"

    show ryuu suit grin
    ryuu "Yes. Thank you, thank you!"

    jump neutral_en
    return


label scene4_1_en:

    scene sushi with dissolve

    show ryuu suit happy
    ryuu "I'll take the onigiri and the California Maki please."
    mc "Salmon for me."

    scene sushi with fade

    show ryuu suit happy
    ryuu "So, about earlier, what were you saying after you invited me to lunch?"

    "Darn, I thought I could get away with that."

    mc "Nothing, really."
    mc "I just wanted to invite you to lunch, that's all."

    show ryuu suit grin
    ryuu "You told me that you were concerned about me, didn't you?"

    "It seems there's no point in lying."

    mc "Yeah, I'm concerned about you."
    mc "That's what a normal human being feels when their friend is sick right?"

    show ryuu suit happy
    ryuu "Yeah. It's just what I read something from a book."
    show ryuu suit happyblush
    ryuu "It said that when a person feels concerned about you, there's a higher chance that they... well, I don't want to say it, but you know what it is, right?"

    # Selection 4.3.
    menu:
        "No, I don't. What did the book say? There's a higher chance that...?":
            # result 4.3.1

            $ ryuu_points += 2

            show ryuu suit shyhappy
            ryuu "There's a higher chance that that person likes you, or something."
            ryuu "But, I was thinking that..."
            mc "Hmm?"

            show ryuu suit worriedblush
            ryuu "I was thinking that what if..."
            mc "What if what?"
            show ryuu suit shyhappy
            ryuu "What if the book were true?"
            mc "Hehe, well, look at the time, let's get back to work!"
            show ryuu suit grinblush
            ryuu "If you say so, haha."

        "Oh, look at the time! We should go back.":
            # result 4.3.2
            show ryuu suit grin
            ryuu "If you say so, haha."

    jump scene4_1_1_en


label scene4_1_1_en:
    scene station_noon with dissolve

    "Once we got to the office, we saw our co-workers going home."
    "It seemed like the office had some maintenance issues that needed to be fixed."
    "Ryuu received some calls from someone."

    show ryuu suit surprised
    ryuu "Oh, yes, yes. Thank you very much."
    mc "Did the president call you?"
    show ryuu suit serious
    ryuu "Yes, he's extending the deadlines for all requirements to next week."
    ryuu "As for my files, I can work on them at home since I saved them via mail."
    show ryuu suit happy
    ryuu "So, it's okay if you don't help me with that."

    "Wow... a rest day from work. What do I do?"

    # Selection 4.4.
    menu:
        "You want to go somewhere?":
            $ ryuu_points += 2
            show ryuu suit grin
            ryuu "Sure thing."

        "Maybe it's better if we went home early.":
            mc "Okay, if you're sure."
            mc "Then, I'll go home early. Good luck!"
            show ryuu suit grin
            ryuu "Thank you."

    jump scene4_2_en
    return

label scene4_2_en:

    scene bg toy_shop with dissolve

    "We went to a toy shop, since I won a discount coupon from a raffle the other day."
    "Ryuu bought me a blue doll."
    "He told me that he likes making dolls as a hobby."

    show ryuu suit happy
    ryuu "My mom taught me to knit dolls."
    ryuu "I didn't like it at first, but it quickly became a hobby."
    ryuu "Every day, I'd make around two or three. If I feel like it, I'd make ten, and then I'd sometimes forget to eat."
    mc "My mom taught me something, too."
    mc "I was just learning how to cook, and she taught me how to fry the 'perfect egg'."
    mc "And then she made me cook adobo for the family..."

    show ryuu suit grin
    ryuu "Hahaha! Your mom sounds interesting."
    ryuu "I'd love to meet her someday."

    scene bg sky_noon with dissolve

    "The afternoon passed by quickly. It was starting to get dark."
    "But it's Saturday, so no worries about going to work tomorrow."

    scene bg game_center with dissolve
    "We went to the game center and won a teddy bear!"
    "We also met my friend Felicia, the owner of the stuffed toy shop."
    "Felicia looked so happy recently, since she told me that she met her childhood friend, who is also working in the same shop."

    scene bg park_night with dissolve

    "Before I knew it, it was evening already."
    show ryuu suit grin
    ryuu "Well, we had so much fun."
    ryuu "Let's rest here for a bit."
    mc "Yeah, I'm feeling tired as well."

    "I'll just rest for a while..."

    scene black with fade

    jump good_en
    return


label good_en:

    scene bg park_dusk with fade

    "Huh... Did I fall asleep? What time is it?"
    "Oh, it's 11:45pm. I felt so warm, I didn't even notice the time."

    "What's this? Is this his jacket?"

    show ryuu suit surprisedblush
    "I suddenly looked at him and saw him looking at me."
    "He looked surprised, like he was caught in the act."
    show ryuu suit happyblush
    "He stopped looking flustered and relaxed. He smiled."
    "Instead of feeling nervous, I felt warm... and comfortable."
    "It was a different feeling from before."
    "Now that we're alone, the feeling only got stronger... more pure."
    "I took his hand without feeling anything else but comfort."
    "Pressed up so close against him, I noticed that the pocket of his jacket was heavy."
    "I slipped my other hand in and saw... a book?"

    show ryuu suit grinblush
    ryuu "You know, I still wonder if that book's right."
    mc "You mean this?"

    "It was a book about relationships."
    "There were tips on dating and how to tell if a person likes someone."
    "There were handwritten notes on many pages... someone really studied this well."
    "I flipped to the back page. There was even more handwritten notes. Those words..."
    "I looked at him again."
    "He looked at me as he rubbed my hand."

    mc "Yes it is. It is."

    scene black with fade
    return

label neutral_bridge_en:
    scene bg cubicle_noon with fade:

    "On Monday, before lunch, Ryuu approached me."
    show ryuu suit serious
    ryuu "I want to talk to you."
    jump scene4_0_2_en


label neutral_en:
    scene bg bar_night with fade

    "I think when it comes to life's decisions, I should take my time and look deeper into the situation."
    "Here in the company, I have friends whom I enjoy being with. Friends, especially Ryuu, trust me for who I am."
    "I have been promoted as executive secretary, that's why we celebrate tonight."
    "As for Ryuu, I think he's right about what he told me six months ago."
    "One should indeed take their time in pursuing those kinds of decisions."
    "It often takes time to bear fruit of one's actions, as they say."
    "Now I think I feel much better about my choices, but sometimes I still think of that possibility."
    "What if he didn't tell me that?"
    "What if he were not scared, despite the company's rules?"
    "Even so, I am still happy for the both of us..."

    coworkers "Oi! Let's drink already!"
    show ryuu suit grin
    ryuu "Hey! We might not be in the office, but %(mc_pronoun1)s's still the executive secretary!"
    ryuu "Hurry up, %(mc_gname)s!"
    mc "Coming!"

    scene black with fade
    return


label bad_en:
    scene bg cubicle_night with fade

    "As I left the president's office, I read the resignation form that Mr. Shigeo gave me."
    "Attached was a small list containing the company terms and conditions."
    "What is this? '...that you should be with a certain person...'"
    "There is something weird about this company."
    "I tried to open the door for the president's office, but it's locked."

    scene bg cubicle_off with dissolve

    "Suddenly the lights went off... I couldn't see anything."
    "Everything was pitch black."
    "I saw a light coming from one of the cubicles. I slowly approached the cubicle."

    mc "Good evening? I saw on the form that I should meet with you on this cubicle?"
    mc "Cubicle 44? Can I ask if you are the right person?"

    show hanako smile
    "The person turned her head to me. I couldn't recognize her face."
    "The person smiled."

    hanako "Yes, I am that person..."
    mc "Can you tell me your name?"
    mc "I noticed that we were in a place I don't recognize."
    hanako "I am Hanako. Nothing more."
    $ hanako_name = "Hanako"
    hanako "You still chose this path, even if you know you have other options, right?"
    mc "What do you mean?"
    hanako "This is all a game, and you have chosen badly."
    hanako "Now you will be with me forever."
    mc "What's so bad about it?"
    mc "I don't even know who you are, exactly."
    show hanako grin
    hanako "Ahh, don't you remember? I was the one in your listening comprehension exercise #17."
    mc "Impossible! I thought I was done with that nightmarish exercise!"

    "Oh no. What curse have I brought myself into?"

    hanako "You thought wrong. Now you'd have to suffer for your choices."
    hanako "So, repeat after me."
    hanako "I {w=1.0}like {w=1.0}you~"
    mc "No... {w=1.0} No... {w=1.0}"
    mc "NOOOOOOOOOOOOOOOOOOOOOO!!!!" with hpunch
    mc "Nagai-sensei, help meeeeeeee!!!!" with hpunch

    scene black with fade

    "And my body froze completely."
    return
