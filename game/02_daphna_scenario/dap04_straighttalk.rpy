﻿###########################
########### LEVEL 04 ##########
###########################
##### REQUEST_04  Straight Talk #####
###########################
label dap_request_04: #LV.4 (Whoring = 11 - 19)
    
    $music("Daphne Theme")

label dap_request_04_complete:
    if daphne.whoring < 11:
        $hero("Думаю, мне не стоит торопиться...// Может позже....")
        call daphne_main_menu_requests
    elif item.Name=="wine" < 1:
        $hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
        call daphne_main_menu_requests
    pass
    if IsRunNumber(1):
        $hero("Хм....// Мисс, как вы относитесь к алкоголю?")
        $daphne("На что вы намекаете, профессор?")
        $hero("Я просто хотел угостить вас вином, из собственного запаса...// Ну раз вы против...")
        $daphne("Чего ради, сэр?")
        $hero("Хотябы ради того, что вы поднялись на 2 пункта в общих списках.")
        $daphne("Что!?// За меня в правду начали голосовать?")
        $hero("Голосовать!?// Да за вас отдают свои голоса, даже дружки ваших конкуренток...")
        $daphne("Правда?!// Это так приятно...// Хм....// Ну хорошо, профессор.... раз такое дело...// Пожалуй я выпью с вами.")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Ну как мисс, вам нравится?")
        $daphne("Безусловно...// Очень богатый букет...")
        $hero("Я рад, что вы можете оценить это по достоинству...// Еще желаете?")
        $daphne("Эм... нет, профессор... думаю мне достаточно...")
        $hero("Ну что ж, Дафна...// Я даже не поинтересовался вашими делами с...")
        $daphne("С мальчиками, сэр?")
        $hero("Именно.")
        $daphne("Ну... Все идет довольно не плохо...// Эм... Ну кажется мое поведение и в правду начало нравится парням.")
        $hero("Были ли какие-то намеки на это?")
        $daphne("Ну если это можно назвать намеком...// Мне понравился один парень из команды Слизерина по квидичу...// И я сказала что если они победят в игре, я подарю ему поцелуй...")
        $hero("И что же?")
        $daphne("Я сдержала свое обещание, ведь он и в правду не плохо играл...")
        $hero("Вы не сожалеете об этом, мисс?")
        $daphne("Конечно нет.// Что в этом такого...// Это же просто поцелуй...")
        $hero("Это похвально.")
        $daphne("Спасибо...")
        $hero("Ну хорошо мисс Гринграсс, можете взять мой не большой подарок, и быть свободны.")
        $daphne.whoring += 1

    elif IsRunNumber(2):
        if item.Name=="wine" < 1:
            $hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
            call daphne_main_menu_requests
        else:
            $hero("Мисс, как вы смотрите на то, что бы выпить со мной?")
            $daphne("Если только это...// Останется между нами.")
            $hero("Конечно.")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Хм....// Эм....")
        $daphne("Что-то не так, профессор?")
        $hero("Эм... да не то чтобы...// ..........// Давайте повторим, и я вам все расскажу.")
        $daphne("Ну хорошо, давайте...")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Эм... в общем, ваше положение в списке...// Ухудшается, мисс...")
        $daphne("Как?!// Я ведь делаю все, чтобы....")
        $hero("Видимо этого не достаточно, мисс...// Понимаете?")
        $daphne("Не совсем, сэр...")
        $hero("Я хочу сказать, что ваши конкурентки, по какой-то причине опережают вас...// И тут нужно действовать быстро и решительно...// Ведь до начала уже совсем не долго...")
        $daphne("Эм....// Я полагаю что вы правы, профессор.// Но... что я еще могу сделать?")
        $hero("Мисс Гринграсс, я думаю что вам не хватает уверенности...// Что не скажешь о других...")
        $daphne("Но... Я же выполняю все ваши поручения, сэр...// Прислушиваюсь к каждому вашиму совету...")
        $hero("И я не могу не похвалить вас за это...// Но если поручение будет вам не посильным...// Вы справитесь?")
        $daphne("Э-э... Смотря о чем будет идти речь...")
        $hero("Скажем....// Я попрошу показать мне, вашу грудь...// Это вам под силу?")
        $daphne("..........// Я... я не знаю, профессор...")
        $hero("А что мешает вам попробовать?")
        $daphne("Эм... Сейчас?")
        $hero("Именно.")
        $daphne("Хорошо...// Дайте мне минутку.")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        "> Сложно не заметить волнение Дафны..."
        "> Но, после долгой возни с бюстгальтером..."
        $daphne.ItemsCustomize(delete={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="g")
        $daphne.ItemsCustomize(delete={"bra"})
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Великолепно Дафна.// Признаться я не думал...")
        $daphne("Эм... что-то еще, сэр?")
        $hero("Гхм... да, мисс...// Вы не могли бы подойти по ближе?")
        $daphne("Э-э... Это обязательно, профессор?")
        $hero("Да, девушка...")
        $daphne("Ну... хорошо...// Только пообещайте что не будете прикасаться...// Эм... трогать...")
        $hero("Я вас понял, мисс...// Я буду просто смотреть.")
        $daphne("Хорошо...")

        $screens.Show(Dissolve(1), "blkfade")
        "Слегка волнуясь, Дафна подходит к вашему столу..."
        $daphne.chibi.State(appearance="g")
        hide screen genie
        show screen dap_look_a2
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Потрясающе...// У вас довольно привлекательные сись... эм... грудь, мисс.")
        $daphne("Профессор, пожалуйста...")
        $hero("Преодолевайте свое стеснение, мисс...// Если вас не будет смущать это, то более легкие задания...// Вы будете щелкать как орешки.")
        $daphne("Хорошо, сэр...// Я постараюсь...")
        $hero("#(Вот и славно)")
        label fel1:
            menu:
                "- Просто смотреть -":
                    $hero("Это восхитительно...// Ваша грудь, мисс, такая молодая...// Смотреть на неё одно удовольствие...")
                    $daphne("...........// Возможно вы правы, сэр...")
                    $hero("Молодец Дафна...// Не останавливайся...")
                    $daphne("Но она меньше чем у других, профессор...// И я кажется комплексую по этому поводу...")
                    $hero("Глупости...// Ваша грудь вполне средних размеров...// Да и к тому же на много красивее, чем у этих эм... полукровок...")
                    $daphne("Верно... я и сама догадывалась...// Что так и есть на самом деле.")
                    $hero("#(Хотя до Гермионы здесь еще далеко)")
                    $daphne("Эм...  Сэр, что, простите...")
                    $hero("Ох... Это просто восхищение Дафна, не обращай внимания...")
                    $daphne("Слушаюсь...")
                    $hero("#(Скоро это слово будет звучать чаще)")
                    "Вы еще какое-то время смотрите на грудь Дафны..."
                    pause.5
                    $hero("Что ж, мисс... можете одеваться.")
                    $daphne("Хорошо.")

                    $screens.Show(Dissolve(1), "blkfade")
                    $daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="a")
                    $daphne.ItemsCustomize(update={"bra"})
                    show screen genie
                    hide screen dap_look_a2
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $daphne.whoring += 1
                "- Начать дрочить -":

                    $screens.Show(Dissolve(1), "blkfade")
                    "Вы достаете свой член, и начинаете дрочить глядя на Дафну..."
                # Чибик дрочащего Джина(Пока отсутствует...)
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $hero("О, да...")
                    $daphne("{size=+5}Профессор что вы делаете?!{/size}// Уберите эту штуку!")
                    $hero("На что вы жалуете, мисс?// Разве я вас трогаю?")
                    $daphne("Да но вы трогаете его...// Это...")

                    $screens.Show(Dissolve(1), "blkfade")
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $daphne.liking-=5
                    $hero("Хорошо... Я кажется немного перегнул...// Давайте забудем это...")
                    $daphne(".........")
                    jump fel1
                "- Схватить Дафну за грудь -":
                    "Вы протягиваете руки, чтобы схватить Дафну за грудь..."
                    $daphne("ПРОФЕССОР!!!// Что вы себе поз...")
                    $hero("Расслабься Дафна, я просто хочу потрогать её...")
                    $daphne("Профессор это слишком...// Я могу вам позволять такое...")
                    $daphne.liking-=10
                    $hero("Хорошо... Я кажется немного перегнул...// Давайте забудем это...")
                    $daphne(".........")
                    jump fel1

        $hero("Вы сегодня на славу постарались, и у меня есть отличный подарок для вас.")

    elif IsRunNumber(3):
        if item.Name=="wine" < 1:
            $hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
            call daphne_main_menu_requests
        else:
            $hero("Мисс, как вы смотрите на то, что бы выпить со мной?")
            $daphne("Если только это...// Останется между нами.")
            $hero("Конечно.")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Хм....// Эм....")
        $daphne("Что-то не так, профессор?")
        $hero("Эм... да не то чтобы...// ..........// Давайте повторим, и я вам все расскажу.")
        $daphne("Ну хорошо, давайте...")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Мисс, я хочу попросить вас, показать мне вашу грудь.")
        $daphne("Снова, сэр?")
        $hero("Да, мисс...")
        $daphne("Хорошо...// Дайте мне минутку.")

        $screens.Show(Dissolve(1), "blkfade")
        "Сложно не заметить как Дафна скрывает свое волнение ..."
        "И после долгой возни с бюстгальтером..."
        $daphne.ItemsCustomize(delete={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="g")
        $daphne.ItemsCustomize(delete={"bra"})
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Великолепно Дафна.// Признаться я не думал...")
        $daphne("Эм... что-то еще, сэр?")
        $hero("Гхм... да, мисс...// Вы не могли бы подойти по ближе?")
        $daphne("Э-э... Это обязательно, профессор?")
        $hero("Да, девушка...")
        $daphne("Ну... хорошо...// Только пообещайте что не будете прикасаться...// Эм... трогать...")
        $hero("Я вас понял, мисс...// Я буду просто смотреть.")
        $daphne("Хорошо...")

        $screens.Show(Dissolve(1), "blkfade")
        "Немного волнуясь, Дафна подходит к вашему столу..."
        $daphne.chibi.State(appearance="g")
        hide screen genie
        show screen dap_look_a2
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Потрясающе...// У вас довольно привлекательные сись... эм... грудь, мисс.")
        $daphne("Профессор, пожалуйста...")
        $hero("Преодолевайте свое стеснение, мисс...// Если вас не будет смущать это, то более легкие задания...// Вы будете щелкать как орешки.")
        $daphne("Хорошо, сэр...// Я постараюсь...")
        $hero("#(Вот и славно)")
        label fel2:
            menu:
                "- Просто смотреть -":
                    $hero("Кажется это мы уже проходили...// Полагаю стоит попробовать что-то по веселее...")
                    jump fel2
                "- Начать дрочить -":

                    $screens.Show(Dissolve(1), "blkfade")
                    "Вы достаете свой член, и начинаете дрочить глядя на Дафну..."
                # Чибик дрочащего Джина(Пока отсутствует...)
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $hero("О, да...")
                    $daphne("{size=+5}Профессор что вы делаете?!{/size}// Уберите эту штуку!")
                    $hero("На что вы жалуете, мисс?// Разве я вас трогаю?")
                    $daphne("Да но вы трогаете его...// Это...")
                    $hero("Что «Это», мисс?// Хотите сказать «это» вас смущает?// Хотите сказать, что чувствуете себя не ловко?")
                    $daphne("Эм... Нет, сэр...// Все в порядке, простите...")
                    $hero("#(Вот это хватка)")
                    "Вы продолжаете дрочить на Дафну..."
                    "Фап - фап - фап"
                    $daphne("..........// Профессор, я хотела сказать...// Что бы вы предупредили, о том...// Когда вы будете... эм... заканчивать...")
                    $hero("О, разумеется, мисс...// Не переживайте.")
                    $daphne("Спасибо....// Сэр....")
                    "Вы набираете более быстрый темп..."
                    "Фап - фап - фап"
                    $hero("Дафна, не отводите от меня взгляд...// Смотрите мне прямо в глаза...")
                    $daphne("Это обязательно, профессор?")
                    $hero("Ты сомневаешься?")
                    $daphne("Нет, сэр... Ни в коем случае...// #(Черт... что я делаю?)// #(Нужно уходить от сюда)")
                    $hero("Скажите, мисс...// Что вы думаете о моем члене?")
                    $daphne("О члене, сэр?!// Я не знаю....// Эм... он большой, сэр...")
                    $hero("Думаете?")
                    $daphne("Да, несомненно это самый огромный член, который я видела...")
                    $hero("О, да....// Кажется я приближаюсь к финалу...// Думаю стоит сбавить темп.")

                    $screens.Show(Dissolve(1), "blkfade")
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $hero("Что ж, вот это высочайшая сила воли...// Ах, да... Можете уже прикрыться, мисс...")

                    $screens.Show(Dissolve(1), "blkfade")
                    $daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="a")
                    $daphne.ItemsCustomize(update={"bra"})
                    show screen genie
                    hide screen dap_look_a2
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $daphne.liking-=2
                    $daphne.whoring += 1
                "- Схватить Дафну за грудь -":
                    "Вы протягиваете руки, чтобы схватить Дафну за грудь..."
                    $daphne("ПРОФЕССОР!!!// Что вы себе поз...")
                    $hero("Расслабься Дафна, я просто хочу потрогать её...")
                    $daphne("Профессор это слишком...// Я могу вам позволять такое...")
                    $daphne.liking-=10
                    $hero("Хорошо... Я кажется немного перегнул...// Давайте забудем это...")
                    $daphne(".........")
                    jump fel2

        $hero("Вы сегодня на славу постарались, и у меня есть подходящий подарок для вас.")

    elif IsRunNumber(4):
        if item.Name=="wine" < 1:
            $hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
            call daphne_main_menu_requests
        else:
            $hero("Мисс, как вы смотрите на то, что бы выпить со мной?")
            $daphne("Если только это...// Останется между нами.")
            $hero("Конечно.")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Хм....// Эм....")
        $daphne("Что-то не так, профессор?")
        $hero("Эм... да не то чтобы...// ..........// Давайте повторим, и я вам все расскажу.")
        $daphne("Ну хорошо, давайте...")

        $screens.Show(Dissolve(1), "blkfade")
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Мисс, я хочу попросить вас, показать мне вашу грудь.")
        $daphne("Снова, сэр?")
        $hero("Да, мисс...")
        $daphne("Хорошо...// Дайте мне минутку.")

        $screens.Show(Dissolve(1), "blkfade")
        "Волнения в Дафне практически нет..."
        "И она уверенно снимает бюстгальтер..."
        $daphne.ItemsCustomize(delete={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="g")
        $daphne.ItemsCustomize(delete={"bra"})
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Великолепно Дафна.// Признаться я не думал...")
        $daphne("Эм... что-то еще, сэр?")
        $hero("Гхм... да, мисс...// Вы не могли бы подойти по ближе?")
        $daphne("Э-э... Это обязательно, профессор?")
        $hero("Да, девушка...")
        $daphne("Ну... хорошо...// Только пообещайте что не будете прикасаться...// Эм... трогать...")
        $hero("Я вас понял, мисс...// Я буду просто смотреть.")
        $daphne("Хорошо...")

        $screens.Show(Dissolve(1), "blkfade")
        "Уверенным шагом, Дафна подходит к вашему столу..."
        $daphne.chibi.State(appearance="g")
        hide screen genie
        show screen dap_look_a2
        pause.5
        $screens.Hide(Dissolve(1), "blkfade")

        $hero("Потрясающе...// У вас довольно привлекательные сись... эм... грудь, мисс.")
        $daphne("Профессор, пожалуйста...")
        $hero("Преодолевайте свое стеснение, мисс...// Если вас не будет смущать это, то более легкие задания...// Вы будете щелкать как орешки.")
        $daphne("Хорошо, сэр...// Я постараюсь...")
        $hero("#(Вот и славно)")
        label fel3:
            menu:
                "- Просто смотреть -":
                    $hero("Кажется это мы уже проходили...// Полагаю стоит попробовать что-то по веселее...")
                    jump fel3
                "- Начать дрочить -":
                    $hero("Кажется это мы уже проходили...// Полагаю стоит попробовать что-то по веселее...")
                    jump fel3
                "- Схватить Дафну за грудь -":
                    "Вы протягиваете руки, чтобы схватить Дафну за грудь..."
                    $daphne("ПРОФЕССОР!!!// Что вы себе поз...")
                    $hero("Расслабься Дафна, я просто хочу потрогать её...")
                    $daphne("Профессор это слишком...// Я... я...// Я не могу так...")
                    $hero("Это последнее о чем я вас сегодня прошу...// Постарайтесь преодолеть это...// Расслабьтесь...")
                    $daphne("Хорошо... Я постараюсь...")
                # Анимашка жмяк - жмяк(Пока отсутствует...)
                    $daphne("Ах....// Ммм....")
                    "Жмяк - жмяк"
                    $hero("Вам нравится, Дафна?")
                    $daphne("Мне?// Я просто...// Все это просто...")
                    $hero("#(А что ты скажешь на это)")
                    "Вы мягко сжимаете грудь Дафны круговыми движениями..."
                    "Жмяк - жмяк"
                    $daphne("Ах....// Мне...// Да...// Да, мне это нравится...")
                    $hero("Хех, это естественно...")
                    $daphne(".........// Ай.....// Сэр, только все это должно остаться между нами...// Я хочу сказать - чтобы об этом никто не узнал…")
                    $hero("О чем речь, мисс...// Наши занятия, это только наше дело.")
                    $daphne("Пообещайте мне.... ах...// Профессор, дайте слово что...// Ай....")
                    $hero("Хорошо, Дафна...// Даю слово что это останется только межу нами.")
                    $daphne("Ах....// Спасибо, сэр...")
                    "Вы еще некоторое время массажируете грудь Дафны..."
                    "Жмяк - жмяк"
                    pause.5

                    $screens.Show(Dissolve(1), "blkfade")
                    pause.5
                # Откатываем чибик на просмотр
                    $screens.Hide(Dissolve(1), "blkfade")

                    $hero("Хорошо, можете прикрыться, Дафна...")
                    $daphne("Да....// Сейчас....")

                    $screens.Show(Dissolve(1), "blkfade")
                    $daphne.ItemsCustomize().chibi.State(appearance="a")
                    pause.5
                    $screens.Hide(Dissolve(1), "blkfade")

                    $hero("Замечательно, мисс Гринграсс.// Вы сегодня превзошли саму себя...")
                    $daphne.whoring += 1

        $hero("И у меня есть отличный подарок для вас.")

    elif IsRunNumber(5):
        $hero("#(На мой взгляд, в этой сфере Дафна уже в полне преуспела)")
        call daphne_main_menu_requests

    return