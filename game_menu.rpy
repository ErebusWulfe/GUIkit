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

    define overlay_save_use = True
    define overlay_save = "gui/game_menu/overlay_save.png"

    define overlay_load_use = True
    define overlay_load = "gui/game_menu/overlay_load.png"

    define overlay_history_use = True
    define overlay_history = "gui/game_menu/overlay_history.png"

    define overlay_about_use = True
    define overlay_about = "gui/game_menu/overlay_about.png"

    define overlay_help_use = True
    define overlay_help = "gui/game_menu/overlay_help.png"

    ##### RECOLOR - HUE MODE ####################################################################################
    ### (does not recolor label and textbutton)

    define gm_button_recolor_gamemenu = False # recolor game menu imagebuttons
    define gm_button_recolor_gamemenuoverlay = False # recolor game menu overlays
    # if you have custom assets, you most likely don't want these ones to be active

    define gm_button_recolor_saveslot = False # recolor save slots
    define gm_button_recolor_misc = False # recolor bars, sliders, etc.

    define gm_button_colorhue = 80 # change the hue color of alternate namebox using the hue rotation
    # value is in 360 DEGREES, meaning 361 = 1, -10 = 350, etc.

    define gm_button_brightness = 0.5 # change the saturation of alternate namebox
    # value is in -1 (darkest) to 1 (brightest); 0 is neutral

    define gm_button_saturation = 1 # change the saturation of alternate namebox
    # value is in 0 (grayscale) to 1 (unaltered saturation)

    ## DUE TO HOW REN'PY ENGINE WORKS, YOU MAY HAVE TO TUNE UP HUE AND BRIGHTNESS TO GET THE SAME EFFECT FROM AN ACTUAL HUE SLIDER

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
    ##### SAVE & LOAD

    define gm_save_xsize = gm_menu_xsize # horizontal size of the help menu content (within game menu base)
    define gm_save_ysize = gm_menu_ysize # vertical size of the help menu content (within game menu base)

    define gm_save_xoffset = gm_menu_xoffset # additional horizontal position adjustment
    define gm_save_yoffset = 50 # additional vertical position adjustment

    define sv_date_size = 20 # size of save files date details
    define sv_date_yoffset = 20 # vertical adjustment, useful to help position the date against the save slots

    define sv_slot_cols = 3 # number of save slot columns (horizontal)
    define sv_slot_rows = 2 # number of save slot rows (vertical)

    define sv_slot_zoom = 0.9 # resize BOTH the save slot frame and screenshot

    define sv_slot_xsize = 414 # save slot width
    define sv_slot_ysize = 309 # save slot height
    # total size of "slot_idle_background" and "slot_hover background" that will be displayed,
    # including any borders or decorations
    # NOT to be mistaken by the size of a save slot in-game screenshot
    
    define sv_slot_spacing_equal = False
    # "True" : use "sv_slot_spacing" value to space file slots equally in horizontal and vertical direction
    # "False" : use "sv_slot_spacing_x" and "sv_slot_spacing_y" to space the file slots

    define sv_slot_spacing = 15 # spacing between save slots
    define sv_slot_spacing_x = 25 # horizontal spacing, if equal spacing is not on
    define sv_slot_spacing_y = 0 # vertical spacing, if equal spacing is not on
    # to make the spice tighter, you can use negative number

    define sv_screenshot_xsize = 385 # minimum screenshot width
    define sv_screenshot_ysize = 242 # minimum screenshot height

    define sv_screenshot_xoffset = -2 # horizontal position adjustment
    define sv_screenshot_yoffset = 0 # vertical position adjustment
    # use this to place the save screenshot in a correct placement


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
    ##### ABOUT SCREEN

    define gm_about_xsize = 1300 # horizontal size of the help menu content (within game menu base)
    define gm_about_ysize = gm_menu_ysize # vertical size of the help menu content (within game menu base)

    define gm_about_xoffset = gm_menu_xoffset # additional horizontal position adjustment
    define gm_about_yoffset = 0 # additional vertical position adjustment

    ### content

    ## Text that is placed on the game's about screen. Place the text between the
    ## triple-quotes, and leave a blank line between paragraphs.

    define gui.about = _p("""GUI script and assets template by {a=https://erebuswulfe.itch.io//}ErebusWulfe.{a}
    """)


    ## A short name for the game used for executables and directories in the built
    ## distribution. This must be ASCII-only, and must not contain spaces, colons,
    ## or semicolons.

    ### build name

    ##### define build.name =
    # you can set the project / build name here, or set one in "options.rpy"

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

    ### RECOLORING

    # hue coloring

    init python:
        def recolor_check_gm(*args):
            if gm_button_recolor_gamemenu:
                return None
            else:
                return 0

    init python:
        def recolor_check_overlay(*args):
            if gm_button_recolor_gamemenuoverlay:
                return None
            else:
                return 0

    init python:
        def recolor_check_sv(*args):
            if gm_button_recolor_saveslot:
                return None
            else:
                return 0

    init python:
        def recolor_check_misc(*args):
            if gm_button_recolor_misc:
                return None
            else:
                return 0

    transform gm_button_recolor:
        function recolor_check_gm
        matrixcolor HueMatrix(gm_button_colorhue)*SaturationMatrix(gm_button_saturation)*BrightnessMatrix(gm_button_brightness)

    transform gm_overlay_recolor:
        function recolor_check_overlay
        matrixcolor HueMatrix(gm_button_colorhue)*SaturationMatrix(gm_button_saturation)*BrightnessMatrix(gm_button_brightness)

    transform sv_slot_recolor:
        function recolor_check_sv
        matrixcolor HueMatrix(gm_button_colorhue)*SaturationMatrix(gm_button_saturation)*BrightnessMatrix(gm_button_brightness)

    transform gm_misc_recolor:
        function recolor_check_misc
        matrixcolor HueMatrix(gm_button_colorhue)*SaturationMatrix(gm_button_saturation)*BrightnessMatrix(gm_button_brightness)

    # tint color

    # misc styles coloring

    style bar:
        left_bar Frame(At("gui/bar/left.png",gm_misc_recolor), gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame(At("gui/bar/right.png",gm_misc_recolor), gui.bar_borders, tile=gui.bar_tile)

    style vbar:
        top_bar Frame(At("gui/bar/top.png",gm_misc_recolor), gui.vbar_borders, tile=gui.bar_tile)
        bottom_bar Frame(At("gui/bar/bottom.png",gm_misc_recolor), gui.vbar_borders, tile=gui.bar_tile)

    style scrollbar:
        base_bar Frame(At("gui/scrollbar/horizontal_[prefix_]bar.png",gm_misc_recolor), gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(At("gui/scrollbar/horizontal_[prefix_]thumb.png",gm_misc_recolor), gui.scrollbar_borders, tile=gui.scrollbar_tile)

    style vscrollbar:
        base_bar Frame(At("gui/scrollbar/vertical_[prefix_]bar.png",gm_misc_recolor), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(At("gui/scrollbar/vertical_[prefix_]thumb.png",gm_misc_recolor), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    style slider:
        base_bar Frame(At("gui/slider/horizontal_[prefix_]bar.png",gm_misc_recolor), gui.slider_borders, tile=gui.slider_tile)
        thumb At("gui/slider/horizontal_[prefix_]thumb.png",gm_misc_recolor)

    style vslider:
        base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        thumb At("gui/slider/vertical_[prefix_]thumb.png",gm_misc_recolor)

    style frame:
        background Frame(At("gui/frame.png",gm_misc_recolor), gui.frame_borders, tile=gui.frame_tile)

    style radio_button:
        foreground At("gui/button/radio_[prefix_]foreground.png",gm_misc_recolor)

    style check_button:
        foreground At("gui/button/check_[prefix_]foreground.png",gm_misc_recolor)

    style choice_button:
        hover_background At("gui/button/choice_hover_background.png",gm_misc_recolor)
        idle_background At("gui/button/choice_idle_background.png",gm_misc_recolor)


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

    ##### SAVE & LOAD (sv)

    transform sv_slot_adjust:
        zoom sv_slot_zoom

    transform sv_screenshot_adjust:
        align (0.5,0.5)
        offset(sv_screenshot_xoffset,sv_screenshot_yoffset)

    style sv_button is gm_button
    style sv_button_text is gm_button_text:
        hover_color gm_textbutton_color_hover
        idle_color gm_textbutton_color_idle
        selected_color gm_textbutton_color_selected

    style sv_name_text is gm_button_text:
        size sv_date_size
        hover_color gm_textbutton_color_hover
        idle_color gm_textbutton_color_selected
        xalign 0.5
        text_align 0.5

        yoffset sv_date_yoffset
    style sv_time_text is sv_name_text

    style slot_button is gm_button:
        xysize (sv_slot_xsize,sv_slot_ysize)

        hover_background At("gui/button/slot_hover_background.png",sv_slot_recolor)
        idle_background At("gui/button/slot_idle_background.png",sv_slot_recolor)
        insensitive_background At("gui/button/slot_insensitive_background.png",sv_slot_recolor)

    style slot_button_text is gm_button_text

    style sv_label is gm_label:
        yalign 0.0
    style sv_label_text is gm_label_text:
        bold False
        hover_color gm_textbutton_color_hover
        idle_color gm_textbutton_color_selected
        text_align 0.5

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

    ##### ABOUT (ab)

    style about_label is gm_label
    style about_label_text is gm_label_text:
        size 40
        text_align 0.0
    style about_text is gm_text
    style about_vbox:
        spacing -70

    ##### EXIT / CONFIRM (ex)

    style confirm_frame is gui_frame:
        background Frame([ "gui/confirm_frame.png", "gui/confirm.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    style confirm_prompt is gui_prompt:
        padding (20,20,20,20)
    style confirm_prompt_text is gui_text
    style confirm_button is gui_medium_button
    style confirm_button_text is gm_button_text
    style confirm_label_text is gm_label_text


    ### BUTTONS

    transform gm_button_adjust:
        zoom 1
        align (0.5,0.5)
        offset (0,0)
        
    style gm_buttons:
        hover_sound gm_button_hover_sound
        activate_sound gm_button_activate_sound
        focus_mask True

    ######################
    ## GAME MENU SCREEN ## DON'T EDIT UNLESS YOU WANT TO CUSTOMIZE IT ON YOUR OWN
    ######################

    #################### GAME MENU

    screen game_menu(title):

        # style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        add gui.game_menu_overlay at gm_overlay_adjust, gm_overlay_recolor
        add gui.game_menu_base at gm_base_adjust

        transclude

        ########## NAVIGATION

        fixed:
            imagebutton auto "gui/button/gm_pref_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action ShowMenu("preferences")
            imagebutton auto "gui/button/gm_save_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action ShowMenu("save")
            imagebutton auto "gui/button/gm_load_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action ShowMenu("load")
            if main_menu: # shows about button when on main menu, otherwise shows history button
                imagebutton auto "gui/button/gm_about_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action ShowMenu("about")
            else:
                imagebutton auto "gui/button/gm_history_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action ShowMenu("history")
            imagebutton auto "gui/button/gm_help_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action ShowMenu("help")
            imagebutton auto "gui/button/gm_exit_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action Show("confirmbutton")

            imagebutton auto "gui/button/gm_return_%s.png" style "gm_buttons" at gm_button_adjust,gm_button_recolor action Return()

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")

    ####################################################################################################
    ##### PREFERENCES
    
    screen preferences():

        tag menu

        use game_menu(_("Preferences")):

            fixed:
                if overlay_pref_use:
                    add overlay_pref at gm_overlay_recolor

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
    ##### SAVE & LOAD

    # save and load screens share the same layout but different utility
    # the "actual" layout is set up in "file_slots" screen

    screen save():
        tag menu
        use file_slots(_("Save"))

    screen load():
        tag menu
        use file_slots(_("Load"))
        
    screen file_slots(title):

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

        use game_menu(title):
            fixed:
                if (title == (_("Save"))) and overlay_save_use:
                    add overlay_save at gm_overlay_recolor
                if (title == (_("Load"))) and overlay_load_use:
                    add overlay_load at gm_overlay_recolor
                
                frame:
                    style_prefix "gm"
                    xysize(gm_save_xsize,gm_save_ysize)
                    offset((config.screen_width-gm_save_xsize)/2 + gm_save_xoffset,(config.screen_height-gm_save_ysize)/2 + gm_save_yoffset)

                    vbox:

                        spacing 10

                        ## this ensures the input will get the enter event before any of the buttons do
                        order_reverse True

                        ## the page name, which can be edited by clicking on a button
                        button:
                            style "sv_label"

                            key_events True
                            xalign 0.5
                            action page_name_value.Toggle()

                            input:
                                style "sv_label_text"
                                value page_name_value

                        ## the grid of file slots

                        grid sv_slot_cols sv_slot_rows:
                            style_prefix "slot"

                            xalign 0.5
                            yalign 0.5

                            if sv_slot_spacing_equal:
                                spacing sv_slot_spacing
                            else:
                                xspacing sv_slot_spacing_x
                                yspacing sv_slot_spacing_y

                            for i in range(sv_slot_cols * sv_slot_rows):

                                $ slot = i + 1

                                button at sv_slot_adjust:
                                    action FileAction(slot)

                                    has vbox
                                    
                                    add FileScreenshot(slot) xysize(sv_screenshot_xsize,sv_screenshot_ysize) at sv_screenshot_adjust

                                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                        style "sv_time_text"

                                    text FileSaveName(slot):
                                        style "sv_name_text"

                                    key "save_delete" action FileDelete(slot)

                        ## buttons to access other pages

                        vbox:
                            style_prefix "sv"

                            xalign 0.5
                            yalign 1.0

                            hbox:
                                xalign 0.5

                                spacing gui.page_spacing

                                textbutton _("<") action FilePagePrevious()
                                key "save_page_prev" action FilePagePrevious()

                                if config.has_autosave:
                                    textbutton _("{#auto_page}A") action FilePage("auto")

                                if config.has_quicksave:
                                    textbutton _("{#quick_page}Q") action FilePage("quick")

                                ## range(1, 10) gives the numbers from 1 to 9.
                                for page in range(1, 10):
                                    textbutton "[page]" action FilePage(page)

                                textbutton _(">") action FilePageNext()
                                key "save_page_next" action FilePageNext()

                            if config.has_sync:
                                if CurrentScreenName() == "save":
                                    textbutton _("Upload Sync"):
                                        action UploadSync()
                                        xalign 0.5
                                        yoffset -12
                                else:
                                    textbutton _("Download Sync"):
                                        action DownloadSync()
                                        xalign 0.5
                                        yoffset -12
                                
    ####################################################################################################
    ###### HISTORY

    screen history():

        tag menu

        ## Avoid predicting this screen, as it can be very large.
        predict False

        use game_menu(_("History")):

            fixed:
                if overlay_history_use:
                    add overlay_history at gm_overlay_recolor
                frame:
                    style_prefix "gm"
                    xysize(gm_history_xsize,gm_history_ysize)
                    offset((config.screen_width-gm_history_xsize)/2 + gm_history_xoffset,(config.screen_height-gm_history_ysize)/2 + gm_history_yoffset)

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
                                label _("The dialogue history is empty."):
                                    xalign 0.5
                                    xoffset gm_history_log_xoffset

    ####################################################################################################
    ##### ABOUT

    screen about():

        tag menu

        ## This use statement includes the game_menu screen inside this one. The
        ## vbox child is then included inside the viewport inside the game_menu
        ## screen.
        use game_menu(_("About")):

            style_prefix "about"

            fixed:
                if overlay_about_use:
                    add overlay_about at gm_overlay_recolor
                vbox:
                    box_wrap True
                    xysize(gm_about_xsize,gm_about_ysize)
                    offset((config.screen_width-gm_about_xsize)/2 + gm_about_xoffset,(config.screen_height-gm_about_ysize)/2 + gm_about_yoffset)

                    style_prefix "about"

                    label "[config.name!t]":
                        xalign 0.0
                    text _("Version [config.version!t]\n"):
                        size 24

                    ## gui.about is usually set in THIS FILE
                    if gui.about:
                        text "[gui.about!t]\n"

                    text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

    ####################################################################################################
    ##### HELP

    screen help():

        tag menu

        default device = "keyboard"

        use game_menu(_("Help")):

            fixed:
                if overlay_help_use:
                    add overlay_help at gm_overlay_recolor
                frame:
                    style_prefix "gm"
                    xysize(gm_help_xsize,gm_help_ysize)
                    offset((config.screen_width-gm_help_xsize)/2 + gm_help_xoffset,(config.screen_height-gm_help_ysize)/2 + gm_help_yoffset)

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
                    text_color gm_text_color
                    xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 100

                    textbutton _("Quit Game") action Quit(confirm=False)
                    textbutton _("Main Menu") action MainMenu(confirm=False)
                    textbutton _("Cancel") action Hide()