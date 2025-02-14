init 100:

    ###################
    ## CONFIGURABLES ##
    ###################

    ### DIALOGUE BOX - adjustment values to the dialogue box

    define s_dialogue_box = "gui/textbox.png"

    # set the textbox image, MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    # you can also use a defined image / layered image

    define s_db_alpha = 0.95
    # by default the dialogue box's transparency is set to 95%
    # set it to 1.0 if you have adjusted the textbox asset's transparency directly

    define s_db_zoom = 1 # zoom value for the dialogue box

    ## POSITIONING
    
    define s_db_xalign = 0.5 # default dialogue box on center of the screen
    define s_db_yalign = 1.0 # default dialogue box on bottom of the screen

    define s_db_xoffset = 0 # horizontal adjustment
    define s_db_yoffset = 0 # vertical adjustment

    ### DIALOGUE TEXT - adjustment values to the dialogue text

    define s_dialogue_text_font = "fonts/Nunito-VariableFont_wght.ttf" # MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    define s_dialogue_text_size = 30
    define s_dialogue_text_color = "#ffffff" # dialogue text color
    
    define s_dialogue_text_kerning = 0 # spacing between characters
    define s_dialogue_text_spacing = 0 # spacing between lines / rows of text
    define s_dialogue_text_alignment = 0.0 # 0.0 = left, 0.5 = centered, 1.0 = right
    define s_dialogue_text_width = 1100 # maximum length of the text before a line break

    ## POSITIONING

    # these positioning uses the TOP LEFT part of the text as the REFERENCE
    define s_dialogue_text_xpos = 0.2 # horizontal position relative to the screen
    define s_dialogue_text_ypos = 0.8 # vertical position relative to the screen

    define s_dialogue_text_xoffset = 0 # horizontal offset, allows for more precise placement
    define s_dialogue_text_yoffset = 0 # vertical offset, allows for more precise placement

    ##############################################################################################################
    ##############################################################################################################

    ### NAMEBOX - adjustment values to the namebox

    define s_namebox = "gui/namebox.png"
    define s_namebox_alt = "gui/namebox_alt.png"

    # set the main and alternate namebox image, MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    # you can also use a defined image / layered image

    ########## ALTERNATE COLOR

    define s_namebox_alternate = False
    # "True"  : use the alternate coloring of the namebox
    # "False" : disable alternate coloring

    # it is recommended to NOT use alternate coloring, unless you want to utilize the color change method below
    # in which case you should set your custom namebox as the alternate namebox

    define s_namebox_colorreplace = False
    # "True"  : REPLACE the alternate namebox color with dynamic-coloring or "s_namebox_tint" value
    # "False" : change the alternate namebox color with hue rotation

    define s_namebox_dynamiccolor = False
    # "True"  : the namebox color will be replaced with "who_color" of each character, allowing you to have
    #           different namebox color for each character, instead of different character name colors
    # "False" : disable namebox dynamic color

    ## == Color Change Mode A ==
    define s_namebox_tint = "#dc4200"
    # COLORIZE the alternate namebox

    ## == Color Change Mode B ==
    define s_namebox_colorhue = 0 # change the hue color of alternate namebox using the hue rotation
    # value is in 360 DEGREES, meaning 361 = 1, -10 = 350, etc.

    define s_namebox_brightness = 0 # change the saturation of alternate namebox
    # value is in -1 (darkest) to 1 (brightest); 0 is neutral

    define s_namebox_saturation = 1 # change the saturation of alternate namebox
    # value is in 0 (grayscale) to 1 (unaltered saturation)

    ## DUE TO HOW REN'PY ENGINE WORKS, YOU MAY HAVE TO TUNE UP HUE AND BRIGHTNESS TO GET THE SAME EFFECT FROM AN ACTUAL HUE SLIDER

    ########## SIZING

    define s_nb_alpha = 1.0
    # by default the namebox's transparency is set to 100%

    define s_nb_zoom = 1 # zoom value for the namebox

    ## AUTO-SCALING - the namebox size will scale based on character's name

    define s_namebox_width_min = 400 # minimum namebox name regardless of the character's name length
    define s_namebox_width_max = None # maximum namebox name regardless of the character's name length

    define s_namebox_border = Borders(20,20,20,20) # ("A":left,"B":top,"C":right,"D":bottom)

    # preserve LEFT-most "A" pixels and RIGHT-most "C" pixels from being stretched HORIZONTALLY (can only be stretched vertically)
    # preserve TOP-most "B" pixels and BOTTON-most "D" pixels from being stretched VERTICALLY (can only be stretched horizontally)
    # USEFUL FOR: keeping specific shape or part of the namebox from being stretched. Only the middle part will be auto-scaled.

    define s_namebox_tile = False # "False" will stretch the namebox, "True" will "repeat" the namebox pattern

    # refer to the following link for better visualization:
    # "https://www.renpy.org/doc/html/displayables.html#Frame"

    define s_namebox_padding = (20,15,20,15) # (left,top,right,bottom) empty pixels between character's name and the outer-most namebox borders

    ## POSITIONING

    define s_nb_xalign = 0.5 # default dialogue box on center of the screen
    define s_nb_yalign = 0.77 # default dialogue box on bottom of the screen

    define s_nb_xoffset = 0 # horizontal adjustment
    define s_nb_yoffset = 0 # vertical adjustment

    ### NAMEBOX TEXT - adjustment values to the namebox text

    define s_namebox_text_font = "fonts/Nunito-VariableFont_wght.ttf" # MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    define s_namebox_text_size = 34
    define s_namebox_text_color = "#ff0000" # default character name color if not defined by "who_color"
    define s_namebox_text_color_alt = "#ffffff" # alternate default character, enabled if "s_namebox_alternate" is "True"
    
    define s_namebox_text_alignment = 0.5 # 0.0 = left, 0.5 = centered, 1.0 = right
    define s_namebox_text_kerning = 5 # spacing between characters

    define s_namebox_text_xoffset = 0 # horizontal offset, allows for more precise placement
    define s_namebox_text_yoffset = 0 # vertical offset, allows for more precise placement

    ########################
    ## TRANSFORM & STYLES ##  SKIP THIS PART - YOU DON'T NEED TO DO ANYTHING HERE
    ########################

    ### DIALOGUE BOX & TEXT

    transform s_db_adjust:
        alpha s_db_alpha
        zoom s_db_zoom
        align (0.5,1.0)
        offset (s_db_xoffset,s_db_yoffset)

    style s_dialogue:
        pos (s_dialogue_text_xpos,s_dialogue_text_ypos)
        offset (s_dialogue_text_xoffset,s_dialogue_text_yoffset)

    define dt_xoffset_default = -390
    define dt_yoffset_default = -70

    ### NAMEBOX & TEXT

    transform s_nb_adjust:
        zoom s_nb_zoom

    transform namebox_color(col="#ffffff"):
        matrixcolor TintMatrix(col)

    style s_namebox:
        xminimum s_namebox_width_min
        xmaximum s_namebox_width_max
        
        align (s_nb_xalign,s_nb_yalign)
        offset (s_nb_xoffset,s_nb_yoffset)

        background Frame(At(s_namebox,s_nb_adjust), s_namebox_border, tile=s_namebox_tile)
        padding s_namebox_padding
    
    style s_namebox_alt:
        background Frame(At(s_namebox_alt,s_nb_adjust), s_namebox_border, tile=s_namebox_tile)

    define nb_xoffset_default = -360
    define nb_yoffset_default = 0

    ##################################
    ## DIALOGUE SCREEN (SAY SCREEN) ## DON'T EDIT UNLESS YOU WANT TO CUSTOMIZE IT ON YOUR OWN
    ##################################

    screen say(who,what): # who = character name (if any) ; what = dialogue text

        fixed:
            add s_dialogue_box at s_db_adjust

        window:

            xoffset dt_xoffset_default
            yoffset dt_yoffset_default

            style "s_dialogue"

            text what id "what":
                font s_dialogue_text_font
                color s_dialogue_text_color

                size s_dialogue_text_size
                kerning s_dialogue_text_kerning
                line_spacing s_dialogue_text_spacing
                text_align s_dialogue_text_alignment

                xmaximum s_dialogue_text_width

        if who is not None:
            window:
                style "s_namebox"
                if s_namebox_alternate:
                    if s_namebox_colorreplace:
                        if s_namebox_dynamiccolor:
                            if (type(renpy.last_say().who) is not str) and ("color" in renpy.last_say().who.who_args):
                                background Frame(Transform(At(s_namebox_alt,s_nb_adjust),matrixcolor=ColorizeMatrix(renpy.last_say().who.who_args["color"],renpy.last_say().who.who_args["color"])), s_namebox_border, tile=s_namebox_tile)
                            else:
                                background Frame(Transform(At(s_namebox_alt,s_nb_adjust),matrixcolor=ColorizeMatrix(s_namebox_tint,s_namebox_tint)), s_namebox_border, tile=s_namebox_tile)
                        else:
                            background Frame(Transform(At(s_namebox_alt,s_nb_adjust),matrixcolor=ColorizeMatrix(s_namebox_tint,s_namebox_tint)), s_namebox_border, tile=s_namebox_tile)
                    
                    else:
                        background Frame(Transform(At(s_namebox_alt,s_nb_adjust),matrixcolor=HueMatrix(s_namebox_colorhue)*BrightnessMatrix(s_namebox_brightness)*SaturationMatrix(s_namebox_saturation)), s_namebox_border, tile=s_namebox_tile)
                text who id "who":
                    font s_namebox_text_font
                    if s_namebox_alternate:
                        color s_namebox_text_color_alt
                    else:
                        color s_namebox_text_color
                    size s_namebox_text_size
                    kerning s_namebox_text_kerning
                    xalign s_namebox_text_alignment

                    offset (s_namebox_text_xoffset,s_namebox_text_yoffset)
            
            if s_namebox_colorreplace and s_namebox_dynamiccolor:
                window:
                    style "s_namebox"
                    background None
                    text who:
                        font s_namebox_text_font
                        color s_namebox_text_color_alt
                        size s_namebox_text_size
                        kerning s_namebox_text_kerning
                        xalign s_namebox_text_alignment

        ## SIDE IMAGE        
        add SideImage() xalign 0.0 yalign 1.0