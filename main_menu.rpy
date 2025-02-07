init -100:

    ###################
    ## CONFIGURABLES ##
    ###################

    # BACKGROUND - adjustment values to the main menu background

    define gui.main_menu_background = "gui/main_menu.png"
    define gui.main_menu_overlay = "gui/overlay/main_menu_overlay.png"

    # set the background image and overlay, MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    # you can also use a defined image / layered image
    # if you don't need the overlay, replace it with a blank image (DO NOT DELETE THE FILE)

    define mm_bg_zoom = 1 # zoom value for the background
    define mm_bg_xoffset = 0 # horizontal adjustment
    define mm_bg_yoffset = 0 # vertical adjustment

    # BUTTONS - adjustment values to the main menu buttons assets

    define mm_button_zoom = 1 # zoom value for the buttons
    define mm_button_xoffset = 0
    define mm_button_yoffset = 0

    # VERSION - version text configuration (overrides the configuration in "options.rpy")
    # if you want to display the project version on main menu, set "mm_version" to True

    define mm_version = False
    define project_version = "v0.01"
    define config.version = project_version # DO NOT EDIT THIS LINE

    define mm_project_version_size = 24
    define mm_project_version_xalign = 1.0 # 0.0 for left, 0.5 for center, 1.0 for right
    define mm_project_version_yalign = 1.0 # 0.0 for top, 0.5 for center, 1.0 for bottom
    define mm_project_version_xoffset = -20
    define mm_project_version_yoffset = -20

    ########################
    ## TRANSFORM & STYLES ##  SKIP THIS PART, YOU DON'T NEED TO DO ANYTHING HERE
    ########################

    # BACKGROUND

    transform mm_bg_adjust:
        zoom mm_bg_zoom
        xalign 0.5
        yalign 0.5
        xoffset mm_bg_xoffset
        yoffset mm_bg_yoffset

    # BUTTONS

    transform mm_button_adjust:
        zoom mm_button_zoom
        xalign 0.5
        yalign 0.5
        xoffset mm_button_xoffset
        yoffset mm_button_yoffset

    # VERSION
    
    style mm_project_version:
        align (mm_project_version_xalign,mm_project_version_yalign)
        offset (mm_project_version_xoffset,mm_project_version_yoffset)

    ######################
    ## MAIN MENU SCREEN ##
    ######################


    screen main_menu():
        tag menu

        add gui.main_menu_background
        add gui.main_menu_overlay

        if renpy.get_screen("main_menu"):
            fixed:
                if main_menu:

                    # Start
                    imagebutton auto "gui/button/mm_start_%s.png" focus_mask True at mm_button_adjust action Start()
                    
                    # Load
                    imagebutton auto "gui/button/mm_load_%s.png" focus_mask True at mm_button_adjust action ShowMenu("load")
                    
                    # Preferences
                    imagebutton auto "gui/button/mm_pref_%s.png" focus_mask True at mm_button_adjust action ShowMenu("preferences")
                    
                    # About
                    imagebutton auto "gui/button/mm_about_%s.png" focus_mask True at mm_button_adjust action ShowMenu("about")

                    ### Help - this menu is not necessary on Android
                    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                        imagebutton auto "gui/button/mm_help_%s.png" focus_mask True at mm_button_adjust action ShowMenu("help")

                    ### Quit - this button is banned on iOS and unnecessary on Android and Web
                    if renpy.variant("pc"):
                        imagebutton auto "gui/button/mm_quit_%s.png" focus_mask True at mm_button_adjust action Quit(confirm=not main_menu)

                    ### used only in replay mode - sample assets are not provided
                    #if _in_replay:
                    #    imagebutton auto "gui/button/mm_endreplay_%s.png" focus_mask True at mm_button_adjust action EndReplay(confirm=True)

            vbox:
                if mm_version:
                    style "mm_project_version"
                    text "[project_version]":
                        size mm_project_version_size