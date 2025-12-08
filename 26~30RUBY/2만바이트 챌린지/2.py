
import sys
w=sys.stdout.write; s="kjoonOnlineJudge!"
for i in range(1,1<<17): w("BaBeBaB"+s[(i&-i).bit_length()-1])
w("BaBeBaB\n")
