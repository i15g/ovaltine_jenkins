# !/usr/bin/env python

import random

def ovaltine_jenkins():
	names = "Die Harder, Matt, Bighead Burton, Fingers, Homeskillet, Big Baby Burton, Burt the Billowy Bear, Curtis, Blackstar, Chocolate Columbo, Magic Head, Spellmaster, SuperSmeller, SuperSniffer, Slicks, Peter Panic, Gus T.T. Showbiz (The Extra T is for Extra Talent), Ovaltine Jenkins, Schoonie \"U-Turn\" Singleton, Vernest Lambert Watkins, Bud, Nick Nack, Bruton \"Gasty\" Gaster, Lavender Gooms, Lemongrass Gogulope, Squirts MacIntosh, Weepy Boy Santos, Stewart Lee, Dr. Mc (Khoesan tongue clicking sounds) Took, Francois, Galileo Humpkins, Gus \"SillyPants\" Jackson, Fearless Guster, Shmuel Cohen, Methuselah Honeysuckle, Shutterfly Simmons, Paddy Simcox, Chesterfield McMilla, Felicia Fancybottom, Tan, Ernesto Agapito Garces con y a de Abelar, Longbranch Pennywhistle, Watson Williams, Scrooge Jones, D\'Andre Pride, Hummingbird Saltalamacchia, Wally Ali, Art Vandelay, Dequan \"Smallpox\" Randolph, Trapezius Milkington, Sterling Cooper, Burton \"Oil Can\" Guster, Hollabackatcha, Jazz Hands, Gus Brown, John Slade, Detective Miles, Greg, Doughnut Holschtein, Ron Davis, Bob Adams, Harry Munroe, Rich Fingerland, Black Magic, Cheswick, Shawn, Magic Eight Ball Head, Shaggy Buddy Snap, Ghee Buttersnaps aka \"The Heater\", The Vault of Secrets, Clementine Woolysocks, Pinky Guscatero, Guts, Ol\' Ironside, Old Iron Stomach, Bruce Lee, Jonathan Jacob \"Jingleheimer\" Schmidt, Santonio Holmes, Deon Richmond, Gurton Buster, Chaz Bono, Chocolate Einstein, MC ClapYoHandz, Sher-Black-Lock, Mrs. Whittlebury, G-Force, Mellowrush, Crankshaft, Sammy, Joey Bishop, Slick Fingers, Imhotep, Control Alt Delete, The Jackal, Adewale Akinnuoye-Agbaje, Donut Holestein, Yasmine Bleeth, Lodge Blackman, Jet Blackness, Mission Figgs, Radio Star (Video will kill him), Gusjay Gubta, Reginald G-String AKA Crowd Pleaser, Fingers, Cinderella, Gasty, Earnest Lambert Watkins, Dr. Guster, Road Rash, Suggs, Fellatio Del Toro, Larenz Tate, Candyman, Gurn Blanston, Pootie Tang, Domo Arigato, Blue Ivy Carter, Bill Ofrights, Vijay Armitraj, Darryl Figgins, Flapjack Palmdale, Burton Trout, King Mongkut, Gigi Van Tran, Robert \"Booooooooooob\" Jones, Zazu"

	names_list = [x.strip() for x in names.split(',')]
	print(random.choice(names_list))

if __name__ == '__main__':
    ovaltine_jenkins()
