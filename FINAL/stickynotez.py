import stickynotez_util as su

su.stickynotez_banner()
su.list_menu()
menu_choice = input(f'Please choose a stickynotez: ')
print()
su.action_menu()
if menu_choice == 1:
    su.output_file_contents()
