#PUT YOUR NAME HERE

pre_registered = ['Bennett', 'Blaisse', 'Bushner', 'Byelich', 'Chinn', 'Conner', 
                  'Eudja', 'Gordon', 'Hoffman', 'Johnson', 'Kidder', 'Kiernan', 
                  'Marriott', 'Pugay', 'Sites', 'Smith', 'Young', 'Ansari', 
                  'Asad', 'Baklund', 'Bawden', 'Collich', 'Corrado', 'Deluca', 
                  'Hassler', 'Heitczman', 'Herrera', 'Jimenez', 'Madison', 
                  'McNamara', 'Memis', 'Nelson', 'Odallo', 'Patel', 'Prashad', 
                  'Presta', 'Reyes', 'Taormina', 'Tattersall', 'Teasley', 'Tyce']

#Begin your code below here
last_name = input('Enter Your Last Name: ')

if last_name in ['Bennett', 'Blaisse', 'Bushner', 'Byelich', 'Chinn', 'Conner', 'Gordon', 'Ansari', 'Asad', 'Baklund', 'Bawden', 'Collich', 'Corrado', 'Deluca']:
    print('Please go to Line 1 (A-G)')
if last_name in ['Hoffman', 'Johnson', 'Kidder', 'Kiernan', 'Marriott','Hassler', 'Heitczman', 'Herrera', 'Jimenez', 'Madison', 'McNamara', 'Memis', 'Nelson',]:
    print('Please go to Line 2 (H-N)')
if last_name in ['Pugay', 'Sites', 'Smith', 'Young','Odallo', 'Patel', 'Prashad', 'Presta', 'Reyes', 'Taormina', 'Tattersall', 'Teasley', 'Tyce']:
    print('Please go to Line 3 (O-Z)')
if last_name not in ['Bennett', 'Blaisse', 'Bushner', 'Byelich', 'Chinn', 'Conner', 
                  'Eudja', 'Gordon', 'Hoffman', 'Johnson', 'Kidder', 'Kiernan', 
                  'Marriott', 'Pugay', 'Sites', 'Smith', 'Young', 'Ansari', 
                  'Asad', 'Baklund', 'Bawden', 'Collich', 'Corrado', 'Deluca', 
                  'Hassler', 'Heitczman', 'Herrera', 'Jimenez', 'Madison', 
                  'McNamara', 'Memis', 'Nelson', 'Odallo', 'Patel', 'Prashad', 
                  'Presta', 'Reyes', 'Taormina', 'Tattersall', 'Teasley', 'Tyce']:
    print('Please go to Line 4 (Onsite Registration)')