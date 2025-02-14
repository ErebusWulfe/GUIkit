init 100:

    ###################
    ## CONFIGURABLES ##
    ###################

    ### BUTTONS - adjustment values to the main menu buttons assets

    define qm_button_zoom = 1 # zoom value for the buttons
    define qm_button_xoffset = 0
    define qm_button_yoffset = 0

    define qm_alternate_pos = False
    # "False" : standard quick menu layout (bottom-mid screen)
    # "True" : positions the quick menu button on top right corner of the screen
    # if you use your own custom buttons, you may need to adjust the position of the buttons yourself

    define qm_button_hover_sound = "<silence 0.0>" 
    define qm_button_activate_sound = "<silence 0.0>"

    # set the audio path (make sure the file extension is correct)
    # if you don't want the sound effect, replace the audio with "<silence 0.0>", for example:
    # define mm_button_hover_sound = "<silence 0.0>"
    # by default the quick menu button SFX is set to SILENCE as it may cause too much distraction

    ### BUTTONS OVERLAY - an image overlay bellow the buttons, usually used for the buttons' "dock"

    define qm_button_overlay_use = False # this image will not be interactable

    define qm_button_overlay = "gui/overlay/quick_menu_overlay.png"
    # set the quick menu overlay image, MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    # DO NOT delete the image even if you don't use it

    ### BUTTONS RECOLORING - adjustment values to the main menu buttons assets

    define qm_color_mode = 0

    # change the color of the quick menu buttons with 3 options
    # (THIS WILL NOT RECOLOR THE OVERLAY):
    # - mode 0 = no changes
    # - mode 1 = COLORIZE the buttons with a specific color
    # - mode 2 = change the buttons color by changing its hue, brightness, and saturation

    ## MODE 1
    define qm_button_tint = "#4335ff"
    # COLORIZE the quick menu buttons

    ## MODE 2
    define qm_button_colorhue = 0 # change the hue color of quick menu buttons using the hue rotation
    # value is in 360 DEGREES, meaning 361 = 1, -10 = 350, etc.

    define qm_button_brightness = 0 # change the saturation of quick menu buttons
    # value is in -1 (darkest) to 1 (brightest); 0 is neutral

    define qm_button_saturation = 1 # change the saturation of quick menu buttons
    # value is in 0 (grayscale) to 1 (unaltered saturation)

    ## DUE TO HOW REN'PY ENGINE WORKS, YOU MAY HAVE TO TUNE UP HUE AND BRIGHTNESS TO GET THE SAME EFFECT FROM AN ACTUAL HUE SLIDER

    ########################
    ## TRANSFORM & STYLES ##  SKIP THIS PART, YOU DON'T NEED TO DO ANYTHING HERE
    ########################

    # BUTTONS

    init python:
        def qm_color_check_0(*args):
            if qm_color_mode == 0:
                return None
            else:
                return 0
        def qm_color_check_1(*args):
            if qm_color_mode == 1:
                return None
            else:
                return 0
        def qm_color_check_2(*args):
            if qm_color_mode == 2:
                return None
            else:
                return 0

    transform qm_button_color0:
        matrixcolor SaturationMatrix(1)

    transform qm_button_color1:
        matrixcolor ColorizeMatrix(qm_button_tint,qm_button_tint)

    transform qm_button_color2:
        matrixcolor HueMatrix(qm_button_colorhue)*BrightnessMatrix(qm_button_brightness)*SaturationMatrix(qm_button_saturation)

    transform qm_button_adjust:
        zoom qm_button_zoom
        xalign 0.5
        yalign 0.5
        xoffset qm_button_xoffset
        yoffset qm_button_yoffset

        parallel:
            function qm_color_check_0
            qm_button_color0
        parallel:
            function qm_color_check_1
            qm_button_color1
        parallel:
            function qm_color_check_2
            qm_button_color2
        
        #qm_button_color1

    style qm_buttons:
        hover_sound qm_button_hover_sound
        activate_sound qm_button_activate_sound
        focus_mask True
    
    #######################
    ## QUICK MENU SCREEN ## DON'T EDIT UNLESS YOU WANT TO CUSTOMIZE IT ON YOUR OWN
    #######################

    screen quick_menu():

        zorder 100 # makes sure it shows up above of other screens - DO NOT EDIT

        if quick_menu:

            fixed:

                ### alternate pos
                if qm_alternate_pos:
                    ypos -0.925
                    xpos 0.38

                showif qm_button_overlay_use:
                    add qm_button_overlay

                # Back
                imagebutton auto "gui/button/qm_back_%s.png" style "qm_buttons" at qm_button_adjust action Rollback()

                # History
                imagebutton auto "gui/button/qm_history_%s.png" style "qm_buttons" at qm_button_adjust action ShowMenu('history')

                # Skip
                imagebutton auto "gui/button/qm_skip_%s.png" style "qm_buttons" at qm_button_adjust action Skip() alternate Skip(fast=True, confirm=True)

                # Auto
                imagebutton auto "gui/button/qm_auto_%s.png" style "qm_buttons" at qm_button_adjust action Preference("auto-forward", "toggle")

                # Save
                imagebutton auto "gui/button/qm_save_%s.png" style "qm_buttons" at qm_button_adjust action ShowMenu('save')

                # Pref
                imagebutton auto "gui/button/qm_pref_%s.png" style "qm_buttons" at qm_button_adjust action ShowMenu('preferences')

                # By default Q.Save and Q.Load are not used
                # imagebutton auto "gui/button/qm_qsave_%s.png" style "qm_buttons" at qm_button_adjust action QuickSave()
                # imagebutton auto "gui/button/qm_qload_%s.png" style "qm_buttons" at qm_button_adjust action QuickLoad()

                # Call custom screen
                # imagebutton auto "gui/button/qm_[custom_button]_%s.png" style "qm_buttons" at qm_button_adjust action Call("custom_screen")