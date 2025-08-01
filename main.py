import pygame
import menu

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
current_buttons = []
previous_buttons = []
running = True
menu.set_screen(screen)
pygame.display.set_caption("Programming Dungeon")


settings = {
    "volume" : 50,
    "simulation speed" : 50,
    "fullscreen" : False
}
#will store any events the buttons return to be enacted later
button_events = []
#start the mouse position at 0,0 so the program doesn't crash trying to reference it before
#retrieving the mouse position for the first time
mouse_position = (0, 0)
current_buttons += menu.initalise_menu_screen()
if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                for button in current_buttons:
                    if button.detect_mouse(mouse_position):
                        button_events.append(button.button_function())
                        print(button_events)

        screen.fill((255, 255, 255))
        mouse_position = pygame.mouse.get_pos()

        #for button in previous_buttons:
        #    button.draw_self()
        for button in current_buttons:
            button.draw_self()


        #if a button has returned an event it will be in button events
        for event in button_events:
            #exits the main loop and uninitialises pygame to exit the game without error
            if event == "quit":
                running = False
                pygame.quit
            elif event == "open options":
                #if options has been opened we store what the previous buttons were
                #this is so we can return easily, since the options menu is just a sub menu
                #after that we can just clear the current buttons and add the buttons
                #for the options menu
                previous_buttons = current_buttons
                current_buttons = menu.open_options_menu()
            elif event == "close options":
                print("wants to close options")
                current_buttons = previous_buttons
                previous_buttons = []
            elif event == "set volume":
                #finds the slider responsible for the volume
                for slider in current_buttons:
                    if slider.variable == "volume":
                        #adjusts the volume to the value of the slider
                        settings["volume"] = slider.value
            elif event == "set simulation speed":
                #finds the slider responsible for the sim speed
                for slider in current_buttons:
                    if slider.variable == "simulation speed":
                        #adjusts the sim speed to the value of the slider
                        settings["simulation speed"] = slider.value
            elif event == "toggle fullscreen":
                settings["fullscreen"] = not settings["fullscreen"]
            #functionality for more buttons can be easily added later by adding more elif statements here
            else:
                pass
        #clear the list of events to avoid acting on a single button press multiple times
        button_events = []

        pygame.display.update()

        clock.tick(60)
