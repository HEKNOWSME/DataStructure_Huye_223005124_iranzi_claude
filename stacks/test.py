def ask_yes_no(question):
   while True:
      response = input(f"{question} (yes/no): ").strip().lower()
      if response in ['yes', 'no', 'y', 'n']:
         return response
      else:
         print('Please choose with answer yes/y or no/n')
def questions_main():
   response1 = ask_yes_no('Continue ?')
   if response1 in ['yes',  'y']:
      print(f'woo you choose {response1}')
   else:
      print(f"You choose to not continue")
questions_main()