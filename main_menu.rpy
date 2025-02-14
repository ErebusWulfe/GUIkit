init 100:

    ###################
    ## CONFIGURABLES ##
    ###################

    ### BACKGROUND - adjustment values to the main menu background

    define gui.main_menu_background = "gui/main_menu.png"
    define gui.main_menu_overlay = "gui/overlay/main_menu_overlay.png"

    # set the background image and overlay, MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    # you can also use a defined image / layered image

    default mm_overlay = True # shows overlay if set to True

    define mm_bg_zoom = 1 # zoom value for the background
    define mm_bg_xoffset = 0 # horizontal adjustment
    define mm_bg_yoffset = 0 # vertical adjustment

    ### BUTTONS - adjustment values to the main menu buttons assets

    define mm_button_zoom = 1 # zoom value for the buttons
    define mm_button_xoffset = 0 # horizontal position adjustment
    define mm_button_yoffset = 0 # vertical position adjustment

    define mm_button_hover_sound = "audio/sfx/click1.ogg" 
    define mm_button_activate_sound = "audio/sfx/click2.ogg"

    # set the audio path (make sure the file extension is correct)
    # if you don't want the sound effect, replace the audio with "<silence 0.0>"
    # define mm_button_hover_sound = "<silence 0.0>"

    ### VERSION - version text configuration (overrides the configuration in "options.rpy")
    # if you want to display the project version on main menu, set "mm_version" to True

    define mm_version = True
    define config.version = "v0.01"

    define mm_project_version_size = 24
    define mm_project_version_xalign = 1.0 # 0.0 for left, 0.5 for center, 1.0 for right
    define mm_project_version_yalign = 1.0 # 0.0 for top, 0.5 for center, 1.0 for bottom
    define mm_project_version_xoffset = -20
    define mm_project_version_yoffset = -20

    ########################
    ## TRANSFORM & STYLES ##  SKIP THIS PART - YOU DON'T NEED TO DO ANYTHING HERE
    ########################

    ### BACKGROUND

    transform mm_bg_adjust:
        zoom mm_bg_zoom
        align (0.5,0.5)
        offset (mm_bg_xoffset,mm_bg_yoffset)

    ### BUTTONS

    transform mm_button_adjust:
        zoom mm_button_zoom
        align (0.5,0.5)
        offset (mm_button_xoffset,mm_button_yoffset)

    style mm_buttons:
        hover_sound mm_button_hover_sound
        activate_sound mm_button_activate_sound
        focus_mask True

    ### VERSION
    
    style mm_project_version:
        align (mm_project_version_xalign,mm_project_version_yalign)
        offset (mm_project_version_xoffset,mm_project_version_yoffset)

    ######################
    ## MAIN MENU SCREEN ## DON'T EDIT UNLESS YOU WANT TO CUSTOMIZE IT ON YOUR OWN
    ######################

    screen main_menu():
        tag menu

        add gui.main_menu_background

        showif mm_overlay:
            add gui.main_menu_overlay

        if renpy.get_screen("main_menu"):
            fixed:
                if main_menu:

                    # Start
                    imagebutton auto "gui/button/mm_start_%s.png" style "mm_buttons" at mm_button_adjust action Start()
                    
                    # Load
                    imagebutton auto "gui/button/mm_load_%s.png" style "mm_buttons" at mm_button_adjust action ShowMenu("load")
                    
                    # Preferences
                    imagebutton auto "gui/button/mm_pref_%s.png" style "mm_buttons" at mm_button_adjust action ShowMenu("preferences")
                    
                    # About
                    imagebutton auto "gui/button/mm_about_%s.png" style "mm_buttons" at mm_button_adjust action ShowMenu("about")

                    ### Help - this menu is not necessary on Android
                    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                        imagebutton auto "gui/button/mm_help_%s.png" style "mm_buttons" at mm_button_adjust action ShowMenu("help")

                    ### Quit - this button is banned on iOS and unnecessary on Android and Web
                    if renpy.variant("pc"):
                        imagebutton auto "gui/button/mm_quit_%s.png" style "mm_buttons" at mm_button_adjust action Quit(confirm=not main_menu)

                    ### used only in replay mode - sample assets are not provided
                    #if _in_replay:
                    #    imagebutton auto "gui/button/mm_endreplay_%s.png" style "mm_buttons" at mm_button_adjust action EndReplay(confirm=True)

            vbox:
                if mm_version:
                    style "mm_project_version"
                    text "[config.version]":
                        size mm_project_version_size