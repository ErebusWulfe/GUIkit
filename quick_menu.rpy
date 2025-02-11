init 100:

    ###################
    ## CONFIGURABLES ##
    ###################

    ### BUTTONS - adjustment values to the main menu buttons assets

    define qm_button_zoom = 1 # zoom value for the buttons
    define qm_button_xoffset = 0
    define qm_button_yoffset = 0

    define qm_alternate_pos = False # positions the quick menu button on top right corner of the screen
    # if you use your own custom buttons, you may need to adjust the position of the buttons yourself

    define qm_button_hover_sound = "<silence 0.0>" 
    define qm_button_activate_sound = "<silence 0.0>"

    # set the audio path (make sure the file extension is correct)
    # if you don't want the sound effect, replace the audio with "<silence 0.0>", for example:
    # define mm_button_hover_sound = "<silence 0.0>"
    # by default the quick menu button SFX is set to SILENCE as it may cause too much distraction

    ########################
    ## TRANSFORM & STYLES ##  SKIP THIS PART, YOU DON'T NEED TO DO ANYTHING HERE
    ########################

    # BUTTONS

    transform qm_button_adjust:
        zoom qm_button_zoom
        xalign 0.5
        yalign 0.5
        xoffset qm_button_xoffset
        yoffset qm_button_yoffset

    style qm_buttons:
        hover_sound qm_button_hover_sound
        activate_sound qm_button_activate_sound
        focus_mask True
    
    #######################
    ## QUICK MENU SCREEN ##
    #######################

    screen quick_menu():

        zorder 100

        if quick_menu:

            fixed:

                ### alternate pos
                if qm_alternate_pos:
                    ypos -0.925
                    xpos 0.38

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