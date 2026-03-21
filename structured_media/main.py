from catalogue import MediaCatalogue # Import the MediaCatalogue class to manage our collection of media items
from input_handler import media_input # Import the media_input function to get user input for media items
from errors import MediaError # Import the custom MediaError exception to handle errors related to media items

# Create an instance of the MediaCatalogue to store our media items
catalogue = MediaCatalogue()


running = True
while running:
    """Main loop to interact with the user,
    allowing them to add media items or exit the program.
    It handles user input and displays the media catalogue after each addition.
    """
    try:
        command = input('Enter command (add/exit): ').strip().lower()
        if command == 'exit':
            running = False
            print('Exiting the media catalogue. Goodbye!')
            break

        if command != 'add':
            print('Invalid command. Please enter "add" or "exit".')
            continue

        media_item = media_input()
        # add the media item to the catalogue after getting the input
        catalogue.add(media_item)
        print(catalogue)

    except ValueError as e:
        print(f'Validation Error: {e}')

    except MediaError as e:
        # This will print the error message along with the object that caused the error
        print(f'Media Error: {e} - Object: {e.obj}')