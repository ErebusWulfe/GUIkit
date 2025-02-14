init 100:

    ###################
    ## CONFIGURABLES ##
    ###################

    ### BACKGROUND - adjustment values to the main menu background

    define gui.game_menu_background = "gui/game_menu.png" # default : transparent / blank image
    # this is a NON-GUI background that is displayed beneath the game menu with DECORATIVE PURPOSE
    # set it to transparent to display the progressing game screen instead

    define gm_bg_zoom = 1 # zoom value for the background
    define gm_bg_xoffset = 0 # horizontal adjustment
    define gm_bg_yoffset = 0 # vertical adjustment

    ### BASE GUI - adjustment values to the game menu screen

    define gui.game_menu_overlay = "gui/game_menu/game_menu_overlay.png" # default : black fill
    define gui.game_menu_base = "gui/game_menu/game_menu_base.png"

    # set the background image and overlay, MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    # BE EXTRA CAREFUL: the game menu overlay is placed inside the "/game_menu" folder, NOT "/overlay"
    # you can also use a defined image / layered image

    define gm_base_zoom = 1 # zoom value for the base
    define gm_base_xoffset = 0 # horizontal adjustment
    define gm_base_yoffset = 0 # vertical adjustment

    default gm_overlay = True # shows overlay if set to True
    define gm_overlay_alpha = 0.4 # set opacity of the overlay

    ### MENU OVERLAYS - overlay layer for each menu screen

    define overlay_pref_use = True
    define overlay_pref = "gui/game_menu/overlay_pref.png"

    define overlay_history_use = True
    define overlay_history = "gui/game_menu/overlay_history.png"

    define overlay_help_use = True
    define overlay_help = "gui/game_menu/overlay_help.png"

    ### GENERAL CONTENT - adjustments for game menu content

    ## TEXT

    define gm_label_font = "fonts/Nunito-VariableFont_wght.ttf" # MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    define gm_label_size = 30
    define gm_label_color = "#ff0000" # label text color
    # "label" includes sub-category title

    define gm_text_font = "fonts/Nunito-VariableFont_wght.ttf" # MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    define gm_text_size = 30
    define gm_text_color = "#000000" # general text color

    define gm_textbutton_font = gm_text_font # MAKE SURE THE PATH AND FILE EXTENSION IS CORRECT
    define gm_textbutton_size = 30
    define gm_textbutton_color_selected = gm_text_color
    define gm_textbutton_color_hover = gm_label_color
    define gm_textbutton_color_idle = "#848484"

    # controls the appearance of textbutton, such as save page number, choices in preference, etc.

    ## SIZE & PLACEMENT

    define gm_menu_xsize = 1600 # horizontal size of the menu content (within game menu base)
    define gm_menu_ysize = 700 # vertical size of the menu content (within game menu base)

    define gm_menu_xoffset = 0 # additional horizontal position adjustment
    define gm_menu_yoffset = 60 # additional vertical position adjustment

    # IMPORTANT: menu screen will be aligned to the center. You need to readjust the offset if you change the size.

    ### AUDIO - SFX setup for game menu buttons

    define gm_button_hover_sound = "<silence 0.0>" 
    define gm_button_activate_sound = "audio/sfx/click2.ogg"

    # set the audio path (make sure the file extension is correct)
    # if you don't want the sound effect, replace the audio with "<silence 0.0>"
    # define mm_button_hover_sound = "<silence 0.0>"

    ##############################################################################################################
    ##############################################################################################################

    ########## SPECIFIC SCREEN ADJUSTMENT

    #################
    ##### PREFERENCES

    define gm_pref_xsize = 1300 # horizontal size of the help menu content (within game menu base)
    define gm_pref_ysize = gm_menu_ysize # vertical size of the help menu content (within game menu base)

    define gm_pref_xoffset = gm_menu_xoffset # additional horizontal position adjustment
    define gm_pref_yoffset = gm_menu_yoffset # additional vertical position adjustment

    #################
    ##### HISTORY

    define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }
    ## determines what tags are allowed to be displayed on the history screen

    define gm_history_charactername_size = 34
    define gm_history_charactername_bold = True # bolds character names in history screen

    define gm_history_divider = True # a divider between each history log
    define history_divider = "gui/game_menu/history_divider.png"

    define history_log_format_alternate = False
    # "True" : use alternate format, placing dialogue under character name for a single entry
    # "False" : use default format, placing dialogue and character name next to each other

    ### SIZE & POSITION

    define gm_history_xsize = 1300 # horizontal size of the help menu content (within game menu base)
    define gm_history_ysize = gm_menu_ysize # vertical size of the help menu content (within game menu base)

    define gm_history_xoffset = -50 # additional horizontal position adjustment
    define gm_history_yoffset = gm_menu_yoffset # additional vertical position adjustment
    # affects the viewport, not the dialogue lines directly

    define gm_history_log_xpadding = 400 # horizontal distance from content its viewport border

    define gm_history_log_spacing = 75 # spacing between a set of history log entry (character name, dialogue, divider)
    define gm_history_log_xoffset = -150 # additional horizontal position for history log entry
    

    #################
    ##### HELP SCREEN

    define gm_help_xsize = 1000 # horizontal size of the help menu content (within game menu base)
    define gm_help_ysize = gm_menu_ysize # vertical size of the help menu content (within game menu base)

    define gm_help_xoffset = 0 # additional horizontal position adjustment
    define gm_help_yoffset = gm_menu_yoffset # additional vertical position adjustment  

    define gm_help_textbutton_xoffset = -300 # additional horizontal position for textbutton
    # ("keyboard", "mouse", "gamepad")

    define gm_help_divider = True # a divider between textbutton with the content
    define help_divider = "gui/game_menu/help_divider.png"

    define gm_help_divider_xzoom = 2 # horizontal zoom for the divider

    ########################
    ## TRANSFORM & STYLES ##  SKIP THIS PART - YOU DON'T NEED TO DO ANYTHING HERE
    ########################

    ### BACKGROUND

    transform gm_bg_adjust:
        zoom gm_bg_zoom
        align (0.5,0.5)
        offset (gm_bg_xoffset,gm_bg_yoffset)

    transform gm_base_adjust:
        zoom gm_base_zoom
        align (0.5,0.5)
        offset (gm_base_xoffset,gm_base_yoffset)

    transform gm_overlay_adjust:
        alpha gm_overlay_alpha

    ### CONTENT

    style gm:
        #align (0.5,0.5)
        color gm_text_color

    style gm_text:
        font gm_text_font
        size gm_text_size
        color gm_text_color

    style gm_label:
        yalign 0.5

    style gm_label_text:
        font gm_label_font
        size gm_label_size
        color gm_label_color
        bold True

        text_align 1.0
        min_width 300
    
    style gm_button:
        xalign 0.5

    style gm_button_text:
        font gm_textbutton_font
        size gm_textbutton_size
        selected_color gm_textbutton_color_selected
        hover_color gm_textbutton_color_hover
        idle_color gm_textbutton_color_idle

    style gm_frame:
        xysize(gm_menu_xsize,gm_menu_ysize)
        offset((config.screen_width-gm_menu_xsize)/2 + gm_menu_xoffset,(config.screen_height-gm_menu_ysize)/2 + gm_menu_yoffset)
        # ensures the screens are placed in the middle THEN adjusted with the offset

        background None

    style gm_vbox:
        xsize gm_menu_xsize

    style gm_hbox:
        spacing 20

    style hyperlink_text:
        color gm_label_color

    ##### PREFERENCES (pf)

    style pref_label:
        yalign 0.5

    style pref_label_text:
        font gm_label_font
        size gm_label_size
        color gm_label_color
        bold True

        text_align 0.0

    style pref_button_text:
        font gm_textbutton_font
        size gm_textbutton_size
        selected_color gm_textbutton_color_selected
        hover_color gm_textbutton_color_hover
        idle_color gm_textbutton_color_idle

    style radio_label is pref_label
    style radio_label_text is pref_label_text
    style radio_button_text is pref_button_text

    style check_label is pref_label
    style check_label_text is pref_label_text
    style check_button_text is pref_button_text

    ##### HISTORY (hs)

    style hs_text:
        font gm_text_font
        size gm_text_size
        color gm_text_color

        xalign 0.0
        text_align 0.0

    style hs_label:
        xalign 1.0

    style hs_label_text:
        font gm_label_font
        size gm_history_charactername_size
        color gm_label_color
        bold gm_history_charactername_bold

        text_align 1.0

    style hs2_label:
        xalign 0.0

    style hs2_label_text:
        font gm_text_font
        size gm_text_size
        color gm_text_color

        text_align 0.0

    ### BUTTONS
        
    style gm_buttons:
        hover_sound gm_button_hover_sound
        activate_sound gm_button_activate_sound
        focus_mask True

    ######################
    ## GAME MENU SCREEN ## DON'T EDIT UNLESS YOU WANT TO CUSTOMIZE IT ON YOUR OWN
    ######################

    #################### GAME MENU

    screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

        # style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        add gui.game_menu_overlay at gm_overlay_adjust
        add gui.game_menu_base at gm_base_adjust

        fixed:
            
            align (0.5,0.5)
            fixed:
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True
                        spacing spacing
                        transclude
                else:
                    transclude

        ########## NAVIGATION

        fixed:
            imagebutton auto "gui/button/gm_pref_%s.png" style "gm_buttons" at mm_button_adjust action ShowMenu("preferences")
            imagebutton auto "gui/button/gm_save_%s.png" style "gm_buttons" at mm_button_adjust action ShowMenu("save")
            imagebutton auto "gui/button/gm_load_%s.png" style "gm_buttons" at mm_button_adjust action ShowMenu("load")
            imagebutton auto "gui/button/gm_history_%s.png" style "gm_buttons" at mm_button_adjust action ShowMenu("history")
            imagebutton auto "gui/button/gm_help_%s.png" style "gm_buttons" at mm_button_adjust action ShowMenu("help")
            imagebutton auto "gui/button/gm_exit_%s.png" style "gm_buttons" at mm_button_adjust action Show("confirmbutton")

        ########## NAVIGATION

        textbutton _("Return"):
            style "return_button"

            action Return()

        #label title

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")

    ####################################################################################################
    ##### PREFERENCES
    
    screen preferences():

        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):

            fixed:
                if overlay_pref_use:
                    add overlay_pref

                frame:
                    style_prefix "gm"

                    xysize(gm_pref_xsize,gm_pref_ysize)
                    offset((config.screen_width-gm_pref_xsize)/2 + gm_pref_xoffset,(config.screen_height-gm_pref_ysize)/2 + gm_pref_yoffset)
                    
                    vbox:

                        hbox:
                            box_wrap True

                            if renpy.variant("pc") or renpy.variant("web"):

                                vbox:
                                    style_prefix "radio"
                                    label _("Display")
                                    textbutton _("Window") action Preference("display", "window")
                                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                            vbox:
                                style_prefix "check"
                                label _("Skip")
                                textbutton _("Unseen Text") action Preference("skip", "toggle")
                                textbutton _("After Choices") action Preference("after choices", "toggle")
                                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                            ## Additional vboxes of type "radio_pref" or "check_pref" can be
                            ## added here, to add additional creator-defined preferences.

                        null height (4 * gui.pref_spacing)

                        hbox:
                            style_prefix "slider"
                            box_wrap True

                            vbox:

                                label _("Text Speed")

                                bar value Preference("text speed")

                                label _("Auto-Forward Time")

                                bar value Preference("auto-forward time")

                            vbox:

                                if config.has_music:
                                    label _("Music Volume")

                                    hbox:
                                        bar value Preference("music volume")

                                if config.has_sound:

                                    label _("Sound Volume")

                                    hbox:
                                        bar value Preference("sound volume")

                                        if config.sample_sound:
                                            textbutton _("Test") action Play("sound", config.sample_sound)


                                if config.has_voice:
                                    label _("Voice Volume")

                                    hbox:
                                        bar value Preference("voice volume")

                                        if config.sample_voice:
                                            textbutton _("Test") action Play("voice", config.sample_voice)

                                if config.has_music or config.has_sound or config.has_voice:
                                    null height gui.pref_spacing

                                    textbutton _("Mute All"):
                                        action Preference("all mute", "toggle")
                                        style "mute_all_button"

    ####################################################################################################
    ###### HISTORY

    screen history():

        tag menu

        ## Avoid predicting this screen, as it can be very large.
        predict False

        use game_menu(_("History"), spacing=gui.history_spacing):

            fixed:
                if overlay_help_use:
                    add overlay_history
                frame:
                    style_prefix "gm"
                    xysize(gm_history_xsize,gm_history_ysize)
                    offset((config.screen_width-gm_history_xsize)/2 + gm_history_xoffset,(config.screen_height-gm_history_ysize)/2 + gm_history_yoffset)
                    #background Solid("#fff000")

                    xalign 0.0

                    viewport:
                        xalign 0.0
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable "vertical"
                        pagekeys True
                        side_yfill True
                        vscrollbar_unscrollable "hide"

                        xysize(gm_history_xsize,gm_history_ysize)

                        vbox:
                            xalign 0.0
                            spacing gm_history_log_spacing
                            
                            for h in _history_list:
                                
                                vbox:
                                    xoffset gm_history_log_xoffset
                                    if history_log_format_alternate: # alternate format
                                        hbox:
                                            xalign 0.5
                                            vbox:
                                                xsize (gm_history_xsize - gm_history_log_xpadding)
                                                xalign 1.0
                                                if h.who:
                                                    xalign 0.0
                                                    label h.who:
                                                            style_prefix "hs"
                                                            substitute False
                                                            xalign 0.0
                                                            ## Take the color of the who text from the Character, if set.
                                                            if "color" in h.who_args:
                                                                text_color h.who_args["color"]

                                                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                                text what:
                                                    xoffset 25
                                                    substitute False
                                    else: # default format
                                        hbox:
                                            xoffset -gm_history_log_xoffset
                                            style_prefix "hs"
                                            xsize (gm_history_xsize - gm_history_log_xpadding)
                                            hbox:
                                                xsize 200
                                                if h.who:
                                                    xalign 0.0
                                                    label h.who:
                                                            substitute False
                                                            ## Take the color of the who text from the Character, if set.
                                                            if "color" in h.who_args:
                                                                text_color h.who_args["color"]
                                            hbox:
                                                yoffset 4
                                                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                                style_prefix "hs2"
                                                label what:
                                                    xsize (gm_history_xsize - gm_history_log_xpadding)
                                                    xoffset 25
                                                    substitute False
                                            #if h.who:
                                            #    xalign 0.0
                                            #    label h.who:
                                            #            #style_prefix "hs"
                                            #            substitute False
                                            #            xalign 0.0
                                            #            ## Take the color of the who text from the Character, if set.
                                            #            if "color" in h.who_args:
                                            #                text_color h.who_args["color"]

                                            #$ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                            #text what:
                                            #    xoffset 25
                                            #    substitute False
                                    
                                    if gm_history_divider:
                                        hbox:
                                            yoffset 50
                                            xalign 0.5
                                            add history_divider:
                                                xzoom 3.5

                            if not _history_list:
                                label _("The dialogue history is empty.")

    ####################################################################################################
    ##### HELP

    screen help():

        tag menu

        default device = "keyboard"

        use game_menu(_("Help")):

            fixed:
                if overlay_help_use:
                    add overlay_help
                frame:
                    style_prefix "gm"
                    xysize(gm_help_xsize,gm_help_ysize)
                    offset((config.screen_width-gm_help_xsize)/2 + gm_help_xoffset,(config.screen_height-gm_help_ysize)/2 + gm_help_yoffset)
                    #background Solid("#fff000") # use this for debug / placement purposes

                    vbox:
                        xoffset -100
                        spacing 15

                        hbox:
                            spacing 50
                            xalign 0.5
                            xoffset gm_help_textbutton_xoffset
                            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                            textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                            if GamepadExists():
                                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

                        add help_divider:
                            xalign 0.5
                            xoffset gm_help_textbutton_xoffset
                            xzoom gm_help_divider_xzoom
                        
                        viewport:
                            yinitial 0.0
                            scrollbars "vertical"
                            mousewheel True
                            draggable "vertical"
                            pagekeys True
                            side_yfill True
                            vscrollbar_unscrollable "hide"

                            xysize(gm_help_xsize,gm_help_ysize)
                            
                            vbox:
                                spacing 23
                                if device == "keyboard":
                                    use keyboard_help
                                elif device == "mouse":
                                    use mouse_help
                                elif device == "gamepad":
                                    use gamepad_help


    screen keyboard_help():
        
        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")

        hbox:
            label _("Arrow Keys")
            text _("Navigate the interface.")

        hbox:
            label _("Escape")
            text _("Accesses the game menu.")

        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")

        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")

        hbox:
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Page Down")
            text _("Rolls forward to later dialogue.")

        hbox:
            label "H"
            text _("Hides the user interface.")

        hbox:
            label "S"
            text _("Takes a screenshot.")

        hbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

        hbox:
            label "Shift+A"
            text _("Opens the accessibility menu.")


    screen mouse_help():

        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Middle Click")
            text _("Hides the user interface.")

        hbox:
            label _("Right Click")
            text _("Accesses the game menu.")

        hbox:
            label _("Mouse Wheel Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")


    screen gamepad_help():

        hbox:
            label _("Right Trigger\nA / Bottom Button")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")

        hbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")

        hbox:
            label _("Start, Guide\nB / Right Button")
            text _("Accesses the game menu.")

        hbox:
            label _("Y / Top Button")
            text _("Hides the user interface.")

        textbutton _("{b}Calibrate") action GamepadCalibrate() xalign 0.1

    ####################################################################################################
    ##### EXIT

    screen confirmbutton():

        modal True
        zorder 999

        style_prefix "confirm"
        add "gui/overlay/confirm.png"

        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _("Any unsaved progress will be lost"):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 100

                    textbutton _("Quit Game") action Quit(confirm=False)
                    textbutton _("Main Menu") action MainMenu(confirm=False)
                    textbutton _("Cancel") action Hide()