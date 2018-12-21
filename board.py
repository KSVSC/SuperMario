"""diplay of the game"""

from __future__ import print_function
from colorama import Fore, Style

A = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [2, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0,
      0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 1],
     [2, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14,
      0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0,
      0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 0,
      0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
	     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

B = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [2, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0,
      0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 1],
     [2, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 14,
      0, 0, 0, 14, 0, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0,
      0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 0,
      0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
	     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

I = [[' '*7, Fore.YELLOW+'X'*7, Fore.YELLOW+'|||'+' '*4,
      ' '*3 + Fore.MAGENTA+'@'+' '*3, Fore.GREEN+' _ _ _ ',
	     Fore.WHITE+' _____ ', Fore.WHITE+'[-----]',
	     Fore.WHITE+' _____ ', Fore.RED+'(%%%%%)', ' '*7,
	     ' '*7, Fore.BLUE+'  _____', Fore.BLUE+'_____  ',
	     Fore.BLUE+' ||    ', Fore.CYAN+'   _   ',
	     ' '*3 + Fore.MAGENTA+'$'+' '*3],
     [' '*7, Fore.YELLOW+'X'*7, Fore.YELLOW+'|||'+' '*4,
	     ' '*2+Fore.MAGENTA+"'0'"+' '*2,
		    Fore.GREEN+'|_|_|_|', Fore.WHITE+'[     ]',
		    Fore.WHITE+'[     ]', Fore.WHITE + '|XXXXX|',
      Fore.RED+' (///) ', Fore.BLUE+'{-----}',
	     Fore.GREEN+' (&&&) ', Fore.BLUE+' ||____',
		    Fore.BLUE+'_____| ', Fore.BLUE+' ||    ',
			   Fore.CYAN+' _( )_ ', ' '*2+Fore.MAGENTA+'"0"'+' '*2],
     [' '*7, Fore.YELLOW+'X'*7, Fore.YELLOW+'|||'+' '*4,
	     ' '*2+Fore.MAGENTA+'^ ^'+' '*2,
		    Fore.GREEN+'|_|_|_|', Fore.WHITE+'[     ]',
		    Fore.WHITE+'[     ]', Fore.WHITE + '|XXXXX|',
		    Fore.RED+'  ) (  ', Fore.BLUE+'  | |  ',
			   Fore.GREEN+'  } {  ', Fore.BLUE+' ||____',
			   Fore.BLUE+'_____| ', Fore.BLUE+' ||    ',
			   Fore.CYAN+'(_____)',
			   ' '*2+Fore.MAGENTA+'^ ^'+' '*2]]

print (Style.RESET_ALL)


def print_board(arr):
    """printboard"""
    for i in range(11):
        for k in range(3):
            p_b = []
            for j in range(15):
                p_b.append(I[k][arr[i][j]])
            print(''.join(p_b))

    print("\n")
