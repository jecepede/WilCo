#
#    __          __  _   _    _____
#    \ \        / / (_) | |  / ____|
#     \ \  /\  / /   _  | | | |        ___
#      \ \/  \/ /   | | | | | |       / _ \
#       \  /\  /    | | | | | |____  | (_) |    W I L d c a r d   C O m p a r e   !
#        \/  \/     |_| |_|  \_____|  \___/
#
#                                                              By: Jecepede 'Weird' Al
#


#
# Import libs
#
import re


#
# Declare vars
#
givenString = "The quick brown fox jumps over the lazy dog (at 17:21.12)..."            # The string that needs to be compared usually given by a (blackbox) process
givenRebuildString = ""                                                                 # A rebuild given string based on blocks from expectedString

expectedString = "_ANY_ quick _ANY_ fox jumps over the lazy _ANY_ (at _ANY_)..._ANY_"   # The expected result when comparing inputString usually used by a test
expectedStrippedString = re.sub('_ANY_', '', expectedString)                            # The reg-edited string, stripped of it's wildcards

foundDifferences = 0                                                                    # How many blocks were different ?
differentBlocks = list()                                                                # What blocks were different ?


#
# Print status message
#
print("So we are comparing :")
print("- - -")
print("givenString         : '{}' ".format(givenString) + "({} characters long)".format(len(str(givenString))))
print("with expectedString : '{}' ".format(expectedString) + "({}-ish characters long) \n\n".format(len(str(expectedString))))


#
# Create a list of fixed blocks using _ANY_ as a delimiter
#
expectedStringList = list(expectedString.split('_ANY_'))


#
# Remove the empty ones
#
for loop in expectedStringList:
    if loop == "":
        expectedStringList.remove("")


#
# Message to the user about the found blocks
#
print("These blocks of characters should be present, unaltered and in this order in the givenString :")
print("- - -")
for loop in expectedStringList:
    print("Length = {:>3} characters : ".format(len(loop)), "'{}'".format(loop))


#
# Search for blocks from the expectedStringList in the givenString
# and create a new givenRebuildString to compare to expectedStrippedString later on
#
for loop in expectedStringList:
    if (givenString.rfind(loop)) > -1:
        givenRebuildString += givenString[givenString.rfind(loop):givenString.rfind(loop) + len(loop)]
    else:
        givenRebuildString += "".ljust(len(loop), "~")
        differentBlocks.append(loop)
        foundDifferences = foundDifferences + 1

#
# Since a wildcard could be the last thing in expectedString,
# we need to do something about that
#
givenRebuildString += givenString[givenString.rfind(loop) + len(loop):len(givenString)]
if expectedString[len(expectedString) - 5:len(expectedString)] == "_ANY_":
    expectedStrippedString += givenString[givenString.rfind(loop) + len(loop):len(givenString)]


#
# Then check the two strings if the are the same
#
print("\n\nSo after rebuilding, stripping and searching we ask ourselves :")
print("Are these strings, without the wildcard(s), the same ?")
print("- - -")
print("givenRebuildString         : '{}' ".format(givenRebuildString))
print("and expectedStrippedString : '{}' ".format(expectedStrippedString), "\n")

if givenRebuildString == expectedStrippedString:
    print("Yes, they totally are !")
else:
    print("Nope, not even close :-(\n")
    for loop in differentBlocks:
        print("Difference found in block '{}'".format(loop))
