# -*- coding: utf-8 -*-
import cmd, sys, textwrap, time

#constant variables
DESC = 'desc'
DIR = 'dir'
BEAST = 'beast'
R_SPELL = 'right_spell'
NORTH = 'north'
SOUTHWEST = 'southwest'
SOUTHEAST = 'southeast'
EAST = 'east'
WEST = 'west'

SCREEN_WIDTH = 80

#Locations in city
NY_WORLD = {
    'Central Park':{
        DESC:'You enter the New York’s bustling Center Station. Unbeknownst to the muggle crowds below, a Billywig whizzes overhead.',
        DIR:'north',
        EAST:'Tina & Queenie\'s Apartment',
        WEST:'Bank of New York',
        BEAST:'billywig',
        R_SPELL:'accio'
        },
    'Tina & Queenie\'s Apartment':{
        DESC:'You walk into Tina’s home where she and her sister have made a beautiful candlelit dinner. You don’t see anything awry here and Tina looks quite lovely in her evening dress.',
        SOUTHWEST:'Bank of New York',
        DIR:'east',
        BEAST:'bowtruckle',
        R_SPELL:'aparcium'
        },
    'Bank of New York':{
        DESC:'You step into the lobby of the historically ornate Bank of New York. High ceilings and marble columns make this place glitter with wealth. Goblins guard the front desks but you can see many closed doors down snaking halls.',
        DIR:'southwest',
        SOUTHEAST:'Ice Lake in Central Park',
        BEAST:'niffler',
        R_SPELL:'alohomora'
        },
    'Ice Lake in Central Park':{
        DESC:'You wander through thick fog in New York’s famous Central Park. The thunder of hooves echoes over a frozen lake. As you step onto the icy surface, a furious erumpent with sharp horns charges out of the fog!',
        DIR:'west',
        NORTH:'St. Patrick\'s Cathedral',
        BEAST:'erumpent',
        R_SPELL:'stupefy'
        },
    'St. Patrick\'s Cathedral':{
        DESC:'You open the towering wooden doors of St. Patrick\’s Cathedral. Rays of dim light peak through stained glass windows. Feint weeping can be heard from the alter. You see Credence standing there with his head down.',
        DIR:'southeast',
        EAST:'Central Park',
        BEAST:'obscurus',
        R_SPELL:'petrificus totalus'
        }
}


#beasts in city
BEASTS = {
    'billywig':{
        DESC:'native to Austrailia: small, speedy insect that causes levitation and giddiness when they sting.'},
    'bowtruckle':{
        DESC:'tree guardians found in the west of England, Southern Germany, and in some Scandinavian forests. Small in size, bowtruckles are mostly peaceful and shy and generally won\’t attack with their sharp fingers unless their tree is threatened.'},
    'niffler':{
        DESC:'Small, cuddly, and affectionate yet completely destructive, nifflers are usually kept by goblins to search for treasure. While they\’re excellent at finding anything that sparkles, they can quickly cause havoc.'},
    'erumpent':{
        DESC:'one of the more dangerous magical creatures on this list, erumpents are visually similar to a rhinoceros except they have an explosive horn on their heads. They\’re native to Africa and are respected by African witches and wizards.'},
    'obscurus':{
        DESC:'a type of magical parasite that forms when a wizard or witch suppresses their magical ability. It looks like an ash-colored, tendril-equipped cloud and thrashes anything and everything in its path.'}
}

def welcome_screen():
    print"Welcome to Finding Fantastic Beasts!\n"
    print"You are Newt Scamander, beast whisperer and creature extroadinaire."
    print"Your suitcase of magical beasts broke open and now the creatures are"
    print"all running about New York City! Find your beasts by visiting locations"
    print"and casting the right spells. But be careful! Not all of them are friendly!"

    time.sleep(2)
    pass

def displayLocation(loc):
    """A helper function for displaying an area's description and options."""
    # Print the room name.
    print(loc)
    print('=' * len(loc))

    # Print the room's description (using textwrap.wrap())
    print('\n'.join(textwrap.wrap(NY_WORLD[loc][DESC], SCREEN_WIDTH)))

    # Print all the places you can go.
    places_list = []
    for direction in (NORTH, SOUTHEAST, SOUTHWEST, EAST, WEST):
        if direction in NY_WORLD[loc].keys():
            places_list.append(direction.title())
    print()
    if showAllPlaces:
        for direction in (NORTH, SOUTHEAST, SOUTHWEST, EAST, WEST):
            if direction in NY_WORLD[location]:
                print('%s: %s' % (direction.title(), NY_WORLD[location][direction]))
    else:
        print('Moves to: %s' % ' '.join(exits))


def moveDirection(direction):
    """A helper function that changes the location of the player."""
    global location

    if direction in NY_WORLD[location]:
        print('You move to the %s.' % direction)
        location = NY_WORLD[location][direction]
        displayLocation(location)
    else:
        print('You cannot go that way')

def view_suitcase():
    if beasts_in_suitcase == []:
        print "There\'s nothing in here. Time to explore."
    else:
        print beasts_in_suitcase

def view_spellbook():
    print"\n Spellbook:"
    print"\nA. Accio - the summoning charm - use it to summon beasts to you."
    print"Beware: some of them bite."
    print"B. Alohomora - the unlocking charm - use it to open and unlock doors"
    print"or whatever else."
    print"C. Petrificus Totalus - the full body-bind curse - paralyzes an"
    print"opponent."
    print"D. Aparcium - the revealing charm - use it to reveal the concealed."
    print"E. Stupefy - the stunning charm - renders victim unconscious (and"
    print"ready for capture)."
    pass

class FantasticBeastsCmd(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('Were you stung by a billywig? Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in FantasticBeastsCmd.cmdloop()

 # These direction commands have a long (i.e. north) and show (i.e. n) form.
    # Since the code is basically the same, I put it in the moveDirection()
    # function.
    def do_north(self, arg):
        """Go to the area to the north, if possible."""
        moveDirection('north')

    def do_southwest(self, arg):
        """Go to the area to the southwest, if possible."""
        moveDirection('southwest')

    def do_southeast(self, arg):
        """Go to the area to the southwest, if possible."""
        moveDirection('southeast')

    def do_east(self, arg):
        """Go to the area to the east, if possible."""
        moveDirection('east')

    def do_west(self, arg):
        """Go to the area to the west, if possible."""
        moveDirection('west')

    # Shortened names:
    do_n = do_north
    do_sw = do_southwest
    do_se = do_southeast
    do_e = do_east
    do_w = do_west
    
location = 'Central Park'
beasts_in_suitcase = []
showAllPlaces = True

if __name__ == '__main__':
    welcome_screen()
    print()
    print('(Type "help" for commands.)')
    print()
    displayLocation(location)
    FantasticBeastsCmd().cmdloop()
    print 'Thanks for playing!'
